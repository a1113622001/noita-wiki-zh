<div align="center">

# 🪄 Noita 中文知识库 · RAG 问答系统
### 📚 4,456 页 Wiki 离线镜像 + BGE-M3 向量 RAG + DeepSeek 生成 + MCP / Agent Skill 协议生态

[![Wiki Pages](https://img.shields.io/badge/Wiki%20Pages-4%2C456-blue.svg?style=flat-square&logo=gitbook)](pages/)
[![RAG Chunks](https://img.shields.io/badge/RAG%20Chunks-37%2C312-orange.svg?style=flat-square)](rag/chunks.json)
[![Embedding](https://img.shields.io/badge/Embedding-BGE--M3%20(1024d)-blueviolet.svg?style=flat-square)](https://huggingface.co/BAAI/bge-m3)
[![Reranker](https://img.shields.io/badge/Reranker-BGE--Reranker--v2--M3-red.svg?style=flat-square)](https://huggingface.co/BAAI/bge-reranker-v2-m3)
[![MCP Standard](https://img.shields.io/badge/MCP-Protocol%20Ready-green.svg?style=flat-square&logo=openai)](https://modelcontextprotocol.io/)
[![LLM](https://img.shields.io/badge/LLM-DeepSeek--V3%20%2F%20R1-blue.svg?style=flat-square)](https://deepseek.com)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=flat-square&logo=python)](https://www.python.org/)
[![License: CC BY-NC-SA 3.0](https://img.shields.io/badge/Wiki%20License-CC%20BY--NC--SA%203.0-orange.svg?style=flat-square)](LICENSE)
[![Code License: MIT](https://img.shields.io/badge/Code%20License-MIT-brightgreen.svg?style=flat-square)](LICENSE)

[简体中文](./README.md) · [快速开始](#-快速开始) · [MCP 接入指南](#-mcp-server-接入配置) · [离线浏览](#-离线知识库查阅) · [技术架构](#-技术栈与流水线)

</div>

---

## 📖 项目简介

**noita-wiki-zh** 是为著名 Roguelike 魔法探索游戏《Noita》打造的**全量中文离线镜像知识库与本地 RAG 问答系统**。

- 📚 **全量离线知识库**：包含全量爬取并清洗格式化的 **4,456 页 Markdown 页面**，站内所有双链均改写为相对路径，支持在 VS Code、Obsidian、Typora 中无损离线跳转浏览。
- 🧠 **工业级 RAG 本地问答**：基于 **BGE-M3 密集向量检索 (1024维)** + **BGE-Reranker-v2 重排** + **DeepSeek 模型生成**，回答精准并自动附带来源 Wiki 引用链接。
- 🔌 **全生态多端接入**：原生支持 **CLI 命令行交互**、**MCP Server（stdio / HTTP）** 与 **Agent Skill（/noita-wiki-rag）** 接入。
- ⚡ **零环境依赖开箱即用**：37,312 文本块切片及向量索引已内置随仓库管理（Git LFS），本地无需拉起向量数据库容器即可毫秒级检索。

---

## 🏗️ 技术栈与流水线 (Pipeline)

```mermaid
graph LR
    subgraph 知识库层 (Knowledge Base)
        A[4,456 页 Wiki Markdown] --> B[按标题层级切分 Hierarchical Chunking]
        B --> C[37,312 文本块 + 面包屑链]
        C --> D[BGE-M3 密集向量索引 index.npy]
    end

    subgraph 检索引擎 (RAG Engine)
        Q[用户提问] --> E[NumPy 极速余弦相似度初筛 Top-30]
        D --> E
        E --> F[BGE-Reranker-v2-M3 上下文重排 Top-6]
        F --> G[DeepSeek LLM 融合生成]
    end

    G --> R[精准答复 + 来源 Wiki 引用锚点]
```

### 核心技术选型

| 环节 | 选型与方案 | 技术说明 |
| :--- | :--- | :--- |
| **文档切分** | 标题层级切分 (Hierarchical) | 保留上级标题上下文链（如 `法术 > 投射物修饰 > 触发机制`），共 37,312 块 |
| **向量嵌入 (Embedding)** | `BAAI/bge-m3` | 1024 维密集多语言向量表示 |
| **初筛检索** | NumPy 矩阵向量余弦相似度 | 毫秒级内存矩阵计算，初筛召回 Top-30 相关切片 |
| **精排重排 (Rerank)** | `BAAI/bge-reranker-v2-m3` | 交叉编码重排打分，精选输出 Top-6 最佳上下文 |
| **大模型生成** | `deepseek-ai/DeepSeek-V3` / `R1` | 基于 SiliconFlow 或官方 API 快速推理并生成 Markdown 答复 |

---

## 🚀 快速开始

### 1. 克隆仓库 (需支持 Git LFS)
```bash
git lfs install
git clone https://github.com/a1113622001/noita-wiki-zh.git
cd noita-wiki-zh
```

### 2. 安装依赖
```bash
pip install numpy mcp
```

### 3. 配置 API Key
复制配置模板并填入您的 API Key（支持 SiliconFlow / DeepSeek 官方）：
```bash
cp rag/config.example.json rag/config.json
```
*或直接设置环境变量：`export SILICONFLOW_API_KEY="sk-..."` (Windows: `$env:SILICONFLOW_API_KEY="sk-..."`)*

### 4. 运行问答 (CLI)
```bash
cd rag

# 完整 RAG 问答 (检索 + 重排 + 大模型生成)
python query.py "黑洞法术怎么获得"

# 仅检索匹配片段 (不调用生成模型，纯离线极速模式)
python query.py "黑洞法术怎么获得" --no-llm
```

---

## 🔌 多端接入生态

| 接入形态 | 适用客户端 / 平台 | 入口文件 / 命令 | 说明 |
| :--- | :--- | :--- | :--- |
| **CLI 命令行** | 终端独立查询 / 交互问答 | `python rag/query.py` | 支持单次提问与多轮交互模式 |
| **MCP Server** | ChatBox / Claude Code / Reasonix / Cursor | `python rag/mcp_server.py` | 标准 MCP 协议，暴露 `noita_query` 与 `noita_search` 工具 |
| **Agent Skill** | 支持标准 Skill 调用的 Agent 平台 | `skills/noita-wiki-rag/` | 会话中键入 `/noita-wiki-rag` 唤起技能 |

---

## ⚙️ MCP Server 接入配置

### 1. ChatBox / Claude Code / Cursor 配置示例 (`mcp.json`)
```json
{
  "mcpServers": {
    "noita-wiki-rag": {
      "command": "python",
      "args": ["rag/mcp_server.py"],
      "cwd": "${workspaceFolder}",
      "env": {
        "SILICONFLOW_API_KEY": "sk-your-api-key"
      }
    }
  }
}
```

---

## 📖 离线知识库查阅

- **全量分类索引**：直接打开根目录 [`index.md`](./index.md) 查看按游戏机制、法术、生物、生物群系组织的目录树；
- **标题映射表**：查看 [`title_to_file.json`](./title_to_file.json) 获取 4,456 个 Wiki 中文条目与 Markdown 文件的精确映射；
- **知识库正文**：所有正文 Markdown 文件均位于 [`pages/`](./pages/) 目录下。

---

## 📁 目录结构

```
noita-wiki-zh/
├── index.md                   # 📚 全量页面分类索引
├── title_to_file.json         # 🗺️ 页面标题 → Markdown 文件名映射
├── pages/                     # 📂 4,456 页 Markdown 离线镜像知识库
├── skills/
│   └── noita-wiki-rag/        # 🤖 Agent Skill 规范目录 (SKILL.md)
├── rag/
│   ├── build_index.py         # 索引构建脚本 (切片 + BGE 向量生成)
│   ├── chunks.json            # 37,312 知识切片库 (Git LFS)
│   ├── index.npy              # BGE 密集向量索引 (Git LFS)
│   ├── query.py               # RAG 问答检索核心入口 (CLI)
│   ├── mcp_server.py          # 标准 Model Context Protocol 服务端
│   └── config.example.json    # 配置文件模板
├── mcp.chatbox.json.example   # ChatBox MCP 配置范例
└── mcp.local.json.example     # 本地 MCP 配置范例
```

---

## 📄 开源许可说明

- **知识库正文内容**：版权归 Noita Wiki 贡献者所有，遵循 [知识共享 署名-非商业性使用-相同方式共享 3.0 (CC BY-NC-SA 3.0)](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh-hans) 许可；
- **RAG 系统与工程代码**：`rag/` 及 `skills/` 下的检索算法与服务端代码均按 [MIT License](LICENSE) 授权开源。

> 💡 *免责声明：本仓库由 AI 辅助整理与维护，游戏机制复杂多变，重要机制信息建议以 [Noita Wiki (zh)](https://noita.wiki.gg/zh) 官方站或游戏最新版本实测为准。*
