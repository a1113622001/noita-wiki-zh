# Documentation: BossDragonComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20BossDragonComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
speed  | float  | 1  | [0,10000]  |   
speed_hunt  | float  | 3  | [0,10000]  |   
acceleration  | float  | 3  | [0,10000]  |   
direction_adjust_speed  | float  | 1  | [0,10000]  |   
direction_adjust_speed_hunt  | float  | 1  | [0,10000]  |   
gravity  | float  | 3  | [0,10000]  |   
tail_gravity  | float  | 30  | [0,10000]  |   
part_distance  | float  | 10  | [0,10000]  |   
ground_check_offset  | int  | 0  | [0,10000]  |   
eat_ground_radius  | float  | 1  | [0,1e+006]  |   
eat_ground  | bool  | 1  |  | does the worm destroy the ground it moves through or not?   
hitbox_radius  | float  | 1  | [0,1e+006]  |   
bite_damage  | float  | 2  | [0,10]  | how much damage does this do when it hits an entity   
target_kill_radius  | float  | 1  | [0,1e+006]  |   
target_kill_ragdoll_force  | float  | 1  | [0,1e+006]  |   
hunt_box_radius  | float  | 512  | [0,10000]  |   
random_target_box_radius  | float  | 512  | [0,10000]  |   
new_hunt_target_check_every  | int  | 30  | [0,10000]  |   
new_random_target_check_every  | int  | 120  | [0,10000]  |   
jump_cam_shake  | float  | 20  | [0,10000]  |   
jump_cam_shake_distance  | float  | 256  | [0,10000]  |   
eat_anim_wait_mult  | float  | 0.05  | [0,10000]  |   
projectile_1  | std::string  | data/entities/projectiles/bossdragon.xml  |  |   
projectile_1_count  | int  | 2  | [0,10]  |   
projectile_2  | std::string  | data/entities/projectiles/bossdragon_ray.xml  |  |   
projectile_2_count  | int  | 5  | [0,10]  |   
ragdoll_filename  | std::string  |  |  |   
Privates   
mTargetEntityId  | int  | 0  |  |   
mTargetVec  | vec2  |  |  |   
mGravVelocity  | float  | 0  |  |   
mSpeed  | float  | 0  |  |   
mRandomTarget  | vec2  |  |  |   
mLastLivingTargetPos  | vec2  |  |  |   
mNextTargetCheckFrame  | int  | 0  |  |   
mNextHuntTargetCheckFrame  | int  | 0  |  |   
mOnGroundPrev  | bool  | 0  |  |   
mMaterialIdPrev  | int  | 0  |  |   
mPhase  | int  | 0  |  |   
mNextPhaseSwitchTime  | int  | 0  |  |   
mPartDistance  | float  | 2  |  |   
mIsInitialized  | bool  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
