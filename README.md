# Noita 中文知识库 · RAG 问答

《Noita》中文 Wiki 的离线镜像与本地问答系统。仓库包含 **4,456 页 Markdown 知识库**,
以及一套基于向量检索 + 重排 + 大模型生成的本地 RAG 问答工具,
支持 CLI、MCP server 与 Agent Skill 三种接入方式。

## 特性

- **离线知识库** — Noita 中文 Wiki 全部正文离线镜像,站内链接已改写为相对路径,本地编辑器(VS Code / Typora)可直接跳转浏览
- **RAG 问答** — 检索 → 重排 → 生成,回答自动附带来源引用
- **多种接入** — 命令行(CLI)、MCP server(stdio / HTTP)、Agent Skill(ChatBox / Claude Code 兼容)
- **开箱即用** — 向量索引已随仓库内置(Git LFS),克隆后无需重建

## 快速开始

```bash
git lfs install
git clone https://github.com/a1113622001/noita-wiki-zh.git
```

**查阅知识库**:打开 `pages/` 下的 Markdown 文件即可浏览;
`index.md` 是全量分类索引,`title_to_file.json` 是页面标题 ↔ 文件名映射。

**RAG 问答**(需 SiliconFlow API key):

```bash
pip install numpy mcp
cp rag/config.example.json rag/config.json   # 填入 API key,或设置环境变量 SILICONFLOW_API_KEY
cd rag
python query.py "黑洞法术怎么获得"          # 问答(检索 + 重排 + 生成)
python query.py "黑洞法术怎么获得" --no-llm  # 仅检索片段,不调用生成模型
```

## 接入方式

| 方式 | 适用场景 | 说明 |
|---|---|---|
| CLI | 命令行直接提问 | `rag/query.py`,支持单次提问与交互模式 |
| MCP | Reasonix / Claude Code / ChatBox | `rag/mcp_server.py`,暴露 `noita_query` / `noita_search` 工具 |
| Skill | ChatBox / Claude Code | `skills/noita-wiki-rag/`,会话中激活 `/noita-wiki-rag` |

## 目录结构

```
noita-wiki-zh/
├── index.md               # 全量页面分类索引
├── title_to_file.json     # 页面标题 → 文件名映射
├── pages/                 # 4,456 页 Markdown 知识库
├── skills/                # Agent Skill(标准格式)
└── rag/                   # RAG 问答系统(CLI + MCP + 索引构建)
```

## 技术栈

| 环节 | 方案 |
|---|---|
| 分块 | 按标题层级切分,保留标题上下文链(37,312 块) |
| Embedding | `BAAI/bge-m3`(1024 维) |
| 向量检索 | numpy 余弦相似度,Top-30 |
| 重排 | `BAAI/bge-reranker-v2-m3`,Top-6 |
| 生成 | `deepseek-ai/DeepSeek-V4-Flash`(SiliconFlow) |

## 许可

知识库内容版权归 Noita Wiki 贡献者所有,遵循
[CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh-hans)
许可(署名 · 非商业 · 相同方式共享),仅供学习与个人查阅。

> 本仓库由 AI 辅助生成与维护,内容可能存在错漏,重要信息请以
> [Noita Wiki (zh)](https://noita.wiki.gg/zh) 或游戏实测为准。
