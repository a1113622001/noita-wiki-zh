# Mod:制作一个自定义生物群系

**分类:** [Category:待翻译条目](Category%3A待翻译条目.md) · [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Mod%3A%20%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB
---

[![Spell transmutation.png](https://noita.wiki.gg/zh/images/thumb/Spell_transmutation.png/50px-Spell_transmutation.png?ea693f)](https://noita.wiki.gg/zh/wiki/Mod:%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB?action=edit)

此页面的内容需要被翻译。

你可以帮助我们来翻译[此页面](https://noita.wiki.gg/zh/wiki/Mod:%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB?action=edit)。至于翻译的话请遵守[本Wiki的翻译准则](https://noita.wiki.gg/zh/wiki/Noita%20Wiki%3A%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5)。

  


模组制作导航  基础   
---  
[入门](Mod.md) • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • 生物群系 • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • [材料](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99) • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
Noita世界生成和操作基础知识指南。   


# 生物群系加载的工作原理

在生成地图时，游戏需要知道的第一件事是加载哪个生物群系。这是在magic number内由`BIOME_MAP`定义的，默认值为`data/biome_impl/biome_map.png`。 

生物群系可以通过以下三种方式之一更改： 

  * 通过将你的新文件放在 Mod 的相同文件夹结构中以覆盖原文件，例如： `mods/yourmod/data/biome_impl/biome_map.png`
  * 通过在init.lua内调用`ModMagicNumbersFileAdd`方法向magic number中加入内容让游戏静态加载不同的生物群系，被加入的xml文件内容为：


    
    
    <MagicNumbers BIOME_MAP="mods/yourmod/yourmap.png"></MagicNumbers>
    

  * 类似第二种方式，通过调用lua文件而非png文件以动态地加载生物群系：


    
    
    <MagicNumbers BIOME_MAP="mods/yourmod/yourmap.lua"></MagicNumbers>
    

由于第2种方法是静态的，这就意味着你不能带有条件地加载它们，因此如果我们希望生物群系模组兼容就必须使用第3种方法。关于这个我们稍后再谈。现在，让我们看看游戏到底是如何处理生物群系地图的。 

一旦一个生物群系地图被加载了，游戏就会遍历所有被定义在`data/biome/_biomes_all.xml`中的生物群系，对于每个其中的条目，**无论它是否在生物群系地图图像上** ，它都会去解析`biome_filename`中定义的文件，例如： 
    
    
    <Biome
      biome_filename="data/biome/coalmine.xml"
      height_index="1"
      color="ffd57917"
    ></Biome>
    

will go look at `data/biome/coalmine.xml`, which in turn has two more definitions, `wang_template_file="data/wang_tiles/coalmine.png"` which defines which wang tiles will be used to generate the biome and `lua_script="data/scripts/biomes/coalmine.lua"`, pointing to a script that will run once every time at game startup (meaning it will run again on quit & reload) and stay loaded throughout the game session. These 2 files defined in the biome's xml will always be accessed by the game, so they **must** exist, otherwise it will crash. 

After parsing the `_biomes_all.xml`, which also sets the `biome_offset_y`, it will load the biome map image and spawn the player in the world. The worlds origin (0, 0) position is defined by: 

  * horizontal, x: Center of the biome map
  * vertical, y: `biome_offset_y` defined in `_biomes_all.xml` (`biome_offset_x` does not exist)



### Biome generation

Now the actual biome generation happens, at whatever position the camera is currently pointing at, meaning what is currently visible and needs to be generated. Everything that's outside the camera will only be generated once it is needed, once it comes close to the viewport. 

The start position will at first be empty space, so the game looks at the biome map to determine which biome needs to be loaded, by taking the camera coordinates, let's say x=1098, y=824. 

One pixel on the biome map image is one chunk (512x512 ingame pixels/units), so to get which pixel this corresponds to on the biome map image, we: 

  * divide x by 512 = 2.144, round down to `2`
  * divide y by 512 = 1.609, round down to `1`
  * which gives us x=2, y=1



which means the corresponding pixel on the biome map is 2 pixels to the right from the center, and 1 pixel down from `biome_offset_y`. So at a size of 70x35 pixels: 

  * x = 70/2 = 35 + 2 = `37`
  * y = biome_offset_y=14 + 1 = `15`



Which gives us x=37, y=15 on the `biome_map.png`. That pixel has the color `ffd57917` (hex ARGB), so the game looks inside the `_biomes_all.xml`, for a `<Biome>` with `color="ffd57917"`. There is one declared with that color, which defines `biome_filename="data/biome/coalmine.xml"`. In that file in turn `wang_template_file` tells the game how to generate the biome. 

Shades of grey will get filled with the materials defined in `coalmine.xml`'s `<Materials>`, while other colors will place the corresponding materials directly. Which color corresponds to which material is defined in `data/materials.xml` in the `wang_colors` attributes. 

### Biome scripts

But what about enemies and items? How do they get placed? By looking at the pixel colors of the wang tiles when placing them, each time it places a wang tile, which is the first time it comes into the camera viewport, it will try to call a predefined function in the biomes `lua_script`. Some are hardcoded and can be found in `data/scripts/wang_scripts.csv`. For instance: `ffffd171,spawn_orb,-1,-1,-1,-1` If it places a wang tile that has a pixel with color `ffffd171` inside it, it will call `spawn_orb(x, y)` where x and y are the coordinates where that pixel is placed in the world. If that function is not present in the biomes `lua_script`, it will produce an error when running `noita_dev.exe` without crashing. Some of these scripts have a default version defined in `data/scripts/biome_scripts.lua`, which can simply be imported like:
    
    
    dofile_once("data/scripts/biome_scripts.lua")
    

But you still need to define all the rest or you get spammed with errors like: 

`Couldn't find function: spawn_props`

We can also define our own pixel colors and corresponding scripts using:
    
    
    RegisterSpawnFunction(0xffabcdef, "my_function_name")
    function my_function_name(x, y)
    -- Gets called for every pixel of color ffabcdef found either in a wang tile, or a pixel scene
    end
    

There is also a special "color" that can be registered:
    
    
    RegisterSpawnFunction(0xffffeedd, "init")
    

whose pixel doesn't need to be placed anywhere, this is a special case. This will run the defined function every time a biome chunk is loaded. 

### Where does the tree to the left of the starting position and the skull in the desert come from?

That is defined in `data/biome/_pixel_scenes.xml`, where global pixel scenes are defined with absolute world coordinates. This path seems to be hardcoded and cannot be changed. So if you want to get rid of those pixel scenes, you will have to overwrite that file. 

There is also this function, which is used by new game+:
    
    
    BiomeMapLoad_KeepPlayer(filename, pixel_scenes='data/biome/_pixel_scenes.xml')
    

But that seems to be only callable once the game is already running and the map had been loaded. `filename` can be a biome map image or a map loading script (it works the same as `MagicNumbers:BIOME_MAP`). This is how you can re-generate the world and load a different pixel scenes file. As of today (12th April 2020) I found that this function is not reliable since it can sometimes crash the game. 

# How to make biome mods compatible

### Problems

Now that we know how biomes get defined and loaded, let's look at what makes compatibility difficult. 

New biomes must be added to `data/biome/_biomes_all.xml`, but this cannot be done programmatically. The only way is to overwrite it with our own `_biomes_all.xml` which we add our biome definitions into. If multiple mods do this however, the last mod that gets loaded overwrites all of the previous versions, nullifying them. So there needs to be a `_biomes_all.xml` which has **all** of every mods biomes defined inside of it and it needs to be the one that gets loaded. Furthermore, since **all** biomes will be declared, the files pointed to **must** always exist, even if that mod is not installed or active, otherwise the game crashes. So: 

  * In `_biomes_all.xml` the files defined in `biome_filename="data/biome/coalmine.xml"`
  * and inside that file: `wang_template_file="data/wang_tiles/coalmine.png"`
  * and `lua_script="data/scripts/biomes/coalmine.lua"`



Then, depending on which mods are active, a different biome map image needs to be loaded or modified, which has all the biomes in their desired place. 

### The current solution:

All mods need to: 

  * Have the same, up-to-date `data/biome/_biomes_all.xml`
  * Have all other mods up-to-date `biome.xml`s and `wang_template_file`s
  * Have the same up-to-date biome map loader script, defined in `MagicNumbers:BIOME_MAP`
  * Have the same biome map height, since the `biome_offset_y` is defined in `_biomes_all.xml`, so a taller map means that offset has to change, but all mods share the same file, so... if one mod decides to make a taller map, everyone needs to have a tall map.



All of those need to be kept up-to-date. Every time a mod wants to change any of those files, meaning either the map layout, adding new biomes, changing the biome files like materials, or modifying wang templates, these files need to be updated for everyone. There are two solutions: 

  * A) Everyone deploys a duplicate of those files in their mod. (This is the current method)
  * B) It all gets seperated out into another mod, which will be a dependency of all biome mods.



One upside of (A) is that there is no need to download a dependency mod. A big downside of solution (A) is that if an outdated mod gets loaded last, it will overwrite all the data files with outdated versions, potentially breaking other mods should they have released an update since then. If it gets loaded first, it will have it's outdated `MagicNumbers:BIOME_MAP` script run. 

Solution (B) is much better for mod developers since only one mod needs to be updated when there is a change. The problem however is, that steam workshop does not allow multiple mod developers to work together on one mod, which would be necessary for (B). It's also not possible to transfer ownership. So one person would have to be responsible for providing and maintaining the mastermod. 

For both methods, mod loading order does not matter. 

* * *

In order to keep everything organized and easier to update, I propose that all files that need to be shared should go into their own subfolder in data: `data/shared/ModName`. This way that folder can simply be deleted and replaced with an updated version instead of finding all individual files. As a mod developer you can also quickly see which files need to be shared. Entities spawned from your biome scripts, pixel scenes etc are independent and can be put wherever you like. 

So to reiterate, all files that need to be shared and up-to-date for everyone are: 

  * `_biomes_all.xml`
  * The files defined in there, like `biome_filename="data/biome/coalmine.xml"`
  * The wang template files like `wang_template_file="data/wang_tiles/coalmine.png"`
  * Biome map loading script defined in `MagicNumbers:BIOME_MAP`



* * *

One solution that I found for making the lua scripts independent is this: The shared files will simply point to a `dummy_script.lua`, in which the actual file will get loaded. Like this, when `biome.xml` points to `biome_dummy.lua`, which is this file:
    
    
    if ModIsEnabled("MyCoolMod") then
      dofile_once("mods/MyCoolMod/biome.lua")
    end
    

If the mod is not active, it's biome will not be present on the map, and won't really have it's functions executed. It **will** get loaded, but none of it's spawner functions called, so having an empty file with just this if statement works. In case the mod is enabled, it will load the actual real file and everything works normally. This allows mod authors to change their `Biome:lua_script` without having to update the shared files, only the dummy scripts need to be shared once. Finally, we need to to actually put the new biomes on the biome map. There are two solutions. First we need to handle map loading inside a script, to do that we point to a lua script instead of a png:
    
    
    <MagicNumbers BIOME_MAP="mods/yourmod/yourmap.lua"></MagicNumbers>
    

Which will allow us to use the `BiomeMap*` functions inside that file to for instance load a pre-generated static map depending on which mods are active:
    
    
    BiomeMapSetSize(70, 45)
    if ModIsEnabled("SomeMod") and ModIsEnabled("OtherMod") then
      -- Has both SomeMod's pixels placed and OtherMod's.
      BiomeMapLoadImage(0, 0, "data/biome_impl/biome_map_somemod_othermod.png")
    elseif not ModIsEnabled("SomeMod") and ModIsEnabled("OtherMod") then
      -- Only has OtherMod's pixels placed.
      BiomeMapLoadImage(0, 0, "data/biome_impl/biome_map_othermod.png")
    end
    -- etc
    

Yes, this will get horribly complicated with more mods, another solution would be to use `BiomeMapSetPixel` to dynamically paint onto the map:
    
    
    BiomeMapSetSize(70, 45)
    BiomeMapLoadImage(0, 0, "data/biome_impl/biome_map.png")
    if ModIsEnabled("SomeMod") then
      BiomeMapSetPixel(35, 14, 0xffabcdef)
    end
    if ModIsEnabled("OtherMod") then
      BiomeMapSetPixel(40, 14, 0xfffedcba)
    end
    

Helper functions to fill rectangle areas would be easy to implement and actually already exist in the nightmare mode mod. 

Things to note: The last mod in the list will overwrite `data` files, but the **first** mod that gets loaded and defines `MagicNumbers:BIOME_MAP` will have it's file loaded, all others that define it again after that will be ignored. 

# How to make your mod compatible with nightmare mode and new game+

### Nightmare mode

Nightmare mode will try to use it's own map generation script by setting `MagicNumbers:BIOME_MAP`. If the mod is at the top of the mod loading order, it will succeed. But luckily it seems to be possible to append to it's map loading script like any other:
    
    
    ModLuaFileAppend("mods/nightmare/files/biome_map.lua", "your_map_loading_script.lua")
    

In addition to that, any `BiomeMapSetSize` and `BiomeMapLoadImage` calls can simply be overwritten and undone, by calling them again. What this means is that you can simply append your usual map loading script and everything will work fine, regardless of mod loading order. 

### New game+

This one is a little trickier, new game+ will get initiated in `data/entities/animals/boss_centipede/ending/sampo_start_ending_sequence.lua` line 41. The part that is important is inside `data/scripts/newgame_plus.lua` line 71:
    
    
    BiomeMapLoad_KeepPlayer("data/biome_impl/biome_map_newgame_plus.lua", "data/biome/_pixel_scenes_newgame_plus.xml")
    

We need to somehow hijack this to again point to our own map loading script. And we might also want to prevent the usage of the NG+ pixel scenes. This can be done by appending this to `biome_map_newgame_plus.lua`:
    
    
    setfenv(do_newgame_plus, setmetatable({
      BiomeMapLoad_KeepPlayer = function(map_file, pixel_scenes_file)
        BiomeMapLoad_KeepPlayer("your_map_loading_script.lua")
      end
    }, {
      __index = _G
    }))
    

This will simply redirect the call to `BiomeMapLoad_KeepPlayer` inside the function `do_newgame_plus` to our own version. 

### Compatibility example

Here are 2 sample mods that demonstrate how compatibility can be done. One of them has 2 versions, the only difference is simply the folder structure. Not sure yet what would be best. 

<https://drive.google.com/open?id=1exlxZ_9WFXGm53i4d1Arx4dD4oxtOerH>

# Material reference for mapping

Open the thumbnail on right and save the file locally. You can then open it in your favorite image editor while editing wang tiles or pixel scenes for easy color-picker selection of any material or biome color. 

[![](https://noita.wiki.gg/zh/images/thumb/Material_Colors.png/320px-Material_Colors.png?4ba923)](/zh/wiki/File:Material_Colors.png)

[](https://noita.wiki.gg/zh/wiki/File%3AMaterial%20Colors.png)

  


# Pixel Scenes

**Pixel Scenes** are images, randomly chosen by the generator or defined manually in `data/biome/_pixel_scenes.xml`

To draw a **pixel scene** , use the reference colors from the thumbnail image. The color **FFFFFF** uses materials from the biome it loads in, so you dont have to draw it yourself. 

Example of a **Pixel Scene** image: 

[![Examplescene.png](https://noita.wiki.gg/zh/images/Examplescene.png?ff1c53)](/zh/wiki/File:Examplescene.png)

_You can spawn your scene with T in devmode._

### Adding pixel scenes to biome generation

First draw your pixel scene (or just copy the one above). To use it in generated biomes you then need to make a .lua file, to append it into the scene pool:
    
    
    table.insert(g_pixel_scene_02, {
      prob = 1000,
      material_file = "mods/yourmod/files/scene.png",
      visual_file = "",
      background_file = "",
      is_unique = 0
    })
    

  * Use `g_pixel_scene_01` for vertical scenes, `g_pixel_scene_02` for horizontal ones.
  * `prob` should be from 0-1000, 1000 being most common.
  * `material_file` spawns the materials,(see example above)
  * `visual_file` does visuals of those materials, like the appearance of wand pedestals. **Note:** this is applied only _on top_ of materials. Eg. visuals have no effect on air.
  * `background_file` is the background, which can any sort of image you wish.



  
Lastly, append your new file to the biome you want to add your scene to, by putting this in your init.lua: 

`ModLuaFileAppend("data/scripts/biomes/coalmine.lua", "mods/somemod/files/examplescene.lua")`

First argument being the path to the biomes script, second to your scenes script. 

  


# Wang Tiles

Making your own wang tiles? Check how they would look like in-game with Horscht's awesome [web-based wang tiler](https://thehorscht.github.io/NoitaWangTiler/)

Examples of the wang tiles from the [Coal Pits](Coal Pits.md) (full, and zoomed section) can be seen below. 

  * [![Coalmine wang tiles.png](https://noita.wiki.gg/zh/images/thumb/Coalmine_wang_tiles.png/94px-Coalmine_wang_tiles.png?2a94d7)](/zh/wiki/File:Coalmine_wang_tiles.png)

  * [![Coalmine wang tiles zoom.png](https://noita.wiki.gg/zh/images/thumb/Coalmine_wang_tiles_zoom.png/120px-Coalmine_wang_tiles_zoom.png?205245)](/zh/wiki/File:Coalmine_wang_tiles_zoom.png)



  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
