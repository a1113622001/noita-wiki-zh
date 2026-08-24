# -*- coding: utf-8 -*-
"""Comprehensive Automated Test Suite for Milestone M4 (Phase 2 / Milestone v1.1 Features).

Test Classes:
1. TestP2TokenStreaming:
   - SSE chunk stream parsing in post_stream()
   - chat(..., stream=True) generator verification
   - answer(..., stream=True) yielding token generator + picked chunks + similarities
   - Typewriter CLI output formatting and citation anchoring
   - Stream error handling and resilience

2. TestP2BM25AndHybridRetrieval:
   - Multi-lingual tokenization (CJK unigrams/bigrams, Finnish terms, English codes, numbers, symbols)
   - BM25 score calculation, title weighting (4x) and exact title match boost (+15)
   - 100% offline fallback mode with title_to_file.json and zero API network calls
   - Reciprocal Rank Fusion (rrf_fuse) ranking formula
   - search_knowledge_dense, search_knowledge_bm25, search_knowledge_hybrid interfaces

3. TestP2LRUCaching:
   - ThreadSafeLRUCache core data structure, eviction, and stats telemetry
   - Embedding LRU cache hit verification (0 network calls on repeat query)
   - Query answer LRU cache hit verification (0 network calls, sub-millisecond response)
   - LRU capacity eviction behavior when exceeding max size
   - Thread safety with concurrent queries across multiple threads
   - use_cache=False bypass and clear_caches() invalidation

4. TestP2MCPServerAuthAndExceptionBarrier:
   - HTTP Bearer Token auth: HTTP 401 on missing or invalid token with WWW-Authenticate: Bearer
   - HTTP 200 / passthrough on valid token
   - Unauthenticated access when MCP_TOKEN is unset / empty
   - CORS preflight OPTIONS request bypass
   - Exception barrier catching quota/network/runtime/LFS errors in noita_query & noita_search

5. TestP2RegressionAndP1Preservation:
   - Full backward compatibility of rag/query.py and rag/mcp_server.py with Phase 1 signatures
   - Noise filtering and 1:1 score-to-document alignment preservation
   - Git LFS defense and vector matrix L2 pre-normalization preservation
"""

import io
import json
import os
import sys
import threading
import time
import unittest
import urllib.error
from collections import Counter
from unittest.mock import MagicMock, patch

import numpy as np
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.testclient import TestClient

# Ensure project root is at the head of sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import rag.mcp_server as rmcp
import rag.query as rq


class TestP2TokenStreaming(unittest.TestCase):
    """Unit and integration tests for Requirement R1 (SSE Token Streaming & Typewriter CLI)."""

    def setUp(self):
        rq.clear_caches()
        rq._chunks = None
        rq._emb = None
        rq._bm25 = None
        self._orig_key = rq.KEY
        rq.KEY = "test_mock_api_key_123"

    def tearDown(self):
        rq.clear_caches()
        rq._chunks = None
        rq._emb = None
        rq._bm25 = None
        rq.KEY = self._orig_key

    def test_post_stream_sse_chunk_parsing(self):
        """Verify post_stream() correctly parses SSE data chunks, ignores comments/empty lines, and stops at [DONE]."""
        sse_lines = [
            b': keep-alive comment\n',
            b'\n',
            b'data: {"id":"chat-1","choices":[{"delta":{"role":"assistant","content":""}}]}\n',
            b'data: {"id":"chat-1","choices":[{"delta":{"content":"\xe9\xbb\x91"}}]}\n',  # "黑"
            b': another keep-alive\n',
            b'data: {"id":"chat-1","choices":[{"delta":{"content":"\xe6\xb4\x9e"}}]}\n',  # "洞"
            b'data: {"id":"chat-1","choices":[{"delta":{"content":"\xe6\xb3\x95\xe6\x9c\xaf"}}]}\n',  # "法术"
            b'data: [DONE]\n',
            b'data: {"id":"chat-1","choices":[{"delta":{"content":"ignored"}}]}\n',
        ]

        class MockStreamingResp:
            def __enter__(self):
                return iter(sse_lines)

            def __exit__(self, exc_type, exc_val, exc_tb):
                pass

        with patch("urllib.request.urlopen", return_value=MockStreamingResp()):
            stream_gen = rq.post_stream("/chat/completions", {"messages": []})
            tokens = list(stream_gen)

        self.assertEqual(tokens, ["黑", "洞", "法术"])

    def test_post_stream_malformed_json_tolerance(self):
        """Verify post_stream() gracefully skips malformed JSON chunks without crashing."""
        sse_lines = [
            b'data: {"choices":[{"delta":{"content":"Valid1"}}]}\n',
            b'data: {corrupted json chunk\n',
            b'data: {"choices":[{"delta":{"content":"Valid2"}}]}\n',
            b'data: [DONE]\n',
        ]

        class MockStreamingResp:
            def __enter__(self):
                return iter(sse_lines)

            def __exit__(self, exc_type, exc_val, exc_tb):
                pass

        with patch("urllib.request.urlopen", return_value=MockStreamingResp()):
            tokens = list(rq.post_stream("/chat/completions", {"messages": []}))

        self.assertEqual(tokens, ["Valid1", "Valid2"])

    def test_chat_streaming_vs_blocking_modes(self):
        """Verify chat() returns full string when stream=False and token generator when stream=True."""
        # 1. Blocking mode
        with patch("rag.query.post", return_value={"choices": [{"message": {"content": "完整文本回答"}}]}) as mock_post:
            res_str = rq.chat([{"role": "user", "content": "hello"}], stream=False)
            self.assertEqual(res_str, "完整文本回答")
            mock_post.assert_called_once()

        # 2. Streaming mode
        def fake_post_stream(path, body):
            for t in ["流", "式", "输", "出"]:
                yield t

        with patch("rag.query.post_stream", side_effect=fake_post_stream):
            res_gen = rq.chat([{"role": "user", "content": "hello"}], stream=True)
            self.assertTrue(hasattr(res_gen, "__iter__"))
            tokens = list(res_gen)
            self.assertEqual(tokens, ["流", "式", "输", "出"])
            self.assertEqual("".join(tokens), "流式输出")

    def test_answer_streaming_mode_immediate_candidates_and_generator(self):
        """Verify answer(stream=True) immediately returns candidates and picked chunks, yielding token generator."""
        mock_chunks = [
            {"id": "c1", "title": "黑洞", "file": "blackhole.md", "ctx": "法术", "text": "黑洞法术可以破坏地形并吸引实体。"},
            {"id": "c2", "title": "白洞", "file": "whitehole.md", "ctx": "法术", "text": "白洞法术效果与黑洞相反。"},
        ]
        mock_sims = np.array([0.92, 0.81], dtype=np.float32)

        def fake_post_stream(path, body):
            for t in ["黑", "洞", "是", "一", "种", "强", "力", "法", "术"]:
                yield t

        with patch("rag.query.load_chunks", return_value=mock_chunks), \
             patch("rag.query.retrieve", return_value=([0, 1], mock_sims)), \
             patch("rag.query.rerank", return_value=[{"index": 0, "relevance_score": 0.95}]), \
             patch("rag.query.post_stream", side_effect=fake_post_stream):

            stream_gen, picked, picked_sims = rq.answer("黑洞", stream=True, no_llm=False, k=10, top_n=6)

            # Picked chunks and sims are accessible BEFORE iterating generator
            self.assertEqual(len(picked), 1)
            self.assertEqual(picked[0]["title"], "黑洞")
            self.assertEqual(len(picked_sims), 1)
            self.assertAlmostEqual(picked_sims[0], 0.92, places=4)

            # Iterating stream yields tokens
            tokens = list(stream_gen)
            full_ans = "".join(tokens)
            self.assertEqual(full_ans, "黑洞是一种强力法术")

            # Streamed answer is cached in query cache upon completion
            cached = rq._query_cache.get("黑洞##0##10##6")
            self.assertIsNotNone(cached)
            cached_ans, cached_picked, cached_sims = cached
            self.assertEqual(cached_ans, "黑洞是一种强力法术")
            self.assertEqual(cached_picked[0]["title"], "黑洞")

    def test_streaming_from_query_cache_hit(self):
        """Verify that streaming answer on a cache hit returns a chunked generator yielding full cached text."""
        mock_chunks = [{"id": "c1", "title": "黑洞", "file": "blackhole.md", "ctx": "法术", "text": "黑洞信息。"}]
        mock_sims = np.array([0.95], dtype=np.float32)

        with patch("rag.query.load_chunks", return_value=mock_chunks), \
             patch("rag.query.retrieve", return_value=([0], mock_sims)), \
             patch("rag.query.rerank", return_value=[{"index": 0, "relevance_score": 0.99}]), \
             patch("rag.query.chat", return_value="黑洞是一种强力法术") as mock_chat:

            # 1. Populate cache naturally via standard non-streaming query
            ans1, picked1, sims1 = rq.answer("黑洞", stream=False, no_llm=False, k=10, top_n=6)
            self.assertEqual(ans1, "黑洞是一种强力法术")
            self.assertEqual(mock_chat.call_count, 1)

        # 2. Second query in streaming mode hits cache (0 network / retrieval calls)
        with patch("rag.query.load_chunks", return_value=mock_chunks), \
             patch("rag.query.retrieve", side_effect=AssertionError("Should not call retrieve on cache hit")), \
             patch("rag.query.post", side_effect=AssertionError("Should not call API on cache hit")), \
             patch("rag.query.chat", side_effect=AssertionError("Should not call chat on cache hit")):

            stream_gen, picked, sims = rq.answer("黑洞", stream=True, no_llm=False, k=10, top_n=6)
            self.assertEqual(len(picked), 1)
            self.assertEqual(picked[0]["title"], "黑洞")
            tokens = list(stream_gen)
            self.assertEqual("".join(tokens), "黑洞是一种强力法术")

    def test_post_stream_mid_stream_exception_resilience(self):
        """Verify post_stream() propagates error without infinite re-tries if tokens were already yielded."""
        call_count = 0

        class FaultyStreamingResp:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                pass

            def __iter__(self):
                nonlocal call_count
                call_count += 1
                yield b'data: {"choices":[{"delta":{"content":"Token1"}}]}\n'
                raise urllib.error.URLError("Mid-stream connection dropped")

        with patch("urllib.request.urlopen", return_value=FaultyStreamingResp()):
            gen = rq.post_stream("/chat/completions", {"messages": []}, retries=3)
            with self.assertRaises(urllib.error.URLError):
                _ = list(gen)

        # Retries must not trigger once tokens have started yielding to avoid duplicate tokens
        self.assertEqual(call_count, 1)

    def test_typewriter_cli_output_and_citations(self):
        """Verify run() prints typewriter tokens and structured citations block cleanly."""
        mock_chunks = [
            {"title": "黑洞", "file": "blackhole.md", "ctx": "法术 > 投射物", "text": "黑洞可以破坏地形。"}
        ]
        mock_sims = [0.95]

        def fake_gen():
            for t in ["黑", "洞", "解析"]:
                yield t

        with patch("rag.query.answer", return_value=(fake_gen(), mock_chunks, mock_sims)), \
             patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:

            args = MagicMock()
            args.no_llm = False
            args.no_stream = False
            args.k = 10
            args.top_n = 6

            rq.run("黑洞", args)
            output = mock_stdout.getvalue()

            self.assertIn("=== 回答 ===", output)
            self.assertIn("黑洞解析", output)
            self.assertIn("--- 引用来源 ---", output)
            self.assertIn("[1] 黑洞 | blackhole.md", output)

    def test_answer_streaming_no_llm_mode(self):
        """Verify answer(no_llm=True, stream=True) returns (None, cand, sims) immediately without streaming."""
        mock_chunks = [{"id": "c1", "title": "黑洞", "file": "blackhole.md", "ctx": "法术", "text": "黑洞法术。"}]
        mock_sims = np.array([0.95], dtype=np.float32)

        with patch("rag.query.load_chunks", return_value=mock_chunks), \
             patch("rag.query.retrieve", return_value=([0], mock_sims)), \
             patch("rag.query.chat", side_effect=AssertionError("Should not call chat in no_llm mode")):

            ans, picked, sims = rq.answer("黑洞", no_llm=True, stream=True, k=10, top_n=6)
            self.assertIsNone(ans)
            self.assertEqual(len(picked), 1)
            self.assertEqual(picked[0]["title"], "黑洞")

    def test_answer_non_streaming_cached_then_stream_retrieval(self):
        """Verify executing non-streaming query first, followed by streaming query, yields chunked tokens from cache."""
        mock_chunks = [{"id": "c1", "title": "黑洞", "file": "blackhole.md", "ctx": "法术", "text": "黑洞法术。"}]
        mock_sims = np.array([0.95], dtype=np.float32)

        with patch("rag.query.load_chunks", return_value=mock_chunks), \
             patch("rag.query.retrieve", return_value=([0], mock_sims)), \
             patch("rag.query.rerank", return_value=[{"index": 0, "relevance_score": 0.99}]), \
             patch("rag.query.chat", return_value="完整生成回答内容") as mock_chat:

            # 1. Non-streaming call populates query cache
            ans1, picked1, sims1 = rq.answer("黑洞", stream=False, no_llm=False, k=10, top_n=6)
            self.assertEqual(ans1, "完整生成回答内容")
            self.assertEqual(mock_chat.call_count, 1)

            # 2. Streaming call retrieves from query cache and yields chunked stream
            stream_gen, picked2, sims2 = rq.answer("黑洞", stream=True, no_llm=False, k=10, top_n=6)
            self.assertEqual(mock_chat.call_count, 1)  # 0 new chat calls
            tokens = list(stream_gen)
            self.assertEqual("".join(tokens), "完整生成回答内容")
            self.assertEqual(picked2[0]["title"], "黑洞")


class TestP2BM25AndHybridRetrieval(unittest.TestCase):
    """Unit and integration tests for Requirement R2 (BM25, Hybrid RRF & Offline Fallback)."""

    def setUp(self):
        rq.clear_caches()
        rq._chunks = None
        rq._emb = None
        rq._bm25 = None

    def tearDown(self):
        rq.clear_caches()
        rq._chunks = None
        rq._emb = None
        rq._bm25 = None

    def test_pure_python_tokenizer_multilingual_and_codes(self):
        """Verify tokenize() correctly decomposes Chinese unigram/bigrams, Finnish terms, English codes, numbers, and symbols."""
        # 1. Chinese phrase
        tokens_zh = rq.tokenize("黑洞合成")
        # Unigrams: 黑, 洞, 合, 成; Bigrams: 黑洞, 洞合, 合成
        for expected in ["黑", "洞", "合", "成", "黑洞", "洞合", "合成"]:
            self.assertIn(expected, tokens_zh)

        # 2. Finnish game terms
        tokens_fi = rq.tokenize("Alkemisti Auringonsiemen Musta aukko")
        self.assertIn("alkemisti", tokens_fi)
        self.assertIn("auringonsiemen", tokens_fi)
        self.assertIn("musta", tokens_fi)
        self.assertIn("aukko", tokens_fi)

        # 3. Spell codes, component identifiers & underscores
        tokens_code = rq.tokenize("LIGHT_BULLET AIAttackComponent DamageModel")
        self.assertIn("light_bullet", tokens_code)
        self.assertIn("light", tokens_code)
        self.assertIn("bullet", tokens_code)
        self.assertIn("aiattackcomponent", tokens_code)
        self.assertIn("damagemodel", tokens_code)

        # 4. Floating-point numbers, stats, and symbols
        tokens_num = rq.tokenize("-0.17s 33魔球 34+ +1 ???")
        self.assertIn("0.17s", tokens_num)
        self.assertIn("0", tokens_num)
        self.assertIn("17s", tokens_num)
        self.assertIn("33", tokens_num)
        self.assertIn("魔球", tokens_num)
        self.assertIn("34", tokens_num)
        self.assertIn("1", tokens_num)

        # 5. Empty and whitespace boundary conditions
        self.assertEqual(rq.tokenize(""), [])
        self.assertEqual(rq.tokenize("   \n\t  "), [])
        self.assertEqual(rq.tokenize("!!!@@@###"), [])

    def test_bm25_retriever_ranking_and_title_weighting(self):
        """Verify BM25Retriever scores exact title matches and title tokens higher than body-only mentions."""
        chunks = [
            {
                "id": "c0",
                "title": "黑洞",
                "file": "blackhole.md",
                "ctx": "法术 > 投射物",
                "text": "黑洞法术可以发射一个引力奇点，破坏大范围地形并吸引实体。",
            },
            {
                "id": "c1",
                "title": "法术组合技巧",
                "file": "combos.md",
                "ctx": "指南 > 进阶",
                "text": "在法术组合中，黑洞可以与加速法术配合提高射程，黑洞是挖掘神器。",
            },
            {
                "id": "c2",
                "title": "蠕虫血液",
                "file": "worm_blood.md",
                "ctx": "药水 > 效果",
                "text": "饮用蠕虫血液可以获得全图透视效果，持续一段时间。",
            },
        ]

        retriever = rq.BM25Retriever(title_weight=4.0, ctx_weight=2.0)
        retriever.fit(chunks)

        idx, scores = retriever.search("黑洞", top_k=3)

        self.assertEqual(len(idx), 2)
        # Chunk 0 (exact title match "黑洞") must be ranked #1 with exact boost (+15.0)
        self.assertEqual(idx[0], 0)
        self.assertEqual(idx[1], 1)
        # Score of chunk 0 must be substantially higher than body-only mention chunk 1
        self.assertGreater(scores[0], scores[1] + 10.0)
        # Chunk 2 should not match query "黑洞"
        self.assertNotIn(2, idx)

    def test_bm25_empty_query_and_out_of_vocab(self):
        """Verify BM25Retriever handles empty queries and OOV words gracefully."""
        chunks = [{"title": "测试", "ctx": "ctx", "text": "内容"}]
        retriever = rq.BM25Retriever()
        retriever.fit(chunks)

        idx_empty, scores_empty = retriever.search("")
        self.assertEqual(len(idx_empty), 0)
        self.assertEqual(len(scores_empty), 0)

        idx_oov, scores_oov = retriever.search("完全不存在的生僻词汇xyz123")
        self.assertEqual(len(idx_oov), 0)
        self.assertEqual(len(scores_oov), 0)

    def test_offline_fallback_mode_zero_api_calls(self):
        """Verify that when KEY is unset, retrieve() and answer(no_llm=True) operate 100% offline with zero network calls."""
        mock_chunks = [
            {"id": "c0", "title": "黑洞", "file": "blackhole.md", "ctx": "法术", "text": "黑洞法术挖掘与毁灭机制。"},
            {"id": "c1", "title": "白洞", "file": "whitehole.md", "ctx": "法术", "text": "白洞法术排斥机制。"},
        ]

        with patch.object(rq, "KEY", ""), \
             patch("rag.query.load_chunks", return_value=mock_chunks), \
             patch("rag.query.post", side_effect=AssertionError("Strict violation: Network POST call in offline mode")):

            # 1. Test retrieve() offline
            idx, sims = rq.retrieve("黑洞", k=2)
            self.assertGreater(len(idx), 0)
            self.assertEqual(idx[0], 0)

            # 2. Test answer(no_llm=True) offline
            ans, picked, picked_sims = rq.answer("黑洞", no_llm=True, k=2, top_n=1)
            self.assertIsNone(ans)
            self.assertEqual(len(picked), 1)
            self.assertEqual(picked[0]["title"], "黑洞")
            self.assertGreater(picked_sims[0], 0.0)

    def test_rrf_fusion_mathematics(self):
        """Verify rrf_fuse() computes exact Reciprocal Rank Fusion scores: sum(w / (k_rrf + rank))."""
        dense_idx = np.array([10, 20, 30], dtype=int)
        dense_scores = np.array([0.95, 0.85, 0.75], dtype=np.float32)
        bm25_idx = np.array([20, 40, 10], dtype=int)
        bm25_scores = np.array([18.5, 12.0, 5.0], dtype=np.float32)

        # Expected calculation:
        # Doc 20: dense rank 2 -> 1/(60+2) = 1/62; bm25 rank 1 -> 1/(60+1) = 1/61. Total = 1/62 + 1/61 ≈ 0.0325225
        # Doc 10: dense rank 1 -> 1/(60+1) = 1/61; bm25 rank 3 -> 1/(60+3) = 1/63. Total = 1/61 + 1/63 ≈ 0.0322668
        # Doc 40: dense unranked; bm25 rank 2 -> 1/(60+2) = 1/62. Total = 1/62 ≈ 0.0161290
        # Doc 30: dense rank 3 -> 1/(60+3) = 1/63; bm25 unranked. Total = 1/63 ≈ 0.0158730
        idx, sims = rq.rrf_fuse(
            dense_idx, dense_scores, bm25_idx, bm25_scores,
            top_k=4, rrf_k=60, w_dense=1.0, w_bm25=1.0
        )

        self.assertEqual(list(idx), [20, 10, 40, 30])
        self.assertAlmostEqual(sims[0], (1.0 / 62.0) + (1.0 / 61.0), places=6)
        self.assertAlmostEqual(sims[1], (1.0 / 61.0) + (1.0 / 63.0), places=6)
        self.assertAlmostEqual(sims[2], 1.0 / 62.0, places=6)
        self.assertAlmostEqual(sims[3], 1.0 / 63.0, places=6)

    def test_rrf_fuse_empty_and_disjoint_inputs(self):
        """Verify rrf_fuse() handles empty, None, and disjoint candidate sets safely."""
        # Both empty
        idx_empty, sims_empty = rq.rrf_fuse(np.array([]), np.array([]), np.array([]), np.array([]))
        self.assertEqual(len(idx_empty), 0)
        self.assertEqual(len(sims_empty), 0)

        # Only Dense candidates
        dense_idx = np.array([1, 2], dtype=int)
        dense_scores = np.array([0.9, 0.8], dtype=np.float32)
        idx_dense_only, sims_dense_only = rq.rrf_fuse(dense_idx, dense_scores, None, None, top_k=2)
        self.assertEqual(list(idx_dense_only), [1, 2])
        self.assertAlmostEqual(sims_dense_only[0], 1.0 / 61.0, places=6)

    def test_search_knowledge_hybrid_dense_failure_fallback(self):
        """Verify search_knowledge_hybrid() falls back to BM25 when dense vector search fails."""
        mock_bm25_idx = np.array([5, 6], dtype=int)
        mock_bm25_sims = np.array([12.0, 8.0], dtype=np.float32)

        with patch("rag.query.search_knowledge_dense", side_effect=Exception("Dense API 500 error")), \
             patch("rag.query.search_knowledge_bm25", return_value=(mock_bm25_idx, mock_bm25_sims)):

            idx, sims = rq.search_knowledge_hybrid("测试问题", k=2)
            self.assertEqual(list(idx), [5, 6])
            np.testing.assert_array_almost_equal(sims, mock_bm25_sims)

    def test_bm25_fit_and_search_with_title_to_file_mapping(self):
        """Verify alias titles from title_to_file.json map to target chunk files with exact match boost."""
        chunks = [
            {"id": "c0", "title": "Black Hole", "file": "blackhole.md", "ctx": "Spell", "text": "Destroys terrain."},
            {"id": "c1", "title": "Wand", "file": "wand.md", "ctx": "Item", "text": "Holds spells."},
        ]
        alias_map = {"黑洞": "blackhole.md", "奇点": "blackhole.md"}

        with patch("os.path.exists", return_value=True), \
             patch("builtins.open", unittest.mock.mock_open(read_data=json.dumps(alias_map))):

            retriever = rq.BM25Retriever()
            retriever.fit(chunks)

            # Query with alias "黑洞"
            idx, scores = retriever.search("黑洞", top_k=2)
            self.assertEqual(len(idx), 1)
            self.assertEqual(idx[0], 0)
            self.assertGreaterEqual(scores[0], 15.0)

            # Query with second alias "奇点"
            idx2, scores2 = retriever.search("奇点", top_k=2)
            self.assertEqual(len(idx2), 1)
            self.assertEqual(idx2[0], 0)
            self.assertGreaterEqual(scores2[0], 15.0)

    def test_search_knowledge_dense_and_bm25_direct_interfaces(self):
        """Verify direct search_knowledge_dense and search_knowledge_bm25 return aligned NumPy arrays."""
        mock_chunks = [{"title": "黑洞", "file": "blackhole.md", "ctx": "法术", "text": "黑洞法术。"}]

        with patch("rag.query.embed_one", return_value=[1.0, 0.0]), \
             patch("rag.query.get_embedder", return_value={"m": np.array([[1.0, 0.0], [0.0, 1.0]], dtype=np.float32)}):

            d_idx, d_sims = rq.search_knowledge_dense("黑洞", k=2)
            self.assertEqual(len(d_idx), 2)
            self.assertEqual(d_idx[0], 0)
            self.assertAlmostEqual(d_sims[0], 1.0, places=4)

        with patch("rag.query.load_chunks", return_value=mock_chunks):
            b_idx, b_sims = rq.search_knowledge_bm25("黑洞", k=1)
            self.assertEqual(len(b_idx), 1)
            self.assertEqual(b_idx[0], 0)

    def test_bm25_hyperparameters_custom_weights(self):
        """Verify BM25Retriever respects custom k1, b, title_weight, and ctx_weight values."""
        retriever = rq.BM25Retriever(k1=2.0, b=0.5, title_weight=8.0, ctx_weight=3.0)
        self.assertEqual(retriever.k1, 2.0)
        self.assertEqual(retriever.b, 0.5)
        self.assertEqual(retriever.title_weight, 8.0)
        self.assertEqual(retriever.ctx_weight, 3.0)

        chunks = [{"title": "超强法术", "ctx": "进阶", "text": "普通内容"}]
        retriever.fit(chunks)
        self.assertEqual(retriever.corpus_size, 1)


class TestP2LRUCaching(unittest.TestCase):
    """Unit and stress tests for Requirement R3 (Thread-Safe Two-Tier LRU Caching)."""

    def setUp(self):
        rq.clear_caches()
        rq._chunks = None
        rq._emb = None
        rq._bm25 = None
        self._orig_key = rq.KEY
        rq.KEY = "test_mock_api_key_123"

    def tearDown(self):
        rq.clear_caches()
        rq._chunks = None
        rq._emb = None
        rq._bm25 = None
        rq.KEY = self._orig_key

    def test_thread_safe_lru_cache_operations(self):
        """Verify ThreadSafeLRUCache put, get, eviction, metrics, and capacity limit."""
        cache = rq.ThreadSafeLRUCache(capacity=3)
        self.assertEqual(len(cache), 0)

        # Invalid capacity
        with self.assertRaises(ValueError):
            rq.ThreadSafeLRUCache(capacity=0)
        with self.assertRaises(ValueError):
            rq.ThreadSafeLRUCache(capacity=-5)

        # Add 3 items
        cache.put("k1", "v1")
        cache.put("k2", "v2")
        cache.put("k3", "v3")
        self.assertEqual(len(cache), 3)

        # Access k1 to make k2 the least recently used
        self.assertEqual(cache.get("k1"), "v1")
        self.assertIn("k1", cache)

        # Put 4th item: should evict k2 (LRU)
        cache.put("k4", "v4")
        self.assertEqual(len(cache), 3)
        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k1"), "v1")
        self.assertEqual(cache.get("k3"), "v3")
        self.assertEqual(cache.get("k4"), "v4")

        # Telemetry stats
        stats = cache.get_stats()
        self.assertEqual(stats["size"], 3)
        self.assertEqual(stats["capacity"], 3)
        self.assertEqual(stats["hits"], 4)  # k1, k1, k3, k4
        self.assertEqual(stats["misses"], 1)  # k2
        self.assertAlmostEqual(stats["hit_rate"], 4.0 / 5.0, places=3)

        # Clear
        cache.clear()
        self.assertEqual(len(cache), 0)
        stats_cleared = cache.get_stats()
        self.assertEqual(stats_cleared["hits"], 0)
        self.assertEqual(stats_cleared["misses"], 0)

    def test_embedding_lru_cache_hit_zero_network_calls(self):
        """Verify embed_one() caches vector embeddings and bypasses network on subsequent calls."""
        fake_emb = [0.1 * i for i in range(10)]

        with patch("rag.query.post", return_value={"data": [{"embedding": fake_emb}]}) as mock_post:
            # 1st call: cache miss
            res1 = rq.embed_one("黑洞法术", use_cache=True)
            self.assertEqual(res1, fake_emb)
            self.assertEqual(mock_post.call_count, 1)

            # 2nd call: cache hit (case & whitespace insensitive)
            res2 = rq.embed_one("  黑洞法术  ", use_cache=True)
            self.assertEqual(res2, fake_emb)
            self.assertEqual(mock_post.call_count, 1)  # 0 new API calls

            # 3rd call with use_cache=False: bypasses cache
            res3 = rq.embed_one("黑洞法术", use_cache=False)
            self.assertEqual(res3, fake_emb)
            self.assertEqual(mock_post.call_count, 2)

    def test_query_lru_cache_hit_zero_network_calls(self):
        """Verify answer() caches full generation results, responding in < 1ms on duplicate queries with 0 API calls."""
        mock_chunks = [{"id": "c1", "title": "黑洞", "file": "blackhole.md", "ctx": "法术", "text": "黑洞挖掘力极强。"}]
        mock_sims = np.array([0.95], dtype=np.float32)

        with patch("rag.query.load_chunks", return_value=mock_chunks), \
             patch("rag.query.retrieve", return_value=([0], mock_sims)) as mock_retrieve, \
             patch("rag.query.rerank", return_value=[{"index": 0, "relevance_score": 0.99}]) as mock_rerank, \
             patch("rag.query.chat", return_value="黑洞是挖掘法术。") as mock_chat:

            # 1st call: executes full RAG pipeline
            ans1, picked1, sims1 = rq.answer("黑洞怎么用", no_llm=False, use_cache=True)
            self.assertEqual(ans1, "黑洞是挖掘法术。")
            self.assertEqual(mock_retrieve.call_count, 1)
            self.assertEqual(mock_rerank.call_count, 1)
            self.assertEqual(mock_chat.call_count, 1)

            # 2nd call: cache hit (0 new retrieval, rerank, or chat calls)
            t0 = time.perf_counter()
            ans2, picked2, sims2 = rq.answer("  黑洞怎么用  ", no_llm=False, use_cache=True)
            elapsed_ms = (time.perf_counter() - t0) * 1000.0

            self.assertEqual(ans2, "黑洞是挖掘法术。")
            self.assertEqual(picked2[0]["title"], "黑洞")
            self.assertEqual(mock_retrieve.call_count, 1)
            self.assertEqual(mock_rerank.call_count, 1)
            self.assertEqual(mock_chat.call_count, 1)
            self.assertLess(elapsed_ms, 5.0)  # Sub-millisecond return

    def test_clear_caches_and_telemetry(self):
        """Verify clear_caches() and get_cache_stats() report accurate telemetry."""
        rq._emb_cache.put("k1", [1.0, 2.0])
        rq._query_cache.put("q1", ("ans", [], []))

        stats_before = rq.get_cache_stats()
        self.assertEqual(stats_before["embedding_cache"]["size"], 1)
        self.assertEqual(stats_before["query_cache"]["size"], 1)

        rq.clear_caches()
        stats_after = rq.get_cache_stats()
        self.assertEqual(stats_after["embedding_cache"]["size"], 0)
        self.assertEqual(stats_after["query_cache"]["size"], 0)

    def test_query_cache_use_cache_false_bypass(self):
        """Verify answer(use_cache=False) bypasses reading from and writing to _query_cache."""
        mock_chunks = [{"id": "c1", "title": "黑洞", "file": "blackhole.md", "ctx": "法术", "text": "黑洞法术。"}]
        mock_sims = np.array([0.95], dtype=np.float32)

        with patch("rag.query.load_chunks", return_value=mock_chunks), \
             patch("rag.query.retrieve", return_value=([0], mock_sims)) as mock_retrieve, \
             patch("rag.query.rerank", return_value=[{"index": 0, "relevance_score": 0.99}]), \
             patch("rag.query.chat", return_value="回答内容") as mock_chat:

            # 1st call without cache
            ans1, picked1, sims1 = rq.answer("黑洞", no_llm=False, use_cache=False, k=10, top_n=6)
            self.assertEqual(ans1, "回答内容")
            self.assertEqual(mock_retrieve.call_count, 1)
            self.assertEqual(mock_chat.call_count, 1)
            # Verify cache was not populated
            self.assertIsNone(rq._query_cache.get("黑洞##0##10##6"))

            # 2nd call without cache: must call retrieve and chat again
            ans2, picked2, sims2 = rq.answer("黑洞", no_llm=False, use_cache=False, k=10, top_n=6)
            self.assertEqual(ans2, "回答内容")
            self.assertEqual(mock_retrieve.call_count, 2)
            self.assertEqual(mock_chat.call_count, 2)

    def test_embedding_cache_eviction_when_capacity_reached(self):
        """Verify custom capacity LRU cache evicts oldest item when capacity is exceeded."""
        mini_cache = rq.ThreadSafeLRUCache(capacity=2)
        mini_cache.put("item1", [1.0])
        mini_cache.put("item2", [2.0])
        self.assertEqual(len(mini_cache), 2)

        # Access item1 to mark it recently used
        _ = mini_cache.get("item1")

        # Insert item3 -> item2 should be evicted
        mini_cache.put("item3", [3.0])
        self.assertEqual(len(mini_cache), 2)
        self.assertIn("item1", mini_cache)
        self.assertNotIn("item2", mini_cache)
        self.assertIn("item3", mini_cache)

    def test_lru_thread_safety_stress(self):
        """Stress test ThreadSafeLRUCache with 10 concurrent threads to ensure zero race conditions or deadlocks."""
        cache = rq.ThreadSafeLRUCache(capacity=20)
        num_threads = 10
        ops_per_thread = 100
        errors = []

        def worker(thread_id):
            try:
                for i in range(ops_per_thread):
                    key = f"key_{(thread_id * 10 + i) % 30}"
                    val = f"val_{thread_id}_{i}"
                    cache.put(key, val)
                    _ = cache.get(key)
                    _ = key in cache
                    _ = len(cache)
                    _ = cache.get_stats()
            except Exception as e:
                errors.append((thread_id, e))

        threads = [threading.Thread(target=worker, args=(t,)) for t in range(num_threads)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertEqual(len(errors), 0, f"Thread safety errors detected: {errors}")
        self.assertLessEqual(len(cache), 20)


class TestP2MCPServerAuthAndExceptionBarrier(unittest.TestCase):
    """Unit and security tests for Requirement R4 (MCP Bearer Token Auth & Exception Barrier)."""

    def setUp(self):
        rq.clear_caches()

        # Build dummy ASGI backend app for pure middleware verification
        async def dummy_endpoint(request):
            return JSONResponse({"status": "ok", "method": request.method})

        self.dummy_app = Starlette(routes=[
            Route("/mcp", dummy_endpoint, methods=["GET", "POST", "OPTIONS"])
        ])

    def tearDown(self):
        rq.clear_caches()

    def test_mcp_http_bearer_auth_missing_token_401(self):
        """Verify HTTP 401 Unauthorized with WWW-Authenticate: Bearer when Authorization header is missing."""
        app = rmcp.BearerAuthMiddleware(self.dummy_app, token="super_secret_token_123")
        client = TestClient(app)

        response = client.post("/mcp", json={"jsonrpc": "2.0", "method": "initialize", "id": 1})
        self.assertEqual(response.status_code, 401)
        self.assertIn("Bearer", response.headers.get("WWW-Authenticate", ""))
        self.assertIn("Unauthorized", response.text)

    def test_mcp_http_bearer_auth_invalid_token_401(self):
        """Verify HTTP 401 Unauthorized when an invalid Bearer token is provided."""
        app = rmcp.BearerAuthMiddleware(self.dummy_app, token="super_secret_token_123")
        client = TestClient(app)

        # Wrong token
        response = client.post(
            "/mcp",
            headers={"Authorization": "Bearer wrong_invalid_token"},
            json={"jsonrpc": "2.0", "method": "initialize", "id": 1}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers.get("WWW-Authenticate"), "Bearer")

        # Wrong scheme (Basic auth)
        response_basic = client.post(
            "/mcp",
            headers={"Authorization": "Basic dXNlcjpwYXNz"},
            json={"jsonrpc": "2.0", "method": "initialize", "id": 1}
        )
        self.assertEqual(response_basic.status_code, 401)

    def test_mcp_http_bearer_auth_valid_token_allowed(self):
        """Verify HTTP request passes through authentication when valid Bearer token is provided."""
        app = rmcp.BearerAuthMiddleware(self.dummy_app, token="valid_mcp_secret")
        client = TestClient(app)

        response = client.post(
            "/mcp",
            headers={"Authorization": "Bearer valid_mcp_secret"},
            json={"jsonrpc": "2.0", "method": "ping", "id": 1}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok", "method": "POST"})

    def test_mcp_http_bearer_auth_cors_options_bypass(self):
        """Verify CORS preflight OPTIONS requests bypass Bearer token authentication."""
        app = rmcp.BearerAuthMiddleware(self.dummy_app, token="secure_token")
        client = TestClient(app)

        response = client.options("/mcp")
        self.assertEqual(response.status_code, 200)

    def test_mcp_http_auth_unconfigured_open_mode(self):
        """Verify that when MCP_TOKEN is unset or empty, requests pass through freely in open mode."""
        app = rmcp.BearerAuthMiddleware(self.dummy_app, token="")
        client = TestClient(app)

        response = client.post("/mcp", json={"jsonrpc": "2.0", "method": "ping", "id": 1})
        self.assertEqual(response.status_code, 200)

    def test_mcp_create_http_app_factory(self):
        """Verify create_http_app factory wraps streamable_http_app with BearerAuthMiddleware."""
        with patch.dict(os.environ, {"MCP_TOKEN": "factory_test_token"}):
            app = rmcp.create_http_app()
            self.assertIsInstance(app, rmcp.BearerAuthMiddleware)
            self.assertEqual(app.token, "factory_test_token")

    def test_mcp_global_exception_barrier_quota_exhausted(self):
        """Verify _format_error() produces human-friendly Chinese diagnostic for HTTP 402/429 quota exhaustion."""
        err_402 = urllib.error.HTTPError("http://api", 402, "Payment Required", {}, None)
        msg_402 = rmcp._format_error("noita_query", err_402)
        self.assertIn("额度超限", msg_402)
        self.assertIn("402", msg_402)

        err_429 = urllib.error.HTTPError("http://api", 429, "Too Many Requests", {}, None)
        msg_429 = rmcp._format_error("noita_query", err_429)
        self.assertIn("额度超限", msg_429)
        self.assertIn("429", msg_429)

    def test_mcp_global_exception_barrier_auth_failure(self):
        """Verify _format_error() produces diagnostic for HTTP 401/403 API key issues."""
        err_401 = urllib.error.HTTPError("http://api", 401, "Unauthorized", {}, None)
        msg_401 = rmcp._format_error("noita_query", err_401)
        self.assertIn("鉴权失败", msg_401)
        self.assertIn("SILICONFLOW_API_KEY", msg_401)

    def test_mcp_global_exception_barrier_upstream_500(self):
        """Verify _format_error() produces diagnostic for HTTP 500/503 upstream server errors."""
        err_500 = urllib.error.HTTPError("http://api", 500, "Internal Server Error", {}, None)
        msg_500 = rmcp._format_error("noita_query", err_500)
        self.assertIn("上游服务异常", msg_500)
        self.assertIn("500", msg_500)

    def test_mcp_global_exception_barrier_network_timeout(self):
        """Verify _format_error() produces diagnostic for network timeouts."""
        err_timeout = TimeoutError("Connection timed out after 30s")
        msg_timeout = rmcp._format_error("noita_query", err_timeout)
        self.assertIn("网络超时", msg_timeout)

        err_url = urllib.error.URLError("Temporary failure in name resolution")
        msg_url = rmcp._format_error("noita_search", err_url)
        self.assertIn("网络超时", msg_url)

    def test_mcp_global_exception_barrier_git_lfs_pointer(self):
        """Verify _format_error() detects Git LFS pointer errors and suggests git lfs pull."""
        err_lfs = RuntimeError("检测到 chunks.json 是 Git LFS 指针文件！请执行 git lfs pull")
        msg_lfs = rmcp._format_error("noita_query", err_lfs)
        self.assertIn("Git LFS", msg_lfs)
        self.assertIn("git lfs pull", msg_lfs)

    def test_mcp_global_exception_barrier_file_not_found(self):
        """Verify _format_error() diagnoses missing knowledge base files."""
        err_fnf = FileNotFoundError("chunks.json not found")
        msg_fnf = rmcp._format_error("noita_query", err_fnf)
        self.assertIn("文件缺失", msg_fnf)

    def test_mcp_tools_exception_wrapping_safety(self):
        """Verify noita_query and noita_search tool handlers never raise unhandled exceptions."""
        with patch.object(rmcp.rag, "answer", side_effect=urllib.error.HTTPError("http://api", 402, "Payment Required", {}, None)):
            res_query = rmcp.noita_query("测试问题")
            self.assertIn("额度超限", res_query)

            res_search = rmcp.noita_search("测试检索")
            self.assertIn("额度超限", res_search)

    def test_mcp_bearer_auth_case_insensitivity_and_whitespace(self):
        """Verify BearerAuthMiddleware accepts lowercase 'bearer ' prefix and trims token whitespace."""
        app = rmcp.BearerAuthMiddleware(self.dummy_app, token="clean_token_abc")
        client = TestClient(app)

        # Lowercase "bearer "
        resp_lower = client.post(
            "/mcp",
            headers={"Authorization": "bearer clean_token_abc"},
            json={"jsonrpc": "2.0", "method": "ping", "id": 1}
        )
        self.assertEqual(resp_lower.status_code, 200)

        # Extra whitespace in token
        resp_space = client.post(
            "/mcp",
            headers={"Authorization": "Bearer   clean_token_abc  "},
            json={"jsonrpc": "2.0", "method": "ping", "id": 1}
        )
        self.assertEqual(resp_space.status_code, 200)


class TestP2RegressionAndP1Preservation(unittest.TestCase):
    """Regression and backward-compatibility verification for all Phase 1 contracts."""

    def setUp(self):
        rq.clear_caches()
        rq._chunks = None
        rq._emb = None
        rq._bm25 = None
        self._orig_key = rq.KEY
        rq.KEY = "test_mock_api_key_123"

    def tearDown(self):
        rq.clear_caches()
        rq._chunks = None
        rq._emb = None
        rq._bm25 = None
        rq.KEY = self._orig_key

    def test_all_p1_interfaces_and_signatures_preserved(self):
        """Verify all Phase 1 function signatures, default arguments, and return types are preserved."""
        # 1. load_chunks() exists and returns list
        mock_chunks = [{"title": "t", "file": "f.md", "ctx": "c", "text": "txt"}]
        with patch("rag.query._check_lfs"), patch("builtins.open", MagicMock()), patch("json.load", return_value=mock_chunks):
            self.assertEqual(rq.load_chunks(), mock_chunks)

        # 2. get_embedder() exists and returns dict with "m"
        raw_m = np.ones((2, 4), dtype=np.float32)
        with patch("rag.query._check_lfs"), patch("numpy.load", return_value=raw_m):
            emb = rq.get_embedder()
            self.assertIn("m", emb)
            self.assertEqual(emb["m"].shape, (2, 4))

        # 3. rerank() returns list of dicts with index and relevance_score in descending order
        mock_rr_resp = {
            "results": [
                {"index": 0, "relevance_score": 0.2},
                {"index": 1, "relevance_score": 0.9},
            ]
        }
        with patch("rag.query.post", return_value=mock_rr_resp):
            rr = rq.rerank("query", ["doc0", "doc1"], top_n=2)
            self.assertEqual(len(rr), 2)
            self.assertEqual(rr[0]["index"], 1)
            self.assertEqual(rr[0]["relevance_score"], 0.9)

        # 4. retrieve() returns (indices, scores)
        with patch("rag.query.search_knowledge_bm25", return_value=(np.array([0]), np.array([1.0]))):
            with patch.object(rq, "KEY", ""):
                idx, sims = rq.retrieve("query", k=5)
                self.assertIsInstance(idx, np.ndarray)
                self.assertIsInstance(sims, np.ndarray)

        # 5. answer() default signature is backward compatible
        with patch("rag.query.retrieve", return_value=([0], np.array([0.9]))), \
             patch("rag.query.load_chunks", return_value=[{"title": "t", "file": "f", "ctx": "c", "text": "long valid text for testing"}]), \
             patch("rag.query.rerank", return_value=[{"index": 0, "relevance_score": 0.9}]), \
             patch("rag.query.chat", return_value="LLM Ans"):
            # Blocking mode
            ans, picked, sims = rq.answer("query", no_llm=False)
            self.assertEqual(ans, "LLM Ans")
            self.assertEqual(len(picked), 1)

            # Retrieve only mode
            ans_none, picked_none, sims_none = rq.answer("query", no_llm=True)
            self.assertIsNone(ans_none)
            self.assertEqual(len(picked_none), 1)

    def test_noise_filter_preserved_in_p2(self):
        """Verify noise filter _noise() rules remain strictly enforced in Phase 2."""
        # Short text < 40 chars
        self.assertTrue(rq._noise({"text": "Short snippet"}))
        # Valid long text
        self.assertFalse(rq._noise({"text": "A" * 50}))
        # Empty links template
        empty_links_text = "Context. " + "[](item.md) " * 4 + "[link](real.md) " * 5
        self.assertTrue(rq._noise({"text": empty_links_text}))
        # Image gallery
        gallery_text = "Gallery: " + "![img](pic.png) " * 5 + " Extra long text description."
        self.assertTrue(rq._noise({"text": gallery_text}))

    def test_rerank_descending_sorting_preserved(self):
        """Verify rerank() preserves strict descending sort order across shuffled and extreme scores."""
        mock_resp = {
            "results": [
                {"index": 0, "relevance_score": -0.5},
                {"index": 1, "relevance_score": 0.88},
                {"index": 2, "relevance_score": 0.12},
                {"index": 3, "relevance_score": 0.99},
            ]
        }
        with patch("rag.query.post", return_value=mock_resp):
            res = rq.rerank("query", [f"doc{i}" for i in range(4)], top_n=4)
            scores = [r["relevance_score"] for r in res]
            indices = [r["index"] for r in res]
            self.assertEqual(scores, [0.99, 0.88, 0.12, -0.5])
            self.assertEqual(indices, [3, 1, 2, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
