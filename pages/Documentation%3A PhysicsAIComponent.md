# Documentation: PhysicsAIComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PhysicsAIComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
target_vec_max_len  | float  | 5  |  |   
force_coeff  | float  | 30  |  |   
force_balancing_coeff  | float  | 1.5  |  |   
force_max  | float  | 100  |  |   
torque_coeff  | float  | 50  |  |   
torque_balancing_coeff  | float  | 0.2  |  |   
torque_max  | float  | 50  |  |   
torque_damaged_max  | float  | 100  |  |   
torque_jump_random  | float  | 0  |  |   
damage_deactivation_probability  | int  | 80  |  |   
damage_deactivation_time_min  | int  | 30  |  |   
damage_deactivation_time_max  | int  | 60  |  |   
die_on_remaining_mass_percentage  | float  | 0.3  |  |   
levitate  | bool  | 1  |  |   
v0_jump_logic  | bool  | 1  |  |   
v0_swim_logic  | bool  | 1  |  |   
v0_body_id_logic  | bool  | 1  |  |   
swim_check_y_min  | int  | -2  |  |   
swim_check_y_max  | int  | 2  |  |   
swim_check_side_x  | int  | 4  |  |   
swim_check_side_y  | int  | -2  |  |   
keep_inside_world  | bool  | 1  |  | fix to the bug in which the spiders spawned inside the holy mountain, if set will try not to go into places which aren't loaded   
free_if_static  | bool  | 0  |  | set true for the boss, because box2d might turn this body into a static body, if it thinks it's glitching out.   
Privates   
rotation_speed  | float  | 0  |  |   
mStartingMass  | float  | 1  |  |   
mMainBodyFound  | bool  | 0  |  |   
mNextFrameActive  | int  | 0  |  |   
mRotationTarget  | float  | 0  |  |   
mLastPositionWhenHadPath  | vec2  |  |  |   
mHasLastPosition  | bool  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
