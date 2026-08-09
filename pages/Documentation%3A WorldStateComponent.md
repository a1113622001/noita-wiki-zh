# Documentation: WorldStateComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20WorldStateComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
is_initialized  | bool  | 0  |  |   
time  | float  | 0  |  |   
time_total  | float  | 0  | [0,1000]  |   
time_dt  | float  | 1  | [0,1000]  | to make the time go really fast or slow?   
day_count  | int  | 0  | [0,3.5]  |   
rain  | float  | 0  |  | should be called clouds, controls amount of cloud cover in the sky   
rain_target  | float  | 0  |  | should be called clouds_target, controls amount of cloud cover in the sky   
fog  | float  | 0  |  |   
fog_target  | float  | 0  |  |   
intro_weather  | bool  | 0  |  | if set, will set the weather to be nice all the time   
wind  | float  | 0  |  |   
wind_speed  | float  | 2  | [-50,50]  |   
wind_speed_sin_t  | float  | 10  |  |   
wind_speed_sin  | float  | 3  | [-50,50]  |   
clouds_01_target  | float  | 0  | [-27,100]  |   
clouds_02_target  | float  | 0  | [-100,185]  |   
gradient_sky_alpha_target  | float  | 0  |  |   
sky_sunset_alpha_target  | float  | 1  |  |   
lightning_count  | int  | 0  | [0,100]  | this gets decreased to 0, this is the frame count of how many times do we do our awesome lightning effect   
next_portal_id  | uint32  | 1  |  |   
session_stat_file  | std::string  |  |  | if empty, we'll create one. This tracks the play time, death, kills... etch   
player_polymorph_count  | int  | 0  |  | how many times player has been polymorphed   
player_polymorph_random_count  | int  | 0  |  | how many times player has been random polymorphed   
player_did_infinite_spell_count  | int  | 0  |  | how many times player has done a secret trick   
player_did_damage_over_1milj  | int  | 0  |  | how many times player has player done damage of over 1000000   
player_living_with_minus_hp  | int  | 0  |  | how many times player has been detected with minus health   
global_genome_relations_modifier  | float  | 0  |  | Genome_GetHerdRelation adds this value to the results. 100 = good relations, 0 is bad   
mods_have_been_active_during_this_run  | bool  | 0  |  |   
twitch_has_been_active_during_this_run  | bool  | 0  |  |   
next_cut_through_world_id  | uint32  | 0  |  |   
perk_infinite_spells  | bool  | 0  |  | if true, almost all spells will have unlimited uses. (black holes, matter eater, heals excluded   
perk_trick_kills_blood_money  | bool  | 0  |  | if true, trick kills will produce blood money (heals player)   
perk_hp_drop_chance  | int  | 0  |  | if > 0, then there's chance that killing an enemy will drop bloodmoney_50   
perk_gold_is_forever  | bool  | 0  |  | drop_money.lua - checks if this is true and removes Lifetime_Component from gold nuggets   
perk_rats_player_friendly  | bool  | 0  |  | if 1, rats don't attack player herd and the other way round. this is a persistent change   
EVERYTHING_TO_GOLD  | bool  | 0  |  | if true everything will be gold + used to track if the wallet should go to infinite   
material_everything_to_gold  | std::string  | gold  |  |   
material_everything_to_gold_static  | std::string  | gold_static  |  |   
INFINITE_GOLD_HAPPENING  | bool  | 0  |  | the secret ending with infinite gold   
ENDING_HAPPINESS_HAPPENING  | bool  | 0  |  | if true, will do the animations for happiness ending   
ENDING_HAPPINESS_FRAMES  | int  | 0  |  | to keep track of the animation   
ENDING_HAPPINESS  | bool  | 0  |  | this is set if ending happiness has happened   
mFlashAlpha  | float  | 0  |  | to keep track of the animation   
DEBUG_LOADED_FROM_AUTOSAVE  | int  | 0  |  | how many times have loaded from autosaves   
DEBUG_LOADED_FROM_OLD_VERSION  | int  | 0  |  | how many times have we loaded from an old version of the game   
Custom data types   
player_spawn_location  | vec2  |  |  |   
lua_globals  | MAP_STRING_STRING  |  |  |   
pending_portals  | VEC_PENDINGPORTAL  |  |  |   
apparitions_per_level  | VECTOR_INT32  |  |  |   
npc_parties  | VEC_NPCPARTY  |  |  |   
orbs_found_thisrun  | VECTOR_INT32  |  |  |   
flags  | VECTOR_STRING  |  |  |   
changed_materials  | VECTOR_STRING  |  |  | pairs of materials changed via ConvertMaterialEverywhere(). stored so these can be restored when loading a save   
cuts_through_world  | VEC_CUTTHROUGHWORLD  |  |  |   
gore_multiplier  | LensValue<int> |  |  |   
trick_kill_gold_multiplier  | LensValue<int> |  |  |   
damage_flash_multiplier  | LensValue<float> |  |  |   
open_fog_of_war_everywhere  | LensValue<bool> |  |  | same as the trailer mode, open fog of war everywhere   
consume_actions  | LensValue<bool> |  |  | same as the trailer mode, spells with limited uses are not consumed if this is false   
Privates   
rain_target_extra  | float  | 0  |  |   
fog_target_extra  | float  | 0  |  |   
perk_rats_player_friendly_prev  | bool  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
