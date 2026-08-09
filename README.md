# Noita 中文 Wiki 离线知识库 + RAG 问答

《Noita》游戏的中文知识库与本地问答系统。仓库内含 Noita 中文 Wiki
(noita.wiki.gg/zh)全部正文内容的离线镜像,以及一套可本地运行的
向量检索(RAG)问答工具。

---

## ⚠️ AI 生成声明(请务必阅读)

本仓库由 **AI 工具辅助生成与维护**,具体包括:

- `pages/` 下的知识库页面:从 [Noita Wiki (zh)](https://noita.wiki.gg/zh)
  抓取后**经 AI 批量转换整理**(HTML → Markdown、链接改写、分块索引),转换过程可能引入错漏;
- `rag/` 下的 RAG 问答系统:由 AI 编写,回答依赖大语言模型,**可能存在幻觉或错误**;
- 知识库页面内容本身是社区维护的 Wiki 数据,可能已过时。

**使用前请注意甄别**:涉及游戏机制、数值、Boss 血量、攻略路线等关键信息,
建议以 [Noita Wiki 官网](https://noita.wiki.gg/zh) 或游戏实测为准。
本仓库不对任何内容的准确性、完整性作保证。

---

## 项目简介

- **知识库**:Noita 中文 Wiki 全部正文内容页,共 **4,456 个 Markdown 文件**,离线可查;
- **RAG 问答**:向本地工具提问(如"黑洞法术怎么获得""机枪杖怎么配"),系统会
  检索知识库 → 重排 → 生成带来源引用的回答;
- **零配置查阅**:克隆后直接打开 `pages/` 即可浏览,无需安装任何依赖。

> **版权说明**:知识库内容版权归 Noita Wiki 贡献者所有,遵循
> [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh-hans)
> 许可(署名 · 非商业 · 相同方式共享),仅供学习与个人查阅。

---

## 快速开始

### 1. 克隆仓库(需 Git LFS)

```bash
git lfs install
git clone https://github.com/a1113622001/noita-wiki-zh.git
cd noita-wiki-zh
```

> 向量索引(`rag/index.npy`,约 146MB)与分块数据(`rag/chunks.json`,约 44MB)
> 已通过 Git LFS 托管并随仓库下载,**克隆后即可使用,无需重新构建索引**。

### 2. 直接查阅内容(零配置)

打开 `pages/` 目录下的 Markdown 文件:

- `pages/法术.md`、`pages/敌人.md`、`pages/天赋.md` 等(中文文件名)
- `index.md`:按分类的全量页面索引
- `title_to_file.json`:页面标题 ↔ 文件名的映射
- 站内链接已改写为相对路径,在本地编辑器(VS Code / Typora 等)中可互相跳转

### 3. 使用 RAG 问答(需 SiliconFlow API key)

**安装依赖:**

```bash
pip install numpy mcp
```

**配置 API key**(二选一):

```bash
# 方式 A:复制配置模板并填写
cp rag/config.example.json rag/config.json
# 编辑 rag/config.json,把 "api_key" 填入你的 SiliconFlow key

# 方式 B:设置环境变量
export SILICONFLOW_API_KEY="你的key"        # Linux / macOS
$env:SILICONFLOW_API_KEY = "你的key"        # Windows PowerShell
```

SiliconFlow 注册:https://siliconflow.cn(免费额度可用于 embedding / rerank)。

**开始提问:**

```bash
cd rag
python query.py "黑洞法术怎么获得"            # 问答(检索 + 重排 + LLM 生成)
python query.py "黑洞法术怎么获得" --no-llm    # 仅检索片段(不调用生成模型,省额度)
python query.py                                # 交互模式,输入 exit 退出
```

示例输出:

```
=== 回答 (用时 7.2s) ===

根据知识库片段,34魔球对应的三眼(Boss)生命值为 **1,057,545,012,718 ♥**。
[来源: 三眼 | 三眼.md]

--- 引用来源 ---
[1] 三眼 | 三眼.md
```

---

## 在 ChatBox 中使用

以下两种方式均在 ChatBox 的 **工作模式** 下生效(输入框工具栏 → 机器人图标 → 工作模式)。

### 方式一:安装 Skill(推荐,最简)

本仓库附带标准 Agent Skills(agentskills.io 规范,兼容 Claude Code 技能),位于
`skills/noita-wiki-rag/`。安装二选一:

1. **从 GitHub 安装**:ChatBox → 设置 → 技能 → 从 GitHub 仓库安装,填入
   `https://github.com/a1113622001/noita-wiki-zh`;
2. **手动放置**:把 `skills/noita-wiki-rag/` 整个文件夹复制到本地技能目录
   (ChatBox 会自动发现 `~/.agents/skills/` 和 `~/.claude/skills/`)。

使用:会话中输入 `/noita-wiki-rag`(或技能面板点选)激活。AI 将按技能说明
自动定位知识库、优先读 `pages/` 源文件回答,需要时调用 `rag/query.py` 做 RAG 问答。

### 方式二:接入 MCP server(工具化)

ChatBox → 设置 → MCP → 添加自定义 server(本地 stdio,仅桌面端):

| 字段 | 值 |
|---|---|
| 名称 | `noita-rag` |
| 类型 | 本地(stdio) |
| 命令 | `python` |
| 参数 | `<仓库绝对路径>\rag\mcp_server.py` |
| 环境变量 | `PYTHONIOENCODING=utf-8` |

保存前需先点 **测试** 验证连通;启用后 `noita_query` / `noita_search` 工具注入给 AI。

### 两种方式的区别

- **Skill**:一份给 AI 的"说明书",AI 自行读文件/跑命令,零安装;
- **MCP**:标准工具接口,AI 直接调用封装好的工具,结果更稳定;
- 两者可同时使用(Skill 内已写明"MCP 优先,无 MCP 时降级读文件")。

---

## 在其他 MCP 客户端中使用(Reasonix / Claude Code 等)

将 `rag/mcp_server.py` 注册为 stdio MCP server:

```json
{
  "mcpServers": {
    "noita-rag": {
      "command": "python",
      "args": ["<仓库路径>/rag/mcp_server.py"],
      "env": { "PYTHONIOENCODING": "utf-8" }
    }
  }
}
```

暴露工具:

- `noita_query(question)`:完整问答(检索 + 重排 + LLM 生成);
- `noita_search(question, top_n)`:仅检索片段(省额度)。

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

流程:问题 → embedding → 向量检索 Top-30 → 过滤噪声块 → rerank Top-6 →
拼接上下文 → LLM 生成带来源的回答。

### 重建索引(一般不需要)

索引损坏或希望用更新内容重建时:

```bash
cd rag
python build_index.py
```

- 约 40 分钟(受 API 限流影响,串行低速调用,遇 429 自动退避重试);
- 支持断点续跑,中断后重跑自动跳过已嵌入部分;
- 消耗 SiliconFlow embedding 额度。

### 调整检索参数

编辑 `rag/config.json`:

```json
{
  "top_k_retrieve": 30,
  "top_n_rerank": 6
}
```

---

## 目录结构

```
noita-wiki-zh/
├── README.md              # 本说明
├── index.md               # 全量页面分类索引
├── title_to_file.json     # 页面标题 → 文件名映射
├── LICENSE                # CC BY-NC-SA 3.0
├── pages/                 # 4,456 个 Markdown 页面(知识库本体)
│   ├── 法术.md
│   ├── 敌人.md
│   ├── Category%3A天赋.md
│   └── ...
├── skills/                # Agent Skills(标准格式,兼容 ChatBox / Claude Code)
│   └── noita-wiki-rag/SKILL.md
└── rag/                   # RAG 问答系统
    ├── query.py           # 命令行问答
    ├── mcp_server.py      # MCP server(stdio / http 两种传输)
    ├── build_index.py     # 索引构建(断点续跑)
    ├── index.npy          # 向量索引(37,312 × 1024,Git LFS)
    ├── chunks.json        # 分块元数据(Git LFS)
    ├── config.json        # API key 配置(不入库,需自行创建)
    └── config.example.json # 配置模板
```

---

## 常见问题 (FAQ)

**Q: 克隆后 `rag/index.npy` 为空或很小?**
A: 该文件走 Git LFS。先执行 `git lfs install`,再 `git lfs pull` 拉取完整文件。

**Q: 报错 `ModuleNotFoundError: No module named 'numpy'/'mcp'`?**
A: 执行 `pip install numpy mcp`。若本机有多个 Python,请确认使用安装了依赖的解释器。

**Q: 报错 429 / 请求频繁?**
A: SiliconFlow 免费额度有限。脚本会自动退避重试,可稍等片刻再试,或改用 `--no-llm` 仅检索。

**Q: 回答不准确?**
A: 见顶部 AI 生成声明。RAG 可能产生幻觉,重要信息请对照 Noita Wiki 官网或游戏实测。

**Q: 图片在哪?**
A: 图片未下载(体积考虑),正文保留了原始 URL(`https://noita.wiki.gg/zh/images/...`),联网可查看。

---

## 统计

- 抓取时间:2026-08-09
- 页面总数:4,456(内容页 1,263 + 分类页 218 + 重定向页 2,975)
- 站内链接:约 35 万条(本地相对路径,0 断链)
- 图片引用:42,673 条(仅记录 URL)
- 知识库文本:约 40 MB;向量索引:146 MB

---

## 免责声明

本仓库由 AI 工具辅助生成与维护,内容来源于社区 Wiki,仅供学习交流。
**使用前请自行甄别内容准确性**;因内容错误、过时或使用方式导致的任何后果,
仓库作者不承担责任。商业用途请遵守
[CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh-hans) 许可条款。

- Noita 官网:https://noitagame.com
- Noita Wiki (zh):https://noita.wiki.gg/zh
