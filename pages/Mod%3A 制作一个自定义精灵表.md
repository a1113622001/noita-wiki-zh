# Mod:制作一个自定义精灵表

**分类:** [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Mod%3A%20%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8
---

模组制作导航  基础   
---  
[入门](Mod.md) • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • 精灵表 • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
定制或创建新的精灵表相对简单。但仍然建议在深入此处之前先了解[Mod:基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80)并设置好模组目录。 

大多数动物(即角色)的视觉部分由以下几部分组成： 

  * 基本动画精灵表
  * 热点精灵表
  * 污渍精灵表
  * 元数据 XML 定义精灵表所有属性：动画位置、名称、帧尺寸、速度等
  * 布娃娃文件夹



## 创建自定义玩家角色

接下来我们将以玩家角色为例进行讲解，因为它可能是被修改最多的角色 

### 动画精灵表

`data/enemies_gfx/player.png`

[![一份带标注的玩家角色精灵表，助你快速上手](https://noita.wiki.gg/zh/images/thumb/Player_spritesheet_helper.png/320px-Player_spritesheet_helper.png?7b0053)](/zh/wiki/File:Player_spritesheet_helper.png)

[](https://noita.wiki.gg/zh/wiki/File%3APlayer%20spritesheet%20helper.png)

玩家精灵表，已标注

为方便入门，你可以在右侧找到带有标注的玩家角色精灵表。 

  * 每一行代表一个动画。
  * 每个动画都有其独立的尺寸、帧数、播放速度、Y坐标、名称等参数。 
    * 这些参数不必与其他动画相匹配。
    * 只需确保与元数据XML文件中指定的数值保持一致即可。
  * 同一个动画在元数据中可以拥有多个名称，从而实质上可以充当多个不同的动画。



玩家角色的精灵表是目前Noita中最大的一个，其中包含近50种动画。并非所有动画都是必需的；有些极少播放，还有几个只是遗留内容。 

### 热点精灵表

`data/enemies_gfx/player_hotspots.png`

  * 用于定义角色额外附着点的简单位置坐标。 
    * 例如：有物理模拟的披风、用于持握魔杖的左臂位置等。
    * 也可用作射击、触发蹲下等动作的通用位置参考点。
  * 热点精灵表仅包含热点像素点，不包含任何其他内容。 
    * 热点位置同样可以直接在实体文件中通过简单的XY坐标定义，无需额外的精灵表。这在魔杖的设定中更为常见。
  * 每个热点都有其特定的颜色，十六进制颜色码必须与定义的值完全匹配。
  * 必须与玩家精灵表的尺寸完全一致(只需将其叠加在另一个图层上，然后单独保存即可)。
  * 热点实体附着在实际的玩家实体之上 `data/entities/player_base.xml`，但颜色值是在精灵表的元数据XML中定义的。



### 污渍精灵表

`data/enemies_gfx/player_uv_src.png`

  * 必须与主动画精灵表位于同一文件夹中。
  * 必须与玩家精灵表的尺寸完全一致。
  * `init.lua` 必须包含以下指向 **默认enemies_gfx目录** , 该目录需包含你要为其生成UV坐标的精灵图。 
    * `ModDevGenerateSpriteUVsForDirectory( "data/enemies_gfx" )`
  * 然后通过 `noita_dev.exe` 运行游戏，即可以生成UV贴图在**你自己的Mod目录** `data/generated/`。
  * 仅当你创建的是全新的“异形”角色时才需关注此问题。如果你只是简单地为玩家长袍更换颜色，默认的污渍系统可能依然适用。



### 元数据XML

`data/enemies_gfx/player.xml`

  * 动画可以绑定事件，比如"踢击"或"扔"；这对其内部运作非常重要。 
    * 实际上即使仅在Lua中手动播放动画，这些事件也会被触发： `GamePlayAnimation(player_entity, "kick", 10)`



### 布娃娃文件夹

`data/ragdolls/player/*`

该文件夹包含两个非常简单的部分：每个身体部位对应独立的图像文件，以及一个列出所有身体部位文件路径的文本文件。 

  * 布娃娃文件必须与精灵表中第一个动画 (即“参考帧”)的首帧尺寸完全一致。
  * 你可以自由设定布娃娃系统身体部位的数量。
  * 关节点会根据 **重叠** 像素自动生成。 
    * 换句话说：如果你不希望布娃娃系统只因浸水就散架，那么需要在你想连接的两个身体部件中至少保留一个“相同”的像素点。



  


### 额外功能: 披风颜色

除玩家外，少数敌人也拥有披风。通常需要通过Lua来修改其颜色。. 

玩家的披风具有特殊名称，因此您可以直接通过该名称来获取它：
    
    
    local cape = EntityGetWithName("cape")
    local cape_verlet = EntityGetFirstComponentIncludingDisabled(cape, "VerletPhysicsComponent")
    ComponentSetValue2(cape_verlet, "cloth_color", 0xFF0011BB)
    ComponentSetValue2(cape_verlet, "cloth_color_edge", 0xFF0011BB)
    

请注意，在Noita中颜色通常以“ABGR”格式定义，这与大多数图形软件通常显示的RGBA十六进制值顺序相反，所以其顺序依次为： 

  * 透明度（Alpha）： `FF`
  * 蓝色（Blue）： `00`
  * 绿色（Green）： `11`
  * 红色 （Red）： `BB`



## 尝试整合所有内容

编辑现有角色精灵表时，你有两种将文件添加进游戏的方式。 

要么直接替换 `data/` 文件夹中的所有文件。 

  * 这通常不是最佳方案，但对于简单的玩家角色Mod尚可接受，毕竟你通常不会同时激活多个此类模组。



或者用Lua在`init.lua`中手动设置这些值。 

  * 可能与其他模组有更好的兼容性。
  * 参考示例Mod `mods/starting_loadouts` 为例子以了解具体操作方法。



如果你正在创建一个全新的角色，只需将文件按你认为最合适的文件夹结构添加到`files/` 目录下即可。 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
