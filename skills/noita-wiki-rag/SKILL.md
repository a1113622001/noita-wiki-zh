---
name: noita-wiki-rag
description: 回答《Noita》游戏相关问题(法术获取、法杖构筑、天赋、敌人、Boss 血量、炼金、地图、世界观、攻略等),使用本地 Noita 中文 Wiki 知识库进行检索与 RAG 问答。当用户询问 Noita 游戏机制、法术/法杖搭配、怪物数据、流程攻略时使用本技能。
license: CC BY-NC-SA 3.0
compatibility: 需要 Python 3、numpy、mcp 库;RAG 生成需要 SiliconFlow API key(仅问答模式需要,纯检索/查文件不需要)。知识库索引已随仓库提供,克隆后开箱即用。
metadata:
  author: a1113622001
  repo: https://github.com/a1113622001/noita-wiki-zh
  version: "1.0"
---

# Noita 中文 Wiki 知识库 (RAG)

本技能让 AI 基于 Noita 中文 Wiki 的**离线知识库**(4,456 个 Markdown 页面 + 向量检索索引)
准确回答《Noita》游戏问题,而不是凭模型记忆猜测。

## 何时使用

用户问任何《Noita》相关的问题,例如:
- "黑洞法术怎么获得""某法术在哪找"
- "机枪杖怎么配""链锯搭配"
- "34魔球 boss 血量""三眼多少血"
- "真菌转换是什么""怎么炼金"
- 敌人属性、天赋效果、地图机制、攻略流程等

只要话题是 Noita 游戏内容,就应使用本知识库。若用户没提 Noita,不要用。

## 知识库位置

先定位仓库目录(二选一):

1. 若用户已克隆/已有本仓库,使用其路径(常见:当前工作目录、`noita-wiki-zh/`、`~/noita-wiki-zh` 等;找不到就问用户)。
2. 若本机没有,先克隆:
   ```bash
   git lfs install
   git clone https://github.com/a1113622001/noita-wiki-zh.git
   cd noita-wiki-zh
   ```

仓库结构:
```
noita-wiki-zh/
├── pages/            # 4,456 个 Markdown 页面(知识库本体,中文文件名)
│   ├── 法术.md
│   ├── 敌人.md
│   ├── Category%3A天赋.md
│   └── ...
├── title_to_file.json   # 页面标题 → 文件名映射
├── index.md             # 分类索引
└── rag/                 # RAG 系统
    ├── query.py         # 命令行问答
    ├── mcp_server.py    # MCP server
    ├── index.npy        # 向量索引(37,312 块)
    ├── chunks.json      # 分块元数据
    └── config.example.json  # 配置模板
```

## 使用方式(按优先级)

> 优先原则:若当前环境已接入 `noita-rag` MCP server(工具名 `noita_query` / `noita_search`),
> **优先直接调用 MCP 工具**——它封装了检索+重排+生成,结果稳定且快,不需要你手动跑命令。
> MCP 工具不可用时,再按下面的方式 A/B 降级执行。

### 方式 0:MCP 工具(如已接入)

- `noita_query(question)`:完整问答(检索+重排+LLM 生成),返回带来源引用。
- `noita_search(question, top_n)`:只检索片段,不调用生成模型(省额度)。

### 方式 A:直接查 pages/ 源文件(最快、离线、无需 key)

对明确目标页面,直接读 Markdown:
```bash
# 中文文件名直接搜索
grep -rl "黑洞" pages/ | head
# 读具体页面
cat "pages/法术.md"
```
文件名可能含 URL 编码(如 `Category%3A天赋.md`),用 `title_to_file.json` 查映射:
```bash
python -c "import json; m=json.load(open('title_to_file.json',encoding='utf-8')); print(m.get('黑洞','?'))"
```
站内链接已是相对路径,可跳转阅读。

### 方式 B:RAG 问答(检索+重排+LLM 生成,需 API key)

```bash
cd rag
python query.py "黑洞法术怎么获得"
```
- 依赖:`pip install numpy mcp`
- API key 配置(二选一):
  - `cp rag/config.example.json rag/config.json`,编辑填入 SiliconFlow key(https://siliconflow.cn 免费申请)
  - 或设置环境变量 `SILICONFLOW_API_KEY`
- 返回带 `[来源: 页面标题]` 引用的回答,用时约 7-20 秒。

### 方式 C:只检索片段(省额度,无 key 时也可用?——不,embedding 仍需 key)

```bash
python query.py "黑洞法术怎么获得" --no-llm
```
只返回相关片段,不调用生成模型。注意:embedding 检索本身仍需 SiliconFlow key。

## 回答规则

1. **优先用知识库事实回答**,不要凭模型记忆编造 Noita 数值/机制。
2. 回答关键事实时标注来源页面(`[来源: 法术.md]`)。
3. 知识库中没有的信息,明确说"知识库中未找到",不要猜测。
4. 若 API key 未配置或调用失败,退回方式 A(直接读 pages/ 文件)回答。

## 常见问题

- **`index.npy` 为空/很小**:该文件走 Git LFS,执行 `git lfs install && git lfs pull`。
- **`ModuleNotFoundError`**:`pip install numpy mcp`,确认用的是装了依赖的 Python。
- **429 限流**:SiliconFlow 免费额度有限,稍等重试,或改用 `--no-llm` / 方式 A。
- **内容准确性**:知识库由 AI 转换整理,可能有错漏;重要信息建议用户对照 Noita Wiki 官网(https://noita.wiki.gg/zh)或游戏实测。
