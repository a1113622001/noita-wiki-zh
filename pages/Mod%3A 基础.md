# Mod:基础

**分类:** [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Mod%3A%20%E5%9F%BA%E7%A1%80
---

模组制作导航  基础   
---  
[入门](Mod.md) • 基础 • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
本页旨在**简要** 介绍Noita修改的所有基本概念。ECS（即 Entity-Component-System（实体-组件-系统） 的缩写），目录结构，Lua钩子，等等 

## Mod的安装位置

两个常见的Mod位置是: 

  * `Noita/mods/` \- 手动下载的Mod或Mod开发。
  * `steamapps/workshop/content/881100/` \- 你通过Steam 创意工坊下载的Mod可以在这里找到。



## Mod目录结构

这是一个示例MOD，显示了你应该遵循的基本文件结构 
    
    
    myAwesomeMod/
    ├── data/
    │   └── enemies_gfx/
    │       └── player.png
    ├── files/
    │   └── my_custom_script.lua
    ├── init.lua
    └── mod.xml
    

让我们把它细分一下: 

  * `myAwesomeMod/`
    * 这是 根 文件夹，是你Mod的基本路径。这个myAwesomeMod是你所自定义的mod文件名，列如法术实验室mod的名字则是spell_lab。这直接就是mod文件夹的名字，需要谨慎起名，因为在之后的开发中这个名字的调用是必须要的。
  * `data/`
    * 这个文件夹的结构与我们之前提取的Noita的[数据文件](Data.wak.md)完全相同。 当你想覆盖基本资源时，请使用这个 _ONLY_ 。
  * `enemies_gfx/`
    * 一个储存所有精灵表的文件夹。（简单来说就是材质/贴图）
  * `player.png`
    * 米纳的动画精灵表（Minä|米纳，玩家控制的主角）。 在data/文件夹内，当这个mod被激活时，它直接替换了基本游戏的精灵表
  * `files/`
    * 这个文件夹用于存放所有你对于Mod所自定义的资源/脚本/数据，主要就是防止和其他mod冲突，自定义的内容应该放在这个文件夹里面。一般开发别动data文件里的内容为好。
  * `my_custom_script.lua`
    * 一个自定义的lua脚本文件，它可以做任何事情，也可以从任何地方调用。在自定义途中你可以给这个脚本起一个和功能相关的名字。
  * `init.lua`
    * 你制作Mod的起点，包括世界初始化的钩子，玩家生成之类的内容。这是一个"Hello world"的开始。
  * `mod.xml`
    * MOD元数据定义文件，包括mod名称、mod描述和一堆其他的初始设置。



### 引用不同路径中的文件

如上所述，`data/` 和 `files/` 这两个文件夹之间的行为非常不同。由于这个原因，你在其中引用的文件也略有不同。`data/` 基本上可以看作是Noita内部自己的虚拟文件系统，可以直接引用，但其他一切都需要有你的完整mod路径。 例如Lua中的文件，同样具有上述结构。
    
    
    -- 数据文件的部分路径（当被覆盖时也是如此，即使它不包括在你自己的mod中）
    dofile_once("data/scripts/lib/utilities.lua")
    
    -- 自己脚本的完整路径
    dofile_once("mods/myAwesomeMod/files/scripts/my_custom_script.lua")
    

在定义路径时，同样的事情也适用于XML。 (例如，精灵表、投射物、效果，任何东西)

## 实体组件系统基础知识

实体是基于一些简单的规则: 

  * 可以包含任何数量的组件，甚至是相同的组件
  * 可以有子实体，定义它们自己的组件
  * 可以继承其他实体，复制其功能
  * 只可以有一个名字（name）
  * 可以有多个标签（tags）



### 例子

让我们从基本游戏文件中分解出一个实体的例子: `data/entities/props/banner.xml`
    
    
    <Entity tags="prop">
    
      <VelocityComponent />
    
      <SimplePhysicsComponent />
    
      <SpriteComponent
        z_index="1"
        image_file="data/props_gfx/banner.xml"
        offset_x="0"
        offset_y="0"
      ></SpriteComponent>
    </Entity>
    

这是你能找到的最简单的实体之一，里面只有三个组件组成。如果在游戏中产生，你应该看到一个简单的动画旗帜掉落在地上，没有任何特殊功能。 

  * `VelocityComponent`速度组件：一般来说，任何与物理有关的东西都需要有一个 "物理学"组件。它可以定义一些东西 (如个别实体的重力), 但在这里我们只是用默认值启动它。你可以在下面找到所有的值 `component_documentation.txt`。
  * `SimplePhysicsComponent`简单的物理组件：赋予这个实体非常简单的物理属性。它会一直往下掉，或停在任何墙壁上，通常不能与一般的物理对象发生碰撞，也不能被踢到。对于适当的物理学，你需要一个物理体组件（PhysicsBodyComponent）和物理形状组件（PhysicsShapeComponent），你可以在数据文件中找到许多不同的例子。
  * `SpriteComponent`精灵组件：简单地将一个图像文件附加到实体上，并带有任何指定的偏移量等。这里定义了一个XML文件作为图像的来源，当你想在实体上添加动画精灵时，这是很有必要的。如果你的精灵图是一个静态图像，你也可以在这里直接引用它。



让我们看一下图像文件 `data/props_gfx/banner.xml` :
    
    
    <Sprite
      filename="data/props_gfx/banner.png"
      offset_x="12"
      offset_y="30"
      default_animation="stand">
    
      <!-- stand -->
      <RectAnimation
        name="stand"
        pos_x="0"
        pos_y="0"
        frame_count="7"
        frame_width="32"
        frame_height="32"
        frame_wait="0.11"
        frames_per_row="7"
        loop="1"
      ></RectAnimation>
    </Sprite>
    

这些独立的元数据文件本质上是在实体组件系统之外的，它们只是以与其他一切相同的XML格式定义精灵元数据。因此，在`component_documentation.txt`中找不到XML元素的文档，因为这些不是组件也不是实体。但是，让我们把这个问题也分解一下： 

  * 在这里，我们终于引用了我们想要绘制的实际图像文件


  * 主要内容 `<Sprite>` 中的元素仅有一个 `<RectAnimation>` 子元素，它可以有多个这样的元素，每个动画都有一个 (对任何角色都是正常的)


  * 动画的名字（name）是 "站立（stand）"，它也被引用为默认动画。名称（name）可以是任何东西，但必须与使用它们的东西相匹配。（这是编程基本规则）


  * `frame_*` 属性是不言自明的，但基本上是定义动画时最重要的部分。这些必须与你的图像文件中的精灵表相匹配。



你可以去看看这个文件`data/props_gfx/banner.png`, 这一切应该就变得相当明了了。 

## 创建和删除实体

有许多方法可以让你产生/杀死实体。最简单的方法是直接使用Lua: 

  * 生成时用`EntityLoad("path/to/entity.xml" , x, y)`
  * 删除用`EntityKill(entity_id)`



仅仅作为一个例子，其他可能的生成/清除地点包括: 

  * `ProjectileComponent::spawn_entity`投射物组件的spawn_entity可用于在投射物碰撞时生成任何实体。
  * `CameraBoundComponent`摄像机边界组件可以用来限制经常使用的实体的生成率/距离 (例如：敌人，灯笼，......)
  * `LifetimeComponent`存在时间组件，从字面上看是给了一个实体一定的存在时间
  * `DamageModelComponenet`损伤组件使得实体拥有命中率和受到伤害。实体在生命值变成0时被杀死。
  * ...除此之外还有更多



## 标签

实体和组件 _都_ 可以有任何数量的**标签** （**tags** ）附加在它们身上。标签是对一种 "事物 "进行分类的非常简单的方法，而且可以很容易地即时创建，不需要任何额外的定义。例如，获取玩家周围所有敌人的列表就是这么简单。`EntityGetWithTag("enemy")`。 
    
    
    来自翻译：EntityGetWithTag("enemy")这段代码是说实体获取标签（EntityGetWithTag）叫做 敌人（enemy）
    

大多数标签没有任何其他内容，但有一组[特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE)其中有引擎内硬编码的功能附加在它们身上 

**注释：**

  * 实体标签被定义在`tags` 当中,而组件标签是在 `_tags` 当中。
  * 引擎目前只支持非常有限**自定义标签** ，这些标签在所有MOD中都是全局性的(也就是所有mod共享)。这对于模型间的兼容性来说非常重要，请记住这一点。 
    * 通过社区测试，目前的上限似乎是`tags`224个，`_tags`则是210个。
  * [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE)是Noita整个实体-组件系统的重要 _组成部分_ ，所以请务必阅读该页面。


    
    
    需要注意的是，由于tag有上限，所以能用name就用name。
    

## 实体继承

  * 通过以下方式执行`Base`基础实体组件。 
    * 基础实体组件的文件路径在`file`文件夹里。
  * 通过定义新的 _**内部**_ 基础元素标签覆盖基础实体组件。 
    * 当覆盖时，基础（Base）实体**必须** 有你试图覆盖的组件被定义。否则会发生错误。
  * 你自己增加的内容通常在基础元素之外。


  * 你可以随心所欲地继承多个基础实体
  * 所有的实体标签都会被捆绑在一起



## 关于组件

官方在游戏根目录的 Noita/tools_modding/component_documentation.txt 记载了所有你能使用的组件 

每个组件都拥有特殊的标签属性，至少我测试下来，可以搞多个LuaComponent然后在不同的时机激活，配合其他组件使用完成复杂逻辑。 

这里举两个例子 

_tags="" 比如：enabled_in_world, enabled_in_hand, enabled_in_inventory, ...... 

_enabled="0" 比如：[0, 1] 

你可以这样快速决定这个组件是否一开始就激活？在世界激活？在玩家手上激活？ 详细可见 [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE)

## init.lua

为任何mod运行的第一段代码。包括预先确定的函数名称，你可以用它来连接某些事件，并提供一个地方来收集你的mod的所有文件重写。 

下面的内容几乎是直接取自`mods/example/init.lua`的。 所有的代码都是可选的，你可以只填写你需要的部分。 

### 可用的功能钩子
    
    
    -- 在加载一个新的(?)游戏时按顺序调用。
    function OnModPreInit() end
    function OnModInit() end
    function OnModPostInit() end
    
    -- 当播放器实体被创建时调用，并确保播放器周围的区块已经被加载和创建。
    function OnPlayerSpawned(player_entity) end
    
    -- 当玩家死亡时被调用。
    function OnPlayerDied( player_entity ) end
    
    -- 一旦游戏世界被初始化就会被调用。 不保证玩家周围有任何大块的东西。
    function OnWorldInitialized() end
    
    -- 每当游戏要开始更新世界时，都会调用。
    function OnWorldPreUpdate() end
    
    -- 每当游戏完成更新世界时，都会调用。
    function OnWorldPostUpdate() end
    
    -- 当生物群落配置被加载时被调用。
    function OnBiomeConfigLoaded() end
    
    -- 最后一点是Mod API可用的地方。在这之后，materials.xml将被加载。
    function OnMagicNumbersAndWorldSeedInitialized() end
    
    -- 当游戏暂停或取消暂停时调用。
    function OnPausedChanged( is_paused, is_inventory_pause ) end
        
    -- 如果玩家在游戏暂停时改变了任何MOD设置，将在游戏取消暂停时被调用。
    function OnModSettingsChanged() end
    
    -- 将在游戏暂停时被调用，可以由暂停菜单或一些库存菜单调用。请注意这一点，因为在游戏暂停时调用，并不是所有东西都会表现良好。
    function OnPausePreUpdate() end
    

### 覆盖和扩展系统

这些句子通常被添加到`init.lua`的末尾/开头。这段代码在所有mods的文件系统被注册后运行。
    
    
    -- 基本上dofile("mods/mymod/files/actions.lua")会出现在gun_actions.lua的末尾
    ModLuaFileAppend("data/scripts/gun/gun_actions.lua", "mods/mymod/files/actions.lua")
    
    -- 同理，但对于药水来说
    ModLuaFileAppend("data/scripts/items/potion.lua", "mods/mymod/files/potion_appends.lua" )
    
    -- 将使用指定的文件覆盖一些神奇的数字
    ModMagicNumbersFileAdd("mods/mymod/files/magic_numbers.xml")
    
    -- 将你自己的材料附加到游戏的材料列表中
    ModMaterialsFileAdd("mods/mymod/files/custom_materials.xml")
    
    -- 使用这个来注册自定义的fmod事件。事件映射文件可以通过FMOD Studio中的文件->导出GUIDs生成。
    ModRegisterAudioEventMappings("mods/mymod/files/audio_events.txt")
    

## 重要而有趣的文件

### 方便的实现

`data/magic_numbers.xml`

  * 很多变量可以控制游戏和玩法许多方面的行为。从虚拟分辨率（用于控制你所看到的区块的数量）到生物溢出的血量，很好实行。



`data/scripts/lib/utilities.lua`

  * 大量由Nolla集成的实用功能。包括很多基本的2D平台游戏的数学帮助，ECS和更多别的。通过阅读就可以了解事物的工作原理，而不是多次重新实现基本的东西。



### 开始时可能不太有用

`data/genome_relations.csv`

  * 游戏中的所有生物（包括玩家）对彼此关系的表格。
  * 可以自由编辑；例如，让所有生物都对玩家友好到爆炸。



`data/translations/common.csv`

  * 包括游戏的所有基本翻译。很适合交叉连接某些法术名称，因为在游戏中看到的大部分文字实际上并不存在于代码中，而是在这里。
  * 也可以自由编辑，让你可以重命名/重写任何法术或游戏的文本内容。
  * 该文件处于Noita游戏文件夹中而不是导出的data文件夹中。



`data/scripts/wang_scripts.csv`

  * "全球 "生物群落功能注册。这里定义的任何名称都可以用于所有的地区和像素场景
  * 注意：所有的生物群落仍然需要单独实现这些功能
  * 可以自由编辑，加入自己的内容。



`data/shaders/post_final.frag`

  * 主要的 "OpenGL着色器 "文件，可以自由编辑和添加以创建你自己的着色器效果。如果没有编程/着色器的经验，不建议使用。



### 好玩的清单

  * 材料: `data/materials.xml`
  * 天赋: `data/scripts/perks/perk_list.lua`
  * 魔药: `data/scripts/items/potion.lua`
  * 法术: `data/scripts/gun/gun_actions.lua`
  * 状态: `data/scripts/status_effects/status_list.lua`
  * 关于如何扩展这些功能，见上文init.lua的部分。



## 调试工作（debug）

Noita目前没有任何一种专门的IDE/测试环境用于开发。很多开发时间确实会花在重启游戏以尝试新的变化上。下面是调试Noita mods的最常见的方法列表: 

  1. 开发建设 `noita_dev.exe`: 
     * 从一个开发控制台开始。这是直接发现你的Lua/XML中发生的任何错误的最好方法
     * 该可执行文件应位于 `tools_modding/`，但只能从根目录下启动(即旁边的`noita.exe`)。如果你到目前为止一直遵循指示，它应该已经在那里了。
     * 按下`F1`来显示绑定键的列表。 按下`F5`来启用大多数调试功能。
     * 需要看到的是`print()`输出到控制台，但 `GamePrint()` 在任何地方仍然有效(在游戏中显示在左下角的位置).
     * 注意：众所周知，这对许多人来说会降低性能。因此，经常在这两种构建之间切换是完全可以的。
  2. 记录到文件中: 
     * 通过特定的魔法数字启用。
     * 或者下载一个不错的MOD，它可以为你做这个: [Modworkshop](https://modworkshop.net/mod/25910)
     * 记录到 `Noita/logger.txt`
  3. 欺骗性的GUI模型: 
     * 很适合测试游戏功能，不需要摆弄任何调试功能。
     * 生成物品/天赋/法杖，传送，增加生命值，等等。所有这些都直接来自游戏中的HUD
     * 下载: [[Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=1984977713) | [Github](https://github.com/probable-basilisk/cheatgui)]
  4. Noita 还支持 [Decoda Lua debugger](https://unknownworlds.com/decoda/): 
     * 需要单独设置。说明见 `tools_modding/lua_debugging.txt`



**注意:** 游戏应该在任何MOD文件发生变化时进行检测，从而在开始新游戏时硬重启游戏，但目前已知这并不太可靠。因此，现在建议你总是通过手动退出/关闭游戏来完全重新启动你的游戏。 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
