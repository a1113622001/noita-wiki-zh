<div align="center">

# 🪄 Noita 中文知识库 · RAG 问答助手
### 📚 4,456 页 Markdown 离线知识库 + BGE 向量检索 + DeepSeek 生成 + MCP / Agent Skill 协议接入

[![Pages](https://img.shields.io/badge/Wiki%20Pages-4%2C456-blue?style=flat-square&logo=gitbook)](pages/)
[![Chunks](https://img.shields.io/badge/RAG%20Chunks-37%2C312-orange?style=flat-square)](rag/chunks.json)
[![MCP](https://img.shields.io/badge/MCP%20Server-Standard%20Ready-green?style=flat-square&logo=openai)](https://modelcontextprotocol.io/)
[![DeepSeek](https://img.shields.io/badge/LLM-DeepSeek--V3%20%2F%20R1-blue?style=flat-square)](https://deepseek.com)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![License: CC BY-NC-SA 3.0](https://img.shields.io/badge/Wiki%20License-CC%20BY--NC--SA%203.0-orange.svg?style=flat-square)](LICENSE) [![Code License: MIT](https://img.shields.io/badge/Code%20License-MIT-brightgreen.svg?style=flat-square)](LICENSE)

[简体中文](./README.md) · [快速开始](#-快速开始) · [MCP 接入指南](#-mcp-接入指南) · [Agent Skill](#-agent-skill)

</div>

---

## 📖 项目简介

**noita-wiki-zh** 是为著名 Roguelike 魔法探索游戏《Noita》打造的**全量中文离线知识库与智能化 RAG 本地问答系统**。

包含全量爬取并经过深度清洗转换的 **4,456 页 Markdown 页面**，以及一套基于 **BGE 密集向量检索 + 重排 + DeepSeek 模型生成** 的本地 RAG 问答套件，全面支持 **CLI 终端**、**MCP Server（stdio / HTTP）** 和 **Agent Skill** 接入。

---

## 🏗️ 架构与数据流

```mermaid
graph LR
    subgraph 知识库层 (Knowledge Base)
        A[4,456 页 Wiki Markdown] --> B[按标题层级切分 Hierarchical Chunking]
        B --> C[37,312 文本块 + 面包屑链]
        C --> D[BGE 密集向量索引 index.npy]
    end

    subgraph 检索引擎 (RAG Engine)
        Q[用户提问] --> E[NumPy 极速余弦相似度初筛]
        D --> E
        E --> F[Top-K 上下文组装与重排]
        F --> G[DeepSeek LLM 融合生成]
    end

    G --> R[带精准引用来源的专业答复]
```

---

## ✨ 核心特性

- 📖 **100% 离线知识库**：正文内所有站内链接均转换为相对路径，在 VS Code、Obsidian、Typora 中无损离线跳转浏览。
- 🧩 **层级感知切分（Hierarchical Chunking）**：切片时保留完整上级标题上下文（如 `法术 > 投射物修饰 > 触发机制`），彻底根绝切片碎片化导致的检索偏离。
- ⚡ **开箱即用免安装库**：向量索引已随仓库打包（Git LFS），本地无需拉起 Milvus / Chroma 数据库，纯 NumPy 矩阵运算毫秒级返回。
- 🌐 **全生态多端协议打通**：支持命令行独立提问、标准 MCP Server 暴露、Agent Skill 标准目录接入。

---

## 🔌 接入方式

| 接入形态 | 适用场景 / 客户端 | 启动与配置方式 |
| :--- | :--- | :--- |
| **CLI 命令行** | 终端直接问答 / 纯检索模式 | `python rag/query.py "黑洞法术怎么获得"` |
| **MCP Server** | ChatBox / Claude Code / Reasonix / Cursor | `python rag/mcp_server.py` |
| **Agent Skill** | 支持标准 Skill 调用的 Agent 平台 | 激活目录 `skills/noita-wiki-rag` |

---

## 🚀 快速开始

```bash
# 1. 安装 Git LFS 并克隆仓库
git lfs install
git clone https://github.com/a1113622001/noita-wiki-zh.git
cd noita-wiki-zh

# 2. 安装依赖
pip install numpy mcp

# 3. 配置 API Key (SiliconFlow / DeepSeek)
cp rag/config.example.json rag/config.json
# 编辑 config.json 填入你的 API Key (或设置环境变量 SILICONFLOW_API_KEY)

# 4. 执行问答
python rag/query.py "如何合成点金石"
```

---

## 📄 开源许可证

本项目知识库内容遵循游戏 Wiki 原协议，RAG 工具代码采用 [MIT License](LICENSE) 开源。
