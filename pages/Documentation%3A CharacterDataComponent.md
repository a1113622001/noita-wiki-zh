# Documentation: CharacterDataComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20CharacterDataComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
platforming_type  | int  | 0  | [0,3]  | 0 = oldest, 1 = newer, 2 = safest   
mass  | float  | 1  | [0,10]  | 1.0 = approx. mass of player   
buoyancy_check_offset_y  | int  | -6  | [-1000,1000]  |   
liquid_velocity_coeff  | float  | 9  | [0,20]  | how much do liquids move this character. e.g. when standing in a flowing river   
gravity  | float  | 100  | [0,250]  |   
fly_recharge_spd  | float  | 0  | [0,250]  |   
fly_recharge_spd_ground  | float  | 0  | [0,250]  |   
flying_needs_recharge  | bool  | 0  |  | const variable... player has this as true   
flying_in_air_wait_frames  | int  | 44  | [0,200]  | to fix the tap tap tap flying cheese, we wait this many frames before recharging in air   
flying_recharge_removal_frames  | int  | 8  | [0,20]  | another fix to the tap tap - this is how many frames from pressing down up we'll remove fly charge   
climb_over_y  | int  | 3  | [0,10]  |   
check_collision_max_size_x  | int  | 5  | [0,50]  |   
check_collision_max_size_y  | int  | 5  | [0,50]  |   
is_on_ground  | bool  | 0  |  |   
is_on_slippery_ground  | bool  | 0  |  |   
ground_stickyness  | float  | 0  |  |   
effect_hit_ground  | bool  | 0  |  |   
eff_hg_damage_min  | int  | 0  |  | if we want to damage ground when hitting it... this is the place   
eff_hg_damage_max  | int  | 0  |  | if we want to damage ground when hitting it... this is the place   
eff_hg_position_x  | float  | 0  | [-15,15]  |   
eff_hg_position_y  | float  | 0  | [-15,15]  |   
eff_hg_size_x  | float  | 0  | [-15,15]  |   
eff_hg_size_y  | float  | 0  | [-15,15]  |   
eff_hg_velocity_min_x  | float  | 0  | [-65,65]  |   
eff_hg_velocity_max_x  | float  | 0  | [-65,65]  |   
eff_hg_velocity_min_y  | float  | 0  | [-65,65]  |   
eff_hg_velocity_max_y  | float  | 0  | [-65,65]  |   
eff_hg_offset_y  | float  | 0  | [-15,15]  |   
eff_hg_update_box2d  | bool  | 0  |  | if true, will move physics bodies that it hits   
eff_hg_b2force_multiplier  | float  | 0.0035  |  | multiplies the velocity with this...   
destroy_ground  | float  | 0  |  | how much damage do we do the ground when land on it   
send_transform_update_message  | bool  | 0  |  | if 1, will send Message_TransformUpdated to updated entities and their children when the component is processed by PlayerCollisionSystem or CharacterCollisionSystem   
dont_update_velocity_and_xform  | bool  | 0  |  | might be useful if you want to use CharacterCollisionSystem to only update on_ground status   
mFlyingTimeLeft  | float  | 1000  |  | How much flying energy do we have left? - NOTE( Petri ): 1.3.2023 - This used to be a private variable. It was changed to fix the save/load infinite flying bug.   
Custom data types   
collision_aabb_min_x  | LensValue<float> |  |  |   
collision_aabb_max_x  | LensValue<float> |  |  |   
collision_aabb_min_y  | LensValue<float> |  |  |   
collision_aabb_max_y  | LensValue<float> |  |  |   
fly_time_max  | LensValue<float> |  |  | how much flying energy +   
Privates   
mFramesOnGround  | int  | 0  |  |   
mLastFrameOnGround  | int  | 0  |  |   
mVelocity  | vec2  |  |  |   
mCollidedHorizontally  | bool  | 0  |  | moved this here from CharacterCollisionComponent - since that is multithreaded and we needed a non multithreaded version 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
