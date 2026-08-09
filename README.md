# Noita 中文 Wiki 离线知识库

本知识库镜像自 [Noita Wiki (zh)](https://noita.wiki.gg/zh) 的全部正文内容页与分类页,转换为 Markdown 格式,供本地查阅与检索。附带一个基于 SiliconFlow API 的 RAG 问答系统(见 `rag/`)。

> 内容版权归 Noita Wiki 贡献者所有,遵循 [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh-hans) 许可。

## 从 git 克隆使用(跨机器迁移)

```bash
git clone https://github.com/a1113622001/noita-wiki-zh.git   # 需 git-lfs(git lfs install)
cd noita-wiki-zh
```

克隆后开箱即用(RAG 索引 `rag/index.npy` 与 `rag/chunks.json` 已随仓库托管)。
首次使用前:

1. 安装依赖:`pip install numpy mcp`(用你的 Python,推荐 conda)
2. 配置 API key:复制 `rag/config.example.json` 为 `rag/config.json` 填入你的
   SiliconFlow key;或设置环境变量 `SILICONFLOW_API_KEY`
3. 若索引损坏/想重建:`python rag/build_index.py`(约 40 分钟,支持断点续跑,需要免费额度)

> `rag/config.json` 含密钥,**不会被 git 跟踪**,勿外传。

## RAG 问答(rag/)

基于 BAAI/bge-m3(embedding)+ bge-reranker-v2-m3(rerank)+ DeepSeek-V4-Flash(生成)。

```bash
cd rag
python query.py "黑洞法术怎么获得"          # 问答(检索+重排+生成)
python query.py "黑洞法术怎么获得" --no-llm  # 只检索,不调用生成模型(省额度)
python query.py                              # 交互模式
```

- 索引: `rag/index.npy`(37,312 块 × 1024 维)+ `rag/chunks.json`
- 配置: `rag/config.json`(API key、模型、top-k 等;注意 key 含敏感信息,勿外传)
- 重建索引: `python build_index.py`(支持断点续跑,中断后重跑自动跳过已嵌入部分)
- 免费额度有限: 脚本串行低速调用,若遇 429 会自动退避重试

## 统计

- 抓取时间: 2026-08-09
- 内容页(主命名空间): 1263
- 分类页: 218
- 重定向页: 2975
- 页面总数: 4456
- 图片引用(仅记录,未下载): 42673
- 总大小: 41.3 MB

## 目录结构

```
noita-wiki-zh/
├── README.md            # 本文件
├── index.md             # 全量页面索引
├── title_to_file.json   # 页面标题 → 文件名的映射
└── pages/               # 所有 Markdown 页面
    ├── 法术.md
    ├── 敌人.md
    ├── Category%3A天赋.md
    └── ...
```

## 说明

- 站内链接已改写为相对路径,可在本地互相跳转(共约 35 万条,均有效)。
- 图片未下载,仅在正文中保留原始引用 URL(`https://noita.wiki.gg/zh/images/...`)。
- 重定向页内容为一行说明,指向目标页面。
- 页面内锚点(#章节)已去除,如需精确定位请直接打开对应文件搜索。

## 常用页面

- [Noita](pages/Noita.md)
- [法术](pages/法术.md)
- [法杖](pages/法杖.md)
- [天赋](pages/天赋.md)
- [敌人](pages/敌人.md)
- [地图](pages/地图.md)
- [魔药](pages/魔药.md)
- [材料](pages/材料.md)
- [状态](pages/状态.md)
- [道具](pages/道具.md)
- [炼金](pages/炼金.md)
- [Mod](pages/Mod.md)
- [世界观](pages/世界观.md)
- [攻略](pages/攻略.md)
