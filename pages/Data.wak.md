# Data.wak

**分类:** [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Data.wak
---

模组制作导航  基础   
---  
[入门](Mod.md) • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • Data.wak • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
data.wak 又称为“数据文件”，包含了原版游戏的资源。当你提取 Noita 游戏本体路径下的 `data.wak` 时可得到本页面的目录结构。制作模组时如果需要直接覆盖原版游戏的资源文件，必须准确按照下面的路径覆盖。 

在 Noita 的讨论中，如果对方提到“数据文件”或者以`data/`开头的路径，那么通常是指 data.wak 解包后的内容（也就是本词条的内容）。 

关于如何对 data.wak 进行提取，请参阅[提取数据文件](Mod.md)。 

## 内容介绍

也可以看看：[攻略：Noita文件路径](https://noita.wiki.gg/zh/wiki/%E6%94%BB%E7%95%A5%EF%BC%9ANoita%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%3Faction%3Dedit%26redlink%3D1)

下面列出的是可以在提取文件中找到的所有**根文件夹** ，重要的部分添加了注释。 
    
    
    data/
     ├── biome/
     │   └── 所有生物群系的定义XML文件，定义了群系元数据（名字、脚本、路径等等）
     │       以及生成参数（拓扑结构、植物生成等等）
     ├── biome_impl/
     │   └── 非王浩瓷砖的群系图像资源；像素场景和背景
     ├── buildings_gfx/
     ├── collapse_masks/
     ├── debug/
     ├── enemies_gfx/
     │   └── 包含敌人、友好生物、玩家；所有游戏中以“单位”形式存在的图像存放在这里
     ├── entities/
     │   └── 相对主要的部分，大多数实体的定义都可以在这里找到
     ├── generated/
     ├── global/
     ├── items_gfx/
     ├── materials_gfx/
     │   └── 具有除基础颜色外的材质信息的材料图像文件
     ├── particles/
     ├── procedural_gfx/
     ├── projectiles_gfx/
     ├── props_breakable_gfx/
     ├── props_gfx/
     ├── ragdolls/
     │   └── 对于需要布偶模型的敌人/友好生物，它们的布偶模型存放在这里
     ├── schemas/
     │   └── XML模式定义，缺少说明文档时，可以从这里获取详细信息，尽管可能不是很有用
     ├── scripts/
     │   └── 大部分的 Lua 代码，已经按照类别分成了不同子目录
     │   └── 比如 data/scripts/gun/gun_actions.lua 包含了一些法术的信息。
     ├── shaders/
     │   └── OpenGL 着色器文件，是完全可编辑的，但推荐用更新的Lua API
     ├── temp/
     ├── translations/
     ├── ui_gfx/
     ├── vegetation/
     ├── wang_tiles/
     │   └── 包含所有生物群系的王浩瓷砖
     └── weather_gfx/
    

## 寻找所需信息用于更新Wiki

  * 所有信息: 
    * UI 字符串：`common/Noita/data/translations/` 路径下的 `common.csv` 和 `common_dev.csv` 文件。
    * 图像：检查[新文件](https://noita.wiki.gg/zh/wiki/Special%3A%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6)（或者[分类:图像](https://noita.wiki.gg/zh/wiki/Category%3A%E5%9B%BE%E5%83%8F%3Faction%3Dedit%26redlink%3D1)）里是否有由其他贡献者新上传的内容。
    * 注：数据文件中所有的生命值和伤害值都是游戏中数值除以 25。例如 `hp="3.5"` 在游戏中实际显示 3.5 * 25 = 87.5 点生命值。
    * 数据文件中所有跟时间有关的数值（充能、延迟、存在时间等等）以 _帧_ 为单位计算。Noita 运行时将帧率锁定在 60fps，因此转换的比例就是 1 比 60。具有 200 帧存在时间的投射物会持续存在：`200 / 60 = 3.33s`。
    * XML 实体文件可以从其他实体文件中继承，这些继承关系会用带有引用父文件的 `<Base>..</Base>` XML 标签标记出。这种情况下，文件会继承另一个文件的所有组件和属性，并且能通过修改通常在 `<Base>...</Base>` _内部_ 的组件和属性对一部分内容进行重写。


  * 法术: 
    * `data/scripts/gun/gun_actions.lua`
    * `data/entities/projectiles/deck/`（包含的各种文件）
    * 施法延迟：`gun_actions.lua` 中的 `c.fire_rate_wait` 控制施法延迟。投射物和修正对施法延迟的重设和增减通过这个表中对应法术的施法函数实现。


  * 敌人: 
    * `data/entities/animals/`（包含的各种文件）
    * 查看[免疫](免疫.md)页面了解如何推断不同敌人拥有的免疫和防护。
    * 最主要的敌人信息包含在 Entity 标签和 DamageModelComponent 组件中。


  * 天赋: 
    * `data/scripts/perks/perk_list.lua`
    * `data/scripts/perks/`（包含的各种文件）
    * `data/scripts/essences/`
    * `data/entities/items/pickup/`
    * `data/entities/misc/essences/`


  * 法杖: 
    * `data/entities/items/wands/`（包含的各种文件）
    * `data/scripts/gun/procedural/`（包含的各种文件）



### 生物群系的代码名和游戏内名称/Wiki名称

代码名 | 游戏内名称/Wiki名称   
---|---  
coalmine | [矿场](矿场.md)  
coalmine_alt | [坍塌矿场](坍塌矿场.md)  
boss_arena | [实验室](实验室.md)  
boss_victoryroom | [伟大之作(结局)](https://noita.wiki.gg/zh/wiki/%E4%BC%9F%E5%A4%A7%E4%B9%8B%E4%BD%9C%5C(%E7%BB%93%E5%B1%80%5C) "伟大之作\(结局\)")  
crypt | [艺之神殿](艺之神殿.md)  
desert | [沙漠](沙漠.md)  
dragoncave | [龙窟](龙窟.md)  
excavationsite | [煤矿矿坑](煤矿矿坑.md)  
hills | [森林](森林.md)  
fungicave | [真菌洞穴](真菌洞穴.md)  
gold | [金矿](金矿.md)  
lake | [湖泊](湖泊.md)  
lava | [火山湖](火山湖.md)  
lavacave | [火山洞穴](https://noita.wiki.gg/zh/wiki/%E7%81%AB%E5%B1%B1%E6%B4%9E%E7%A9%B4%3Faction%3Dedit%26redlink%3D1)  
magic_gate | [庇护所](https://noita.wiki.gg/zh/wiki/Sanctuary%3Faction%3Dedit%26redlink%3D1)  
null_room | [无效化祭坛](无效化祭坛.md)  
pyramid | [金字塔](金字塔.md)  
rainforest | [地下丛林](地下丛林.md)  
sandcave | [砂之洞穴](砂之洞穴.md)  
secret_entrance | [神秘之门](https://noita.wiki.gg/zh/wiki/%E7%A5%9E%E7%A7%98%E4%B9%8B%E9%97%A8%3Faction%3Dedit%26redlink%3D1)  
shop_room | [秘密商店](席西基地.md)  
snowcastle | [席西基地](席西基地.md)  
snowcave | [积雪深渊](积雪深渊.md)  
town_under | [扭曲通道](扭曲通道.md)  
vault | [避难所](避难所.md)  
wandcave | [魔法神殿](魔法神殿.md)  
water | [水(生物群系)](https://noita.wiki.gg/zh/wiki/%E6%B0%B4%5C(%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB%5C) "水\(生物群系\)")  
winter | [落雪荒原](落雪荒原.md)  
holymountain | [神圣之山](神圣之山.md)  
tower | [魔塔](魔塔.md)  
vault_frozen | [冻结避难所](冻结避难所.md)  
clouds | [云景](云景.md)  
liquidcave | [古代实验室](古代实验室.md)  
secret_lab | [废弃炼金实验室](废弃炼金实验室.md)  
weathercrystal | [晶体密室](https://noita.wiki.gg/zh/wiki/%E6%99%B6%E4%BD%93%E5%AF%86%E5%AE%A4%3Faction%3Dedit%26redlink%3D1)  
greed_room | [财富殿堂](世界树.md)  
orbroom | [魔球室](真理魔球.md)  
wizardcave | [巫师巢穴](巫师巢穴.md)  
rainforest_dark | [蜘蛛巢穴](蜘蛛巢穴.md)  
mestari_secret | [王座室](王座室.md)  
ghost_secret | [遗忘洞穴](遗忘洞穴.md)  
winter_caves | [冰封峡谷](冰封峡谷.md)  
robobase | [发电站](发电站.md)  
fungiforest | [繁茂洞穴](繁茂洞穴.md)  
underwater | [沉没洞穴](https://noita.wiki.gg/zh/wiki/%E6%B2%89%E6%B2%A1%E6%B4%9E%E7%A9%B4%3Faction%3Dedit%26redlink%3D1)  
the_end | [伟大之作(地狱)](https://noita.wiki.gg/zh/wiki/%E4%BC%9F%E5%A4%A7%E4%B9%8B%E4%BD%9C%5C(%E5%9C%B0%E7%8B%B1%5C) "伟大之作\(地狱\)")  
the_sky | [伟大之作(天空)](https://noita.wiki.gg/zh/wiki/%E4%BC%9F%E5%A4%A7%E4%B9%8B%E4%BD%9C%5C(%E5%A4%A9%E7%A9%BA%5C) "伟大之作\(天空\)")  
potion_mimics | [拟态神庙](天空神庙.md)  
boss_sky | [Lohkare Temple](https://noita.wiki.gg/zh/wiki/Lohkare%20Temple%3Faction%3Dedit%26redlink%3D1)  
boss_sky2 | [奇石神庙](天空神庙.md)  
barren | [贫瘠神庙](天空神庙.md)  
darkness | [不祥神庙](天空神庙.md)  
watchtower | [瞭望塔](瞭望塔.md)
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
