# Documentation: VelocityComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20VelocityComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
gravity_x  | float  | 0  |  |   
gravity_y  | float  | 400  |  |   
mass  | float  | 0.05  | [0,10]  |   
air_friction  | float  | 0.55  |  |   
terminal_velocity  | float  | 1000  |  |   
apply_terminal_velocity  | bool  | 1  |  |   
updates_velocity  | bool  | 1  |  |   
displace_liquid  | bool  | 1  |  |   
affect_physics_bodies  | bool  | 0  |  | if true, will move the physics body by the difference of mVelocity to the previous frame   
limit_to_max_velocity  | bool  | 1  |  | if true will limit the velocity to 61440. You can turn this off, but it's not recommended, since there are some nasty bugs that can happen with extremely high velocities.   
liquid_death_threshold  | int  | 0  |  | if > 0, entity will die if liquid hit count is greater than this.   
liquid_drag  | float  | 1  |  | 1 = slows down in liquid, 0 = doesn't slow down at all   
Custom data types   
mVelocity  | vec2  |  |  |   
Privates   
mPrevVelocity  | vec2  |  |  | used to update physics bodies   
mLatestLiquidHitCount  | int  | 0  |  |   
mAverageLiquidHitCount  | int  | 0  |  |   
mPrevPosition  | ivec2  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
