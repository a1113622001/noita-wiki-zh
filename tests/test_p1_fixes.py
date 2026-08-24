# -*- coding: utf-8 -*-
"""Official Automated Test Suite for Milestone M2 (P0/P1 Fixes).

This test suite verifies all Phase 1 fixes in Noita ZH Wiki RAG:
1. Dynamic relative path resolution in `build_index.py` (test_build_index_path_resolution)
2. Strictly descending relevance_score sort order in `rerank()` (test_rerank_descending_sort_order)
3. Noise filter 1:1 score-to-document alignment in `answer()` (test_noise_filter_score_doc_alignment)
4. Lazy singleton caching and memory identity in `load_chunks()` (test_chunks_json_singleton_caching)
5. Defensive Git LFS pointer detection with actionable error (test_git_lfs_pointer_detection_and_error)
6. Vector matrix L2 pre-normalization and caching in `get_embedder()` (test_vector_matrix_l2_pre_normalization)
7. Standard model names in `rag/config.example.json` (test_config_standard_model_names)
"""

import os
import sys
import json
import tempfile
import unittest
from unittest.mock import patch, mock_open, MagicMock
import numpy as np

# Ensure project root is at the head of sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import rag.query as rq
import rag.build_index as rbi


class TestP1Fixes(unittest.TestCase):
    """Automated unit and regression test suite for P0/P1 defect fixes."""

    def setUp(self):
        """Reset singleton caches before each test run."""
        rq._chunks = None
        rq._emb = None

    def tearDown(self):
        """Clean up singleton caches after each test run."""
        rq._chunks = None
        rq._emb = None

    # =========================================================================
    # Case 1: Dynamic relative path resolution in build_index.py
    # =========================================================================
    def test_build_index_path_resolution(self):
        """Verify build_index.py dynamically resolves paths relative to project root."""
        # 1. Verify paths are absolute
        self.assertTrue(os.path.isabs(rbi.BASE), f"BASE must be absolute: {rbi.BASE}")
        self.assertTrue(os.path.isabs(rbi.PAGES), f"PAGES must be absolute: {rbi.PAGES}")
        self.assertTrue(os.path.isabs(rbi.RAG), f"RAG must be absolute: {rbi.RAG}")
        self.assertTrue(os.path.isabs(rbi.CHUNKS_JSON), f"CHUNKS_JSON must be absolute: {rbi.CHUNKS_JSON}")
        self.assertTrue(os.path.isabs(rbi.INDEX_NPY), f"INDEX_NPY must be absolute: {rbi.INDEX_NPY}")
        self.assertTrue(os.path.isabs(rbi.BIN), f"BIN must be absolute: {rbi.BIN}")

        # 2. Verify exact directory relationships
        expected_base = os.path.normpath(PROJECT_ROOT)
        expected_pages = os.path.normpath(os.path.join(PROJECT_ROOT, "pages"))
        expected_rag = os.path.normpath(os.path.join(PROJECT_ROOT, "rag"))
        expected_chunks = os.path.normpath(os.path.join(expected_rag, "chunks.json"))
        expected_index = os.path.normpath(os.path.join(expected_rag, "index.npy"))

        self.assertEqual(os.path.normpath(rbi.BASE), expected_base)
        self.assertEqual(os.path.normpath(rbi.PAGES), expected_pages)
        self.assertEqual(os.path.normpath(rbi.RAG), expected_rag)
        self.assertEqual(os.path.normpath(rbi.CHUNKS_JSON), expected_chunks)
        self.assertEqual(os.path.normpath(rbi.INDEX_NPY), expected_index)

        # 3. Verify path validity and dynamic resolution
        for path_str in [rbi.BASE, rbi.PAGES, rbi.RAG, rbi.CHUNKS_JSON, rbi.INDEX_NPY]:
            self.assertTrue(os.path.isabs(path_str), f"Path must be absolute: {path_str}")
            self.assertTrue(path_str.startswith(expected_base), f"Path must reside under project root: {path_str}")

        # 4. Verify path invariance regardless of cwd
        original_cwd = os.getcwd()
        temp_dir = tempfile.mkdtemp()
        try:
            os.chdir(temp_dir)
            rag_dir = os.path.dirname(os.path.abspath(rbi.__file__))
            base_dir = os.path.dirname(rag_dir)
            pages_dir = os.path.join(base_dir, "pages")
            self.assertEqual(os.path.normpath(base_dir), expected_base)
            self.assertEqual(os.path.normpath(pages_dir), expected_pages)
        finally:
            os.chdir(original_cwd)
            try:
                os.rmdir(temp_dir)
            except Exception:
                pass

    # =========================================================================
    # Case 2: Rerank results strictly descending by relevance_score
    # =========================================================================
    @patch("rag.query.post")
    def test_rerank_descending_sort_order(self, mock_post):
        """Verify rerank() sorts results strictly in descending order of relevance_score."""
        # Unsorted API response
        mock_post.return_value = {
            "results": [
                {"index": 0, "relevance_score": 0.25},
                {"index": 1, "relevance_score": 0.98},
                {"index": 2, "relevance_score": 0.65},
                {"index": 3, "relevance_score": 0.88},
                {"index": 4, "relevance_score": 0.05},
            ]
        }
        docs = [f"Doc {i}" for i in range(5)]
        
        # Test full descending sort
        results = rq.rerank("test query", docs, top_n=5)
        scores = [r["relevance_score"] for r in results]
        indices = [r["index"] for r in results]

        self.assertEqual(scores, [0.98, 0.88, 0.65, 0.25, 0.05])
        self.assertEqual(indices, [1, 3, 2, 0, 4])
        
        # Verify strict descending property across all adjacent pairs
        for i in range(len(results) - 1):
            self.assertGreaterEqual(
                results[i]["relevance_score"],
                results[i + 1]["relevance_score"],
                f"Sort order inversion at index {i}: {results[i]} < {results[i+1]}"
            )

        # Test top_n truncation
        results_top2 = rq.rerank("test query", docs, top_n=2)
        self.assertEqual(len(results_top2), 2)
        self.assertEqual([r["relevance_score"] for r in results_top2], [0.98, 0.88])
        self.assertEqual([r["index"] for r in results_top2], [1, 3])

        # Test edge case: missing relevance_score defaults safely
        mock_post.return_value = {
            "results": [
                {"index": 0},
                {"index": 1, "relevance_score": 0.77},
            ]
        }
        results_missing = rq.rerank("test query", docs[:2], top_n=2)
        self.assertEqual(results_missing[0]["index"], 1)
        self.assertAlmostEqual(results_missing[0]["relevance_score"], 0.77)
        self.assertEqual(results_missing[1]["index"], 0)
        self.assertEqual(results_missing[1].get("relevance_score", 0.0), 0.0)

    # =========================================================================
    # Case 3: Noise filter score-to-document 1:1 alignment in answer()
    # =========================================================================
    @patch("rag.query.load_chunks")
    @patch("rag.query.retrieve")
    def test_noise_filter_score_doc_alignment_no_llm(self, mock_retrieve, mock_load_chunks):
        """Verify answer(no_llm=True) preserves 1:1 score-to-document alignment after noise filter."""
        # 5 mock chunks: indices 0 and 2 are noise; 1, 3, 4 are valid
        mock_chunks = [
            {"id": "c0", "title": "Noise Short", "file": "n1.md", "ctx": "ctx0", "text": "too short"},
            {"id": "c1", "title": "Valid Alpha", "file": "a.md", "ctx": "ctx1", "text": "This is a valid long text describing wand mechanics in Noita in great detail."},
            {"id": "c2", "title": "Noise Empty Links", "file": "n2.md", "ctx": "ctx2", "text": "[](1.md) [](2.md) [](3.md) [](4.md) [](5.md) [](6.md) [](7.md) [](8.md) [](9.md)"},
            {"id": "c3", "title": "Valid Beta", "file": "b.md", "ctx": "ctx3", "text": "This is another valid long text describing spell combinations and modifiers."},
            {"id": "c4", "title": "Valid Gamma", "file": "g.md", "ctx": "ctx4", "text": "This is a third valid long text describing enemy vulnerabilities and drops."},
        ]
        mock_load_chunks.return_value = mock_chunks
        
        # Raw retrieve returns indices [0, 1, 2, 3, 4] with corresponding similarities [0.99, 0.85, 0.80, 0.70, 0.65]
        retrieved_idx = [0, 1, 2, 3, 4]
        retrieved_sims = np.array([0.99, 0.85, 0.80, 0.70, 0.65], dtype=np.float32)
        mock_retrieve.return_value = (retrieved_idx, retrieved_sims)

        # In no_llm mode with top_n=2: should filter out 0 and 2, yielding 1 and 3
        ans, picked, sims = rq.answer("query", no_llm=True, k=5, top_n=2)

        self.assertIsNone(ans)
        self.assertEqual(len(picked), 2)
        self.assertEqual(len(sims), 2)

        # Check document identity
        self.assertEqual(picked[0]["title"], "Valid Alpha")
        self.assertEqual(picked[0]["id"], "c1")
        self.assertEqual(picked[1]["title"], "Valid Beta")
        self.assertEqual(picked[1]["id"], "c3")

        # Check aligned similarity scores (MUST correspond to c1=0.85, c3=0.70, NOT c0=0.99, c1=0.85)
        self.assertAlmostEqual(sims[0], 0.85, places=4)
        self.assertAlmostEqual(sims[1], 0.70, places=4)

    @patch("rag.query.chat")
    @patch("rag.query.rerank")
    @patch("rag.query.load_chunks")
    @patch("rag.query.retrieve")
    def test_noise_filter_score_doc_alignment_with_llm(self, mock_retrieve, mock_load_chunks, mock_rerank, mock_chat):
        """Verify answer(no_llm=False) preserves 1:1 score-to-document alignment through rerank."""
        mock_chunks = [
            {"id": "c0", "title": "Noise Short", "file": "n.md", "ctx": "ctx0", "text": "too short"},
            {"id": "c1", "title": "Valid Alpha", "file": "a.md", "ctx": "ctx1", "text": "Valid text Alpha describing alchemy mechanics in Noita."},
            {"id": "c2", "title": "Valid Beta", "file": "b.md", "ctx": "ctx2", "text": "Valid text Beta describing perk lottery mechanics in Noita."},
        ]
        mock_load_chunks.return_value = mock_chunks
        mock_retrieve.return_value = ([0, 1, 2], np.array([0.95, 0.80, 0.70], dtype=np.float32))
        
        # Filter removes c0 -> cand = [c1 (sim 0.80), c2 (sim 0.70)]
        # Rerank inverts order: candidate 1 (c2) ranked first, candidate 0 (c1) ranked second
        mock_rerank.return_value = [
            {"index": 1, "relevance_score": 0.99},
            {"index": 0, "relevance_score": 0.60},
        ]
        mock_chat.return_value = "Generated LLM response"

        ans, picked, picked_sims = rq.answer("query", no_llm=False, k=3, top_n=2)

        self.assertEqual(ans, "Generated LLM response")
        self.assertEqual(len(picked), 2)
        self.assertEqual(len(picked_sims), 2)

        # Candidate 1 (c2) should be picked first with its similarity 0.70
        self.assertEqual(picked[0]["id"], "c2")
        self.assertEqual(picked[0]["title"], "Valid Beta")
        self.assertAlmostEqual(picked_sims[0], 0.70, places=4)

        # Candidate 0 (c1) should be picked second with its similarity 0.80
        self.assertEqual(picked[1]["id"], "c1")
        self.assertEqual(picked[1]["title"], "Valid Alpha")
        self.assertAlmostEqual(picked_sims[1], 0.80, places=4)

    @patch("rag.query.load_chunks")
    @patch("rag.query.retrieve")
    def test_noise_filter_fallback_when_all_noisy(self, mock_retrieve, mock_load_chunks):
        """Verify answer() fallback mechanism when all candidates are classified as noise."""
        mock_chunks = [
            {"id": f"n{i}", "title": f"Noise {i}", "file": f"n{i}.md", "ctx": f"ctx{i}", "text": "short"}
            for i in range(4)
        ]
        mock_load_chunks.return_value = mock_chunks
        mock_retrieve.return_value = ([0, 1, 2, 3], np.array([0.9, 0.8, 0.7, 0.6], dtype=np.float32))

        # When all are noisy, fallback relaxes filter and preserves all chunks with aligned scores
        _, picked, sims = rq.answer("query", no_llm=True, k=4, top_n=3)

        self.assertEqual(len(picked), 3)
        self.assertEqual(len(sims), 3)
        self.assertEqual([c["id"] for c in picked], ["n0", "n1", "n2"])
        self.assertAlmostEqual(sims[0], 0.9, places=4)
        self.assertAlmostEqual(sims[1], 0.8, places=4)
        self.assertAlmostEqual(sims[2], 0.7, places=4)

    # =========================================================================
    # Case 4: chunks.json lazy singleton caching and memory identity
    # =========================================================================
    def test_chunks_json_singleton_caching(self):
        """Verify load_chunks() reads from disk only once and reuses in-memory singleton."""
        dummy_chunks = [
            {"id": "1", "title": "Page 1", "file": "p1.md", "ctx": "ctx1", "text": "Content 1"},
            {"id": "2", "title": "Page 2", "file": "p2.md", "ctx": "ctx2", "text": "Content 2"},
        ]
        json_content = json.dumps(dummy_chunks)

        with patch("rag.query._check_lfs") as mock_check_lfs:
            with patch("builtins.open", mock_open(read_data=json_content)) as mocked_file:
                rq._chunks = None

                # First call loads from file
                res1 = rq.load_chunks()
                self.assertEqual(res1, dummy_chunks)
                mocked_file.assert_called_once()
                mock_check_lfs.assert_called_once()

                # Second and third calls must return exact cached singleton reference
                res2 = rq.load_chunks()
                res3 = rq.load_chunks()
                self.assertIs(res1, res2)
                self.assertIs(res2, res3)
                
                # File open and LFS check should not be called again
                mocked_file.assert_called_once()
                mock_check_lfs.assert_called_once()

                # In-place modification is reflected in singleton
                res1.append({"id": "3", "title": "Page 3", "file": "p3.md", "ctx": "ctx3", "text": "Content 3"})
                self.assertEqual(len(rq.load_chunks()), 3)

                # Resetting cache allows re-reading
                rq._chunks = None
                res4 = rq.load_chunks()
                self.assertEqual(len(res4), 2)
                self.assertEqual(mocked_file.call_count, 2)

    # =========================================================================
    # Case 5: Git LFS pointer detection and actionable RuntimeError
    # =========================================================================
    def test_git_lfs_pointer_detection_and_error(self):
        """Verify _check_lfs() detects Git LFS pointer files and raises actionable RuntimeError."""
        lfs_pointer_content = (
            "version https://git-lfs.github.com/spec/v1\n"
            "oid sha256:4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a\n"
            "size 46377721\n"
        )
        normal_json_content = json.dumps([{"id": "test", "text": "valid knowledge base content"}])

        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as f_lfs:
            f_lfs.write(lfs_pointer_content)
            temp_lfs_path = f_lfs.name

        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as f_normal:
            f_normal.write(normal_json_content)
            temp_normal_path = f_normal.name

        try:
            # 1. LFS pointer file must raise RuntimeError
            with self.assertRaises(RuntimeError) as ctx:
                rq._check_lfs(temp_lfs_path, "chunks.json")
            
            err_msg = str(ctx.exception).lower()
            self.assertIn("git lfs pull", err_msg, "Error message must suggest 'git lfs pull'")
            self.assertIn("git lfs install", err_msg, "Error message must suggest 'git lfs install'")
            self.assertIn("chunks.json", str(ctx.exception), "Error message should mention the file name")

            # 2. Normal file must pass without raising any exception
            rq._check_lfs(temp_normal_path, "normal_file.json")

            # 3. Non-existent file must raise FileNotFoundError
            with self.assertRaises(FileNotFoundError):
                rq._check_lfs(os.path.join(tempfile.gettempdir(), "non_existent_file_12345.bin"))

            # 4. Integration check: load_chunks() triggers _check_lfs and raises RuntimeError on pointer
            with patch("rag.query.RAG", os.path.dirname(temp_lfs_path)):
                with patch("os.path.join", return_value=temp_lfs_path):
                    rq._chunks = None
                    with self.assertRaises(RuntimeError) as ctx_load:
                        rq.load_chunks()
                    self.assertIn("git lfs pull", str(ctx_load.exception).lower())

        finally:
            if os.path.exists(temp_lfs_path):
                os.remove(temp_lfs_path)
            if os.path.exists(temp_normal_path):
                os.remove(temp_normal_path)

    # =========================================================================
    # Additional Verification: Vector L2 Pre-normalization (F7)
    # =========================================================================
    def test_vector_matrix_l2_pre_normalization(self):
        """Verify get_embedder() normalizes matrix to unit L2 norm on load and caches singleton."""
        raw_matrix = np.array([
            [3.0, 4.0, 0.0, 0.0],
            [0.0, 0.0, 6.0, 8.0],
            [1.0, 2.0, 2.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],  # zero vector edge case
        ], dtype=np.float32)

        with patch("rag.query._check_lfs"):
            with patch("numpy.load", return_value=raw_matrix.copy()) as mock_np_load:
                rq._emb = None

                # First call loads and normalizes
                embedder1 = rq.get_embedder()
                mock_np_load.assert_called_once()
                m_norm = embedder1["m"]

                # Check L2 norm for non-zero vectors is 1.0
                norms = np.linalg.norm(m_norm, axis=1)
                self.assertAlmostEqual(norms[0], 1.0, places=5)
                self.assertAlmostEqual(norms[1], 1.0, places=5)
                self.assertAlmostEqual(norms[2], 1.0, places=5)
                
                # Check vector directions preserved
                self.assertAlmostEqual(m_norm[0, 0], 0.6, places=5)
                self.assertAlmostEqual(m_norm[0, 1], 0.8, places=5)
                self.assertAlmostEqual(m_norm[1, 2], 0.6, places=5)
                self.assertAlmostEqual(m_norm[1, 3], 0.8, places=5)

                # Second call reuses cached singleton without re-calling np.load
                embedder2 = rq.get_embedder()
                self.assertIs(embedder1, embedder2)
                mock_np_load.assert_called_once()

    # =========================================================================
    # Additional Verification: Standard Model Names in config.example.json (F2)
    # =========================================================================
    def test_config_standard_model_names(self):
        """Verify config.example.json specifies valid standard models without hallucinated names."""
        config_path = os.path.join(PROJECT_ROOT, "rag", "config.example.json")
        self.assertTrue(os.path.exists(config_path), f"Config example missing: {config_path}")

        with open(config_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)

        # Validate chat_model is valid DeepSeek-V3, not DeepSeek-V4-Flash
        chat_model = cfg.get("chat_model", "")
        self.assertEqual(chat_model, "deepseek-ai/DeepSeek-V3", f"Invalid chat_model: {chat_model}")
        self.assertNotIn("Flash", chat_model)
        self.assertNotIn("V4", chat_model)

        # Validate embedding and rerank models
        self.assertEqual(cfg.get("embedding_model"), "BAAI/bge-m3")
        self.assertEqual(cfg.get("rerank_model"), "BAAI/bge-reranker-v2-m3")


if __name__ == "__main__":
    unittest.main(verbosity=2)
