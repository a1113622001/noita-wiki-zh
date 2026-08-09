# Documentation: AIAttackComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20AIAttackComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
use_probability  | int  | 100  | [0,100]  | The probability for using this attack if it's otherwise possible   
min_distance  | float  | 10  | [0,10000]  | The minimum distance from enemy at which we can perform this attack.   
max_distance  | float  | 160  | [0,10000]  | The maximum distance from enemy at which we can perform this attack.   
angular_range_deg  | float  | 90  | [0,90]  | When looking for threats/prey this is our field of view around the X axis. 90 means we scan the whole 180 degrees around the X axis, to the left and right.   
state_duration_frames  | int  | 45  | [0,1000]  | How long do we stay in the attack state, before other states are allowed?   
frames_between  | int  | 180  | [0,1000]  | The minimum number of frames we wait between these attacks   
frames_between_global  | int  | 30  | [0,1000]  | The minimum number of frames we wait after this attack before doing any other ranged attack   
animation_name  | std::string  | attack_ranged  |  | The animation to play when performing this attack   
attack_landing_ranged_enabled  | bool  | 0  |  | If 1, we try to land before doing the attack, if there's ground near nearby under us   
attack_ranged_action_frame  | int  | 2  | [0,1000]  | The frame of the 'attack_ranged' animation during which the ranged attack actually occurs   
attack_ranged_offset_x  | float  | 0  | [-1000,1000]  | 'attack_ranged_entity_file' is created here when performing a ranged attack   
attack_ranged_offset_y  | float  | 0  | [-1000,1000]  | 'attack_ranged_entity_file' is created here when performing a ranged attack   
attack_ranged_root_offset_x  | float  | 0  | [-1000,1000]  |   
attack_ranged_root_offset_y  | float  | 0  | [-1000,1000]  |   
attack_ranged_use_message  | bool  | 0  |  | If 1, we do ranged attacks by sending a Message_UseItem   
attack_ranged_predict  | bool  | 0  |  | If 1, we attempt to predict target movement and shoot accordingly   
attack_ranged_entity_file  | std::string  | data/entities/projectiles/spear.xml  |  | File to projectile entity that is created when performing a ranged attack   
attack_ranged_entity_count_min  | int  | 1  | [0,1000]  | Minimum number of projectiles shot when performing a ranged attack   
attack_ranged_entity_count_max  | int  | 1  | [0,1000]  | Maximum number of projectiles shot when performing a ranged attack   
attack_ranged_use_laser_sight  | bool  | 0  |  | If 1, we draw a laser sight to our target. Requires entity to have a sprite with tag 'laser_sight'   
attack_ranged_aim_rotation_enabled  | bool  | 0  |  | If 1, we use a laser sight   
attack_ranged_aim_rotation_speed  | float  | 3  |  | How fast can we rotate our aim to track targets   
attack_ranged_aim_rotation_shooting_ok_angle_deg  | float  | 10  |  | If our aim is closer than this to the target we shoot   
Privates   
mRangedAttackCurrentAimAngle  | float  | 0  |  | which direction does our gun currently point at, physically saying?   
mNextFrameUsable  | int  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
