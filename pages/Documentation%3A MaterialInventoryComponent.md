# Documentation: MaterialInventoryComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20MaterialInventoryComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
drop_as_item  | bool  | 1  |  | if true, drops a bag that the player can big up   
on_death_spill  | bool  | 0  |  | if true, on the death this will explode all the materials into air   
leak_gently  | bool  | 1  |  | NOTE( Petri ): 11.8.2023 - set this to false for old style leaky hidden piles situation.   
leak_on_damage_percent  | float  | 0  |  | if higher than 0 then it might leak when projectile damage happens   
leak_pressure_min  | float  | 0.7  |  | leak pressure coefficient   
leak_pressure_max  | float  | 1.1  |  | leak pressure coefficient   
min_damage_to_leak  | float  | 0.09  |  | the minimum damage that has to be done in order for a leak to occur   
b2_force_on_leak  | float  | 0  | [0,10]  | if 0, nothing happens, elsewise will add a b2 force to the particleemitter which will push the b2body   
death_throw_particle_velocity_coeff  | float  | 1  |  | how far do we throw material particles on death?   
kill_when_empty  | bool  | 0  |  | if set, will send MessageDeath when materials are drained   
halftime_materials  | bool  | 0  |  | if true, will multiply the materials with the given halftimes   
do_reactions  | int  | 0  | [0,100]  | NOTE( Petri ): 15.8.2023 - if > 0, will do CellReactions between the materials. Value is the percent chance of how often. 100 = every frame   
do_reactions_explosions  | bool  | 0  |  | requires do_reactions > 0 - are we allowed to do reaction explosions?   
do_reactions_entities  | bool  | 0  |  | requires do_reactions > 0 - are we allowed to load entities when doing reactions?   
reaction_speed  | int  | 5  |  | Note( Petri ): 17.8.2023 - how 'fast' do we let reactions happen. How many pixels of material do we convert at one time (5-10) seems like a nice speed.   
reactions_shaking_speeds_up  | bool  | 1  |  | Note( Petri ): 17.8.2023 - added the ability of shaking the bottle to cause reactions to happen quicker.   
max_capacity  | double  | -1  |  | how much materials we can store in total. < 0 = infinite   
audio_collision_size_modifier_amount  | float  | 0  |  | if > 0, 'fullness of this container' * 'audio_collision_size_modifier_amount' is added to collision audio event size   
last_frame_drank  | int32  | -100  |  | last frame someone ingested from this via IngestionSystem   
Custom data types   
count_per_material_type  | MATERIAL_VEC_DOUBLES  |  |  | Count of each material indexed by material type ID   
Privates   
is_death_handled  | bool  | 0  |  |   
ex_position  | vec2  |  |  | used to figure out movement velocity   
ex_angle  | float  | 0  |  | used to figure out movement velocity 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
