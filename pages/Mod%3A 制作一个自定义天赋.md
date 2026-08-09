# Mod:制作一个自定义天赋

**分类:** [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Mod%3A%20%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B
---

模组制作导航  基础   
---  
[入门](Mod.md) • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • 天赋 • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
如果你已经读过了[Mod:基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80)，并且已经有了自己模组的文件夹，制作自定义天赋相对会比较简单。 

## 创建和注册自定义天赋

  1. 在你的Mod里新建一个文件（比如，`files/perk_list.lua`），之后定义的任何的自定义天赋都要通过这个文件添加到原版游戏提供的`perk_list`表中。每加一个天赋就把以下代码重复一遍：
         
         table.insert(perk_list,
           {
             id = "MY_CUSTOM_PERK",
             ui_name = "My Custom Perk Name",
             ui_description = "A Fancy Description",
             ui_icon = "data/ui_gfx/perk_icons/electricity.png",  -- 这里改成自己的图片
             perk_icon = "data/items_gfx/perks/electricity.png",  -- 这里改成自己的图片
             game_effect = "PROTECTION_ELECTRICITY",  -- 硬编码游戏效果，你可以改动或者删除这部分
             usable_by_enemies = false,
             not_in_default_perk_pool = false, --设为true的话在圣山的天赋池不会出现
             func = function( entity_perk_item, entity_who_picked, item_name )
               -- 拾取天赋时运行的代码写在这
             end,
           }
         )
         -- 如果还要加天赋的话
         table.insert(perk_list,
           {
             id = "MY_CUSTOM_PERK_TWO",
             -- 以此类推
           }
         )
         

  2. 把下面这一行代码加到你的`init.lua`的最前面，用来引用上面创建的文件：
         
         ModLuaFileAppend("data/scripts/perks/perk_list.lua", "mods/<MY_AWESOME_MOD>/files/perk_list.lua")
         

  3. 不错，我们的新天赋已经加入到游戏中了！



  
**注：**

`game_effect`通常是引擎中的硬编码效果，无法用Lua来自定义。我们只能要么把它们串接在一起，要么不要它们，重新写一个自定义的效果。当然两者混合也是可以的。 

[ID#天赋](https://noita.wiki.gg/zh/wiki/ID%3Faction%3Dedit%26redlink%3D1)页面或者`data/scripts/perks/perk_list.lua`可以帮助你查询到可用的游戏效果列表。 

## 生成和拾取天赋

如果你想通过脚本来加载自定义天赋（并且不依赖圣山），用下面一小段代码就可以生成并拾取天赋：
    
    
    -- 注：如果写在 init.lua 里，请写在 ModLuaFileAppend 这一行以及玩家生成 *之后* 
    -- 比如回调 OnPlayerSpawned 的过程中
    dofile_once("data/scripts/perks/perk.lua")
    function OnPlayerSpawned(player_entity)
        -- 把实体生成在玩家的位置
        local x, y = EntityGetTransform(player_entity)
        local perk = perk_spawn(x, y, "MY_CUSTOM_PERK")
        -- 如果要直接捡起的话可以继续写下面这句：
        perk_pickup(perk, player_entity, EntityGetName(perk), false, false)
    end
    

  


## 检查天赋是否生效

默认的`perk_pickup()`函数会给每个捡起的天赋加上一个“运行标记”，这个标记的形式是一个格式化字符串`PERK_PICKED_<PERK_ID>`。因此，你可以用下面这个函数简单地测试一个天赋是否已经处于生效中：
    
    
    function has_perk(perk_id)
      return GameHasFlagRun("PERK_PICKED_" .. perk_id)
    end
    

  


## 更多内容

  * 你可以在`data/scripts/perks/perk_list.lua`找到原版所有天赋的列表


  * 你可以在`data/scripts/perks/perk.lua`中找到天赋的基础实现 
    * 重点阅读函数：`perk_spawn()`和`perk_pickup()`



  

  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
