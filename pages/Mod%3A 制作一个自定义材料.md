# Mod:制作一个自定义材料

**分类:** [Category:待翻译条目](Category%3A待翻译条目.md) · [Category:Modding](Category%3AModding.md)
**来源:** https://noita.wiki.gg/zh/wiki/Mod%3A%20%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99
---

[![Spell transmutation.png](https://noita.wiki.gg/zh/images/thumb/Spell_transmutation.png/50px-Spell_transmutation.png?ea693f)](https://noita.wiki.gg/zh/wiki/Mod:%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99?action=edit)

此页面的内容需要被翻译。

你可以帮助我们来翻译[此页面](https://noita.wiki.gg/zh/wiki/Mod:%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9D%90%E6%96%99?action=edit)。至于翻译的话请遵守[本Wiki的翻译准则](https://noita.wiki.gg/zh/wiki/Noita%20Wiki%3A%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5)。

  


模组制作导航  基础   
---  
[入门](Mod.md) • [基础](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9F%BA%E7%A1%80) • [Lua脚本](https://noita.wiki.gg/zh/wiki/Mod%3ALua%E8%84%9A%E6%9C%AC) • [Data.wak](Data.wak.md) • [实用工具](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7)  
制作指南   
[音频](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%9F%B3%E9%A2%91) • [敌人](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%8C%E4%BA%BA) • [生物群系](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%94%9F%E7%89%A9%E7%BE%A4%E7%B3%BB) • [天赋](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%A9%E8%B5%8B) • [法术](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B3%95%E6%9C%AF) • [精灵表](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%88%B6%E4%BD%9C%E4%B8%80%E4%B8%AA%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B2%BE%E7%81%B5%E8%A1%A8) • 材料 • [图像放射器](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9B%BE%E5%83%8F%E6%94%BE%E5%B0%84%E5%99%A8) • [特殊行为](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E8%A1%8C%E4%B8%BA) • [创意工坊](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%9C%A8%E5%88%9B%E6%84%8F%E5%B7%A5%E5%9D%8A%E4%B8%8A%E4%BC%A0%E4%BD%A0%E7%9A%84mod) • [CMake使用](https://noita.wiki.gg/zh/wiki/Mod%3ACMake%E4%BD%BF%E7%94%A8)  
组件/实体   
[组件文档](Category%3ADocumentation.md) • [枚举](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%9E%9A%E4%B8%BE) • [特殊标签](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%89%B9%E6%AE%8A%E6%A0%87%E7%AD%BE) • [所有标签列表](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%89%80%E6%9C%89%E6%A0%87%E7%AD%BE%E5%88%97%E8%A1%A8) • [组件更新顺序](https://noita.wiki.gg/zh/wiki/Mod%3A%E7%BB%84%E4%BB%B6%E6%9B%B4%E6%96%B0%E9%A1%BA%E5%BA%8F)  
Lua编程   
[Lua API](https://noita.wiki.gg/zh/wiki/Mod%3ALua%20API) • [实用脚本](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC)  
其他信息   
[法术和天赋的ID](https://noita.wiki.gg/zh/wiki/Mod%3A%E6%B3%95%E6%9C%AF%E5%92%8C%E5%A4%A9%E8%B5%8B%E7%9A%84ID) • [声音事件](https://noita.wiki.gg/zh/wiki/Mod%3A%E5%A3%B0%E9%9F%B3%E5%88%97%E8%A1%A8) • [魔数(Magic Numbers)](https://noita.wiki.gg/zh/wiki/Mod%3A%E9%AD%94%E6%95%B0%5C(Magic%20Numbers%5C) "Mod:魔数\(Magic Numbers\)")  
  
## Getting started

To make a custom material and even reactions between materials, like acid eating through ground, create an XML file with the same structure as the original materials file `data/materials.xml`, though it does not have to be named materials.xml, for instance: 
    
    
    <Materials>
    
      <CellData 
        name="my_custom_material"
        ui_name="$mat_my_custom_material"
        wang_color="ff223344"
        >
      </CellData>
    
      <CellDataChild
        _parent="my_custom_material"
        name="my_custom_material2"
        ui_name="$mat_my_custom_material2"
        wang_color="ff223345"
        >
      </CellDataChild>
    
      <Reaction probability="1"
        input_cell1="my_custom_material"    input_cell2="air"
        output_cell1="my_custom_material2"  output_cell2="air"  
        >
      </Reaction>
    
    </Materials>
    

  
Then, in your mod's `init.lua` you need to tell the game to add your custom material(s) like so: 
    
    
    ModMaterialsFileAdd("mods/your_mod/path_to_your_materials_file.xml")
    

  
This will add two new materials and a reaction that turns the first material into the second when it comes in contact with air. Because we did not specify any properties it will use the defaults instead, which in this case means they are liquids with the same color as specified in `wang_color`. That's the minimum amount of work that's required to add a new material. It's boring but it gives you a starting point from which you can start experimenting. 

Add translation information as well in init.lua. Otherwise it will not show the name when hovering the cursor over the new material, though you can still spawn it, and when put in flasks will display "empty flask" instead of the specified name.
    
    
    local content = ModTextFileGetContent("data/translations/common.csv")
    ModTextFileSetContent("data/translations/common.csv", content .. [[
    mat_my_custom_material, Custom Name,
    mat_my_custom_material2, Custom Name 2,
    ]])
    

## Basics

Now that we know how to get our custom materials into the game, let's first learn about a few important things. First of all, the `name` of each material needs to be unique, if you define a new material with an already existing name it will overwrite the previously defined material with the same name. The name is not shown ingame so go ahead and prefix it with something, for instance `coolmaterialmod_superpoison` instead of just `superpoison`, make sure the prefix has a low chance of ever being used by anyone else. 

Next up, there are two ways to define a material, either as a completely new material in which case you would use `<CellData>`, or by basing it off an existing material by using `<CellDataChild>`, when you use the latter, you need to specify a material to inherit from using the property `_parent`, if you don't, the game will crash. The same goes for specifying a `_parent` on `<CellData>`, only `<CellDataChild>` can **and must** have a `_parent`. This allows you to basically make a copy of an existing material with just slightly different properties. 

The next important thing is the `wang_color`, which also needs to be unique and is how the game knows what materials to place in the world when loading wang tiles or pixel scenes. So when there is a big blob of the color `ffff6000` (the format being hexadecimal ARGB, alpha, red, green, blue), it will know to place lava there, because lava has `wang_color="ffff6000"`. When you define a new material with the same wang color as an existing one, that new material will get placed instead wherever that wang color is used. So make sure to use something unique. But... how? The only way is to pick one randomly and then simply use your text editor to search for that value to check if it already exists or not. The chances of picking an already existing one randomly are relatively small though, because with 255 different values for red, green and blue, there are a total of 16.581.375 different combinations! And that's even without taking alpha into account. 

Making a new material based on an already existing one is a fun and easy way to experiment. You have two options, copying an existing material entirely, or simply extending it by inheriting from it. As an example, let's make a liquid version of sand: 
    
    
    <CellDataChild
      _parent="sand"
      name="mymod_liquid_sand"
      ui_name="Liquid sand"
      wang_color="ff0b4115"
      liquid_sand="0"
      >
    </CellDataChild>
    

Here we inherited from the material `sand` by using `<CellDataChild>` and specifying `_parent="sand"`, gave it a custom `name`, `wang_color` and then the important part, we override the parents property `liquid_sand="1"` by specifying our own: `liquid_sand="0"`. 

At this point you should be able to make any material you like by looking at similar existing materials and creating a modified version of them. 

## Adding graphics and texture

When no graphics are specified, the `wang_color` with full opacity will be used as a graphic instead. That's not good so let's define our own by adding it as a child element of our material: 
    
    
    <CellDataChild
      _parent="sand"
      name="mymod_liquid_sand"
      ui_name="Liquid sand"
      wang_color="ff0b4115"
      liquid_sand="0"
      >
      <Graphics color="8000ff00">
      </Graphics>
    </CellDataChild>
    

This will make the material translucent green, if we want to use a texture instead we would do this: 
    
    
    <Graphics texture_file="data/materials_gfx/lavarock.png">
    </Graphics>
    

Now our material would use a different texture. It's also possible to fine tune the graphics by adding textures for the edges for all kinds of orientations, but that is beyond the scope of this article. 

## Material types

The type of a material is determined by multiple properties, the first and most defining one being `cell_type`, which can be one of 4 different values: `solid, liquid, fire, gas`. They are confusing because you might think that ground is solid, right? WRONG! It's static liquid sand!... What? So what exactly is solid then? Solids are mostly physics objects like boxes, ice, glass, etc and will be simulated using the Box2D physics system. If you make your entire world out of a solid material, it's going to lag like hell because it will constantly collide with itself. So instead you would use static sand, that is sand that floats in the air and can be stood upon, that's basically what every "ground" in noita is. 

Sand itself however is not it's own type, but simply a subtype of liquid. A combination of `cell_type="liquid"` and `liquid_sand="1"`. Most types of materials are a combination of different properties, just check out a similar material as to what you want to make in the default materials in order to find out how to make it. 

As for properties, usually all properties starting with `liquid_` only apply when `cell_type="liquid"`. All properties starting with `solid_` to `cell_type="solid"` and so on. If you specify a inapplicable one it will simply have no effect. Explanations for most properties can be found at the bottom of this article. 

## Stain and ingestion effects

Materials can apply different effects like wet, slimed, oiled etc when entities get stained with that material, or apply ingestion effects when eaten. Only liquids can apply stains, although sand can too, just not very reliably since the material needs to be on top of the to-be-stained entity. To define those effects, add them as a child element, just like `<Graphics>`: 
    
    
    <CellDataChild
      _parent="sand"
      name="mymod_liquid_sand"
      ui_name="Liquid sand"
      wang_color="ff0b4115"
      liquid_sand="0"
      liquid_stains="2"
      >
      <StatusEffects>
        <Stains>
          <StatusEffect type="SLIMY" />
        </Stains>
        <Ingestion>
          <StatusEffect type="FOOD_POISONING" amount="0.2" />
        </Ingestion>
      </StatusEffects>
    </CellDataChild>
    

To make your material stain, you also need to set `liquid_stains="2"`. 

## Reactions

Reactions define how materials interact with each other, for example lava melting metals, acid eating through ground, steam condensating into water, or draught of midas turning everything to gold. This is how you define a reaction: 
    
    
    <Reaction probability="1"
      input_cell1="my_custom_material"    input_cell2="air"
      output_cell1="my_custom_material2"  output_cell2="air"
      >
    </Reaction>
    

The probability determines how fast the reaction happens, input cell 1 and 2 are the materials required for the reaction to happen and output cell 1 and 2 what they turn into respectively. This one would slowly turn `my_custom_material` into `my_custom_material2` when it comes in contact with air. It's also possible to define a reaction that happens when a reaction does **not** meet the requirement, for that you can use `<ReqReaction>`. 

Have you noticed that you can add tags to materials? This makes the reaction system very flexible. Instead of specifying reactions for every material, you can also specify a tag inside a reaction, which means it will react with **any** material using that tag. For instance: 
    
    
    <Reaction probability="20"
      input_cell1="[meltable]"              input_cell2="[lava]"
      output_cell1="[meltable]_molten"      output_cell2="[lava]"
      >
    </Reaction>
    

This is a reaction that applies a reaction to every material with a `[meltable]` tag, that on contact with a material that has a `[lava]` tag turns it into a material with the same name but `_molten` appended. For instance,`wax` has the `[meltable]` tag, so the reaction would turn it into `wax_molten`. Don't forget that for this to work, a material with `name="wax_molten"` needs to exist. 

There is a whole lot more to reactions that is best to be explored by studying the `data/materials.xml` as it would go well beyond the scope of this article. 

## Making materials deal damage

How much damage a materials deals is not a property of the material, but rather a property of the `DamageModelComponent` of the to-be-damaged entity. That means if you want a material to deal contact damage to the player, you would have to get the player entity, get it's `DamageModelComponent` and change the `materials_that_damage` and `materials_how_much_damage` properties to include your new material. The properties are both a comma seperated string. Example: 

`materials_that_damage="acid,lava,magic_gas_hp_regeneration"`

`materials_how_much_damage="0.005,0.003,-0.005"`

This would cause acid to deal 0.005 damage, lava 0.003 and magic_gas_hp_regeneration would heal 0.005 because it's a negative number. The numbers are damage per particle, per tick, divided by 25. So if you want something to deal 0.1 damage per particle, you have to set the damage to 0.004. However, because modifying a comma seperated string is clunky and changes to `materials_that_damage` and `materials_how_much_damage` don't take immediate effect, you can use these helper functions: 
    
    
    local function stringsplit(inputstr, sep)
      sep = sep or "%s"
      local t = {}
      for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
        table.insert(t, str)
      end
      return t
    end
    -- Returns a key-value table, where they keys are the material name and the values the damage.
    function get_materials_that_damage(entity_id)
      local out = {}
      local damage_model_component = EntityGetFirstComponentIncludingDisabled(entity_id, "DamageModelComponent")
      if damage_model_component then
        local materials_that_damage = ComponentGetValue2(damage_model_component, "materials_that_damage")
        materials_that_damage = stringsplit(materials_that_damage, ",")
        local materials_how_much_damage = ComponentGetValue2(damage_model_component, "materials_how_much_damage")
        materials_how_much_damage = stringsplit(materials_how_much_damage, ",")
        for i, v in ipairs(materials_that_damage) do
          out[v] = materials_how_much_damage[i]
        end
        return out
      end
    end
    -- <materials> should be a key-value table with the keys being the name of the material to change and the value the new damage.
    -- For instance: change_materials_that_damage(entity_id, { lava = 0, new_material = 0.004 }) would make the entity immune to lava
    -- and the material with name="new_material" would deal 0.004 damage.
    function change_materials_that_damage(entity_id, materials)
      -- At the time of writing (1st of September 2020) changes to DamageModelComponent:materials_that_damage
      -- do not take effect. One of the ways to work around that is to remove and re-add the component with
      -- the changes applied and the same old values for everything else
      local damage_model_component = EntityGetFirstComponentIncludingDisabled(entity_id, "DamageModelComponent")
      if damage_model_component then
        -- Retrieve and store all old values of the DamageModelComponent
        local old_values = {}
        local old_damage_multipliers = {}
        for k,v in pairs(ComponentGetMembers(damage_model_component)) do
          -- ComponentGetMembers does not return the value for ragdoll_fx_forced, ComponentGetValue2 is necessary
          if k == "ragdoll_fx_forced" then
            v = ComponentGetValue2(damage_model_component, k)
          end
          old_values[k] = v
        end
        for k,_ in pairs(ComponentObjectGetMembers(damage_model_component, "damage_multipliers")) do
          old_damage_multipliers[k] = ComponentObjectGetValue(damage_model_component, "damage_multipliers", k)
        end
        -- Build comma separated string
        old_values.materials_that_damage = ""
        old_values.materials_how_much_damage = ""
        local old_materials_that_damage = get_materials_that_damage(entity_id)
        for material, damage in pairs(materials) do
          old_materials_that_damage[material] = damage
        end
        for material, damage in pairs(old_materials_that_damage) do
          local comma = old_values.materials_that_damage == "" and "" or ","
          old_values.materials_that_damage = old_values.materials_that_damage .. comma .. material
          old_values.materials_how_much_damage = old_values.materials_how_much_damage .. comma .. damage
        end
        EntityRemoveComponent(entity_id, damage_model_component)
        damage_model_component = EntityAddComponent(entity_id, "DamageModelComponent", old_values)
        ComponentSetValue2(damage_model_component, "ragdoll_fx_forced", old_values.ragdoll_fx_forced)
        for k, v in pairs(old_damage_multipliers) do
          ComponentObjectSetValue(damage_model_component, "damage_multipliers", k, v)
        end
      end
    end
    

Then use them like this in your `init.lua` right after your player spawns: 
    
    
    function OnPlayerSpawned(player_entity)
      change_materials_that_damage(player_entity, { your_new_material = 0.004 })
    end
    

Making enemies take damage from a certain material is much harder since it requires modification of every enemies `DamageModelComponent` individually and therefore not explained in this article at this time. 

## List of all known material properties

Lastly here is a list that was compiled through experimentation and analyzing the `data/materials.xml` file. 

### General properties

Property | Value type / range | Info   
---|---|---  
_parent | slime_green | Name of the material to inherit from. Only valid for CellDataChild.   
_inherit_reactions | [0, 1] | If reactions from the parent element should be inherited.   
name | sand | Internal name, should be unique, otherwise will overwrite materials.   
ui_name | Sand | What the player will see as the material name.   
cell_type | [solid, liquid, fire, gas] | Type of the material. default = liquid   
platform_type | [0, 2] | 0 = fall through, 1 = can stand on, 2 = unused?   
tags | [tag1],[tag2],[tag3] | A list of tags.   
wang_color | ffb80902 | Should be unique, the color which wang tiles and pixel scenes use to load materials.   
wang_noise_percent | [0, 3.5] | ???   
wang_noise_type | [0, 2] | ???   
wang_curvature | [0.25, 0.5] | ???   
gfx_glow | [0, 255] | Higher values will make the material glow brighter.   
gfx_glow_color | 0xffffffff ARGB | Color of glow if gfx_glow is set.   
electrical_conductivity | [0, 1] | Makes the material conduct elecricity.   
color | FF890000 | Unused?   
hp | [5, 1000000] | ???   
stickyness | [0.0, ??] | The amount of slowdown in liquid, can go above 1.0 but the change becomes increasingly unnoticable.   
durability | [0, 14] | How hard it is to break (e.g. with spells, explosions etc)   
density | [1, 50 (no limits?)] | (liquids, sand) More dense materials seep through lesser ones   
slippery | [0, 1] | For solids or for liquid_sand liquid_static materials, makes surface slippery, causing entities to slide.   
stainable | [0, 1] | default seems to be 1   
lifetime | [0, 1350] | Liquids and gases only, material disappears when lifetime runs out   
collapsible | [0, 1] | Unused? Only concrete has it set to 1   
status_effects | [WET, OILED, RADIOACTIVE, ON_FIRE, SLIMY, POLYMORPH, ALCOHOLIC, CONFUSION, MOVEMENT_FASTER_2X, WORM_ATTRACTOR, PROTECTION_ALL, MANA_REGENERATION, TELEPORTATION, HP_REGENERATION, POLYMORPH_RANDOM, BERSERK, CHARM, INVISIBILITY, BLOODY] "WET" | May be obsolete? Or just a shorthand version of the new status effect system.   
show_in_creative_mode | [0, 1] | Make it show up in the dev mode material painting dialog?   
  
### For cell_type="liquid"

Property | Value type / range | Info   
---|---|---  
liquid_sand | [0, 1] | 1 = it's sand, you can stand on it   
liquid_slime | [0, 1] | 1 = it flows slower   
liquid_solid | [0, 1] | ???   
liquid_static | [0, 1] | Liquid doesn't flow, instead stays wherever it's placed   
liquid_gravity | [0.0, 5.0] | no max, with 0 it still falls, but slow and weird   
liquid_stains_custom_color | AA830000 | if liquid_stains="2" and liquid_stains_self="1" the liquid will stain the world with this color   
liquid_stains_self | [0, 1] | Determines if the liquid can stain itself with liquid_stains_custom_color   
liquid_stains | [0, 4] | (also works for gases) 1 = gives stain effect, but no visuals, 2 stain/color entities and world, 3 = apply stains but visual effect to world only, 4 = ?? (only oil has 4)   
liquid_sprite_stain_ignited_drop_chance | [0, 10] | How fast stains disappear when on fire   
liquid_sprite_stains_check_offset | [-1, 1] | ???   
liquid_sprite_stain_shaken_drop_chance | [0, 5] | How quickly it can be shaken off, higher values = wears of more quickly   
liquid_sprite_stains_status_threshold | [0.2, 0.3] | How much you need on you before you get the status effect?   
liquid_damping | [0.9, 0.9] | other values produce glitchy behaviour   
liquid_viscosity | [0, 150] | no noticable difference?   
liquid_sand_never_box2d | [0, 1] | pretty much unused   
liquid_sticks_to_ceiling | [0, 1] | Needs liquid_sand="1", actually only 0 and 1 work, even though the game uses 50, is used for ground sand that should not move   
liquid_flow_speed | [0.0*, 1.0*] | *actually can go beyond the limits but looks bad and glitchy   
cell_holes_in_texture | [0, 1] | Only works for cell_type="liquid", doesn't place material where texture alpha is zero   
  
### For cell_type="solid"

Property | Value type / range | Info   
---|---|---  
explosion_power | [2.5, 2.5] | Only used by an unused material (meteorite_green)   
solid_break_on_explosion_rate | [10, 90] | Only 5 unused materials use it   
solid_on_break_explode | [0, 1] | On break, will turn the material into the material defined in solid_break_to_type   
solid_break_to_type | material_name | ???   
convert_to_box2d_material | material_name | When it takes damage, immediately converts the whole structure into that material   
crackability | [0, 100] | How easily it breaks like glass/ice, higher values mean easier to crack   
solid_on_collision_explode | [0, 1] | Requires <ExplosionConfig>  
solid_on_collision_splash_power | [1, 1] | ???   
solid_on_collision_convert | [0, 1] | When it hits something (ground, projectiles etc), converts to solid_on_collision_material   
solid_on_collision_material | slime | See above   
solid_collide_with_self | [0, 1] | ???   
solid_on_sleep_convert | [0, 1] | ???   
solid_restitution | [0, 0.7] | Bouncyness? 0 = no bounce, 1 = bounce forever, higher numbers make it bounce more and more   
solid_friction | [0.05, 1.0] | lower number = more slippery, higher = stops sliding faster   
solid_go_through_sand | [0, 1] | ???   
solid_gravity_scale | ???   
solid_static_type | [0, 5] | 0 = it can fall, player can pass, projectiles not 1 = static, nothing can pass, 2,3,4,5 = static, player can pass, bullets not   
  
### Audio related

Property | Value type / range | Info   
---|---|---  
audio_materialbreakaudio_type | [WOOD] | ???   
audio_size_multiplier | [0.0, 3.0] | ???   
audio_physics_material_solid | [rock, wood, ice, sand, slime, meat, gravel, organicbouncy, metalhollow_gold, bone, metalhollow, gold, glass, metalhollow_barrel, snow, organicsoft] |   
audio_physics_material_event | [rock, sand, gravel, slime, metalhollow_gold, metalhollow, snow] |   
audio_physics_material_wall | [gravel, rock, woodwall, ice, sand, slime, meat, organicbouncy, metalwall, bone, glass, metalhollow, metalhollow_barrel, snow, organicsoft] |   
audio_materialaudio_type | [LAVA] |   
audio_is_soft | [0, 1] | no difference?   
  
### Fire related

Property | Value type / range | Info   
---|---|---  
always_ignites_damagemodel | [0, 1] | Ignites anyone who touches it   
burnable | [0, 1] | If it can catch fire   
fire_hp | [-1, 99999999] | Fire takes away fire_hp and when it runs out, material disappears? If -1 will burn forever   
on_fire | [0, 1] | If 1, will start out on fire   
on_fire_convert_to_material | material_name | When it catches fire convert to this material?   
requires_oxygen | [0, 1] | if 0, only the edges exposed to air will burn, with 1, the whole material   
generates_flames | [20, 20] | How many flames are generated   
temperature_of_fire | [0, 200] | Higher temperatures make it easier for other nearby materials to catch on fire   
autoignition_temperature | [0, 99] | ??? What temperature is required for it to start burning?   
generates_smoke | [0, 20] | How much smoke is generated by burning   
  
### Vegetation

Property | Value type / range | Info   
---|---|---  
vegetation_full_lifetime_growth | [700, 6000] | How big/small vegetation starts out?   
vegetation_sprite | data/vegetation/bush_growth_$[1-8].xml | The sprite to use, supports $[1-8] notation.   
supports_collapsible_structures | [0, 1] | ???   
  
### Info for AI

Property | Value type / range | Info   
---|---|---  
danger_radioactive | [0, 1] | For enemy AI so they know where to stay away from and where to go to extinguish flames?   
danger_fire | [0, 1] |   
danger_water | [0, 1] |   
danger_poison | [0, 1] | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
