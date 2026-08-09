# Documentation: HomingComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20HomingComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
target_tag  | std::string  | homing_target  |  |   
target_who_shot  | bool  | 0  |  | If 1, targets who shot the projectile, ignores 'target_tag'.   
detect_distance  | float  | 150  | [0,1000]  |   
homing_velocity_multiplier  | float  | 0.9  | [-100,100]  |   
homing_targeting_coeff  | float  | 160  | [0,1000]  |   
just_rotate_towards_target  | bool  | 0  |  | the default accelerates towards a target. If true will only rotate towards the target.   
max_turn_rate  | float  | 0.05  | [0,6.283]  | radians. If just_rotate_towards_target then this is the maximum radians it can turn per frame   
predefined_target  | EntityID  | 0  |  | If set, we track this entity   
look_for_root_entities_only  | bool  | 0  |  | if set, will only look for entities that are _not_ child entities.   
  
当HomingSystem更新一个just_rotate_towards_target为false的HomingComponent时, 设它的detect_distance, homing_velocity_multiplier, homing_targeting_coeff分别为d0, λ, k, 它所在实体的VelocityComponent速度为 𝐯, 从它所在实体的原点到目标位置的矢量为 𝐝, 且 d<d0, 则本次更新将上述速度变为 

𝐯′=λ𝐯+Δ𝐯

其中 Δ𝐯 的大小为 kd(d0−d)60d0, 方向与 𝐝 相同. 

若 d≥d0 或没有有效追踪目标, 则不会影响速度, 𝐯′=𝐯.

目标位置是追踪目标第一个命中碰撞箱的中心点, 若追踪目标没有命中碰撞箱就取它的实体原点. 

当target_who_shot为true且发射者是存活的实体时, 追踪目标就是发射者; 否则, 追踪目标是实体原点与HomingComponent所在实体的原点距离最近且不超过 d0 的具有target_tag的目标. 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
