# Noita Wiki ZH · RAG 知识库系统 v1.1.0 更新日志 (Changelog)

本版本为 **Milestone v1.1.0** 核心升级，重点引入纯本地离线检索、打字机流式传输、LRU 缓存降本与全局异常屏障，并修复全部历史已知缺陷。

---

## 🚀 新增功能 (What's New)

- **纯 Python BM25 倒排检索引擎**：
  - 新增纯标准库实现的多语言分词器（支持中文字符 1/2-gram、芬兰语词缀、法术代码与数值分词）。
  - 支持 **100% 纯离线检索模式**：未配置 API Key 或添加 `--no-llm` 时自动降级为本地 BM25 检索，实现 0 网络依赖、0 费用消耗。
  - 联网模式下支持 **Dense (BGE-M3) + Sparse (BM25)** 互惠排名融合（RRF, $k=60$）双路召回，显著提升法术代码、怪物代号与精确数值的检索召回率。
- **终端打字机式实时流式传输 (SSE Token Streaming)**：
  - 大模型生成问答支持 Server-Sent Events (SSE) 流式传输（`stream=True`），首字感知延迟（TTFT）降低至 **< 300ms**，并在生成结束后自动附带结构化 Wiki 引用来源。
- **两级线程安全 LRU 缓存 (Query & Embedding Cache)**：
  - 基于 `OrderedDict` 与 `threading.RLock` 实现两级内存缓存（Embedding 向量 1024 条，Query 问答 512 条），高频提问实现 **< 1ms 毫秒级即时响应**，节省 100% 重复 API 消耗。
- **Windows 一键极速启动批处理 (`run_mcp.bat`)**：
  - 自动检测并优先调用 Python 3.10+ 环境，强制配置 UTF-8 编码，小白用户双击一键拉起 MCP 服务。
- **通用 AI 大模型兼容**：
  - 彻底解耦第三方厂商强绑定，标准化兼容任意 OpenAI 格式接口及自建大语言模型。

---

## 🛡️ 缺陷修复与稳健性提升 (Bug Fixes & Hardening)

- **修复 Rerank 降序逻辑**：修复重排结果被错误按 index 升序排列的逻辑缺陷，严格按相关性得分降序排列。
- **修复切片相似度分数错位**：修复噪声过滤导致得分数组与返回文档错位的缺陷，确保得分与文档 1:1 精确绑定。
- **修复跨平台绝对路径硬编码**：`rag/build_index.py` 移除绝对路径，统一采用相对路径动态解析根目录。
- **MCP HTTP Bearer 鉴权与防侧信道攻击**：HTTP 部署模式支持 Bearer Token 鉴权，采用 `secrets.compare_digest` 恒定时间安全比对，放行 CORS OPTIONS 预检请求。
- **MCP 全局友好异常拦截屏障**：为 MCP 工具添加全局异常防护，外部 API 欠费（402）、限流（429）、鉴权失败（401）、网络超时或断网时不崩溃协议连接，返回清晰友好的结构化中文提示。
- **Git LFS 防御性自检拦截**：当检测到 `index.npy` 或 `chunks.json` 为 Git LFS 指针文件时，优雅拦截并输出明确的 `git lfs pull` 指引。
- **向量矩阵 L2 预归一化**：在矩阵加载时完成 L2 预归一化，消除单次检索时重复计算静态全量范数的性能开销。

---

## 🧪 质量保证 (Quality Assurance)

- 全量构建 **73 项自动化单元与集成测试套件**（`tests/test_p1_fixes.py` 与 `tests/test_p2_features.py`），测试通过率 **100% (73/73 Passed)**。
- 覆盖 SSE 流式解析、BM25 倒排索引与 RRF 融合排序、LRU 缓存命中与 120 线程并发安全压测、MCP Bearer 鉴权拦截与全局异常容错屏障。

---

## 📦 变更文件清单 (Changed Files)

- `rag/query.py`：新增 BM25 检索、RRF 混合双路召回、SSE 流式输出、两级 LRU 缓存，修复重排与分数对齐缺陷。
- `rag/mcp_server.py`：新增 ASGI Bearer 鉴权中间件与全局异常拦截屏障。
- `rag/build_index.py`：修复动态路径解析。
- `rag/config.example.json`：标准化通用大模型配置模板。
- `run_mcp.bat`：新增 Windows 一键启动脚本。
- `DEPLOY_LOCAL.md`：新增本地桌面客户端（ChatBox 等）图文部署指南。
- `skills/noita-wiki-rag/SKILL.md`：升级至 v1.1.0 规范，支持本地 100% 离线 BM25 检索。
- `tests/test_p1_fixes.py` & `tests/test_p2_features.py`：新增自动化测试套件。
