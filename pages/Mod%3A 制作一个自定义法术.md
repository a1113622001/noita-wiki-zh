# Mod:制作一个自定义法术

**分类:** [Category:待翻译条目](Category%3A待翻译条目.md) · [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Mod%3A%20%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF
---

[![Spell transmutation.png](https://noita.wiki.gg/zh/images/thumb/Spell_transmutation.png/50px-Spell_transmutation.png?ea693f)](https://noita.wiki.gg/zh/wiki/Mod:%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF?action=edit)  
  
此页面的内容需要被翻译。

你可以帮助我们来翻译[此页面](https://noita.wiki.gg/zh/wiki/Mod:%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF?action=edit)。至于翻译的话请遵守[本Wiki的翻译准则](https://noita.wiki.gg/zh/wiki/Noita%20Wiki%3A%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5)。

  


模组制作导航  基础   
---  
[入门](Mod.md) • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • 法术 • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
It is recommended to have gone through the [Modding: Basics](Modding%3A Basics.md) and have a mod directory set up before delving deeper here. 

You can find all the existing vanilla spell IDs listed on the page [ID#Spells](https://noita.wiki.gg/zh/wiki/ID%3Faction%3Dedit%26redlink%3D1) or in the data files `data/scripts/gun/gun_actions.lua`. 

### A Note on nomenclature

Due to Noita's many phases of development, internally spells still use a sort of "card game" terminology: 

  * _actions_ are the spells themselves, consisting of everything one spell does (projectiles, physics objects, shields, magic effects, particles, etc.)
  * _cards_ are the "spell items" you pick up in the world and move around in your inventory and wands, and only contain a reference to the `action_id`



You don't usually need to care about this, but occasionally you might run into these references. 

## Registering your new spell

  1. Add a new file to your mod (eg. `files/actions.lua`), where you define all your custom spells by appending to the `actions` table provided by the base game Lua:
         
         table.insert(actions,
           {
             id                 = "MY_CUSTOM_SPELL",
             name               = "My Fancy Spell",
             description        = "Fancy spell doing fancy things",
             sprite             = "data/ui_gfx/gun_actions/air_bullet.png",
             type               = ACTION_TYPE_PROJECTILE,
             spawn_level        = "1,2",
             spawn_probability  = "1,1",
             price              = 80,
             mana               = 5,
             max_uses           = 120,  -- optional
             custom_xml_file = "data/entities/misc/custom_cards/torch_electric.xml", -- optional
             action = function()
               add_projectile("data/entities/projectiles/deck/light_bullet_air.xml")
         
               -- Examples for triggers:
               --add_projectile_trigger_hit_world("data/entities/projectiles/deck/light_bullet.xml", 1)
               --add_projectile_trigger_timer("data/entities/projectiles/deck/light_bullet.xml", 10, 1)
               --add_projectile_trigger_death("data/entities/projectiles/deck/mine.xml", 1)
             end,
           }
         )
         

_* ID must be all uppercase._
  2. Add the following line to the very beginning of your `init.lua`, referencing the file you just created:
         
         ModLuaFileAppend("data/scripts/gun/gun_actions.lua", "mods/<MY_FANCY_MOD>/files/actions.lua")
         

  3. Your new spell should now be found in the game, with mostly the default values we copied from "light air bullet".



## Spawning custom spells

Now that your spell _exists_ , you can test it by adding it to your custom wand directly, or spawning it via Lua:
    
    
    -- Easiest place to test new stuff, in reality the code could be anywhere.
    function OnPlayerSpawned(player)
      local x, y = EntityGetTransform(player)
      CreateItemActionEntity("MY_CUSTOM_SPELL", x+20, y)
    end
    

Note that the function doesn't seem to print/return any errors, so be wary of typos in SPELL_ID. 

## Customizing your new spell

Most of the fields found in the object we inserted into `actions` are quite self-explanatory, but a few notes on the special cases: 

  * `sprite` is the image of the _card_ (ie. what you pick up from the world), not the projectile
  * `type` can be any of the following known valid values: 
    * ACTION_TYPE_PROJECTILE
    * ACTION_TYPE_STATIC_PROJECTILE
    * ACTION_TYPE_MODIFIER
    * ACTION_TYPE_DRAW_MANY
    * ACTION_TYPE_PASSIVE
    * ACTION_TYPE_MATERIAL
    * ACTION_TYPE_UTILITY
    * ACTION_TYPE_OTHER
  * `max_uses` is optional, leaving it out or setting it to `-1` means unlimited uses
  * `action` is where most of the magic happens, this function is called upon shooting and can basically do anything you can think of with Lua 
    * This is where you register any projectiles you want to shoot upon using the spell (which you will have to define separately through XML)
    * This is also where you register any projectile triggers you might want (timer, hit_world, death)
    * This can also be entirely empty (see passive spells, like shields)
  * `custom_xml_file` is optional. Rarely needed, but super useful. This defines the XML for a custom _card_
    * In addition to controlling the world item, cards also work on the wand itself, attaching custom effects on them (like the electric torch)
    * Can be used to eg. make spell items physics objects, glow differently, etc.
    * If left empty, the file `data/entities/misc/custom_cards/action.xml` is used. You can note that the reference `ItemActionComponent::action_id` is empty. This is filled in silently in the background for each action.



  
For full list of all actions and great learning material, see `data/scripts/gun/gun_actions.lua`

## Creating a custom projectile

See `data/entities/projectiles/` for examples. 

Check out [Enums: RAGDOLL FX](Modding%3A Enums.md) for what effects your projectile can have. 

Note: The game affects some projectiles, for example Black Holes, with particular behaviours based on the Entity tags defined in the .xml file. It also searches for precise strings contained in said tags instead of checking the entire word, so for example utilizing the tag `"black_hole_custom"` the projectile is still recognized as one of said type. 

**WIP**
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
