# -*- coding: utf-8 -*-
"""Noita Wiki RAG - MCP server (stdio).
暴露工具:
  noita_query(question)  -> 检索+重排+LLM 生成的回答(含来源)
  noita_search(question, top_n=6) -> 只检索片段(省额度)

运行: python mcp_server.py   (被 MCP client 以 stdio 方式拉起)
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import query as rag

from mcp.server.mcpserver import MCPServer

server = MCPServer("noita-rag", version="1.0.0")

@server.tool()
def noita_query(question: str) -> str:
    """基于 Noita 中文 Wiki 知识库回答游戏问题(检索+重排+LLM 生成)。
    参数 question: 玩家问题,例如 \"34魔球boss血量多少\"。
    返回: 含来源引用的完整回答。"""
    ans, picked, sims = rag.answer(question, no_llm=False)
    out = [ans, "\n--- 引用来源 ---"]
    for i, c in enumerate(picked, 1):
        out.append(f"[{i}] {c['title']} | {c['file']}")
    return "\n".join(out)

@server.tool()
def noita_search(question: str, top_n: int = 6) -> str:
    """在 Noita 中文 Wiki 知识库中检索相关片段(不调用生成模型,节省额度)。
    参数 question: 检索关键词或问题; top_n: 返回片段数(1-15)。
    返回: 最相关的知识库片段列表及来源。"""
    top_n = max(1, min(top_n, 15))
    ans, picked, sims = rag.answer(question, no_llm=True, top_n=top_n)
    out = []
    for i, c in enumerate(picked, 1):
        out.append(f"[{i}] (相似度 {sims[i-1]:.3f}) {c['title']} | {c['file']}")
        out.append(f"    {c['text'][:400]}")
    return "\n".join(out)

if __name__ == "__main__":
    server.run("stdio")
