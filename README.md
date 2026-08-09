# Noita 中文 Wiki 离线知识库 + RAG 问答

> ⚠️ **AI 生成声明**
>
> 本仓库的**内容**(`pages/` 下的全部页面)是从 [Noita Wiki (zh)](https://noita.wiki.gg/zh)
> 抓取的原文镜像,**经 AI 工具批量转换整理**(HTML → Markdown、链接改写、索引构建),
> 并附带一套同样由 AI 搭建的 RAG 问答系统。
>
> **请读者注意甄别:** 转换过程可能引入错漏、页面内容可能已过时、RAG 回答也可能
> 存在幻觉或错误。涉及游戏机制、数值、攻略等关键信息,建议以
> [Noita Wiki 官网](https://noita.wiki.gg/zh) 或游戏实测为准。本仓库不对内容准确性作任何保证。

---

## 这是什么?

一套 **Noita 游戏的中文知识库 + 本地 RAG 问答系统**:

- **知识库**:Noita 中文 Wiki(noita.wiki.gg/zh)的全部正文内容页,共 **4,456 个 Markdown 文件**,离线可查。
- **RAG 问答**:基于向量检索 + 重排 + LLM 生成,向它提问游戏问题(如"黑洞怎么获得""机枪杖怎么配"),返回带来源引用的回答。

> 内容版权归 Noita Wiki 贡献者所有,遵循 [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh-hans) 许可(**非商业、署名、相同方式共享**)。本仓库仅作学习与个人查阅用途。

---

## 快速开始

### 1. 克隆仓库(需 Git LFS)

```bash
git lfs install
git clone https://github.com/a1113622001/noita-wiki-zh.git
cd noita-wiki-zh
```

> 索引文件(`rag/index.npy` 约 146MB、`rag/chunks.json` 约 44MB)通过 Git LFS 托管,已随仓库一并下载,克隆后开箱即用。

### 2. 只查阅内容(无需任何配置)

打开 `pages/` 目录下的 Markdown 文件即可,例如:

- `pages/法术.md`、`pages/敌人.md`、`pages/天赋.md`
- `index.md`(按分类的全量索引)、`title_to_file.json`(标题 ↔ 文件名映射)
- 站内链接已改写为相对路径,在本地编辑器(VS Code / Typora 等)里可互相跳转

### 3. 使用 RAG 问答(需要 SiliconFlow API key)

**a) 安装依赖**

```bash
pip install numpy mcp
```

**b) 配置 API key**

```bash
cp rag/config.example.json rag/config.json
# 编辑 rag/config.json,把 "api_key" 填成你的 SiliconFlow key
```

或者不建配置文件,直接设环境变量:

```bash
# Windows PowerShell
$env:SILICONFLOW_API_KEY = "你的key"
# Linux/macOS
export SILICONFLOW_API_KEY="你的key"
```

SiliconFlow 注册地址:`https://siliconflow.cn`(免费额度可用于 embedding/rerank)。

**c) 开始提问**

```bash
cd rag
python query.py "黑洞法术怎么获得"           # 问答(检索+重排+LLM 生成)
python query.py "黑洞法术怎么获得" --no-llm   # 只检索片段,不调用生成模型(省额度)
python query.py                               # 交互模式,输入 exit 退出
```

示例输出(节选):

```
=== 回答 (用时 7.2s) ===

根据知识库片段,34魔球对应的三眼(Boss)生命值为 **1,057,545,012,718 ♥**。
[来源: 三眼 | 三眼.md]

--- 引用来源 ---
[1] 三眼 | 三眼.md
```

---

## 技术架构

| 环节 | 方案 |
|---|---|
| 知识库来源 | Noita Wiki (zh),2026-08-09 抓取 |
| 页面规模 | 4,456 页(1,263 内容页 + 218 分类页 + 2,975 重定向页) |
| 分块 | 按标题层级切分,37,312 块,保留标题上下文链 |
| Embedding | `BAAI/bge-m3`(1024 维) |
| 向量检索 | numpy 余弦相似度,Top-30 |
| Rerank 重排 | `BAAI/bge-reranker-v2-m3`,取 Top-6 |
| 生成模型 | `deepseek-ai/DeepSeek-V4-Flash`(SiliconFlow) |
| API | SiliconFlow(`https://api.siliconflow.cn/v1`) |

流程:问题 → embedding → 向量检索 Top-30 → 过滤噪声块 → rerank Top-6 → 拼接上下文 → LLM 生成带来源的回答。

---

## 进阶用法

### 在 Reasonix / Claude Code 等 MCP 客户端中使用

本仓库附带一个 MCP server(`rag/mcp_server.py`),暴露两个工具:

- `noita_query(question)`:完整问答(检索+重排+生成)
- `noita_search(question, top_n)`:只检索片段(省额度)

在支持 MCP 的客户端(如 Reasonix、ChatBox、Claude Code)中,把 `rag/mcp_server.py`
注册为一个 stdio MCP server 即可:

```
command: python
args:    ["<本仓库路径>/rag/mcp_server.py"]
```

### 重建索引

索引损坏或想用新内容重建时:

```bash
cd rag
python build_index.py
```

- 约 40 分钟(受 API 限流影响,串行低速调用,遇 429 自动退避重试)
- 支持**断点续跑**:中断后重跑会自动跳过已嵌入部分
- 消耗 SiliconFlow embedding 免费额度,建议非高峰时段执行

### 调整检索参数

编辑 `rag/config.json`:

```json
{
  "top_k_retrieve": 30,   // 向量检索候选数
  "top_n_rerank": 6       // 重排后送入生成模型的片段数
}
```

---

## 目录结构

```
noita-wiki-zh/
├── README.md            # 本教程
├── index.md             # 全量页面分类索引
├── title_to_file.json   # 页面标题 → 文件名映射
├── LICENSE              # CC BY-NC-SA 3.0
├── pages/               # 4,456 个 Markdown 页面(知识库本体)
│   ├── 法术.md
│   ├── 敌人.md
│   ├── Category%3A天赋.md
│   └── ...
└── rag/                 # RAG 系统
    ├── query.py         # 命令行问答
    ├── mcp_server.py    # MCP server(供 Reasonix/ChatBox 等调用)
    ├── build_index.py   # 索引构建(断点续跑)
    ├── index.npy        # 向量索引(37,312 × 1024,Git LFS)
    ├── chunks.json      # 分块元数据(Git LFS)
    ├── config.json      # 你的 API key 配置(不入库)
    └── config.example.json  # 配置模板(入库)
```

---

## 常见问题 (FAQ)

**Q: 克隆后 `rag/index.npy` 是空的 / 很小?**
A: 该文件走 Git LFS,请先执行 `git lfs install`,再 `git pull` 重新拉取;或在仓库目录运行 `git lfs pull`。

**Q: 报错 `ModuleNotFoundError: No module named 'numpy'/'mcp'`?**
A: 执行 `pip install numpy mcp`。若本机有多个 Python,确认用的是安装了依赖的那个解释器(如 conda 环境)。

**Q: 报错 429 / 请求频繁?**
A: SiliconFlow 免费额度有限。脚本已自动退避重试;可稍等片刻再试,或改用 `--no-llm` 只做检索。

**Q: 回答不准确?**
A: 见顶部 AI 生成声明。RAG 可能产生幻觉,重要信息请对照 Noita Wiki 官网或游戏实测。

**Q: 图片在哪?**
A: 图片未下载(体积考虑),正文中保留了原始 URL(`https://noita.wiki.gg/zh/images/...`),联网可查看。

---

## 统计

- 抓取时间: 2026-08-09
- 页面总数: 4,456(内容页 1,263 + 分类页 218 + 重定向页 2,975)
- 站内链接: 约 35 万条(已改写为本地相对路径,0 断链)
- 图片引用: 42,673 条(仅记录 URL)
- 知识库文本: 约 40 MB;向量索引: 146 MB

---

## 免责声明

本仓库由 AI 工具辅助生成与维护,内容来源于社区 Wiki,仅供学习交流。
**使用前请自行甄别内容准确性**;因内容错误、过时或使用方式导致的任何后果,仓库作者不承担责任。
商业用途请遵守 [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh-hans) 许可条款。

- Noita 官网: https://noitagame.com
- Noita Wiki (zh): https://noita.wiki.gg/zh
