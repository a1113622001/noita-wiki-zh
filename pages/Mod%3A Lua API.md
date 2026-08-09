# Mod:Lua API

**分类:** [Category:待翻译条目](Category%3A待翻译条目.md) · [[Category:Modding_Resources]]
**来源:** https://noita.wiki.gg/zh/wiki/Mod%3A%20Lua%20API
---

[![Spell transmutation.png](https://noita.wiki.gg/zh/images/thumb/Spell_transmutation.png/50px-Spell_transmutation.png?ea693f)](https://noita.wiki.gg/zh/wiki/Mod:Lua_API?action=edit)

此页面的内容需要被翻译。

你可以帮助我们来翻译[此页面](https://noita.wiki.gg/zh/wiki/Mod:Lua_API?action=edit)。至于翻译的话请遵守[本Wiki的翻译准则](https://noita.wiki.gg/zh/wiki/Noita%20Wiki%3A%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5)。

  


模组制作导航  基础   
---  
[入门](Mod.md) • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
Lua API • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
本页收集了所有来自 `lua_api_documentation.txt`的api,伴随着社区可能做出的注释。 

  
**注意:** 用括号包裹的返回值，如`{entity_id}`, 意味着是一个table类型的实体的阵列。请特别注意这一点! 

The extended [Noita](Noita.md) **Lua API** documentation, using Lua 5.1. 

This page gathers together everything from `lua_api_documentation.txt`, with possible notes made by the community. 

**Note:** Return values wrapped in brackets, like `{entity_id}`, mean an array of entities. Pay special attention to this! 

[Template:TOC](https://noita.wiki.gg/zh/wiki/Template%3ATOC%3Faction%3Dedit%26redlink%3D1)

## Version

Current modding API version
    12

## Lua Tables

Noita is using Lua 5.1, and restricts the API usage unless _Unsafe mods_ is set to "Allowed". 

### Restricted API

The restricted ("Safe") API is as follows: 

  * [Basic Functions](https://www.lua.org/manual/5.1/manual.html#5.1) \- Except for load, loadstring, require, gcinfo, collectgarbage
  * [Table Manipulation](https://www.lua.org/manual/5.1/manual.html#5.5) \- `table`
  * [String Manipulation](https://www.lua.org/manual/5.1/manual.html#5.4) \- `string`
  * [Mathematical Functions](https://www.lua.org/manual/5.1/manual.html#5.6) \- `math`
  * [BitOp](http://bitop.luajit.org/api.html) \- `bit`
  * [jit.* Library](https://luajit.org/ext_jit.html) \- `jit`
  * There is a hidden undocumented function, `newproxy()`



### Unrestricted API

The unsafe API includes everything in [the Lua Reference Manual](https://www.lua.org/manual/5.1/index.html#index), plus [BitOp](http://bitop.luajit.org/api.html), [jit.*](https://luajit.org/ext_jit.html), and `newproxy`. 

## Core Functions

Top level functions defined by Noita. 

### do_mod_appends

`do_mod_appends( filename:string )`

### dofile

`dofile( filename:string ) -> (nil|script_return_type)|(nil,error_string) `

Noita overrides the built-in `dofile` function with its own implementation. Returns the script's return value, if any. Returns nil,error_string if the script had errors. 

### dofile_once

`dofile_once( filename:string ) -> (nil|script_return_type)|(nil,error_string) `

Runs the script only once per lua context, returns the script's return value, if any. Returns nil,error_string if the script had errors. For performance reasons it is recommended scripts use dofile_once(), unless the standard dofile behaviour is required. 

  


### loadfile

`loadfile( filename:string ) -> (nil|script_as_function)|(nil,error_string)`

Noita overrides the Lua built-in `loadfile` function with its own implementation. This loads a Lua file and returns both a function and an error string (in case of failure). 

### print

`print`

Noita overrides the Lua built-in `print` function with its own implementation. 

  


### print_error

`print_error`

Works similar to [print](#print) but also prints the text to _logger.txt_ in the Noita folder. 

## Hooks

### OnBiomeConfigLoaded

`OnBiomeConfigLoaded()`

This is the first moment during mod initialisation from which the `CellFactory_*` functions can be called. 

### OnCountSecrets

`OnCountSecrets() -> int,int`

The first number to return is the total and the second is the number of secrets found. 

### OnMagicNumbersAndWorldSeedInitialized

`OnMagicNumbersAndWorldSeedInitialized()`

### OnModInit

`OnModInit()`

Called once for each mod. It is done for every mod after `[OnModPreInit](#OnModPreInit)` and before `[OnModPostInit](#OnModPostInit)` is called. 

### OnModPostInit

`OnModPostInit()`

Called once for each mod. It is done for every mod after `[OnModPreInit](#OnModPreInit)` and `[OnModInit](#OnModInit)` are called. 

### OnModPreInit

`OnModPreInit()`

Called once for each mod. It is done for every mod before either `[OnModInit](#OnModInit)` and `[OnModPostInit](#OnModPostInit)` is called. 

### OnModSettingsChanged

`OnModSettingsChanged()`

Will be called when the game is unpaused, if player changed any mod settings while the game was paused. Does not get called when `[ModSettingSet](#ModSettingSet)` is called. 

Note: This callback doesn't appear to work. Modders have resorted to using `[OnPausedChanged](#OnPausedChanged)` instead to detect potential settings changes. 

### OnPausePreUpdate

`OnPausePreUpdate()`

Will be called when the game is paused, either by the pause menu or some inventory menus. Please be careful with this, as not everything will behave well when called while the game is paused. 

### OnPausedChanged

`OnPausedChanged( is_paused:bool, is_inventory_pause:bool )`

### OnPlayerDied

`OnPlayerDied( player_entity:int )`

Run when the player dies. The parameter passed in is the player_entity ID number. It is also run when starting a new game in the same session. 

### OnPlayerSpawned

`OnPlayerSpawned( player_entity:int )`

Run whenever the game spawns the player entity. The parameter passed in is the player_entity ID number. It runs each time either a new game is started, or whenever it's loaded. 

### OnWorldInitialized

`OnWorldInitialized()`

Run whenever the game creates/loads a new world. Despite the name, `[OnWorldPreUpdate](#OnWorldPreUpdate)` and `[OnWorldPostUpdate](#OnWorldPostUpdate)` will still be called at least once before `OnWorldInitialized` is called. 

### OnWorldPostUpdate

`OnWorldPostUpdate()`

This is called every time the game has finished updating the world 

### OnWorldPreUpdate

`OnWorldPreUpdate()`

This is called every time the game is about to start updating the world 

## Game Callback Order

The hooks are called in this order during initialisation: 

  * OnModPreInit
  * OnModInit
  * OnModPostInit
  * OnMagicNumbersAndWorldSeedInitialized
  * OnBiomeConfigLoaded
  * OnWorldPreUpdate
  * OnWorldPostUpdate
  * OnWorldInitialized
  * OnPlayerSpawned



The game first calls the hook in `data/scripts/init.lua` if it exists, followed by each mod in their respective load order. 

## Mod Settings (settings.lua)

Each of these are hooks defined in settings.lua. 

### ModSettingsGui

`ModSettingsGui( gui, in_main_menu:bool )`

This function is called to display the settings UI for this mod. Your mod's settings won't be visible in the mod settings menu if this function isn't defined correctly. 

  


### ModSettingsUpdate

`ModSettingsUpdate( init_scope:int )`

This function is called to ensure the correct setting values are visible to the game via [ModSettingGet](#ModSettingGet)(). Your mod's settings don't work if you don't have a function like this defined in settings.lua. 

This function is called: 

  * when entering the mod settings menu (_init_scope_ will be MOD_SETTING_SCOPE_ONLY_SET_DEFAULT)
  * before mod initialization when starting a new game (init_scope will be MOD_SETTING_SCOPE_NEW_GAME)
  * when entering the game after a restart (_init_scope_ will be MOD_SETTING_SCOPE_RESTART)
  * at the end of an update when mod settings have been changed via [ModSettingSetNextValue](#ModSettingSetNextValue)() and the game is unpaused (_init_scope_ will be MOD_SETTING_SCOPE_RUNTIME)



Note: It is unclear what values the documented constants refer to, but the possible values are between 0 and 3 (inclusive). 

  


### ModSettingsGuiCount

`ModSettingsGuiCount() -> int`

This function should return the number of visible setting UI elements. Your mod's settings wont be visible in the mod settings menu if this function isn't defined correctly. 

If your mod changes the displayed settings dynamically, you might need to implement custom logic. The value will be used to determine whether or not to display various UI elements that link to mod settings. 

At the moment it is fine to simply return 0 or 1 in a custom implementation, but we don't guarantee that will be the case in the future. This function is called every frame when in the settings menu. 

## General functions

### EntityLoad

`EntityLoad( filename:string, pos_x:number = 0, pos_y:number = 0 ) -> entity_id:int`

The **EntityLoad**() function is used to create an entity (game object) at a specified position in the game world. 

  * `filename`: The path to the XML file that defines the entity to be created.
  * `pos_x`: The x-coordinate of the position in the game world where the entity should be created. This argument is optional and defaults to 0.
  * `pos_y`: The y-coordinate of the position in the game world where the entity should be created. This argument is optional and defaults to 0.



It returns the ID of the newly-created entity. 

The following example uses the [GetUpdatedEntityID](#GetUpdatedEntityID)() function to get the ID of the entity that is currently being updated, and then uses the **EntityLoad**() function to create an entity at the position of that entity. 
    
    
    -- Get the ID of the entity that is currently being updated.
    local entity_id = GetUpdatedEntityID()
    
    -- Get the position of the entity that is currently being updated.
    local pos_x, pos_y = EntityGetTransform( entity_id )
    
    -- Create an entity defined in "data/entities/particles/image_emitters/spell_refresh_effect.xml" at the position of the entity that is currently being updated.
    local new_entity_id = EntityLoad( "data/entities/particles/image_emitters/spell_refresh_effect.xml", pos_x, pos_y )
    

Note: The [GetUpdatedEntityID](#GetUpdatedEntityID)() function should only be used in functions that are called from within an entity's script, as it will only return the ID of the entity that is currently being updated. In other contexts, it will return nil. Other ways to get a position may include [GameGetCameraPos](#GameGetCameraPos)(), [DEBUG_GetMouseWorld](#DEBUG_GetMouseWorld)(), or [EntityGetTransform](#EntityGetTransform)() with other entities such as the one tagged with "player_unit" (player character). 

### EntityLoadEndGameItem

`EntityLoadEndGameItem( filename:string, pos_x:number = 0, pos_y:number = 0 ) -> entity_id:int`

  


### EntityLoadCameraBound

`EntityLoadCameraBound( filename:string, pos_x:number = 0, pos_y:number = 0 )`

  


### EntityLoadToEntity

`EntityLoadToEntity( filename:string, entity:int ) `

Loads components from 'filename' to 'entity'. Does not load tags and other stuff. 

  


### EntitySave

`EntitySave( entity_id:int, filename:string ) `

The **EntitySave**() function saves an entity to a specified xml file. It takes two arguments: 

  * `entity_id`: integer representing the ID of the entity to be saved.
  * `filename`: string specifying the name and location where the entity should be saved to xml.



This function should be used with care, as it can potentially overwrite existing files. It is only available in development builds of the game. 

Here is an example of how to use this function: 
    
    
    -- load an entity from a file
    local entity_id = EntityLoad("data/entities/test_sprite.xml")
    
    -- save the entity to a new file
    EntitySave(entity_id, "temptemp/out_new_entity.xml")
    

This function is typically used in conjunction with [EntityLoad](#EntityLoad)() and [EntityCreateNew](#EntityCreateNew)() to create and save new entities. It can also be used to save entities that have been modified in some way, such as by adding or removing components. 
    
    
    -- create a new entity
    local entity_id = EntityCreateNew("humppa")
    
    -- add a component to the entity
    EntityAddComponent2(entity_id, "SpriteComponent")
    
    -- save the modified entity to a file
    EntitySave(entity_id, "temptemp/out_modified_entity.xml")
    

Note that **EntitySave**() should only be used in development builds of the game. It is not available in the official release of the game. See also [DebugGetIsDevBuild](#DebugGetIsDevBuild)() to test whether this can be used. 

### EntityCreateNew

`EntityCreateNew( name:string = "" ) -> entity_id:int`

  


### EntityKill

`EntityKill( entity_id:int )`

  


### EntityGetIsAlive

`EntityGetIsAlive( entity_id:int ) -> bool`

  


### EntityAddComponent

`EntityAddComponent( entity_id:int, component_type_name:string, table_of_component_values:{string} = nil ) -> component_id:int`

See [Components Documentation](https://noita.wiki.gg/zh/wiki/Components%20Documentation%3Faction%3Dedit%26redlink%3D1) for a list of all possible component types. 

  


### EntityRemoveComponent

`EntityRemoveComponent( entity_id:int, component_id:int )`

  


### EntityGetAllComponents

`EntityGetAllComponents( entity_id:int ) -> {int} `

Returns a table of component ids. 

  


### EntityGetComponent

`EntityGetComponent( entity_id:int, component_type_name:string, tag:string = "" ) -> {component_id}|nil`

Note: Despite its name, this function actually returns an array, and **not** a single component. See [Components Documentation](https://noita.wiki.gg/zh/wiki/Components%20Documentation%3Faction%3Dedit%26redlink%3D1) for a list of all possible component types. 

  


### EntityGetFirstComponent

`EntityGetFirstComponent( entity_id:int, component_type_name:string, tag:string = "" ) -> component_id|nil`

Does **not** return components that are disabled, effectively "hiding" components that you might actually want. See [Components Documentation](https://noita.wiki.gg/zh/wiki/Components%20Documentation%3Faction%3Dedit%26redlink%3D1) for a list of all possible component types. 

  


### EntityGetComponentIncludingDisabled

`EntityGetComponentIncludingDisabled( entity_id:int, component_type_name:string, tag:string = "" ) -> {component_id}|nil`

Note: Despite its name, this function actually returns an array, and **not** a single component. See [Components Documentation](https://noita.wiki.gg/zh/wiki/Components%20Documentation%3Faction%3Dedit%26redlink%3D1) for a list of all possible component types. 

  


### EntityGetFirstComponentIncludingDisabled

`EntityGetFirstComponentIncludingDisabled( entity_id:int, component_type_name:string, tag:string = "" ) -> component_id|nil`

See [Components Documentation](https://noita.wiki.gg/zh/wiki/Components%20Documentation%3Faction%3Dedit%26redlink%3D1) for a list of all possible component types. 

  


### EntitySetTransform

`EntitySetTransform( entity_id:int, x:number, y:number = 0, rotation:number = 0, scale_x:number = 1, scale_y:number = 1 )`

  


### EntityApplyTransform

`EntityApplyTransform( entity_id:int, x:number, y:number = 0, rotation:number = 0, scale_x:number = 1, scale_y:number = 1 ) `

Sets the transform and tries to immediately refresh components that calculate values based on an entity's transform. Some components store old positions (and calculates the new one based on those). This tries to refresh those. 

  


### EntityGetTransform

`EntityGetTransform( entity_id:int ) -> x:number,y:number,rotation:number,scale_x:number,scale_y:number`

  


### EntityAddChild

`EntityAddChild( parent_id:int, child_id:int )`

  


### EntityGetAllChildren

`EntityGetAllChildren( entity_id:int, tag:string = "" ) -> {entity_id:int}|nil`

If passed the optional 'tag' parameter, will return only child entities that have that tag (If 'tag' isn't a valid tag name, will return no entities). If no entities are returned, might return either an empty table or nil. 

  * **[2024年04月08日(Epilogue2)](版本日志.md)**: Added the tag parameter.



### EntityGetParent

`EntityGetParent( entity_id:int ) -> entity_id:int`

  


### EntityGetRootEntity

`EntityGetRootEntity( entity_id:int ) -> entity_id:int `

Returns the given entity if it has no parent, otherwise walks up the parent hierarchy to the topmost parent and returns it. 

  


### EntityRemoveFromParent

`EntityRemoveFromParent( entity_id:int )`

  


### EntitySetComponentsWithTagEnabled

`EntitySetComponentsWithTagEnabled( entity_id:int, tag:string, enabled:bool )`

  


### EntitySetComponentIsEnabled

`EntitySetComponentIsEnabled( entity_id:int, component_id:int, is_enabled:bool )`

  


### EntityGetName

`EntityGetName( entity_id:int ) -> name:string`

  


### EntitySetName

`EntitySetName( entity_id:int, name:string )`

  


### EntityGetTags

`EntityGetTags( entity_id:int ) -> string|nil `

Returns a string where the tags are comma-separated, or nil if 'entity_id' doesn't point to a valid entity. 

  


### EntityGetWithTag

`EntityGetWithTag( tag:string ) -> {entity_id:int} `

Returns all entities with 'tag'. 

  


### EntityGetInRadius

`EntityGetInRadius( pos_x:number, pos_y:number, radius:number ) -> {entity_id:int} `

Returns all entities in 'radius' distance from 'x','y'. You can use `math.huge` as the radius to get all entities. 

  


### EntityGetInRadiusWithTag

`EntityGetInRadiusWithTag( pos_x:number, pos_y:number, radius:number, entity_tag:string ) -> {entity_id:int} `

Returns all entities in 'radius' distance from 'x','y' with the given tag. You can use `math.huge` as the radius to get all entities. 

  


### EntityGetClosest

`EntityGetClosest( pos_x:number, pos_y:number ) -> entity_id:int`

  


### EntityGetClosestWithTag

`EntityGetClosestWithTag( pos_x:number, pos_y:number, tag:string ) -> entity_id:int`

  


### EntityGetWithName

`EntityGetWithName( name:string ) -> entity_id:int`

  


### EntityAddTag

`EntityAddTag( entity_id:int, tag:string )`

This function will add a single permanent tag to an entity. The tag will be serialized with the entity and remain with it until it is removed. 

  * `entity_id`: integer representing the ID of the entity to add the tag to
  * `tag`: A string representing a single tag name to attach to the entity, this can be any string.



Important: You cannot add multiple tags in a single call with a comma, you must add them one by one using a function call for each one. For example, `EntityAddTag(e, "enemy,ui_use_raw_name")` does _not_ add two tags, it adds a single tag with a comma in the tag name. 

### EntityRemoveTag

`EntityRemoveTag( entity_id:int, tag:string )`

  


### EntityHasTag

`EntityHasTag( entity_id:int, tag:string ) -> bool`

  


### EntityGetFilename

`EntityGetFilename( entity_id:int ) -> full_path:string `

Returns the name of the file (game directory included) which was originally used to create the entity. 

Return value example: 'data/entities/items/flute.xml'. Incorrect value is returned if the entity has passed through the world streaming system. 

  


### EntitiesGetMaxID

`EntitiesGetMaxID() -> entity_max_id:number `

Returns the max entity ID currently in use. Entity IDs are increased linearly. 

  * **[2024年04月08日(Epilogue2)](版本日志.md)**: Added EntitiesGetMaxID function.



### ComponentAddTag

`ComponentAddTag( component_id:int, tag:string )`

  


### ComponentRemoveTag

`ComponentRemoveTag( component_id:int, tag:string )`

  


### ComponentHasTag

`ComponentHasTag( component_id:int, tag:string ) -> bool`

  


### ComponentGetTags

`ComponentGetTags( component_id:int ) -> string|nil`

Returns a string where the tags are comma-separated, or nil if can't find 'component_id' component. 

  * **[2024年04月08日(Epilogue2)](版本日志.md)**: Added ComponentGetTags function



### ComponentGetValue2

`ComponentGetValue2( component_id:int, field_name:string ) -> multiple_types|nil `

Returns one or many values matching the type or subtypes of the requested field. Reports error and returns nil if the field type is not supported or field was not found. This is up to 7.5x faster than the old ComponentGetValue functions. 

  


### ComponentSetValue2

`ComponentSetValue2( component_id:int, field_name:string, value_or_values:multiple_types ) `

Sets the value of a field. Value(s) should have a type matching the field type. Reports error if the values weren't given in correct type, the field type is not supported, or the component does not exist. This is up to 20x faster than the old ComponentSetValue functions. 

  


### ComponentObjectGetValue2

`ComponentObjectGetValue2( component_id:int, object_name:string, field_name:string ) -> multiple types|nil `

Returns one or many values matching the type or subtypes of the requested field in a component subobject. Reports error and returns nil if the field type is not supported or 'object_name' is not a metaobject. 

  


### ComponentObjectSetValue2

`ComponentObjectSetValue2( component_id:int, object_name:string, field_name:string, value_or_values:multiple_types ) `

Sets the value of a field in a component subobject. Value(s) should have a type matching the field type. Reports error if the values weren't given in correct type, the field type is not supported or 'object_name' is not a metaobject. 

  


### EntityAddComponent2

`EntityAddComponent2( entity_id:int, component_type_name:string, table_of_component_values:{string-multiple_types} = nil ) -> component_id:int`

Creates a component of type 'component_type_name' and adds it to 'entity_id'. 'table_of_component_values' should be a string-indexed table, where keys are field names and values are field values of correct type. The value setting works like `[ComponentObjectSetValue2](#ComponentObjectSetValue2)()`, with the exception that multivalue types are not supported. Additional supported values are _tags:comma_separated_string and _enabled:bool, which basically work like the same values work in entity XML files. Returns the created component, if creation succeeded, or nil. 

See [Components Documentation](https://noita.wiki.gg/zh/wiki/Components%20Documentation%3Faction%3Dedit%26redlink%3D1) for a list of all possible component types. 

[Template:Notice](https://noita.wiki.gg/zh/wiki/Template%3ANotice%3Faction%3Dedit%26redlink%3D1)

  


### ComponentGetVectorSize

`ComponentGetVectorSize( component_id:int, array_member_name:string, type_stored_in_vector:string ) -> int `

'type_stored_in_vector' should be "int", "float" or "string". 

  


### ComponentGetVectorValue

`ComponentGetVectorValue( component_id:int, array_name:string, type_stored_in_vector:string, index:int ) -> int|number|string|nil `

'type_stored_in_vector' should be "int", "float" or "string". 

  


### ComponentGetVector

`ComponentGetVector( component_id:int, array_name:string, type_stored_in_vector:string ) -> {int|number|string}|nil `

'type_stored_in_vector' should be "int", "float" or "string". 

  


### ComponentGetEntity

`ComponentGetEntity( component_id:int ) -> entity_id:int`

Returns the id of the entity that owns a component, or 0. 

  * **[2024年04月08日(Epilogue2)](版本日志.md)**: Added ComponentGetEntity function



### ComponentGetIsEnabled

`ComponentGetIsEnabled( component_id:int ) -> bool `

Returns true if the given component exists and is enabled, else false. 

  


### ComponentGetMembers

`ComponentGetMembers( component_id:int ) -> {string-string}|nil `

Returns a string-indexed table of string. 

  


### ComponentObjectGetMembers

`ComponentObjectGetMembers( component_id:int, object_name:string ) -> {string-string}|nil `

Returns a string-indexed table of string or nil. 

  


### ComponentGetTypeName

`ComponentGetTypeName( component_id:int ) -> string`

  


### GetUpdatedEntityID

`GetUpdatedEntityID() -> entity_id:int`

  


### GetUpdatedComponentID

`GetUpdatedComponentID() -> component_id:int`

  


### SetTimeOut

`SetTimeOut( time_to_execute:number, file_to_execute:string, function_to_call:string = nil )`

Used to execute a function from a file after a certain duration. 

  * `time_to_execute`: The time in seconds from now before the file and function is executed. Can be fractional, i.e. `0.5` for 500ms, or `0` for the next update.
  * `file_to_execute`: The path to the file to be loaded and executed once the duration expires.
  * `function_to_call`: Optional name of a function to call when the timer expires. Useful when trying to keep logic within the same file, for example in a component script.



Simplified example from `scripts/buildings/egg_damage.lua`: 
    
    
    function spawn_boss_dragon()
    	local entity_id    = GetUpdatedEntityID()
    	local pos_x, pos_y = EntityGetTransform( entity_id )
    
    	GlobalsSetValue("boss_dragon_spawned_pos_x", pos_x)
    	GlobalsSetValue("boss_dragon_spawned_pos_y", pos_y)
    
    	play_animation( entity_id, "open")
    
    	SetTimeOut( 0.54, "data/scripts/buildings/egg_damage.lua", "impl_spawn_boss_dragon")
    end
    
    function impl_spawn_boss_dragon()
    	local pos_x = GlobalsGetValue("boss_dragon_spawned_pos_x")
    	local pos_y = GlobalsGetValue("boss_dragon_spawned_pos_y")
    	EntityLoad( "data/entities/animals/boss_dragon.xml", pos_x, pos_y - 16 )
    end
    

This example first starts playing an animation followed by a delay before spawning the [Dragon](https://noita.wiki.gg/zh/wiki/Dragon%3Faction%3Dedit%26redlink%3D1), that delay is achieved through **SetTimeOut**. 

You should assume that the script being run is executed in a new Lua context without access to previously set variables, and pass variables via [GlobalsSetValue](#GlobalsSetValue) and [GlobalsGetValue](#GlobalsGetValue) or other shared variable mechanisms like flags or stats. 

### RegisterSpawnFunction

`RegisterSpawnFunction( color:int, function_name:string )`

  


### SpawnActionItem

`SpawnActionItem( x:number, y:number, level:int )`

  


### SpawnStash

`SpawnStash( x:number, y:number, level:int, action_count:int ) -> entity_id:int`

  


### SpawnApparition

`SpawnApparition( x:number, y:number, level:int, spawn_now:bool = false ) -> spawn_state_id:int,entity_id:int`

  * **???? ?? ??** : Added `spawn_now` parameter



### LoadEntityToStash

`LoadEntityToStash( entity_file:string, stash_entity_id:int )`

  


### AddMaterialInventoryMaterial

`AddMaterialInventoryMaterial( entity_id:int, material_name:string, count:int )`

Used to set the count of a given material in an entity's [MaterialInventoryComponent](Documentation%3A MaterialInventoryComponent.md). The function always picks the first MaterialInventoryComponent on the entity, even when it is disabled. 

Somewhat surprisingly, this does not add to the existing `material_name` count. To do that you first read the `count_per_material_type` property and sum together how much you want to add and the current count. 

The function takes three arguments: 

  * `entity_id`: id of the entity that owns the material inventory.
  * `material_name`: name of the material to be added to the inventory.
  * `count`: units of the material to set in the inventory.



Here is an example of how the function might be used in code: 
    
    
    function init( entity_id )
    	-- Set a random seed based on the entity's position and the current game frame
    	local x,y = EntityGetTransform( entity_id )
    	SetRandomSeed( x + GameGetFrameNum(), y )
    
    	-- Choose a random potion from the list of available potions
    	local potion = random_from_array( potions )
    
    	-- Put 1000 units of the chosen potion material in the entity's material inventory
    	AddMaterialInventoryMaterial( entity_id, potion.material, 1000 )
    end
    

In this example, the `init` function sets a random seed based on the position of the given entity and the current game frame. It then chooses a random potion from the `potions` array and makes it so there are 1000 units of the potion's material in the entity's material inventory using the `AddMaterialInventoryMaterial` function. 

### RemoveMaterialInventoryMaterial

`RemoveMaterialInventoryMaterial( entity_id:int, material_name:string = "" ) -> material_type:int `

If material_name is empty, all materials will be removed. 

  * **[2024年04月08日(Epilogue2)](版本日志.md)**: Added RemoveMaterialInventoryMaterial function



### GetMaterialInventoryMainMaterial

`GetMaterialInventoryMainMaterial( entity_id:int, ignore_box2d_materials:bool = true ) -> material_type:int `

Returns the id of the material taking the largest part of the first [MaterialInventoryComponent](Documentation%3A MaterialInventoryComponent.md) in 'entity_id', or 0 if nothing is found. 

  * **???? ?? ??** : Added ignore_box2d_materials parameter
  * **[2021年03月30日(Epilogue1)](版本日志.md)**: Added GetMaterialInventoryMainMaterial function



### GameScreenshake

`GameScreenshake( strength:number, x:number = camera_x, y:number = camera_y )`

  


### GameOnCompleted

`GameOnCompleted()`

  


### GameGiveAchievement

`GameGiveAchievement( id:string )`

  


### GameDoEnding2

`GameDoEnding2()`

  


### GetParallelWorldPosition

`GetParallelWorldPosition( world_pos_x:number, world_pos_y:number ) -> x, y `

x = 0 normal world, -1 is first west world, +1 is first east world, if y < 0 it is sky, if y > 0 it is hell 

  


### BiomeMapLoad_KeepPlayer

`BiomeMapLoad_KeepPlayer( filename:string, pixel_scenes:string = "data/biome/_pixel_scenes.xml" )`

  


### GameIsIntroPlaying

`GameIsIntroPlaying() -> bool`

  


### GameGetIsGamepadConnected

`GameGetIsGamepadConnected() -> bool`

  


### GameGetWorldStateEntity

`GameGetWorldStateEntity() -> entity_id:int`

  


### GameGetPlayerStatsEntity

`GameGetPlayerStatsEntity() -> entity_id:int`

  


### GameGetOrbCountAllTime

`GameGetOrbCountAllTime() -> int`

  


### GameGetOrbCountThisRun

`GameGetOrbCountThisRun() -> int`

  


### GameGetOrbCollectedThisRun

`GameGetOrbCollectedThisRun( orb_id_zero_based:int ) -> bool`

  


### GameGetOrbCollectedAllTime

`GameGetOrbCollectedAllTime( orb_id_zero_based:int ) -> bool`

  


### GameClearOrbsFoundThisRun

`GameClearOrbsFoundThisRun()`

  


### GameGetOrbCountTotal

`GameGetOrbCountTotal() -> int `

Returns the number of orbs, picked or not. 

  


### CellFactory_GetName

`CellFactory_GetName( material_id:int ) -> string `

Converts a numeric material id to the material's strings id. 

  


### CellFactory_GetType

`CellFactory_GetType( material_name:string ) -> int `

Returns the id of a material. 

  


### CellFactory_GetUIName

`CellFactory_GetUIName( material_id:int ) -> string `

Returns the UI translation key for a material, or an empty string if 'material_id' is not valid. Use [GameTextGetTranslatedOrNot](#GameTextGetTranslatedOrNot) to translate it. 

### CellFactory_GetAllLiquids

`CellFactory_GetAllLiquids( include_statics:bool = true, include_particle_fx_materials:bool = false ) -> {string}`

  


### CellFactory_GetAllSands

`CellFactory_GetAllSands( include_statics:bool = true, include_particle_fx_materials:bool = false ) -> {string}`

  


### CellFactory_GetAllGases

`CellFactory_GetAllGases( include_statics:bool = true, include_particle_fx_materials:bool = false ) -> {string}`

  


### CellFactory_GetAllFires

`CellFactory_GetAllFires( include_statics:bool = true, include_particle_fx_materials:bool = false ) -> {string}`

  


### CellFactory_GetAllSolids

`CellFactory_GetAllSolids( include_statics:bool = true, include_particle_fx_materials:bool = false ) -> {string}`

  


### CellFactory_HasTag

`CellFactory_HasTag( material_id:int, tag:string ) -> {bool}`

  * **[2024年04月30日(Epilogue2)](版本日志.md)**: Added CellFactory_HasTag function



### CellFactory_GetTags

`CellFactory_GetTags( material_id:int ) -> {string}`

  


### GameGetCameraPos

`GameGetCameraPos() -> x:number,y:number`

  


### GameSetCameraPos

`GameSetCameraPos( x:number, y:number )`

  


### GameSetCameraFree

`GameSetCameraFree( is_free:bool )`

  


### GameGetCameraBounds

`GameGetCameraBounds() -> x:number,y:number,w:number,h:number `

Returns the camera rectangle. This may not be 100% pixel perfect with regards to what you see on the screen. 'x','y' = top left corner of the rectangle. 

  


### GameRegenItemAction

`GameRegenItemAction( entity_id:int )`

  


### GameRegenItemActionsInContainer

`GameRegenItemActionsInContainer( entity_id:int )`

  


### GameRegenItemActionsInPlayer

`GameRegenItemActionsInPlayer( entity_id:int )`

  


### GameKillInventoryItem

`GameKillInventoryItem( inventory_owner_entity_id:int, item_entity_id:int )`

  


### GamePickUpInventoryItem

`GamePickUpInventoryItem( who_picks_up_entity_id:int, item_entity_id:int, do_pick_up_effects:bool = true )`

  


### GameGetAllInventoryItems

`GameGetAllInventoryItems( entity_id:int ) -> {item_entity_id}|nil`

Returns all the inventory items that entity_id has. This function was added in the [March 11, 2023 Bugfix update](Release Notes.md). 

### GameDropAllItems

`GameDropAllItems( entity_id:int )`

  


### GameDropPlayerInventoryItems

`GameDropPlayerInventoryItems( entity_id:int )`

  


### GameDestroyInventoryItems

`GameDestroyInventoryItems( entity_id:int )`

  


### GameIsInventoryOpen

`GameIsInventoryOpen() -> bool`

  


### GameTriggerGameOver

`GameTriggerGameOver()`

  


### LoadPixelScene

`LoadPixelScene( materials_filename:string, colors_filename:string, x:number, y:number, background_file:string, skip_biome_checks:bool = false, skip_edge_textures:bool = false, color_to_material_table:{string-string} = {}, background_z_index:int = 50, load_even_if_duplicate:bool = false )`

`color_to_material_table` needs a table that maps the ARGB color to a material name like this: `{["ff404650"]="lava", ["ff36311e"]="water"}`

  * **[2024年04月08日(Epilogue2)](版本日志.md)**: Added `load_even_if_duplicate` parameter



### LoadBackgroundSprite

`LoadBackgroundSprite( background_file:string, x:number, y:number, background_z_index:number = 40.0, check_biome_corners:bool = false )`

  


### RemovePixelSceneBackgroundSprite

`RemovePixelSceneBackgroundSprite( background_file:string, x:number, y:number ) -> bool`

Removes the pixel scene sprite if the name and position match. Will return true if manages the find and destroy the background sprite. 

  * **[2024年04月08日(Epilogue2)](版本日志.md)**: Added RemovePixelSceneBackgroundSprite function



### RemovePixelSceneBackgroundSprites

`RemovePixelSceneBackgroundSprites( x_min:number, y_min:number, x_max:number, y_max:number )`

Removes pixel scene background sprites inside the given area. 

  * **[2024年04月08日(Epilogue2)](版本日志.md)**: Added RemovePixelSceneBackgroundSprites function



  


### GameCreateCosmeticParticle

`GameCreateCosmeticParticle( material_name:string, x:number, y:number, how_many:int, xvel:number, yvel:number, color:uint32 = 0, lifetime_min:number = 5.0, lifetime_max:number = 10, force_create:bool = true, draw_front:bool = false, collide_with_grid:bool = true, randomize_velocity:bool = true, gravity_x:float = 0, gravity_y:float = 100.0 )`

This function was added in the [March 11, 2023 Bugfix update](Release Notes.md). 

  * **[2024年04月08日(Epilogue2)](版本日志.md)**: Added `gravity_x` and `gravity_y` parameters



### GameCreateCosmeticParticle

`GameCreateCosmeticParticle( material_name:string, x:number, y:number, how_many:int, xvel:number, yvel:number, color:uint32 = 0, lifetime_min:number = 5.0, lifetime_max:number = 10, force_create:bool = true, draw_front:bool = false, collide_with_grid:bool = true, randomize_velocity:bool = true, gravity_x:float = 0, gravity_y:float = 100.0 )`

gravity_x and gravity_y were added in the [June 2, 2023 Beta patch](https://noita.wiki.gg/zh/wiki/Release%20Notes%2FBeta%3Faction%3Dedit%26redlink%3D1). 

### GameCreateParticle

`GameCreateParticle( material_name:string, x:number, y:number, how_many:int, xvel:number, yvel:number, just_visual:bool, draw_as_long:bool = false, randomize_velocity:bool = true )`

The `randomize_velocity` argument was added in the [March 11, 2023 Bugfix update](Release Notes.md). 

### GameCreateSpriteForXFrames

`GameCreateSpriteForXFrames( filename:string, x:number, y:number, centered:bool = true, sprite_offset_x:number = 0, sprite_offset_y:number = 0, frames:int = 1, emissive:bool = false )`

If `emissive` is true, the sprite is drawn regardless of the fog of war, otherwise the fog of war is respected. 

### GameShootProjectile

`GameShootProjectile( shooter_entity:int, x:number, y:number, target_x:number, target_y:number, projectile_entity:int, send_message:bool = true, verlet_parent_entity:int = 0 ) `

'shooter_entity' can be 0. Warning: If 'projectile_entity' has [PhysicsBodyComponent](Documentation%3A PhysicsBodyComponent.md) and [ItemComponent](Documentation%3A ItemComponent.md), components without the "enabled_in_world" tag will be disabled, as if the entity was thrown by player. 

  


### EntityInflictDamage

`EntityInflictDamage( entity:int, amount:number, damage_type:string, description:string, ragdoll_fx:string, impulse_x:number, impulse_y:number, entity_who_is_responsible:int = 0, world_pos_x:number = entity_x, world_pos_y:number = entity_y, knockback_force:number = 0 )`

For `damage_type` values, see [DAMAGE_TYPES](Modding%3A Enums.md). 

### EntityIngestMaterial

`EntityIngestMaterial( entity:int, material_type:number, amount:number ) `

Has the same effects that would occur if 'entity' eats 'amount' number of cells of 'material_type' from the game world. Use this instead of directly modifying [IngestionComponent](Documentation%3A IngestionComponent.md) values, if possible. Might not work with non-player entities. Use `[CellFactory_GetType](#CellFactory_GetType)()` to convert a material name to material type. 

### EntityRemoveIngestionStatusEffect

`EntityRemoveIngestionStatusEffect( entity:int, status_type_id:string )`

  


### EntityAddRandomStains

`EntityAddRandomStains( entity:int, material_type:number, amount:number ) `

Adds random visible stains of 'material_type' to entity. 'amount' controls the number of stain cells added. Does nothing if 'entity' doesn't have a [SpriteStainsComponent](Documentation%3A SpriteStainsComponent.md). Use `[CellFactory_GetType](#CellFactory_GetType)()` to convert a material name to material type. 

### EntitySetDamageFromMaterial

`EntitySetDamageFromMaterial( entity:int, material_name:string, damage:number ) `

Modifies [DamageModelComponents](Documentation%3A DamageModelComponent.md) `materials_that_damage` and `materials_how_much_damage` variables (and their parsed out data structures) 

  


### EntityRefreshSprite

`EntityRefreshSprite( entity:int, sprite_component:int ) `

Immediately refreshes the given [SpriteComponent](Documentation%3A SpriteComponent.md). Might be useful with text sprites if you want them to update more often than once a second. 

  


### EntityGetWandCapacity

`EntityGetWandCapacity( entity:int ) -> int `

Returns the capacity of a wand entity, or 0 if 'entity' doesnt exist. 

  


### GamePlayAnimation

`GamePlayAnimation( entity_id:int, name:string, priority:int, followup_name:string = "", followup_priority:int = 0 ) `

Plays animation. Follow up animation ('followup_name') is applied only if 'followup_priority' is given. 

  


### GameGetVelocityCompVelocity

`GameGetVelocityCompVelocity( entity_id:int ) -> x:number,y:number`

  


### GameGetGameEffect

`GameGetGameEffect( entity_id:int, game_effect_name:string ) -> component_id:int`

See [GAME_EFFECTS](Modding%3A Enums.md) for `game_effect_name`. 

### GameGetGameEffectCount

`GameGetGameEffectCount( entity_id:int, game_effect_name:string ) -> int`

See [GAME_EFFECTS](Modding%3A Enums.md) for `game_effect_name`. 

### LoadGameEffectEntityTo

`LoadGameEffectEntityTo( entity_id:int, game_effect_entity_file:string ) -> effect_entity_id:int`

  


### GetGameEffectLoadTo

`GetGameEffectLoadTo( entity_id:int, game_effect_name:string, always_load_new:bool ) -> effect_component_id:int,effect_entity_id:int`

See [GAME_EFFECTS](Modding%3A Enums.md) for `game_effect_name`. 

### SetPlayerSpawnLocation

`SetPlayerSpawnLocation( x:number, y:number )`

  


### UnlockItem

`UnlockItem( action_id:string )`

  


### GameGetPotionColorUint

`GameGetPotionColorUint( entity_id:int ) -> uint`

  


### EntityGetFirstHitboxCenter

`EntityGetFirstHitboxCenter( entity_id:int ) -> (x:number,y:number)|nil `

Returns the centroid of first enabled [HitboxComponent](Documentation%3A HitboxComponent.md) found in entity, the position of the entity if no hitbox is found, or nil if the entity does not exist. All returned positions are in world coordinates. 

  


### Raytrace

`Raytrace( x1:number, y1:number, x2:number, y2:number ) -> did_hit:bool,hit_x:number,hit_y:number `

Does a raytrace that stops on any cell it hits. 

  


### RaytraceSurfaces

`RaytraceSurfaces( x1:number, y1:number, x2:number, y2:number ) -> did_hit:bool,hit_x:number,hit_y:number `

Does a raytrace that stops on any cell that is not fluid, gas (yes, technically gas is a fluid), or fire. 

  


### RaytraceSurfacesAndLiquiform

`RaytraceSurfacesAndLiquiform( x1:number, y1:number, x2:number, y2:number ) -> did_hit:bool,hit_x:number,hit_y:number `

Does a raytrace that stops on any cell that is not gas or fire. 

  


### RaytracePlatforms

`RaytracePlatforms( x1:number, y1:number, x2:number, y2:number ) -> did_hit:bool,hit_x:number,hit_y:number `

Does a raytrace that stops on any cell a character can stand on. 

  


### FindFreePositionForBody

`FindFreePositionForBody( ideal_pos_x:number, idea_pos_y:number, velocity_x:number, velocity_y:number, body_radius:number ) -> x:number,y:number`

  


### GetSurfaceNormal

`GetSurfaceNormal( pos_x:number, pos_y:number, ray_length:number, ray_count:int ) -> found_normal:bool,normal_x:number,normal_y:number,approximate_distance_from_surface:number`

  


### DoesWorldExistAt

`DoesWorldExistAt( min_x:int, min_y:int, max_x:int, max_y:int ) -> bool`

Returns true if the area inside the bounding box defined by the parameters has been streamed in and no pixel scenes are loading in the area. 

### StringToHerdId

`StringToHerdId( herd_name:string ) -> int`

  


### HerdIdToString

`HerdIdToString( herd_id:int ) -> string`

  


### GetHerdRelation

`GetHerdRelation( herd_id_a:int, herd_id_b:int ) -> number`

  


### EntityGetHerdRelation

`EntityGetHerdRelation( entity_a:int, entity_b:int ) -> number`

  


### EntityGetHerdRelationSafe

`EntityGetHerdRelationSafe( entity_a:int, entity_b:int ) -> number `

does not spam errors, but returns 0 if anything fails 

  


### PolymorphTableAddEntity

`PolymorphTableAddEntity( entity_xml:string, is_rare:bool = false, add_only_one_copy:bool = true )`

Adds the entity to the polymorph random table 

  


### PolymorphTableRemoveEntity

`PolymorphTableRemoveEntity( entity_xml:string, from_common_table:bool = true, from_rare_table:bool = true )`

Removes the entity from the polymorph random table 

  


### PolymorphTableGet

`PolymorphTableGet( bool rare_table = false ) -> {string}`

Returns a list of all the entities in the polymorph random table 

  


### PolymorphTableSet

`PolymorphTableSet( {table_of_xml_entities}, bool rare_table = false )`

Set a list of all entities as the polymorph random table 

  


### EntityGetClosestWormAttractor

`EntityGetClosestWormAttractor( pos_x:number, pos_y:number ) -> entity_id:int, pos_x:number, pos_y:number `

NOTE: entity_id might be NULL, but pos_x and pos_y could still be valid. 

  


### EntityGetClosestWormDetractor

`EntityGetClosestWormDetractor( pos_x:number, pos_y:number ) -> entity_id:int, pos_x:number, pos_y:number, radius:number `

NOTE: entity_id might be NULL, but pos_x and pos_y could still be valid 

  


### GamePrint

`GamePrint( log_line:string )`

  


### GamePrintImportant

`GamePrintImportant( title:string, description:string = "", ui_custom_decoration_file:string = "" )`

  


### DEBUG_GetMouseWorld

`DEBUG_GetMouseWorld() -> x:number,y:number`

Returns the x and y coordinates of the mouse cursor in world space. Used by various debug menus and scripts. 

### DEBUG_MARK

`DEBUG_MARK( x:number, y:number, message:string = "", color_r:number = 1, color_g:number = 0, color_b:number = 0 )`

  


### GameGetFrameNum

`GameGetFrameNum() -> int`

  


### GameGetRealWorldTimeSinceStarted

`GameGetRealWorldTimeSinceStarted() -> number`

  


### InputIsKeyDown

`InputIsKeyDown( key_code:int ) -> bool`

Debugish function - returns if a key is down, does not depend on state. E.g. player could be in menus or inputting text. See data/scripts/debug/keycodes.lua for the constants 

  


### InputIsKeyJustDown

`InputIsKeyJustDown( key_code:int ) -> bool`

Debugish function - returns if a key is down this frame, does not depend on state. E.g. player could be in menus or inputting text. See data/scripts/debug/keycodes.lua for the constants 

  


### InputIsKeyJustUp

`InputIsKeyJustUp( key_code:int ) -> bool`

Debugish function - returns if a key is up this frame, does not depend on state. E.g. player could be in menus or inputting text. See data/scripts/debug/keycodes.lua for the constants 

  


### InputGetMousePosOnScreen

`InputGetMousePosOnScreen() -> x:number, y:number`

Debugish function - returns raw x, y coordinates of the mouse on screen 

  


### InputIsMouseButtonDown

`InputIsMouseButtonDown( mouse_button:int ) -> bool`

Debugish function - returns if mouse button is down. Does not depend on state. E.g. player could be in menus. See data/scripts/debug/keycodes.lua for the constants 

  


### InputIsMouseButtonJustDown

`InputIsMouseButtonJustDown( mouse_button:int ) -> bool`

Debugish function - returns if mouse button is down. Does not depend on state. E.g. player could be in menus. See data/scripts/debug/keycodes.lua for the constants. 

### InputIsMouseButtonJustUp

`InputIsMouseButtonJustUp( mouse_button:int ) -> bool`

Debugish function - returns if mouse button is down. Does not depend on state. E.g. player could be in menus. See data/scripts/debug/keycodes.lua for the constants 

  


### IsPlayer

`IsPlayer( entity_id:int ) -> bool`

  


### IsInvisible

`IsInvisible( entity_id:int ) -> bool`

  


### GameIsDailyRun

`GameIsDailyRun() -> bool`

  


### GameIsDailyRunOrDailyPracticeRun

`GameIsDailyRunOrDailyPracticeRun() -> bool`

  


### GameIsModeFullyDeterministic

`GameIsModeFullyDeterministic() -> bool`

  


### GlobalsSetValue

`GlobalsSetValue( key:string, value:string )`

[Template:Notice](https://noita.wiki.gg/zh/wiki/Template%3ANotice%3Faction%3Dedit%26redlink%3D1)

  


### GlobalsGetValue

`GlobalsGetValue( key:string, default_value:string = "" )`

  


### MagicNumbersGetValue

`MagicNumbersGetValue( key:string ) -> string`

  


### SetWorldSeed

`SetWorldSeed( new_seed:int )`

  


### SessionNumbersGetValue

`SessionNumbersGetValue( key:string ) -> string`

The possible keys are listed on [Documentation:_SessionNumbers](https://noita.wiki.gg/zh/wiki/Documentation%3A%20SessionNumbers%3Faction%3Dedit%26redlink%3D1). 

  


### SessionNumbersSetValue

`SessionNumbersSetValue( key:string, value:string )`

The possible keys are listed on [Documentation:_SessionNumbers](https://noita.wiki.gg/zh/wiki/Documentation%3A%20SessionNumbers%3Faction%3Dedit%26redlink%3D1). 

  


### SessionNumbersSave

`SessionNumbersSave()`

  


### AutosaveDisable

`AutosaveDisable()`

  


### StatsGetValue

`StatsGetValue( key:string ) -> string|nil`

Retrieves a statistics value for the current run. The possible keys are listed on [Documentation:_GameStats](https://noita.wiki.gg/zh/wiki/Documentation%3A%20GameStats%3Faction%3Dedit%26redlink%3D1). More examples can be found in your "AppData\LocalLow\Nolla_Games_Noita\save##\stats\sessions\\*.xml" files as attributes of the `<stats>` tag. 

  * Note: "killed_by" will be in the format "[origin] | [cause]", for example: "Minä | slice" or " | explosion".



Example: 
    
    
    	local raw_death_msg = StatsGetValue("killed_by")
    	local origin, cause = string.match(raw_death_msg, "(.*) | (.*)")
    

### StatsGlobalGetValue

`StatsGlobalGetValue( key:string ) -> string`

The possible keys are listed on [Documentation:_GameStats](https://noita.wiki.gg/zh/wiki/Documentation%3A%20GameStats%3Faction%3Dedit%26redlink%3D1). 

### StatsBiomeGetValue

`StatsBiomeGetValue( key:string ) -> string`

Works the same as `[StatsGetValue](#StatsGetValue)`, the difference is that `StatsBiomeGetValue()` tracks the stats diff since calling `[StatsResetBiome](#StatsResetBiome)()`. 

### StatsBiomeReset

`StatsBiomeReset()`

  


### StatsLogPlayerKill

`StatsLogPlayerKill( killed_entity_id:int = 0 )`

  


### CreateItemActionEntity

`CreateItemActionEntity( action_id:string, x:number = 0, y:number = 0 ) -> entity_id:int`

  


### GetRandomActionWithType

`GetRandomActionWithType( x:number, y:number, max_level:int, type:int, i:int = 0 ) -> string`

  


### GetRandomAction

`GetRandomAction( x:number, y:number, max_level:number, i:int = 0) -> string`

  


### GameGetDateAndTimeUTC

`GameGetDateAndTimeUTC() -> year:int,month:int,day:int,hour:int,minute:int,second:int`

  


### GameGetDateAndTimeLocal

`GameGetDateAndTimeLocal() ->year:int,month:int,day:int,hour:int,minute:int,second:int,jussi:bool`

The `jussi` boolean tells you whether it's currently the [midsummer holiday](Holidays.md). This return value is not documented in the `lua_api_documentation.txt` file that comes with Noita, probably to obscure the holiday easter egg. 

### GameEmitRainParticles

`GameEmitRainParticles( num_particles:int, width_outside_camera:number, material_name:string, velocity_min:number, velocity_max:number, gravity:number, droplets_bounce:bool, draw_as_long:bool )`

This function is used to create [weather](https://noita.wiki.gg/zh/wiki/Weather%3Faction%3Dedit%26redlink%3D1) precipitation in the game world. It must be called every update to continue the effect. The particle material used will remain in the game world once it has contacted a surface. 

  * `num_particles`: The number of particles to emit. Snow is between 1 and 4, light rain is between 4 and 7, and heavy rain is between 10 and 15.
  * `width_outside_camera`: The width of the particle emitter outside the camera's view.
  * `material_name`: The name of the material to use for the particles. Must be a valid material name.
  * `velocity_min`: The minimum velocity of the particles.
  * `velocity_max`: The maximum velocity of the particles.
  * `gravity`: The gravity to apply to the particles. Snow is set to 10 while rain is set to 200.
  * `droplets_bounce`: Whether or not the droplets should bounce off surfaces. If set to true, the droplets will bounce off surfaces like raindrops. If set to false, the droplets will land on surfaces like snowflakes.
  * `draw_as_long`: Whether or not the particles should be drawn as elongated streaks to simulate rain. If set to true, the particles will be drawn as elongated streaks. If set to false, the particles will be drawn as small dots.



The `velocity_min` and `velocity_max` parameters control the range of velocity values for the particles. A higher range will result in faster particles. Snow has a range of 30-60 while rain has a range of 200-220. 

### GameCutThroughWorldVertical

`GameCutThroughWorldVertical( x:int, y_min:int, y_max:int, radius:number, edge_darkening_width:number ) `

Each beam adds a little overhead to things like chunk creation, so please call this sparingly. 

  


### BiomeMapGetVerticalPositionInsideBiome

`BiomeMapGetVerticalPositionInsideBiome( x:number, y:number ) -> number`

  


### BiomeMapGetName

`BiomeMapGetName( x:number = camera_x, y:number = camera_y ) -> name`

Return the name of the biome. As a general rule, the biome's name will be in the format `$biome_[biome name]`. For example, it will return `$biome_snowcastle` for the Hiisi Base (`snowcastle.xml`). 

Return `_EMPTY_` for the surface. 

### SetRandomSeed

`SetRandomSeed( x:number, y:number )`

Sets the current seed of the random number generator, so that for the same input you get the same sequence every time. 

  


### Random

`Random( a:int = optional, b:int = optional ) -> number|int. `

This is kinda messy. If given 0 arguments, returns number between 0.0 and 1.0. If given 1 arguments, returns int between 0 and 'a'. If given 2 arguments returns int between 'a' and 'b'. 

  


### Randomf

`Randomf( min:number = optional, max:number = optional ) -> number `

This is kinda messy. If given 0 arguments, returns number between 0.0 and 1.0. If given 1 arguments, returns number between 0.0 and 'a'. If given 2 arguments returns number between 'a' and 'b'. 

  


### RandomDistribution

`RandomDistribution( min:int, max:int, mean:int, sharpness:number = 1, baseline:number = 0.005 ) -> int`

  


### RandomDistributionf

`RandomDistributionf( min:number, max:number, mean:number, sharpness:number = 1, baseline:number = 0.005 ) -> number`

  


### ProceduralRandom

`ProceduralRandom( x:number, y:number, a:int|number = optional, b:int|number = optional ) -> int|number `

This is kinda messy. If given 2 arguments, returns number between 0.0 and 1.0. If given 3 arguments, returns int between 0 and 'a'. If given 4 arguments returns number between 'a' and 'b'. 

  


### ProceduralRandomf

`ProceduralRandomf( x:number, y:number, a:number = optional, b:number = optional ) -> number `

This is kinda messy. If given 2 arguments, returns number between 0.0 and 1.0. If given 3 arguments, returns a number between 0 and 'a'. If given 4 arguments returns a number between 'a' and 'b'. 

  


### ProceduralRandomi

`ProceduralRandomi( x:number, y:number, a:int = optional, b:int = optional ) -> number `

This is kinda messy. If given 2 arguments, returns 0 or 1. If given 3 arguments, returns an int between 0 and 'a'. If given 4 arguments returns an int between 'a' and 'b'. 

  


### PhysicsAddBodyImage

`PhysicsAddBodyImage( entity_id:int, image_file:string, material:string = "", offset_x:number = 0, offset_y:number = 0, centered:bool = false, is_circle:bool = false, material_image_file:string = "", use_image_as_colors:bool = true ) -> int_body_id `

Does not work with [PhysicsBody2Component](Documentation%3A PhysicsBody2Component.md). Returns the id of the created physics body. 

  


### PhysicsAddBodyCreateBox

`PhysicsAddBodyCreateBox( entity_id:int, material:string, offset_x:number, offset_y:number, width:int, height:int, centered:bool = false ) -> int|nil `

Does not work with [PhysicsBody2Component](Documentation%3A PhysicsBody2Component.md). Returns the id of the created physics body. 

  


### PhysicsAddJoint

`PhysicsAddJoint( entity_id:int, body_id0:int, body_id1:int, offset_x:number, offset_y:number, joint_type:string ) -> int|nil `

Does not work with [PhysicsBody2Component](Documentation%3A PhysicsBody2Component.md). Returns the id of the created joint. 

For `joint_type` values, see [JOINT_TYPE](Modding%3A Enums.md). 

### PhysicsApplyForce

`PhysicsApplyForce( entity_id:int, force_x:number, force_y:number )`

  


### PhysicsApplyTorque

`PhysicsApplyTorque( entity_id:int, torque:number )`

  


### PhysicsApplyTorqueToComponent

`PhysicsApplyTorqueToComponent( entity_id:int, component_id:int, torque:number )`

  


### PhysicsApplyForceOnArea

`PhysicsApplyForceOnArea( calculate_force_for_body_fn:function, ignore_this_entity:int, area_min_x:number, area_min_y:number,area_max_x:number, area_max_y:number )`

Applies a force calculated by 'calculate_force_for_body_fn' to all bodies in an area. 'calculate_force_for_body_fn' should be a lua function with the following signature: 

`function( body_entity:int, body_mass:number, body_x:number, body_y:number, body_vel_x:number, body_vel_y:number, body_vel_angular:number ) -> force_world_pos_x:number,force_world_pos_y:number,force_x:number,force_y:number,force_angular:number`

### PhysicsRemoveJoints

`PhysicsRemoveJoints( world_pos_min_x:number, world_pos_min_y:number, world_pos_max_x:number, world_pos_max_y:number )`

  


### PhysicsSetStatic

`PhysicsSetStatic( entity_id:int, is_static:bool )`

  


### PhysicsGetComponentVelocity

`PhysicsGetComponentVelocity( entity_id:int, component_id:int ) -> vel_x:number,vel_y:number`

  


### PhysicsGetComponentAngularVelocity

`PhysicsGetComponentAngularVelocity( entity_id:int, component_id:int ) -> vel:number`

  


### PhysicsBody2InitFromComponents

`PhysicsBody2InitFromComponents( entity_id:int )`

  


### PhysicsVecToGameVec

`PhysicsVecToGameVec( x:number, y:number = 0 ) -> x:number,y:number`

  


### GameVecToPhysicsVec

`GameVecToPhysicsVec( x:number, y:number = 0 ) -> x:number,y:number`

  


### LooseChunk

`LooseChunk( world_pos_x:number, world_pos_y:number, image_filename:string, max_durability:int = 2147483647 )`

  


### AddFlagPersistent

`AddFlagPersistent( key:string ) -> bool_is_new`

  


### RemoveFlagPersistent

`RemoveFlagPersistent( key:string )`

  


### HasFlagPersistent

`HasFlagPersistent( key:string ) -> bool`

  


### GameAddFlagRun

`GameAddFlagRun( flag:string )`

Adds a run flag if it's not yet set, else it does nothing. 

This function does nothing if it's called before the world is initialised (see [OnWorldInitialized](https://noita.wiki.gg/zh/wiki/Modding%3A%20Lua%20API%3Faction%3Dedit%26redlink%3D1)). 

### GameRemoveFlagRun

`GameRemoveFlagRun( flag:string )`

Removes the run flag if it's set, else it does nothing. 

This function does nothing if it's called before the world is initialised (see [OnWorldInitialized](https://noita.wiki.gg/zh/wiki/Modding%3A%20Lua%20API%3Faction%3Dedit%26redlink%3D1)). 

### GameHasFlagRun

`GameHasFlagRun( flag:string ) -> bool`

Returns `true` if the run flag is set. 

This function returns `false` if it's called before the world is initialised (see [OnWorldInitialized](https://noita.wiki.gg/zh/wiki/Modding%3A%20Lua%20API%3Faction%3Dedit%26redlink%3D1)). 

You can get all set flags at once by reading [WorldStateComponent:flags](Documentation%3A WorldStateComponent.md). 

### GameTriggerMusicEvent

`GameTriggerMusicEvent( event_path:string, can_be_faded:bool, x:number, y:number )`

  


### GameTriggerMusicCue

`GameTriggerMusicCue( name:string )`

  


### GameTriggerMusicFadeOutAndDequeueAll

`GameTriggerMusicFadeOutAndDequeueAll( relative_fade_speed:number = 1 )`

  


### GamePlaySound

`GamePlaySound( bank_filename:string, event_path:string, x:number, y:number )`

  


### GameEntityPlaySound

`GameEntityPlaySound( entity_id:int, event_name:string ) `

Plays a sound through all [AudioComponents](Documentation%3A AudioComponent.md) with matching sound in 'entity_id'. 

  


### GameEntityPlaySoundLoop

`GameEntityPlaySoundLoop( entity:int, component_tag:string, intensity:number ) `

Plays a sound loop through an [AudioLoopComponent](Documentation%3A AudioLoopComponent.md) tagged with 'component_tag' in 'entity'. 'intensity' affects the intensity passed to the audio event. Must be called every frame when the sound should play. 

  


### GameSetPostFxParameter

`GameSetPostFxParameter( name:string, x:number, y:number, z:number, w:number ) `

Can be used to pass custom parameters to the post_final shader, or override values set by the game code. The shader uniform called 'name' will be set to the latest given values on this and following frames. 

  


### GameUnsetPostFxParameter

`GameUnsetPostFxParameter( name:string ) `

Will remove a post_final shader parameter value binding set via game `[GameSetPostFxParameter](#GameSetPostFxParameter)()`. 

  


### GameTextGetTranslatedOrNot

`GameTextGetTranslatedOrNot( text_or_key:string ) -> string`

Retrieves a translation by key if the string starts with a dollar sign, or echoes the text that was passed in. If using a translation key it must start with a dollar sign. 

A blank string is returned if 

  * The translation key doesn't exist.
  * If the translation expects params.
  * The string passed in is blank or nil.



The original text is returned if the string does not start with a dollar sign. 

### GameTextGet

`GameTextGet( key:string, param0:string = "", param1:string = "", param2:string = "" ) -> string`

Retrieves a translation by key with optional arguments to be used in the translation. The translation key must start with a dollar sign. 

A blank string is returned if 

  * The translation key doesn't exist.
  * If the translation expects params but none were given.
  * The translation key does not begin with '$'.



The two-letter language code is returned if 'key' is a single character. The game crashes if 'key' is nil or a blank string. 

  
For example to retrieve a cause of death message: `GameTextGet("$menugameover_causeofdeath_killer_cause", "Wiki", "editing")` returns "Wiki's editing" for English or "editing de Wiki" for French. 

### GuiCreate

`GuiCreate() -> gui:obj`

  


### GuiDestroy

`GuiDestroy( gui:obj )`

  


### GuiStartFrame

`GuiStartFrame( gui:obj )`

  


### GuiOptionsAdd

`GuiOptionsAdd( gui:obj, option:int ) `

Sets the options that apply to widgets during this frame. For 'option' use the values in the GUI_OPTION table in "data/scripts/lib/utilities.lua". Values from consecutive calls will be combined. For example calling this with the values GUI_OPTION.Align_Left and GUI_OPTION.GamepadDefaultWidget will set both options for the next widget. The options will be cleared on next call to `[GuiStartFrame](#GuiStartFrame)()`. 

### GuiOptionsRemove

`GuiOptionsRemove( gui:obj, option:int ) `

Sets the options that apply to widgets during this frame. For 'option' use the values in the GUI_OPTION table in "data/scripts/lib/utilities.lua". Values from consecutive calls will be combined. For example calling this with the values GUI_OPTION.Align_Left and GUI_OPTION.GamepadDefaultWidget will set both options for the next widget. The options will be cleared on next call to `[GuiStartFrame](#GuiStartFrame)()`. 

### GuiOptionsClear

`GuiOptionsClear( gui:obj ) `

Clears the options that apply to widgets during this frame. 

  


### GuiOptionsAddForNextWidget

`GuiOptionsAddForNextWidget( gui:obj, option:int )`

Sets the options that apply to the next widget during this frame. For 'option' use the values in the GUI_OPTION table in "data/scripts/lib/utilities.lua". Values from consecutive calls will be combined. For example calling this with the values GUI_OPTION.Align_Left and GUI_OPTION.GamepadDefaultWidget will set both options for the next widget 

### GuiColorSetForNextWidget

`GuiColorSetForNextWidget( gui:obj, red:number, green:number, blue:number, alpha:number ) `

Sets the color of the next widget during this frame. Color components should be in the 0-1 range. 

  


### GuiZSet

`GuiZSet( gui:obj, z:float ) `

Sets the rendering depth ('z') of the widgets following this call. Larger z = deeper. The z will be set to 0 on the next call to `[GuiStartFrame](#GuiStartFrame)()`. 

### GuiZSetForNextWidget

`GuiZSetForNextWidget( gui:obj, z:float )`

Sets the rendering depth ('z') of the next widget following this call. Larger z = deeper. 

### GuiIdPush

`GuiIdPush( gui:obj, id:int ) `

Can be used to solve ID conflicts. All ids given to Gui* functions will be hashed with the ids stacked (and hashed together) using `GuiIdPush()` and `[GuiIdPop](#GuiIdPop)()`. The id stack has a max size of 1024, and calls to the function will do nothing if the size is exceeded. 

  


### GuiIdPushString

`GuiIdPushString( gui:obj, str:string ) `

Pushes the hash of 'str' as a gui id. See `[GuiIdPush](#GuiIdPush)()`. 

  


### GuiIdPop

`GuiIdPop( gui:obj ) `

See `[GuiIdPush](#GuiIdPush)()`. 

  


### GuiAnimateBegin

`GuiAnimateBegin( gui:obj ) `

Starts a scope where animations initiated using `[GuiAnimateAlphaFadeIn](#GuiAnimateAlphaFadeIn)()` etc. will be applied to all widgets. 

  


### GuiAnimateEnd

`GuiAnimateEnd( gui:obj ) `

Ends a scope where animations initiated using `[GuiAnimateAlphaFadeIn](#GuiAnimateAlphaFadeIn)()` etc. will be applied to all widgets. 

  


### GuiAnimateAlphaFadeIn

`GuiAnimateAlphaFadeIn( gui:obj, id:int, speed:number, step:number, reset:bool ) `

Does an alpha tween animation for all widgets inside a scope set using `[GuiAnimateBegin](#GuiAnimateBegin)()` and `[GuiAnimateEnd](#GuiAnimateEnd)()`. 

  


### GuiAnimateScaleIn

`GuiAnimateScaleIn( gui:obj, id:int, acceleration:number, reset:bool ) `

Does a scale tween animation for all widgets inside a scope set using `[GuiAnimateBegin](#GuiAnimateBegin)()` and `[GuiAnimateEnd](#GuiAnimateEnd)()`. 

  


### GuiText

`GuiText( gui:obj, x:number, y:number, text:string )`

  


### GuiImage

`GuiImage( gui:obj, id:int, x:number, y:number, sprite_filename:string, alpha:number = 1, scale:number = 1, scale_y:number = 0, rotation:number = 0, rect_animation_playback_type:int = GUI_RECT_ANIMATION_PLAYBACK.PlayToEndAndHide, rect_animation_name:string = "" ) `

'scale' will be used for 'scale_y' if 'scale_y' equals 0. 

  


### GuiImageNinePiece

`GuiImageNinePiece( gui:obj, id:int, x:number, y:number, width:number, height:number, alpha:number = 1, sprite_filename:string = "data/ui_gfx/decorations/9piece0_gray.png", sprite_highlight_filename:string = "data/ui_gfx/decorations/9piece0_gray.png" )`

  


### GuiButton

`GuiButton( gui:obj, id:int, x:number, y:number, text:string ) -> clicked:bool,right_clicked:bool `

The old parameter order where 'id' is the last parameter is still supported. The function dynamically picks the correct order based on the type of the 4th parameter. 

  


### GuiImageButton

`GuiImageButton( gui:obj, id:int, x:number, y:number, text:string, sprite_filename:string ) -> clicked:bool,right_clicked:bool`

  


### GuiSlider

`GuiSlider( gui:obj, id:int, x:number, y:number, text:string, value:number, value_min:number, value_max:number, value_default:number, value_display_multiplier:number, value_formatting:string, width:number ) -> new_value:number `

This is not intended to be outside mod settings menu, and might bug elsewhere. 

  


### GuiTextInput

`GuiTextInput( gui:obj, id:int, x:number, y:number, text:string, width:number, max_length:int, allowed_characters:string = "" ) -> new_text `

'allowed_characters' should consist only of ASCII characters. This is not intended to be outside mod settings menu, and might bug elsewhere. 

  


### GuiBeginAutoBox

`GuiBeginAutoBox( gui:obj )`

Together with `[GuiEndAutoBoxNinePiece](#GuiEndAutoBoxNinePiece)()` this can be used to draw an auto-scaled background box for a bunch of widgets rendered between the calls. 

### GuiEndAutoBoxNinePiece

`GuiEndAutoBoxNinePiece( gui:obj, margin:number = 5, size_min_x:number = 0, size_min_y:number = 0, mirrorize_over_x_axis:bool = false, x_axis:number = 0, sprite_filename:string = "data/ui_gfx/decorations/9piece0_gray.png", sprite_highlight_filename:string = "data/ui_gfx/decorations/9piece0_gray.png" )`

  


### GuiTooltip

`GuiTooltip( gui:obj, text:string, description:string )`

  


### GuiBeginScrollContainer

`GuiBeginScrollContainer( gui:obj, id:int, x:number, y:number, width:number, height:number, scrollbar_gamepad_focusable:bool = true, margin_x:number = 2, margin_y:number = 2 ) `

This can be used to create a container with a vertical scroll bar. Widgets between `GuiBeginScrollContainer()` and `[GuiEndScrollContainer](#GuiEndScrollContainer)()` will be positioned relative to the container. 

  


### GuiEndScrollContainer

`GuiEndScrollContainer( gui:obj )`

See `[GuiBeginScrollContainer](#GuiBeginScrollContainer)()`. 

  


### GuiLayoutBeginHorizontal

`GuiLayoutBeginHorizontal( gui:obj, x:number, y:number, position_in_ui_scale:bool = false, margin_x:number = 2, margin_y:number = 2 ) `

If 'position_in_ui_scale' is 1, x and y will be in the same scale as other gui positions, otherwise x and y are given as a percentage (0-100) of the gui screen size. 

  


### GuiLayoutBeginVertical

`GuiLayoutBeginVertical( gui:obj, x:number, y:number, position_in_ui_scale:bool = false, margin_x:number = 0, margin_y:number = 0 ) `

If 'position_in_ui_scale' is 1, x and y will be in the same scale as other gui positions, otherwise x and y are given as a percentage (0-100) of the gui screen size. 

  


### GuiLayoutAddHorizontalSpacing

`GuiLayoutAddHorizontalSpacing( gui:obj, amount:number = optional ) `

Will use the horizontal margin from current layout if amount is not set. 

  


### GuiLayoutAddVerticalSpacing

`GuiLayoutAddVerticalSpacing( gui:obj, amount:number = optional ) `

Will use the vertical margin from current layout if amount is not set. 

  


### GuiLayoutEnd

`GuiLayoutEnd( gui:obj )`

  


### GuiLayoutBeginLayer

`GuiLayoutBeginLayer( gui:obj ) `

Puts following things to a new layout layer. Can be used to create non-layouted widgets inside a layout. 

  


### GuiLayoutEndLayer

`GuiLayoutEndLayer( gui:obj )`

  


### GuiGetScreenDimensions

`GuiGetScreenDimensions( gui:obj ) -> width:number,height:number `

Returns dimensions of viewport in the gui coordinate system (which is equal to the coordinates of the screen bottom right corner in gui coordinates). The values returned may change depending on the game resolution because the UI is scaled for pixel-perfect text rendering. 

  


### GuiGetTextDimensions

`GuiGetTextDimensions( gui:obj, text:string, scale:number = 1, line_spacing:number = 2 ) -> width:number,height:number `

Returns size of the given text in the gui coordinate system. 

  


### GuiGetImageDimensions

`GuiGetImageDimensions( gui:obj, image_filename:string, scale:number = 1 ) -> width:number,height:number `

Returns size of the given image in the gui coordinate system. 

  


### GuiGetPreviousWidgetInfo

`GuiGetPreviousWidgetInfo( gui:obj ) -> clicked:bool, right_clicked:bool, hovered:bool, x:number, y:number, width:number, height:number, draw_x:number, draw_y:number, draw_width:number, draw_height:number `

Returns the final position, size etc calculated for a widget. Some values aren't supported by all widgets. 

  


### GameIsBetaBuild

`GameIsBetaBuild() -> bool`

  


### DebugGetIsDevBuild

`DebugGetIsDevBuild() -> bool`

  


### DebugEnableTrailerMode

`DebugEnableTrailerMode()`

  


### GameGetIsTrailerModeEnabled

`GameGetIsTrailerModeEnabled() -> bool`

  


### Debug_SaveTestPlayer

`Debug_SaveTestPlayer() `

This doesn't do anything at the moment. 

  


### DebugBiomeMapGetFilename

`DebugBiomeMapGetFilename( x:number = camera_x, y:number = camera_y ) -> string`

  


### EntityConvertToMaterial

`EntityConvertToMaterial( entity_id:int, material:string )`

  


### ConvertEverythingToGold

`ConvertEverythingToGold( material_dynamic:string = "", material_static:string = "" )`

  


### ConvertMaterialEverywhere

`ConvertMaterialEverywhere( material_from_type:int, material_to_type:int ) `

Converts 'material_from' to 'material_to' everwhere in the game world, replaces 'material_from_type' to 'material_to_type' in the material (CellData) global table, and marks 'material_from' as a "Transformed" material. Every call will add a new entry to [WorldStateComponent](Documentation%3A WorldStateComponent.md) which serializes these changes, so please call sparingly. The material conversion will be spread over multiple frames. 'material_from' will still retain the original name id and wang color. Use `[CellFactory_GetType](#CellFactory_GetType)()` to convert a material name to material type. 

  


### ConvertMaterialOnAreaInstantly

`ConvertMaterialOnAreaInstantly( area_x:int, area_y:int, area_w:int, area_h:int, material_from_type:int, material_to_type:int, trim_box2d:bool, update_edge_graphics_dummy:bool ) `

Converts cells of 'material_from_type' to 'material_to_type' in the given area. If 'box2d_trim' is true, will attempt to trim the created cells where they might otherwise cause physics glitching. 'update_edge_graphics_dummy' is not yet supported. 

  


### LoadRagdoll

`LoadRagdoll( filename:string, pos_x:float, pos_y:float, material:string ="meat", scale_x:float=1, impulse_x:float=0, impulse_y:float=0 )`

Loads a given .txt file as a ragdoll into the game, made of the material given in material. 

### GetDailyPracticeRunSeed

`GetDailyPracticeRunSeed() -> int`

  


### ModIsEnabled

`ModIsEnabled( mod_id:string ) -> bool `

Returns true if a mod with the id 'mod_id' is currently active. For example mod_id = "nightmare". 

  


### ModGetActiveModIDs

`ModGetActiveModIDs() -> {string} `

Returns a table filled with the IDs of currently active mods. The IDs are ordered by the mod load order. 

### ModGetAPIVersion

`ModGetAPIVersion() -> int`

  


### ModSettingGet

`ModSettingGet( id:string ) -> bool|number|string|nil `

Returns the value of a mod setting. 'id' should normally be in the format 'mod_name.setting_id'. Cache the returned value in your lua context if possible. 

  


### ModSettingSet

`ModSettingSet( id:string, value:bool|number|string )`

Sets the value of a mod setting. 'id' should normally be in the format 'mod_name.setting_id'. 

### ModSettingGetNextValue

`ModSettingGetNextValue( id:string ) -> bool|number|string|nil `

Returns the latest value set by the user, which might not be equal to the value that is used in the game (depending on the 'scope' value selected for the setting). 

  


### ModSettingSetNextValue

`ModSettingSetNextValue( id:string, value:bool|number|string, is_default:bool ) `

Sets the latest value set by the user, which might not be equal to the value that is displayed to the game (depending on the 'scope' value selected for the setting). 

  


### ModSettingRemove

`ModSettingRemove( id:string ) -> was_removed:bool`

  


### ModSettingGetCount

`ModSettingGetCount() -> int `

Returns the number of mod settings defined. Use `[ModSettingGetAtIndex](#ModSettingGetAtIndex)` to enumerate the settings. 

  


### ModSettingGetAtIndex

`ModSettingGetAtIndex( index:int ) -> (name:string, value:bool|number|string|nil, value_next:bool|number|string|nil) | nil `

'index' should be 0-based index. Returns nil if 'index' is invalid. 

  


### StreamingGetIsConnected

`StreamingGetIsConnected() -> bool`

  


### StreamingGetConnectedChannelName

`StreamingGetConnectedChannelName() -> string`

  


### StreamingGetVotingCycleDurationFrames

`StreamingGetVotingCycleDurationFrames() -> int`

  


### StreamingGetRandomViewerName

`StreamingGetRandomViewerName() -> string`

Returns the name of a random stream viewer who recently sent a chat message. Returns "" if the 'Creatures can be named after viewers' setting is off. 

  


### StreamingGetSettingsGhostsNamedAfterViewers

`StreamingGetSettingsGhostsNamedAfterViewers() -> bool`

  


### StreamingSetCustomPhaseDurations

`StreamingSetCustomPhaseDurations( time_between_votes_seconds:number, time_voting_seconds:number ) `

Sets the duration of the next wait and voting phases. Use -1 for default duration. 

  


### StreamingForceNewVoting

`StreamingForceNewVoting() `

Cancels whatever is currently going on, and starts a new voting. _streaming_on_vote_start() and _streaming_get_event_for_vote() will be called as usually. 

  


### StreamingSetVotingEnabled

`StreamingSetVotingEnabled( enabled:bool ) `

Turns the voting UI on or off. 

  


### SetValueNumber

`SetValueNumber( key:string, value:number )`

  


### GetValueNumber

`GetValueNumber( key:string, default_value:number ) -> number`

  


### SetValueInteger

`SetValueInteger( key:string, value:int )`

  


### GetValueInteger

`GetValueInteger( key:string, default_value:int ) -> int`

  


### SetValueBool

`SetValueBool( key:string, value:number )`

  


### GetValueBool

`GetValueBool( key:string, default_value:number ) -> bool`

## Available only inside a custom BIOME_MAP

### BiomeMapSetSize

`BiomeMapSetSize( width:int, height:int ) `

This is available if BIOME_MAP in magic_numbers.xml points to a lua file, in the context of that file. 

  


### BiomeMapGetSize

`BiomeMapGetSize() -> width:int,height:int `

if BIOME_MAP in magic_numbers.xml points to a lua file returns that context, if not will return the biome_map size 

  


### BiomeMapSetPixel

`BiomeMapSetPixel( x:int, y:int, color_int:int ) `

This is available if BIOME_MAP in magic_numbers.xml points to a lua file, in the context of that file. 

  


### BiomeMapGetPixel

`BiomeMapGetPixel( x:int, y:int ) -> color:int `

This is available if BIOME_MAP in magic_numbers.xml points to a lua file, in the context of that file. 

  


### BiomeMapConvertPixelFromUintToInt

`BiomeMapConvertPixelFromUintToInt( color:int ) -> int `

Swaps red and blue channels of 'color'. This can be used make sense of the `[BiomeMapGetPixel](#BiomeMapGetPixel)()` return values. E.g. `if( BiomeMapGetPixel( x, y ) == BiomeMapConvertPixelFromUintToInt( 0xFF36D517 ) ) then print('hills') end`

  


### BiomeMapLoadImage

`BiomeMapLoadImage( x:int, y:int, image_filename:string ) `

This is available if BIOME_MAP in magic_numbers.xml points to a lua file, in the context of that file. 

  


### BiomeMapLoadImageCropped

`BiomeMapLoadImageCropped( x:int, y:int, image_filename:string, image_x:int, image_y:int, image_w:int, image_h:int ) `

This is available if BIOME_MAP in magic_numbers.xml points to a lua file, in the context of that file. 

  


## Available only during mod initialization

### ModLuaFileAppend

`ModLuaFileAppend( to_filename:string, from_filename:string ) `

Appends the contents of one Lua file to another. It is used in the init.lua file of a mod to modify existing game scripts by adding new functionality. Note that **ModLuaFileAppend** is only available during mod initialization, and cannot be called at runtime, so it is typically found in a mod's init.lua. 

The function takes two string arguments: `to_filename` and `from_filename`. `to_filename` is the file to which the contents of `from_filename` will be appended. 

Example: 
    
    
    ModLuaFileAppend( "data/scripts/gun/gun_actions.lua", "mods/mymod/files/scripts/append_gun_actions.lua")
    

In this example, the contents of `mods/mymod/files/scripts/append_gun_actions.lua` will be appended to the end of `data/scripts/gun/gun_actions.lua`. 

**NOTE:** To avoid mod compatibility issues, it is recommended you append any new functionality instead of replacing an existing script entirely. 

**WARNING:** Since you are appending files, it is possible to create incompatibilities if your lua variables aren't uniquely named. You can give your lua functions and variables a prefix to avoid naming conflicts or put your code inside of a table. 

#### Function Detours

A method of replacing existing functionality while retaining mod compatibility is detouring a lua function, this can be accomplished by reassigning functions. For example when replacing functionality in `generate_shop_item.lua`: 
    
    
    local mymod_old_generate_shop_item = generate_shop_item
    
    generate_shop_item = function(x, y, cheap_item, biomeid_, is_stealable)
      SetRandomSeed( x, y )
      if Randomf() <= 0.5 then
        mymod_generate_custom_shopitem(x, y, cheap_item, biomeid_, is_stealable)
      else
        mymod_old_generate_shop_item(x, y, cheap_item, biomeid_, is_stealable)
      end
    end
    

This example has a 50% chance of replacing an original shop item with your custom shop item. If for example you called the variable `old_generate_shop_item`, and another mod also used the same name, a conflict would occur, so it is important you use a unique name. The same applies to any other variables and functions. An easy way to ensure uniqueness is to place them all inside of a uniquely named table or some other scope. 

### ModTextFileGetContent

`ModTextFileGetContent( filename:string ) -> string `

Returns the current (modded or not) content of the data file 'filename'. Allows access only to data files and files from enabled mods. Available only during mod initialization. 

Can only be used on files with these extensions: `.txt`, `.csv`, `.xml`, `.lua`, `.frag`, and `.vert`

  


### ModTextFileSetContent

`ModTextFileSetContent( filename:string, new_content:string ) `

Sets the content the game sees for the file 'filename'. Allows access only to mod and data files. Available only during mod initialization. 

Can only set the content for files with these extensions: `.txt`, `.csv`, `.xml`, `.lua`, `.frag`, and `.vert`

  


### ModTextFileWhoSetContent

`ModTextFileWhoSetContent( filename:string ) -> string `

Returns the id of the last mod that called ModTextFileSetContent with 'filename', or "". Available only during mod initialization. 

  


### ModMagicNumbersFileAdd

`ModMagicNumbersFileAdd( filename:string ) `

Available only during mod initialization. 

  


### ModMaterialsFileAdd

`ModMaterialsFileAdd( filename:string ) `

Adds all the materials from a custom `materials.xml` file to the existing pool of materials. See [Modding: Making a custom material](https://noita.wiki.gg/zh/wiki/Modding%3A%20Making%20a%20custom%20material%3Faction%3Dedit%26redlink%3D1) for a tutorial and usage. Available only during mod initialization. 

### ModRegisterAudioEventMappings

`ModRegisterAudioEventMappings( filename:string ) `

Available only during mod initialization. 

  


### ModDevGenerateSpriteUVsForDirectory

`ModDevGenerateSpriteUVsForDirectory( directory_path:string, override_existing:bool = false ) `

Please supply a path starting with "mods/YOUR_MOD_HERE/" or "data/". If override_existing is true, will always generate new maps, overriding existing files. UV maps are generated when you start or continue a game with your mod enabled. Available only during mod initialization via noita_dev.exe 

  


### BiomeSetValue

`BiomeSetValue( filename:string, field_name:string, value:multiple_types ) `

Can be used to edit [biome configs](Documentation%3A Biome.md) during initialization. See the nightmare mod for an usage example. 

  


### BiomeGetValue

`BiomeGetValue( filename:string, field_name:string ) -> multiple types|nil `

Can be used to read [biome configs](Documentation%3A Biome.md). Returns one or many values matching the type or subtypes of the requested field. Reports error and returns nil if the field type is not supported or field was not found. 

  


### BiomeObjectSetValue

`BiomeObjectSetValue( filename:string, meta_object_name:string, field_name:string, value:multiple_types ) `

Can be used to edit [biome modifier configs](Documentation%3A BiomeModifiers.md) during initialization. See biome_modifiers.lua for an usage example. 

  


### BiomeVegetationSetValue

`BiomeVegetationSetValue( filename:string, material_name:string, field_name:string, value:multiple_types ) `

Can be used to edit biome config [MaterialComponents](https://noita.wiki.gg/zh/wiki/Documentation%3A%20MaterialComponent%3Faction%3Dedit%26redlink%3D1) during initialization. Sets the given value in all found [VegetationComponent](https://noita.wiki.gg/zh/wiki/Documentation%3A%20VegetationComponent%3Faction%3Dedit%26redlink%3D1) with matching tree_material. See biome_modifiers.lua for an usage example. 

  


### BiomeMaterialSetValue

`BiomeMaterialSetValue( filename:string, material_name:string, field_name:string, value:multiple_types ) `

Can be used to edit biome config [MaterialComponents](https://noita.wiki.gg/zh/wiki/Documentation%3A%20MaterialComponent%3Faction%3Dedit%26redlink%3D1) during initialization. Sets the given value in the first found MaterialComponent with matching material_name. See biome_modifiers.lua for an usage example. 

  


### BiomeMaterialGetValue

`BiomeMaterialGetValue( filename:string, material_name:string, field_name:string ) -> multiple types|nil `

Can be used to read biome config [MaterialComponents](https://noita.wiki.gg/zh/wiki/Documentation%3A%20MaterialComponent%3Faction%3Dedit%26redlink%3D1) during initialization. Returns the given value in the first found MaterialComponent with matching material_name. See biome_modifiers.lua for an usage example. 

## Available only in data/scripts/gun/gun.lua

### RegisterProjectile

`RegisterProjectile( entity_filename:string )`

  


  


### RegisterGunAction

`RegisterGunAction()`

  


  


### RegisterGunShotEffects

`RegisterGunShotEffects()`

  


  


### BeginProjectile

`BeginProjectile( entity_filename:string )`

  


  


### EndProjectile

`EndProjectile()`

  


  


### BeginTriggerTimer

`BeginTriggerTimer( timeout_frames:int )`

  


  


### BeginTriggerHitWorld

`BeginTriggerHitWorld()`

  


  


### BeginTriggerDeath

`BeginTriggerDeath()`

  


  


### EndTrigger

`EndTrigger()`

  


  


### SetProjectileConfigs

`SetProjectileConfigs()`

  


  


### StartReload

`StartReload( reload_time:int )`

  


  


### ActionUsesRemainingChanged

`ActionUsesRemainingChanged( inventoryitem_id:int, uses_remaining:int ) -> uses_remaining_reduced:bool `

  


  


### ActionUsed

`ActionUsed( inventoryitem_id:int )`

  


  


### LogAction

`LogAction( action_name:string )`

  


  


### OnActionPlayed

`OnActionPlayed( action_id:string )`

  


  


### OnNotEnoughManaForAction

`OnNotEnoughManaForAction()`

  


  


### BaabInstruction

`BaabInstruction( name:string )`

  


### _ConfigGunActionInfo_ReadToGame

`_ConfigGunActionInfo_ReadToGame(...)`

This function takes 64 arguments, each corresponding to [ConfigGunActionInfo](Documentation%3A ConfigGunActionInfo.md), in the same listed order. Opposite of [ConfigGunActionInfo_ReadToLua](#ConfigGunActionInfo_ReadToLua). 

  


### Hooks

#### ConfigGun_ReadToLua

`ConfigGun_ReadToLua( actions_per_round:int, shuffle_deck_when_empty:bool, reload_time:int, deck_capacity:int )`

  


#### ConfigGunActionInfo_ReadToLua

`_ConfigGunActionInfo_ReadToLua(...)`

Calls the defined lua function with the 64 parameters of [ConfigGunActionInfo](Documentation%3A ConfigGunActionInfo.md), in the same listed order. Opposite of [_ConfigGunActionInfo_ReadToGame](#_ConfigGunActionInfo_ReadToGame). 

  


#### _clear_deck

`_clear_deck( use_game_log:bool )`

  


#### _add_card_to_deck

`_add_card_to_deck( action_id:string, inventoryitem_id:int, uses_remaining:int, is_identified:bool )`

  


#### _change_action_uses_remaining

`_change_action_uses_remaining( inventoryitem_id:int, uses_remaining:int )`

  


#### _play_permanent_card

`_play_permanent_card( action_id:string )`

  


#### _set_gun

`_set_gun()`

  


#### _set_gun2

`_set_gun()`

  


#### _start_shot

`_start_shot( current_mana:number )`

  


#### _add_extra_modifier_to_shot

`_add_extra_modifier_to_shot( name:string )`

  


#### _draw_actions_for_shot

`_draw_actions_for_shot( can_reload_at_end:bool )`

  


#### _handle_reload

`_handle_reload() -> mana:number`

## Available only in data/scripts/gun/gun_collect_metadata.lua

### RegisterGunAction

Same as above. 

  


### Reflection_RegisterProjectile

`Reflection_RegisterProjectile( entity_filename:string )`

Pairs with [RegisterGunAction](#RegisterGunAction). 

  


## Available only in data/scripts/status_effects/status_reflect.lua

### GameRegisterStatusEffect

`GameRegisterStatusEffect( id:string, ui_name:string, ui_description:string, ui_icon:string, protects_from_fire:bool, remove_cells_that_cause_when_activated:bool, effect_entity:string, min_threshold_normalized:float, extra_status_00:string, effect_permanent:bool, is_harmful:bool )`

This function is what adds all the main status effects to the game 

Parameters  Parameter  | Default  | Type Range  | Info   
---|---|---|---  
id  | REQUIRED  | string  | Unique ID of the effect.   
ui_name  | REQUIRED  | string  | UI Name for the effect   
ui_description  | REQUIRED  | string  | UI Description for the effect   
ui_icon  | REQUIRED  | string (path to icon.png)  | UI Icon for the effect   
protects_from_fire  | false  | bool  | Self-explantory, extinguishes fire. Used for status effects like Bloody or Wet   
remove_cells_that_cause_when_activated  | false  | bool  | When the effect activates, remove the stain/ingestions?? (guess)   
effect_entity  | ""  | string (path to entity.xml)  | Path to the status effect entity that is attached to the status owner   
min_threshold_normalized  | 0.0  | float  | Minimum amount of the trigger required before the effect activates. ratio is 1.0 : 60 seconds   
extra_status_00  | ""  | string  | Maybe adds another status if this one is enabled???   
effect_permanent  | false  | bool  | Decides whether the effect is permanent or not (presumably)   
is_harmful  | false  | bool  | if true, the effect will be blocked by [Iron Stomach](Iron Stomach.md)  
ui_timer_offset_normalized  | 0  | float  | Removes the offset seconds from the display timer normalized is once again 1.0 : 60 seconds   
  
The [![Tripping](https://noita.wiki.gg/zh/images/thumb/Effect_trip.png/16px-Effect_trip.png?3c2422)](/zh/wiki/%E7%8A%B6%E6%80%81#Tripping "Tripping") **[Tripping](状态.md)** (Trippings) effect uses the `min_threshold_normalized` to create its "stages" by having 4 effects in the status list with the later effects having higher thresholds so that the earlier status is overwritten. 

The parameters from `data/scripts/status_effects/status_list.lua` can be found here:
    
    
    	{
    		id="TRIP", --same status ID
    		ui_name="$status_trip_00", -- "Tripping"
    		ui_description="$statusdesc_trip_00", -- "You sense that something is off."
    		ui_icon="data/ui_gfx/status_indicators/trip.png", -- Icon does not change
    		effect_entity="data/entities/misc/effect_trip_00.xml", -- Stage 1 effects
    	},	--default effect starting from 0 seconds
    	{
    		id="TRIP", --same status ID
    		ui_name="$status_trip_01",-- "Tripping Some" 
    		ui_description="$statusdesc_trip_01",-- "You feel in harmony with the magic."
    		ui_icon="data/ui_gfx/status_indicators/trip.png",-- Icon does not change
    		effect_entity="data/entities/misc/effect_trip_01.xml", -- Stage 2 effects
    		min_threshold_normalized=0.5,	--30 seconds
    	},
    	{
    		id="TRIP", --same status ID
    		ui_name="$status_trip_02", -- "Heavily Tripping" 
    		ui_description="$statusdesc_trip_02", -- "Maan, that color smells interesting."
    		ui_icon="data/ui_gfx/status_indicators/trip.png", -- Icon does not change
    		effect_entity="data/entities/misc/effect_trip_02.xml", -- Stage 3 effects
    		min_threshold_normalized=1.5,	--90 seconds
    	},
    	{
    		id="TRIP", --same status ID
    		ui_name="$status_trip_03", -- "Tripping Balls" 
    		ui_description="$statusdesc_trip_03", -- "Usual concepts don't apply."
    		ui_icon="data/ui_gfx/status_indicators/trip.png", -- Icon does not change
    		effect_entity="data/entities/misc/effect_trip_03.xml", -- Stage 4 effects
    		min_threshold_normalized=3.0,	--180 seconds
    	} --comments added by yours truly <3 (not nolla)
    

(this table is run through the function to add all the effects after one another) 

## Available only in data/scripts/perks/perk_reflect.lua

### RegisterPerk

`RegisterPerk( id:string, ui_name:string, ui_description:string, ui_icon:string, perk_icon:string )`

  


## Available only in data/scripts/streaming_integration/event_list.lua

### RegisterStreamingEvent

`RegisterStreamingEvent( id:string, ui_name:string, ui_description:string, ui_icon_path:string, kind:int, weight:number )`  
  
---  
  
### Hooks

#### _reflect

#### _streaming_on_vote_start

#### _streaming_get_event_for_vote

#### _streaming_run_event

#### _streaming_on_irc

#### _streaming_set_event_enabled

## Other/Unspecified

### Hooks

#### wake_up_waiting_threads

`wake_up_waiting_threads( frames_delta:number )`

#### ____cached_func

`____cached_func()`

  


#### biome_modifiers_inject_spawns

`biome_modifiers_inject_spawns( biome_name:string )`

Defined in biome scripts. 

  


## Available only in data/scripts/debug/generate_lua_documentation.lua

### ___main

`___main`

### in_function_signatures

`in_function_signatures:table`

Table with most API function signatures. This is provided by Noita. 

### out_html

`out_html:table`

Table with the resulting html output to be written. This is set in your script. 

### out_json

`out_json:table`

Table with the resulting json output to be written. This is set in your script. 

## Deprecated

Functions that are either deprecated or removed entirely. 

`BiomeMapLoad( filename:string ) `
    Might trigger various bugs. Use [#BiomeMapLoad_KeepPlayer](#BiomeMapLoad_KeepPlayer) instead.
`ComponentGetMetaCustom( component_id:int, variable_name:string ) -> string|nil `
    Use [#ComponentGetValue2](#ComponentGetValue2) instead.
`ComponentGetValueBool( component_id:int, variable_name:string ) -> bool|nil `
    Use [#ComponentGetValue2](#ComponentGetValue2) instead.
`ComponentGetValueFloat( component_id:int, variable_name:string ) -> number|nil `
    Use [#ComponentGetValue2](#ComponentGetValue2) instead.
`ComponentGetValueInt( component_id:int, variable_name:string ) -> int|nil `
    Use [#ComponentGetValue2](#ComponentGetValue2) instead.
`ComponentGetValueVector2( component_id:int, variable_name:string ) -> x:number,y:number|nil `
    Use [#ComponentGetValue2](#ComponentGetValue2) instead.
`ComponentObjectGetValue( component_id:int, object_name:string, variable_name:string ) -> string|nil `
    Use [#ComponentObjectGetValue2](#ComponentObjectGetValue2) instead.
`ComponentObjectGetValueBool( component_id:int, object_name:string, variable_name:string ) -> string|nil `
    Use [#ComponentObjectGetValue2](#ComponentObjectGetValue2) instead.
`ComponentObjectGetValueFloat( component_id:int, object_name:string, variable_name:string ) -> string|nil `
    Use [#ComponentObjectGetValue2](#ComponentObjectGetValue2) instead.
`ComponentObjectGetValueInt( component_id:int, object_name:string, variable_name:string ) -> string|nil `
    Use [#ComponentObjectGetValue2](#ComponentObjectGetValue2) instead.
`ComponentObjectSetValue( component_id:int, object_name:string, variable_name:string, value:string ) `
    Use [#ComponentObjectSetValue2](#ComponentObjectSetValue2) instead.
`ComponentSetMetaCustom( component_id:int, variable_name:string, value:string ) `
    Use [#ComponentSetValue2](#ComponentSetValue2) instead.
`ComponentSetValueValueRange( component_id:int, variable_name:string, min:number, max:number ) `
    Use [#ComponentSetValue2](#ComponentSetValue2) instead.
`ComponentSetValueValueRangeInt( component_id:int, variable_name:string, min:number, max:number ) `
    Use [#ComponentSetValue2](#ComponentSetValue2) instead.
`ComponentSetValueVector2( component_id:int, variable_name:string, x:number, y:number ) `
    Use [#ComponentSetValue2](#ComponentSetValue2) instead.
`GenomeSetHerdId( entity_id:int, new_herd_id:string ) `
    Use [#StringToHerdId](#StringToHerdId) and [#ComponentSetValue2](#ComponentSetValue2) instead.
`GuiTextCentered( gui:obj, x:number, y:number, text:string ) `
    Use [#GuiOptionsAdd](#GuiOptionsAdd) or [#GuiOptionsAddForNextWidget](#GuiOptionsAddForNextWidget) with `GUI_OPTION.Align_HorizontalCenter` and [#GuiText](#GuiText) instead.

### ComponentGetValue

`ComponentGetValue( component_id:int, variable_name:string ) -> string|nil `

Deprecated, use `[ComponentGetValue2](#ComponentGetValue2)()` instead. 

Even though this is deprecated, there are still be rare occasions where you will want to use this older function. `ComponentGetValue` and `ComponentSetValue` can be used on `uint64` type fields, which the new version of these functions can not do. These functions are also the only way to operate `int64` fields without data loss for large values. 

### ComponentSetValue

`ComponentSetValue( component_id:int, variable_name:string, value:string ) `

Deprecated, use `[ComponentSetValue2](#ComponentSetValue2)()` instead. 

Even though this is deprecated, there are still be rare occasions where you will want to use this older function. `ComponentGetValue` and `ComponentSetValue` can be used on `uint64` type fields, which the new version of these functions can not do. These functions are also the only way to operate `int64` fields without data loss for large values. 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
