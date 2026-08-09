# Mod:Lua脚本

**分类:** [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Mod%3A%20Lua%E8%84%9A%E6%9C%AC
---

模组制作导航  基础   
---  
[入门](Mod.md) • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • Lua脚本 • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
  
为Noita mods编写Lua脚本的基本信息和例子。请注意，脚本只是修改的一个组成部分,请务必阅读[ECS-实体组件系统(Entity Component System)](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80)有关内容。 

## Lua脚本基础内容

`init.lua`

  * 初见最好的文件
  * 不需要覆盖或者修改任何内容，这些内容都只作用于你的mod。
  * 参见 [模组修改基础知识](Modding%3A Basics.md)



`data/scripts/gun/gun.lua`

  * 每一次使用法杖时都会被调用, 与引擎代码高度交织在一起。
  * 注意兼容性，如下所述



`data/scripts/biomes/<biome_name>.lua`

  * 在进入生物群落时被调用一次
  * 注意兼容性，如下所述



`<LuaComponent>`

  * 可以挂载你的任意代码的最佳与最常用的地方。
  * 大多数其他的东西，你可以在`data/scripts/`找到，实际上是通过这个组件在某个实体中定义的。
  * 见官方的 `lua_api_documentation.txt` 以了解如何通过该组件挂载不同行为。



### 以兼容的方式使用钩子函数

当处理游戏本身和其他MOD大量使用的普通脚本文件时，通过`ModLuaFileAppend`函数对其进行 _附加_ 可能是一个好主意，而不是简单地通过`data/`路径覆盖它。 

如果每个模组制作者都这样做，他们的代码会根据玩家的mod加载顺序被挨个强行覆盖，只留下最后加载的那版文件。 
    
    
    -- 任何文件都可以被任何文件所附加，gun.lua只是一个例子。
    -- *但*这只能在init.lua内进行。
    ModLuaFileAppend("data/scripts/gun/gun.lua", "mods/mymod/files/gun.lua")
    

## Lua说明与提示

### 受限的库

一些默认的Lua库被限制，不能在mod文件中运行。一个不完整的受限库和函数的列表: 

  * IO
  * OS
  * require



这些库的一些功能已经在Lua API中重新实现。 
    
    
    -- 你没法这样做
    local file = require "/mods/MODNAME/files/somefile.lua"
    -- 但是你可以这样
    local file = dofile_once("/mods/MODNAME/files/somefile.lua")
    
    -- 你没法这样做
    local time = os.time()
    -- 但是你可以这样
    local year,month,day,hour,minute,second = GameGetDateAndTimeLocal()
    local time = year .. month .. day .. hour .. minute .. second
    

因为没有IO库，在多局游戏间保存持久性数据要困难得多。存储持久数据的仅有两种方法是使用Flag或`mod_settings`文件。 

## 脚本示例

### 获取当前实体
    
    
    local entity = GetUpdatedEntityID()
    

“当前实体”是指通过`<LuaComponent>`（或其他类似触发器）运行脚本的实体。不过并非所有脚本都是由实体运行的，例如`init.lua`。 

在上面的代码片段中，获得的实体可以是玩家、魔杖、投射物或者其他任何东西，这取决于脚本的运行位置。这是获取当前运行的实体的最简单方法，因此值得一提。 

**注意：** 在`data/scripts/gun/gun.lua`中这个函数会给你玩家实体。 

### 获取玩家实体

内置的utility脚本会返回一个玩家实体列表，所以我们必须经过一个小步骤才能得到单个玩家实体。 

简洁起见，下面的示例中省略了获取玩家实体的操作。许多钩子都已经能够获取玩家实体了，但这段代码可以留作备用，如果它们失效了没有返回玩家实体的话。 
    
    
    dofile_once("data/scripts/lib/utilities.lua")
    
    function get_player()
      local players = get_players()
      if players then
        return players[1]
      end
    
      -- 当找不到玩家（例如玩家死亡）时
      return nil
    end
    
    local player = get_player()
    

### 获取当前手持魔杖
    
    
    dofile_once("data/scripts/gun/procedural/gun_action_utils.lua")
    
    -- 可能适用于任何带有Inventory2Component的实体，例如一些敌人
    local wand = find_the_wand_held(player)
    

### 获取当前手持物品（包括魔杖）
    
    
    function get_held_item(animal)
      local inv_comp = EntityGetFirstComponentIncludingDisabled(
        animal, "Inventory2Component"
      )
    
      -- 尽管这个组件应该永远存在，但是指不定会有人点炒饭
      -- （比如另一个模组瞎搞把它搞没了之类的）
      if not inv_comp then
        return nil
      end
    
      return ComponentGetValue2(inv_comp, "mActiveItem")
    end
    
    -- 应该返回一个数字ID
    local wand = get_held_item(player)
    

### 简单地向物品栏中加入物品
    
    
    -- 注意，玩家不是唯一具有物品栏的实体
    function add_items_to_inventory(player, items)
      for _, path in ipairs(items) do
        local item = EntityLoad(path)
        if item then
          GamePickUpInventoryItem(player, item)
        else
          GamePrint("Error: Couldn't load the item ["..path.."]!")
        end
      end
    end
    
    function OnPlayerSpawned(player)
      local items = {
        "data/entities/items/pickup/thunderstone.xml",
      }
      add_items_to_inventory(player, items)
    end
    

### 生成并启用天赋
    
    
    -- 天赋系统有点复杂，所以使用现成的函数
    dofile_once("data/scripts/perks/perk.lua")
    
    local perk = perk_spawn(x, y, "PROTECTION_RADIOACTIVITY")
    
    -- 如果你只是想在世界中生成天赋，就把这部分去掉
    if perk then
      perk_pickup(perk, player, EntityGetName(perk), false, false)
    end
    

### 生成其他大多数事物
    
    
    -- 敌人
    EntityLoad("data/entities/animals/duck.xml", x, y)
    
    -- 黄金
    EntityLoad("data/entities/items/pickup/goldnugget_200.xml", x, y)
    

### 只加载一次init.lua

即只在开始新游戏时才加载，加载保存的已有游戏时不会加载 
    
    
    local LOAD_KEY = "MYMOD_FIRST_LOAD_DONE"
    
    function OnPlayerSpawned(player)
      if GlobalsGetValue(LOAD_KEY, "0") == "1" then
        return
      end
      GlobalsSetValue(LOAD_KEY, "1")
    
      -- 你其他的代码可以继续放在这里
    end
    

### 通过Lua发射一个投射物
    
    
    dofile_once("data/scripts/lib/utilities.lua")
    
    -- 根据你想要的发射规则，在此定义投射物发射的位置
    -- 以及投射物的速度
    
    shoot_projectile(player, "mods/mymod/files/projectiles/supernuke.xml", from_x, from_y, vel_x, vel_y)
    

要注意的是，用`GameShootProject()`也可以完成此功能，但它需要几行设置，而这段代码中包含的utility函数已经帮你完成了这些设置。 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
