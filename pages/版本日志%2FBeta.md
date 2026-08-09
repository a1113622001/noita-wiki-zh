# Current Beta Changes

**分类:** [[Category:Beta_content]] · [[Category:Release_Notes]]
**来源:** https://noita.wiki.gg/zh/wiki/%E7%89%88%E6%9C%AC%E6%97%A5%E5%BF%97%2FBeta
---

[![Experimental](https://noita.wiki.gg/images/thumb/Information.png/44px-Information.png?c7ec8d)](/zh/wiki/File:Information.png "Experimental")

_本文(部分)信息描述的是Beta版本特有内容，目前不是正式版的一部分_

[![](https://noita.wiki.gg/images/thumb/Information.png/48px-Information.png?c7ec8d)](/zh/wiki/File:Information.png)

See previous notes: [Dec 2020 - Apr 2021](https://noita.wiki.gg/wiki/Release_Notes/Beta?oldid=21770), and [Undocumented Changes](https://noita.wiki.gg/zh/wiki/Undocumented%20Changes%3Faction%3Dedit%26redlink%3D1). 

This page serves as a home for all the known **beta changes** in the current up-to-date beta branch of the game.**This may include:**

  * Changes mentioned in patch notes.
  * Data-mined changes that were excluded from patch notes.
  * Images/gifs of new content.
  * Links to new articles or existing articles that have beta content, to serve as a quick reference when consolidating the information here into patch notes and updating affected articles after the beta content is added back into the main branch of the game.



When adding beta-branch content to any other pages, please place information in a separate section to the rest of the page (don't mix main branch and beta-branch information in the same sections), and ensure the **`{{[beta](https://noita.wiki.gg/zh/wiki/Template%3ABeta)}}`** template is added to any page or section that contains information from the beta branch of the game. 

For instructions on how to install the beta branch, see [How To Play Guide For Noita#Beta](https://noita.wiki.gg/zh/wiki/How%20To%20Play%20Guide%20For%20Noita%3Faction%3Dedit%26redlink%3D1). 

The official notes are [extracted](Modding.md) from `steamapps\common\Noita\_release_notes.txt`. 

New `FEATURE`s are linked. 

## Latest Beta Patches

### April 23 2021

Main Branch updated: [Release Notes#Apr 23 2021 - Hotfixes](Release Notes.md)

### April 22 2021

[![](https://noita.wiki.gg/images/thumb/Information.png/48px-Information.png?c7ec8d)](/zh/wiki/File:Information.png)

And more! Incl. 2 new [bosses](Enemies.md), and 3 new [Achievement Pillars](Achievement Pillars.md). 
    
    
    *GENERAL*
    FEATURE: New perk: [Iron Stomach](Iron Stomach.md)
    UPDATE: Nightmare mode - reduced the amount of blood
    

### April 21 2021

[![](https://noita.wiki.gg/images/thumb/Information.png/48px-Information.png?c7ec8d)](/zh/wiki/File:Information.png)

And a WHOLE BUNCH MORE! See below. 
    
    
    *GENERAL*
    FEATURE: 3 new [biome modifiers](Biome Modifiers.md)!
    FEATURE: New structure in a sandy area
    FEATURE: New, hidden structures deep underground
    FEATURE: New creature: [Toveri](Toveri.md)
    
    UPDATE: [Kuihduttajamestari](https://noita.wiki.gg/zh/wiki/Kuihduttajamestari%3Faction%3Dedit%26redlink%3D1) reworked into [Kohdennusmestari](Kohdennusmestari.md)
    UPDATE: More fish in a fishy place
    
    BUGFIX: Fixed a floating spoon
    BUGFIX: Orb room text was lacking a number
    
    *SPELLS*
    FEATURE: New spell: [Blood to Power](Blood to Power (1).md)
    FEATURE: New spell: [Omega Black Hole](Omega Black Hole.md)
    FEATURE: New spell: [Giga Holy Bomb](Giga Holy Bomb.md)
    
    BUGFIX: Further tweaks to Essence to Power
    

![Spoiler Warning](https://noita.wiki.gg/zh/images/thumb/Item_Emerald_tablet.png/42px-Item_Emerald_tablet.png?8687e8)

**This section contains undocumented changes, which will generally include quite a few spoilers**  


_点击以显示/隐藏内容_

  * Added Heart Mimics (named _dark_alchemist_ on their progress icon file. 
    * Sprite XML file is `data/enemies_gfx/coward_alt.xml`
    * Sprite image file is `data/items_gfx/normals_orb_base` (note the lack of a file extension; adding **.png** to the file name will allow you to open/view it).
    * Their enemy file is hidden in `data/entities/misc/effect_heart.xml`
  * A new [Celestial Scale](https://noita.wiki.gg/zh/wiki/Celestial%20Scale%3Faction%3Dedit%26redlink%3D1) structure is visible in the desert, dilapidated and ancient. Progressing the [Uusi Aurinko](Uusi Aurinko.md) questline will help you balance and restore the scale.
  * [Omega Black Hole](Omega Black Hole.md) was added as a reward for balancing the scale.
  * Additional [Achievement Pillars](Achievement Pillars.md) were added, relating to [Toveri](Toveri.md).
  * Modifications to Tiny ([Limatoukka](Limatoukka.md)): 
    * Added proper ragdoll sprites.
    * Now correctly drops loot, and drops **one** Tier 10 and **one** T6 [wand](Wand.md), rather than two T10 wands.
    * Is immune to [Touch of](Touch of.md) spells, freezing, and electric stun.
    * Is a little slower when turning.
    * Has a new projectile attack.
  * An array of "permanently drunk" creature variants were added, seemingly spawned in a rare easter egg pixel scene that has very specific spawn conditions. The spawn conditions are currently unknown, but may be related to the current date/time. 
    * [Beer Bottle](https://noita.wiki.gg/zh/wiki/Beer%20Bottle%3Faction%3Dedit%26redlink%3D1) items (previously seemingly unused) were overhauled and now contain a new liquid material, [juhannussima](https://noita.wiki.gg/zh/wiki/Juhannussima%3Faction%3Dedit%26redlink%3D1).
    * Regular [Potions](Potions.md) can rarely spawn with the new [juhannussima](https://noita.wiki.gg/zh/wiki/Juhannussima%3Faction%3Dedit%26redlink%3D1) material if those same date/time conditions are met.
  * [Haamukivi](Haamukivi.md)'s ethereal enemies now all deal contact damage in addition to their regular attacks.
  * [Toveri](Toveri.md) and [Kauhuhirviö](Kauhuhirviö.md): 
    * Both no longer have the _final_secret_orb_ tag; it has been replaced with _big_friend_ and _small_friend_ respectively.
    * [Toveri](Toveri.md) now gets extremely upset if you start killing his smaller friends. You have been warned.
    * Killing 9 small friends and then tackling Toveri is required to complete one of the new Achievement Pillars. You monster.
    * Now naturally spawn at 1 of 6 possible locations in the world, depending on the world seed.
  * [Stevari](Stevari.md) and [Skoude](Skoude.md) are now immune to suffocation / drowning.
  * The small controllable cart from the [Racetrack](https://noita.wiki.gg/zh/wiki/Racetrack%3Faction%3Dedit%26redlink%3D1) (a.k.a. _Karl_) can be used to more easily move the Suns for the [Uusi Aurinko](Uusi Aurinko.md) questline. 
    * Karl will no longer kill entities polymorphed into the small friend.
  * A pair of new [Books](https://noita.wiki.gg/zh/wiki/Books%3Faction%3Dedit%26redlink%3D1) was added, one each by the [Coral Chest](Coral Chest.md) and [Dark Chest](Dark Chest.md)
  * [Giga Black Hole](Giga Black Hole.md) no longer uses the same passive visual effect on wands as the regular [Black Hole](Black Hole (1).md), it has a new effect of its own.
  * [Spatial Awareness](Spatial Awareness.md) perk now shows Dark/Coral Chest locations, and the location of the Friend Room where Toveri is located.
  * A new [Book](https://noita.wiki.gg/zh/wiki/Books%3Faction%3Dedit%26redlink%3D1) has been added near the [Kuulokivi](Kuulokivi.md).
  * Checks looking for parallel world positions (shadow bosses and [Guiding Powder](Guiding Powder.md) mainly) have been adjusted and should work a bit better.
  * Perk removal via the [Nullification Altar](https://noita.wiki.gg/zh/wiki/Nullification%20Altar%3Faction%3Dedit%26redlink%3D1) should work a little more effectively to neutralize the effects of the [Lukki](Lukki Mutation.md) and [Leggy Mutation](Leggy Mutation.md) perk.
  * [Essence to Power](Essence to Power (2).md) was buffed immensely, and can quite easily destroy [Kolmisilmä](Kolmisilmä.md) even at high orb counts. 
    * This may be a bug / just overkill and is likely subject to change.



### April 20 2021
    
    
    *GENERAL*
    FEATURE: New structure in Hiisi Base
    UPDATE: Perk spawn balance has been tweaked
    
    *SPELLS*
    BUGFIX: Fixed [Essence to Power](Essence to Power (2).md) in rare cases lowering damage instead of increasing it
    
    *BUG FIXES*
    BUGFIX: Fixed game stats always displaying infinite symbol for gold
    BUGFIX: Optimized particle effects
    BUGFIX: [Electric Arc](Electric Arc.md) now causes electric damage
    

### April 16 2021

[![](https://noita.wiki.gg/images/thumb/Information.png/48px-Information.png?c7ec8d)](/zh/wiki/File:Information.png)

Also made the [Ylialkemisti](Ylialkemisti.md) immune to slice-damage. 
    
    
    *GENERAL*
    UPDATE: Steam Cloud - added a warning if the save is too big to sync
    UPDATE: Several enemies that used to be immune to freezing and electricity changed to only be immune to the stun, not the damage type
    
    *PERKS*
    UPDATE: Changed Kills to mana to give a buff effect instead of staining the player with mana-recharge liquid
    UPDATE: Increased Close Call's range and critical hit bonus slightly
    UPDATE: Personal Plasma Beam now slows down wands significantly less, and stacking it increases the beam length and damage
    

### April 15 2021

See [Release Notes#Apr 15 2021 - Hotfixes](Release Notes.md) \- Updates Merged to main branch. 

### April 14 2021
    
    
    *BUG FIXES*
    BUGFIX: Fast travel in PWs is now more stable
    BUGFIX: Rare crash in PWs fixed
    

### April 13 2021
    
    
    ﻿*BUG FIXES*
    BUGFIX: Physics body duplication bug should be fixed
    BUGFIX: Stability of PWs has been improved
    
    *MODDING*
    MODDING: Localization - loading translation files now reports errors
    

### April 12 2021
    
    
    ﻿*GENERAL*
    UPDATE: Added localization for missing items
    
    *BUG FIXES*
    BUGFIX: Rare bug in wand code fixed
    BUGFIX: Progress achievements sometimes failed
    BUGFIX: Typos in few descriptions have been fixed
    BUGFIX: Sauvojen Tuntija certain spawn configuration didn't work properly
    
    *MODDING*
    MODDING: Lua - added EntityGetHerdRelationSafe() 
    

### April 9 2021
    
    
    ﻿*GENERAL*
    UPDATE: Added support for 4th and 5th mouse buttons
    
    *BUG FIXES*
    BUGFIX: Fixed sprites that caused a minor graphics glitch
    BUGFIX: Inventory quick keys can now be mouse buttons
    BUGFIX: Update available notice should now work
    BUGFIX: Removal of the Lukki perk is now fixed
    BUGFIX: Too many error messages could have affected performance
    BUGFIX: Few rare crashes have been fixed
    
    *MODDING*
    MODDING: Options / Mod Settings - error spam reduced
    MODDING: Lua - added CellFactory_GetTags() 
    MODDING: Game now supports a greater number of CameraBounded entities
    

### April 2 2021 - HOTFIXES
    
    
    *GENERAL*
    UPDATE: Rooms holding secret items now look a bit prettier
    UPDATE: Explosive Box & Large Explosive Box should now work with more modifiers
    UPDATE: Explosive box spells are walk-through again
    UPDATE: Summon Rock works with more modifiers
    UPDATE: Achievement localizations on Steam and GOG
    UPDATE: Buffed a couple enemies slightly
    
    *BUG FIXES*
    BUGFIX: A miniboss no longer shoots tentacles from [ehm] the wrong place
    BUGFIX: Fixed Summon Rock disappearing at the slightest damage
    BUGFIX: Fixed certain player spells
    BUGFIX: Fixed a broken item room graphic
    BUGFIX: Unclickable slot in mod save slot select menu could be mouse focused
    BUGFIX: Continue game tooltip was a bit broken
     
    *PERKS*
    UPDATE: Exploding Gold stacks; the damage increases per stack
    UPDATE: Plague Rats stacks, stacking any rat-themed perks increases the amount of rats as well as their HP and damage
    UPDATE: Stacking fungal-themed perks increases the amount of mushrooms spawned by Cordyceps
    UPDATE: Mournful Spirit can be stacked; stacks increase damage and amount of ghosts per killed enemy
    
    *LOCALIZATION*
    FEATURE: 100% Finnished localization (Options, Language)
    
    *MODDING*
    MODDING: Mod save slot support - via game_mode_supports_save_slots="1" in mod.xml.
    
    *MODDING - DOCUMENTATION*
    MODDING: Lua API documentation - added a "t" to a word that was missing a "t"
    
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
  *[1/44.5]: 2.244%
  *[1/93.3]: 1.070%
  *[1/172]: 0.580%
  *[1/185]: 0.538%
  *[1/238]: 0.419%
  *[1/649]: 0.153%
  *[1/417]: 0.239%
  *[1/410]: 0.243%
  *[1/59.8]: 1.672%
  *[1/1428]: 0.069%
  *[1/1252]: 0.079%
  *[1/105]: 0.951%
  *[1/129]: 0.769%
  *[1/166]: 0.598%
  *[1/84]: 1.189%
  *[1/153]: 0.653%
  *[1/144]: 0.692%
  *[1/420]: 0.237%
  *[1/275]: 0.363%
  *[1/204]: 0.489%
  *[1/280]: 0.356%
  *[1/459]: 0.217%
  *[1/259]: 0.384%
  *[1/273]: 0.365%
  *[1/173]: 0.577%
  *[1/142]: 0.699%
  *[1/164]: 0.609%
  *[1/137]: 0.726%
  *[1/82]: 1.218%
  *[1/168]: 0.594%
  *[1/229]: 0.435%
  *[1/357]: 0.279%
  *[1/1377]: 0.072%
  *[1/324]: 0.307%
  *[1/285]: 0.349%
  *[1/313]: 0.319%
  *[1/688]: 0.145%
  *[1/250]: 0.399%
  *[1/178]: 0.559%
  *[1/156]: 0.638%
  *[1/117]: 0.853%
  *[1/210]: 0.475%
  *[1/891]: 0.112%
  *[1/1681]: 0.059%
  *[1/162]: 0.615%
  *[1/102]: 0.974%
  *[1/140]: 0.713%
  *[1/74.2]: 1.346%
  *[1/205]: 0.487%
  *[1/208]: 0.479%
  *[1/344]: 0.290%
  *[1/136]: 0.731%
  *[1/148]: 0.673%
  *[1/433]: 0.230%
  *[1/714]: 0.139%
  *[1/55.6]: 1.795%
  *[1/216]: 0.461%
  *[1/476]: 0.209%
  *[1/299]: 0.334%
  *[1/158]: 0.629%
  *[1/89.1]: 1.122%
  *[1/125]: 0.798%
  *[1/192]: 0.519%
  *[1/840]: 0.118%
  *[1/8206]: 0.012%
  *[1/445]: 0.224%
  *[1/626]: 0.159%
  *[1/196]: 0.508%
  *[1/149]: 0.668%
  *[1/63.6]: 1.571%
  *[1/1721]: 0.058%
  *[1/12.9k]: 0.007%
  *[1/14.2k]: 0.006%
  *[1/12.5k]: 0.007%
  *[1/1299]: 0.076%
  *[1/317]: 0.314%
  *[1/288]: 0.346%
  *[1/91.1]: 1.096%
  *[1/111]: 0.897%
  *[1/120]: 0.832%
  *[1/119]: 0.836%
  *[RNG]: 随机数生成器
  *[PRNG]: 伪随机数生成器
  *[1/222]: 0.448%
  *[1/2599]: 0.038%
  *[1/109]: 0.913%
  *[1/199]: 0.501%
  *[1/2857]: 0.034%
  *[HP]: 生命值
  *[1/6]: 16.66%
  *[1/236]: 0.423%
  *[1/519]: 0.192%
  *[1/336]: 0.297%
  *[1/22.2]: 4.489%
  *[1/219]: 0.454%
