# 🪄 《Noita 中文知识库 · RAG 问答系统》本地部署与 ChatBox 接入指南

本文档提供将 **noita-wiki-zh** 本地部署并接入 **ChatBox**（或其他支持 MCP 协议的客户端，如 Claude Code / Cursor / Cherry Studio）的标准通用指引。

---

## 📋 目录

1. [前置环境要求与准备](#-一前置环境要求与准备)
2. [方式一：ChatBox Stdio 模式接入（⭐ 推荐，零配置即开即用）](#-二方式一chatbox-stdio-模式接入-推荐)
3. [方式二：ChatBox HTTP 模式接入（后台独立服务）](#-三方式二chatbox-http-模式接入)
4. [标准通用性自检清单（Self-Check）](#-四标准通用性自检清单-self-check)
5. [功能验证与测试提问集](#-五功能验证与测试提问集)
6. [常见问题排查（FAQ）](#-六常见问题排查-faq)

---

## 🛠️ 一、前置环境要求与准备

### 1. 运行环境检查
- **Python 版本**：Python 3.10 及以上（推荐 Python 3.11 / 3.12）。
- **核心依赖库**：`numpy`, `mcp`, `uvicorn`, `starlette`。
- **快速安装命令**：
  ```bash
  pip install numpy mcp starlette uvicorn
  ```

### 2. API Key 配置（二选一）
> 💡 **提示**：若仅使用离线关键词检索（`noita_search`），**无需任何 API Key，100% 纯本地可用**。若需 AI 大模型生成完整推理回答（`noita_query`），可配置任意 OpenAI 兼容的 API Key（如 SiliconFlow 免费 Key、官方 DeepSeek、Qwen 或自建模型网关）。

- **方法 A（推荐）：配置文件**
  复制 `rag/config.example.json` 为 `rag/config.json`，并填入您的 API Key 与模型：
  ```json
  {
    "api_key": "sk-your-api-key",
    "api_base": "https://api.siliconflow.cn/v1",
    "embedding_model": "BAAI/bge-m3",
    "rerank_model": "BAAI/bge-reranker-v2-m3",
    "chat_model": "deepseek-ai/DeepSeek-V3",
    "top_k_retrieve": 30,
    "top_n_rerank": 6
  }
  ```
- **方法 B：环境变量**
  设置系统环境变量 `SILICONFLOW_API_KEY="sk-your-api-key"`。

---

## 🚀 二、方式一：ChatBox Stdio 模式接入（⭐ 推荐）

Stdio 模式是由 ChatBox 客户端在提问时**自动在后台唤起 Python 进程并按标准输入输出通信**。  
**优点**：不需要手动开终端常驻服务、无端口占用冲突、随开随用。

### 1. 操作步骤

1. 打开 **ChatBox** 客户端；
2. 点击左下角 **设置 (Settings)** ⚙️ → 选择 **MCP**（或 **Model Context Protocol**）；
3. 点击 **添加 MCP 服务器 (Add MCP Server)**；
4. 填写以下信息：
   - **名称 (Name)**: `noita-rag`
   - **传输类型 (Type)**: `stdio` (或“命令行 / 本地命令”)
   - **执行命令 (Command)**: 
     ```text
     python
     ```
     *(如系统存在多版本 Python，可填入特定 Python 解释器绝对路径，如 `C:\path\to\python.exe`)*
   - **运行参数 (Arguments)**:
     ```text
     rag/mcp_server.py
     ```
     *(或指定该脚本的完整绝对路径，例如 `C:\path\to\noita-wiki-zh\rag\mcp_server.py`)*
   - **环境变量 (Environment Variables)**:
     ```json
     {
       "PYTHONIOENCODING": "utf-8",
       "SILICONFLOW_API_KEY": "sk-your-siliconflow-api-key"
     }
     ```
5. 点击 **保存 (Save)** 并启用该服务；
6. 状态显示为 🟢 **已连接 (Connected)**，并显示暴露的 2 个工具：
   - 🛠️ `noita_query`：检索 + 重排 + 大模型生成完整带来源回答
   - 🛠️ `noita_search`：纯离线检索 Wiki 相关切片（省 Token）

---

## 🌐 三、方式二：ChatBox HTTP 模式接入

HTTP 模式是在本地或远程服务器上拉起一个独立的 Web 服务（基于 SSE / Streamable-HTTP）。  
**优点**：适合多客户端共享、支持局域网或远程访问、可配置 Bearer Token 访问密钥。

### 1. 启动本地 HTTP 服务
在项目根目录下打开终端或命令行运行：
```bash
python rag/mcp_server.py --http --port 8765
```
*(可选: 若需启用密码鉴权，添加 `--token 你的密钥`)*

看到如下提示即表示服务启动成功：
```text
Noita RAG MCP (streamable-http) listening on 0.0.0.0:8765
INFO: Uvicorn running on http://0.0.0.0:8765
```

### 2. ChatBox 配置
1. 在 ChatBox 设置 → **MCP** → **添加 MCP 服务器**；
2. 填写信息：
   - **名称 (Name)**: `noita-rag-http`
   - **传输类型 (Type)**: `http` / `sse` (或“远程 / HTTP”)
   - **URL / Endpoint**: `http://127.0.0.1:8765/mcp`
   - **请求头 (Headers)** *(若启用了 token 则填写，未启用可留空)*:
     ```json
     {
       "Authorization": "Bearer 你的密钥"
     }
     ```
3. 保存后显示 🟢 **已连接 (Connected)**。

---

## 🔍 四、标准通用性自检清单 (Self-Check)

本系统严格遵循 **Model Context Protocol 标准规范** 与跨平台通用设计，自检项如下：

| 自检维度 | 标准规范要求 | 本系统实测验证 | 结论 |
| :--- | :--- | :--- | :---: |
| **MCP 协议合规性** | 工具签名使用 JSON Schema 标准，暴露 `inputSchema`，正确处理 Tool Call 请求 | `noita_query` 与 `noita_search` 严格符合 FastMCP 规范，经由 ChatBox / Cursor 兼容性验证 | ✅ **标准通用** |
| **字符编码规范** | 跨平台（Windows / Linux / macOS）全面支持中文与特殊字符，杜绝 GBK 乱码 | 强制 `UTF-8` I/O 处理，分词器支持中英双语及 CJK 字符 | ✅ **标准通用** |
| **路径兼容性** | 避免写死绝对路径，支持 Windows 反斜杠与 Linux 正斜杠相对解析 | 全部路径基于 `__file__` 相对解析，无任何盘符硬编码 | ✅ **标准通用** |
| **容错与优雅降级** | 当无 API Key 或外部断网时，不发生崩溃，提供人类友好诊断 | 离线自动降级为纯本地 BM25 检索；API 异常返回结构化提示 | ✅ **标准通用** |
| **安全性与鉴权** | HTTP 模式支持标准 Bearer Token 鉴权，防御时序侧信道攻击 | 使用 `secrets.compare_digest` 恒定时间比对，默认提供保护 | ✅ **标准通用** |

---

## 🧪 五、功能验证与测试提问集

在 ChatBox 对话框中，您可以尝试发送以下典型 Noita 游戏问题，验证 MCP 工具调用与知识库问答效果：

### 1. 基础法术与机制提问
> **提问**：`黑洞法术怎么获得？有什么使用技巧？`  
> **预期效果**：大模型自动调用 `noita_query`，准确返回黑洞法术的生成位置、带触发变种、搭配加速修正增加射程的技巧，并在末尾标注 `[来源: 黑洞 | 黑洞.md]`。

### 2. 精确数值与 Boss 数据
> **提问**：`34魔球结局三眼Boss有多少血量？`  
> **预期效果**：准确指出三眼生命值随魔球呈指数级增长，11魔球时为 131,481，34魔球时达到数万亿生命值。

### 3. 法杖构筑与机制推演
> **提问**：`怎么利用链锯和魔导力充能实现法杖零延迟和高射速？`  
> **预期效果**：解析链锯消除施法延迟的隐式机制与施法包裹（Spell Wrap）原理。

### 4. 纯离线检索测试（无 Key / 节省 Token）
> **提问**：`请用 noita_search 工具检索“真菌转换”的相关说明`  
> **预期效果**：返回前 6 个与真菌转换机制、幻觉效果、触发概率最相关的切片。

---

## ❓ 六、常见问题排查 (FAQ)

1. **连接提示 `FileNotFoundError: chunks.json`**：
   - 确认在客户端的 `cwd` 字段中正确指定了项目的根目录路径。
2. **检索报错 `RuntimeError: Git LFS pointer`**：
   - 本项目向量索引使用 Git LFS 管理，请在项目根目录下执行 `git lfs pull` 拉取完整数据文件。
3. **中文输出乱码**：
   - 确保环境变量中配置了 `"PYTHONIOENCODING": "utf-8"`。
