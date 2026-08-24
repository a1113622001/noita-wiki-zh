# -*- coding: utf-8 -*-
"""Noita Wiki RAG - MCP server.
暴露工具:
  noita_query(question)  -> 检索+重排+LLM 生成的回答(含来源)
  noita_search(question, top_n=6) -> 只检索片段(省额度)

传输模式:
  python mcp_server.py                            # stdio(本地,被 MCP client 拉起)
  python mcp_server.py --http                     # streamable-http(服务器部署,远程接入)
  python mcp_server.py --http --port 8765
  python mcp_server.py --http --port 8765 --token secret123
"""
import argparse
import json
import os
import secrets
import sys
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import query as rag

from mcp.server.mcpserver import MCPServer
from starlette.responses import JSONResponse

server = MCPServer("noita-rag", version="1.0.0")


class BearerAuthMiddleware:
    """ASGI Middleware to enforce Bearer token authentication in HTTP mode."""

    def __init__(self, app, token: str = ""):
        self.app = app
        self.token = token.strip() if token else ""

    async def __call__(self, scope, receive, send):
        # Only inspect HTTP requests when a token is configured
        if scope["type"] != "http" or not self.token:
            await self.app(scope, receive, send)
            return

        # Bypass CORS preflight requests
        if scope.get("method") == "OPTIONS":
            await self.app(scope, receive, send)
            return

        # Extract Authorization header
        headers = dict(scope.get("headers", []))
        auth_header = headers.get(b"authorization", b"").decode("utf-8", errors="ignore").strip()

        authenticated = False
        if auth_header.lower().startswith("bearer "):
            token_val = auth_header[7:].strip()
            # Constant-time comparison prevents timing side-channel attacks
            if secrets.compare_digest(token_val, self.token):
                authenticated = True

        if not authenticated:
            response = JSONResponse(
                {"error": "Unauthorized", "detail": "Invalid or missing Bearer token."},
                status_code=401,
                headers={"WWW-Authenticate": "Bearer"},
            )
            await response(scope, receive, send)
            return

        await self.app(scope, receive, send)


def _format_error(tool_name: str, exc: Exception) -> str:
    """Format human-friendly structured error messages without breaking MCP protocol."""
    err_str = str(exc)
    if isinstance(exc, urllib.error.HTTPError):
        if exc.code in (401, 403):
            return f"【{tool_name} 鉴权失败】SiliconFlow API Key 无效或权限不足 (HTTP {exc.code})。请检查 SILICONFLOW_API_KEY 环境变量配置。"
        elif exc.code in (402, 429):
            return f"【{tool_name} 额度超限】SiliconFlow API 额度已耗尽或请求过于频繁 (HTTP {exc.code})。请前往 siliconflow.cn 充值或稍后重试。"
        elif exc.code >= 500:
            return f"【{tool_name} 上游服务异常】SiliconFlow 服务端暂时不可用 (HTTP {exc.code})。请稍后重试。"
        else:
            return f"【{tool_name} API 调用错误】HTTP {exc.code}: {exc.reason}"
    elif isinstance(exc, (urllib.error.URLError, TimeoutError)):
        return f"【{tool_name} 网络超时】无法连接到大模型/检索服务 ({exc!r})。请检查网络连通性或代理配置。"
    elif isinstance(exc, RuntimeError) and "Git LFS" in err_str:
        return f"【{tool_name} 知识库未就绪】检测到 Git LFS 指针文件。请在服务器执行 `git lfs pull` 拉取完整索引数据。"
    elif isinstance(exc, FileNotFoundError):
        return f"【{tool_name} 文件缺失】知识库索引文件不存在 ({err_str})。请先运行 build_index.py 构建知识库。"
    else:
        return f"【{tool_name} 处理异常】{exc!r}。如持续出现，请尝试使用 noita_search 纯检索模式。"


@server.tool()
def noita_query(question: str) -> str:
    """基于 Noita 中文 Wiki 知识库回答游戏问题(检索+重排+LLM 生成)。
    参数 question: 玩家问题,例如 \"34魔球boss血量多少\"。
    返回: 含来源引用的完整回答。"""
    try:
        ans, picked, sims = rag.answer(question, no_llm=False)
        out = [ans, "\n--- 引用来源 ---"]
        for i, c in enumerate(picked, 1):
            out.append(f"[{i}] {c['title']} | {c['file']}")
        return "\n".join(out)
    except Exception as e:
        return _format_error("noita_query", e)


@server.tool()
def noita_search(question: str, top_n: int = 6) -> str:
    """在 Noita 中文 Wiki 知识库中检索相关片段(不调用生成模型,节省额度)。
    参数 question: 检索关键词或问题; top_n: 返回片段数(1-15)。
    返回: 最相关的知识库片段列表及来源。"""
    try:
        top_n = max(1, min(top_n, 15))
        ans, picked, sims = rag.answer(question, no_llm=True, top_n=top_n)
        out = []
        for i, c in enumerate(picked, 1):
            out.append(f"[{i}] (相似度 {sims[i-1]:.3f}) {c['title']} | {c['file']}")
            out.append(f"    {c['text'][:400]}")
        return "\n".join(out)
    except Exception as e:
        return _format_error("noita_search", e)


def create_http_app(token: str | None = None):
    """Create a secured Starlette ASGI app for MCP Streamable-HTTP mode."""
    if token is not None:
        configured_token = token
    else:
        configured_token = os.environ.get("MCP_TOKEN", "")
        if not configured_token and hasattr(rag, "cfg") and isinstance(rag.cfg, dict):
            configured_token = rag.cfg.get("mcp_token", "")
    raw_app = server.streamable_http_app()
    return BearerAuthMiddleware(raw_app, token=configured_token)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Noita RAG MCP server")
    ap.add_argument("--http", action="store_true", help="以 streamable-http 模式运行(服务器部署)")
    ap.add_argument("--port", type=int, default=8765, help="http 模式端口(默认 8765)")
    ap.add_argument("--host", type=str, default="0.0.0.0", help="http 模式监听地址(默认 0.0.0.0)")
    ap.add_argument("--token", type=str, default=None, help="Bearer Token 密钥(默认读取 MCP_TOKEN 环境变量)")
    args = ap.parse_args()

    if args.http:
        token = args.token if args.token is not None else os.environ.get("MCP_TOKEN", "")
        print(f"Noita RAG MCP (streamable-http) listening on {args.host}:{args.port}", flush=True)
        if token:
            print(f"  [Security] Bearer Token authentication enabled (length: {len(token)})", flush=True)
        else:
            print("  [Security] WARNING: Running in open mode without Bearer Token", flush=True)

        app = create_http_app(token=token)
        import uvicorn
        uvicorn.run(app, host=args.host, port=args.port, log_level="info")
    else:
        server.run("stdio")
