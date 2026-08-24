# Noita Wiki ZH · RAG 知识库系统 v1.1.0 发布说明

Noita Wiki 中文知识库 RAG 系统迎来 Milestone v1.1.0 重大更新！本次版本在保持零外部重型依赖的前提下，全面引入了纯 Python 本地 BM25 检索、打字机式流式输出、两级 LRU 缓存，并对 MCP 服务端安全与异常拦截进行了加固，同时全面标准化了通用 AI 大模型接口协议。

---

## 🚀 核心新增特性 (Features)

1. **纯 Python 零依赖 BM25 倒排检索与 100% 离线可用**：
   - 内置轻量级多语言分词器（支持中文字符 1/2-gram、芬兰语词缀、法术代码与数值）。
   - **离线模式（无 API Key）**：支持 100% 纯本地离线关键词精确匹配，0 API 费用消耗。
   - **联网模式**：密集向量（BGE-M3）+ 稀疏关键词（BM25）通过倒排互惠排名融合（RRF, $k=60$）双路召回，显著提升法术代码、怪物代号与精确数值的召回率。

2. **打字机式实时流式输出 (SSE Token Streaming)**：
   - 命令行问答与客户端交互全面支持 Server-Sent Events (SSE) 流式传输（`stream=True`）。
   - 首字感知延迟（TTFT）由原本的 3~5 秒大幅降低至 **< 300ms**，并在生成结束后自动附带结构化 Wiki 来源引用。

3. **双层线程安全 LRU 缓存 (Query & Embedding Cache)**：
   - 基于 `OrderedDict` 与 `threading.RLock` 实现两级内存缓存（Embedding 向量 1024 条，Query 回答 512 条）。
   - 高频重复提问达到 **< 1ms 毫秒级即时响应**，节省 100% 重复 API 消耗。

4. **Windows 一键极速启动 (`run_mcp.bat`)**：
   - 新增 Windows 批处理启动脚本，自动探测本地 Python 3.10+ 环境，强制配置 UTF-8 编码，小白用户双击即用。

5. **通用 AI 大模型标准化兼容 (Model-Agnostic)**：
   - 彻底解耦第三方厂商强绑定，全面拥抱标准 OpenAI 兼容接口协议，无缝接入各类通用 LLM 大语言模型与自建/开源模型服务。

---

## 🛡️ 核心缺陷修复与健壮性提升 (Bug Fixes & Hardening)

- **修复 Rerank 降序逻辑**：修复重排结果被错误升序排列的缺陷，严格按相关性得分降序排列。
- **修复切片分数对齐**：修复噪声过滤后相似度分数错位问题，确保文档与分数 1:1 精确绑定。
- **MCP HTTP Bearer 鉴权与防侧信道攻击**：HTTP 部署模式支持 Bearer Token 鉴权，采用 `secrets.compare_digest` 恒定时间安全比对。
- **MCP 全局异常拦截屏障**：外部 API 欠费（HTTP 402）、限流（HTTP 429）、断网或超时时，自动返回人类友好的中文诊断提示，杜绝 MCP 协议崩溃。
- **Git LFS 防御性检测**：自动拦截 LFS 指针文件并给出直观的 `git lfs pull` 修复指引。
- **向量矩阵 L2 预归一化**：在矩阵加载时完成预归一化，大幅降低单次检索计算开销。

---

## 🧪 质量保证 (Quality Assurance)

- **73 / 73 项自动化单元与集成测试全量通过**（耗时 0.34s）。
- 覆盖 SSE 流式解析、BM25 检索与 RRF 排序、LRU 线程安全压测、MCP 鉴权及全部历史接口向后兼容性。

---

## 📖 快速上手

```bash
# 1. 克隆仓库与拉取完整数据
git lfs install
git clone https://github.com/a1113622001/noita-wiki-zh.git
cd noita-wiki-zh

# 2. 安装轻量依赖
pip install numpy mcp starlette uvicorn

# 3. Windows 一键启动 MCP
run_mcp.bat

# 4. 或直接体验本地离线检索 (0 配置 / 无需 Key)
python rag/query.py "黑洞法术怎么配" --no-llm
```
详细的本地桌面客户端（ChatBox 等）接入指南请参阅 [DEPLOY_LOCAL.md](DEPLOY_LOCAL.md)。
