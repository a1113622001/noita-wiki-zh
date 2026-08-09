# Mod

**分类:** [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Mod
---

模组制作导航  基础   
---  
入门 • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
    _**本页面 面向 模组制作者。关于 安装模组，请参阅[如何安装模组](如何安装模组.md)。**_
    _关于 已经存在的某个特定模组 的信息，请参阅[Mod:模组百科](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%A8%A1%E7%BB%84%E7%99%BE%E7%A7%91)。_

  
制作Noita的模组 是非常 简单 且 **有趣** 的，但是 这个过程 可能隐含了许多 具体实现的细节。这些页面 意在 降低 制作模组 的门槛、避开制作模组过程中常见的坑 

制作模组 只需要以下 工具： 

  1. 一个合适的 文本编辑器 （比如 VS Code、Sublime、Vim）
  2. 一个合适的 图像编辑器 （比如 Aseprite、Gimp、Paint.net、Photoshop）



Noita的 游戏逻辑 主要作为一个 [实体组件系统（ECS，Entity Component System）](https://en.wikipedia.org/wiki/Entity_component_system)，以 [Lua](https://www.lua.org/about.html) 和 [XML](https://en.wikipedia.org/wiki/XML) 语言实现。游戏中每个独立的 “东西”（敌人、子弹、魔杖、物品 甚至包括 玩家）都是 实体，只不过构成它们的组件不同。虽然在 没有任何编程知识 的情况下，通过 简单地编辑 实体XML 或 相关的 精灵表 也可以完成很多内容，但是还是推荐对Lua有所了解。 

## 入门

在继续下去之前，第一步是 找到 Noita本体 所在的文件夹 （大多数情况下位于 `C:\Program Files (x86)\Steam\steamapps\common\Noita`），然后阅读 `tools_modding\READ_ME_FIRST.txt`。 

### 提取数据文件

Noita的所有 基础资产（精灵表、脚本、实体定义）都被打包在 `[Noita\data\data.wak](Data.wak.md)` 中。 _技术层面_ 来说，提取这些文件 _并不是必须的_ ，但是查看 文件结构 和 示例代码 会非常有帮助。 

#### 对于 Windows平台

要访问 Noita的数据文件，请按照以下步骤操作： 

  1. 将 `tools_modding\` 文件夹 中的 所有文件 复制到 Noita的根目录。
  2. 运行 `data_wak_unpack.bat`。应该会打开 一个终端窗口。
  3. 应该会打开 一个包含Noita资源的 资源管理器窗口：`%UserProfile%\AppData\LocalLow\Nolla_Games_Noita` 。
  4. 将 这个文件夹 固定到快速访问 或 复制到 `一个之后方便访问的地方`。
  5. 很多资源可能是 隐藏的，要查看它们的话，点击 资源管理器 的 `查看` 选项卡，勾选 `显示/隐藏`分组 中的 `隐藏的项目` 即可。



现在你可以直接访问 Noita的所有Lua代码、实体XML定义、精灵表 啦，也就是说你现在可以 直接查看 游戏内容的秘密，所以要记得 不要剧透 哦。 

#### 对于 Linux平台

[![](https://noita.wiki.gg/zh/images/thumb/Launch_options.png/400px-Launch_options.png?1f1960)](/zh/wiki/Special:%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84/Launch_options.png "Special:文件路径/Launch options.png")

[](https://noita.wiki.gg/zh/wiki/File%3ALaunch%20options.png)

Launch options

  1. 在 Steam 上启动一次 Noita，在启动选项中加入参数 `-wizard_unpak`。（右键-属性-通用-启动选项）
  2. 这将会把 数据文件 提取到 `~/.steam/steam/steamapps/compatdata/881100/pfx/drive_c/users/steamuser/AppData/LocalLow/Nolla_Games_Noita/data`
  3. 再次移除启动选项。
  4. 添加书签或把文件夹复制到某个位置，以便以后访问。



### 下一步

已经开了个好头，那么接下来进一步阅读： 

  * 浏览 [模组制作 基础、调试、最佳实践](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80)
  * 将 `mods\example` 复制一份并对它进行一些更改，让你更熟悉 文件结构。
  * 熟悉 `tools_modding\` 目录下的 **文档** : 
    * `component_documentation.txt`（组件文档）
    * `lua_api_documentation.txt`（Lua API文档）
    * 这些是你能找到的 始终保持最新的文档。当下而言，它们是你最好的朋友。
  * 下载并查看 其它模组制作者制作的模组，编辑 这些模组，感受一下发生了什么变化。 
    * <https://modworkshop.net/game/noita>
    * [https://steamcommunity.com/workshop/browse/?appid=881100&](https://steamcommunity.com/workshop/browse/?appid=881100&)



## 需要帮助？

在 [Noita Discord 服务器](https://discord.gg/SZtrP2r) 的 `#modding-general` 和 `#modding-support` 有一个 活跃且有好的 关于模组制作的社区。大可放心加入并提问交流！ 

## 相关

  * [如何安装模组](如何安装模组.md)
  * [data.wak](Data.wak.md)


  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
