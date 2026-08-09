# Documentation: VerletPhysicsComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20VerletPhysicsComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
num_points  | int  | 2  |  |   
num_links  | int  | 2  |  |   
width  | int  | 1  |  |   
resting_distance  | float  | 2  | [0,16]  |   
mass_min  | float  | 0.8  | [0.03,2]  |   
mass_max  | float  | 1  | [0.03,2]  |   
stiffness  | float  | 1  |  |   
velocity_dampening  | float  | 0.99  | [0.2,1]  |   
liquid_damping  | float  | 0.7  |  | how much we dampen when in liquid   
gets_entity_velocity_coeff  | float  | 0  | [0,10]  |   
collide_with_cells  | bool  | 1  |  |   
simulate_gravity  | bool  | 1  |  |   
simulate_wind  | bool  | 1  |  |   
wind_change_speed  | float  | 1  |  |   
constrain_stretching  | bool  | 0  |  |   
pixelate_sprite_transforms  | bool  | 1  |  |   
scale_sprite_x  | bool  | 1  |  |   
follow_entity_transform  | bool  | 1  |  |   
animation_amount  | float  | 2  |  |   
animation_speed  | float  | 5  |  |   
animation_energy  | float  | 0.6  |  |   
cloth_sprite_z_index  | float  | 1  |  |   
stain_cells_probability  | int  | 0  |  | 0 = never, 1 = most likely, 10 = less likely - and so on   
m_is_culled_previous  | bool  | 0  |  | Developer note: this needs to be serialized in case we serialize SpriteComponent.is_visible   
Custom data types   
type  | VERLET_TYPE::Enum  |  |  |   
animation_target_offset  | vec2  |  |  |   
cloth_color_edge  | uint32  | 4288376730  |  |   
cloth_color  | uint32  | 4286534774  |  |   
m_position_previous  | vec2  |  |  |   
colors  | UintArrayInline  |  |  |   
materials  | UintArrayInline  |  |  |   
Privates   
masses  | FloatArrayInline  |  |  |   
positions  | Vec2ArrayInline  |  |  |   
positions_prev  | Vec2ArrayInline  |  |  |   
velocities  | Vec2ArrayInline  |  |  |   
dampenings  | FloatArrayInline  |  |  |   
freedoms  | FloatArrayInline  |  |  |   
links  | VerletLinkArrayInline  |  |  |   
sprite  | VerletSprite*  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
