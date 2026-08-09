# Documentation: WormComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20WormComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
speed  | float  | 1  | [0,10000]  |   
acceleration  | float  | 3  | [0,10000]  |   
gravity  | float  | 3  | [0,10000]  |   
tail_gravity  | float  | 30  | [0,10000]  |   
part_distance  | float  | 10  | [0,10000]  |   
ground_check_offset  | int  | 0  | [0,10000]  |   
hitbox_radius  | float  | 1  | [0,1e+006]  |   
bite_damage  | float  | 1  | [0,10]  | how much damage does this do when it hits an entity   
target_kill_radius  | float  | 1  | [0,1e+006]  |   
target_kill_ragdoll_force  | float  | 1  | [0,1e+006]  |   
jump_cam_shake  | float  | 4  | [0,10000]  |   
jump_cam_shake_distance  | float  | 256  | [0,10000]  |   
eat_anim_wait_mult  | float  | 0.05  | [0,10000]  |   
ragdoll_filename  | std::string  |  |  |   
is_water_worm  | bool  | 0  |  | if true, tries to stay in liquids   
max_speed  | float  | 25  |  | max speed, used when attracted to a point   
Custom data types   
ground_decceleration  | LensValue<float> |  |  |   
Privates   
mTargetVec  | vec2  |  |  |   
mGravVelocity  | float  | 0  |  |   
mSpeed  | float  | 0  |  |   
mTargetPosition  | vec2  |  |  |   
mTargetSpeed  | float  | 0  |  |   
mOnGroundPrev  | bool  | 0  |  |   
mMaterialIdPrev  | int  | 0  |  |   
mFrameNextDamage  | int  | 0  |  |   
mDirectionAdjustSpeed  | float  | 1  |  |   
mPrevPositions  | WormPartPositions  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
