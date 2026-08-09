# Documentation: ParticleEmitterComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20ParticleEmitterComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
emitted_material_name  | std::string  | blood  |  |   
create_real_particles  | bool  | 0  |  | used to be emit_real_particles - creates these particles in the grid, if that happens velocity and lifetime are ignored   
emit_real_particles  | bool  | 0  |  | this creates particles that will behave like particles, but work outside of the screen   
emit_cosmetic_particles  | bool  | 0  |  | particle does have collisions, but no other physical interactions with the world. the particles are culled outside camera region   
cosmetic_force_create  | bool  | 1  |  | cosmetic particles are created inside grid cells   
render_back  | bool  | 1  |  | for cosmetic particles, if they are rendered on front or in the back...   
render_ultrabright  | bool  | 0  |  | if 1, particles made of a glowing material will be 3x as bright as usually   
collide_with_grid  | bool  | 1  |  | for cosmetic particles, if 1 the particles collide with grid and only exist in screen space   
collide_with_gas_and_fire  | bool  | 1  |  | does it collide with gas and fire, works with create_real_particles and raytraced images   
particle_single_width  | bool  | 1  |  | for cosmetic particles, forces them (gas,fire) to be only 1 pixel wide   
emit_only_if_there_is_space  | bool  | 0  |  | This is turned for potions after they take some damage and start leaking   
emitter_lifetime_frames  | int  | -1  |  | emitter lifetime in frames. -1 = infinite   
fire_cells_dont_ignite_damagemodel  | bool  | 0  |  | if set, and fire cells are created, this changes their default behaviour of igniting DamageModels   
color_is_based_on_pos  | bool  | 0  |  | if true, will get the particle color based on the world position (instead of randomizing it)   
custom_alpha  | float  | -1  |  | if >= 0, will use this as particle alpha   
x_pos_offset_min  | float  | 0  | [-20,20]  |   
y_pos_offset_min  | float  | 0  | [-20,20]  |   
x_pos_offset_max  | float  | 0  | [-20,20]  |   
y_pos_offset_max  | float  | 0  | [-20,20]  |   
area_circle_sector_degrees  | float  | 360  | [0,360]  |   
x_vel_min  | float  | 0  | [-100,100]  |   
x_vel_max  | float  | 0  | [-100,100]  |   
y_vel_min  | float  | 0  | [-100,100]  |   
y_vel_max  | float  | 0  | [-100,100]  |   
direction_random_deg  | float  | 0  | [0,90]  |   
velocity_always_away_from_center  | float  | 0  | [-256,256]  | if set, will make the velocity's rotation always away from center of randomized aabb   
lifetime_min  | float  | 5  | [0,10]  |   
lifetime_max  | float  | 10  | [0,10]  |   
airflow_force  | float  | 0  | [0,6]  |   
airflow_time  | float  | 1  | [0,2]  |   
airflow_scale  | float  | 1  | [0,2]  |   
friction  | float  | 0  | [0,10]  |   
attractor_force  | float  | 0  | [0,100]  | If > 0, an attractor is created at the position of the entity that owns this component   
emission_interval_min_frames  | int  | 5  | [0,120]  |   
emission_interval_max_frames  | int  | 10  | [0,120]  |   
emission_chance  | int  | 100  | [0,100]  |   
delay_frames  | int  | 0  |  | if set will delay this many frames until starts   
is_emitting  | bool  | 1  |  |   
use_material_inventory  | bool  | 0  |  | if set, it'll use MaterialInventoryComponent as the source of the particles emitted   
is_trail  | bool  | 0  |  | if set, will do a trail based on the previous position and current position   
trail_gap  | float  | 0  |  | if > 0, trail particles will be generated this far from each other between our old and new position, else [count_min-count_max] particles will be generated on the line   
render_on_grid  | bool  | 0  |  | if set, particle render positions will be snapped to cell grid   
fade_based_on_lifetime  | bool  | 0  |  | if set, particle's position in its lifetime will determine the rendering alpha   
draw_as_long  | bool  | 0  |  | if set, particle will rendered as a trail along it's movement vector   
b2_force  | float  | 0  | [0,10]  | if 0 nothing happens, if 1 will apply a force to the physics body (if has one), also requires that we use the material inventory   
set_magic_creation  | bool  | 0  |  | if set will set the magic creation 1 in the cells and do the white glow effect   
image_animation_file  | std::string  |  |  | file to use for image-based animation   
image_animation_colors_file  | std::string  |  |  | file to use for image-based animation   
image_animation_speed  | float  | 1  | [0,255]  | how long do we stay on one frame of image-based animation. 0.5 means two game frames per one animation frame. 2.0 means two animation frames per one game frame, and so on. 0 means we always emit at time 0 of the animation.   
image_animation_loop  | bool  | 1  |  | does image-based animation keep looping while this component is active?   
image_animation_phase  | float  | 0  |  | the point in time [0,1] where the image-based animation will start the first cycle   
image_animation_emission_probability  | float  | 1  |  | [0,1], probability of emitting image based particles is multiplied with this   
image_animation_raytrace_from_center  | bool  | 0  |  | enable this to disable image_animations (from the center) going through the world   
image_animation_use_entity_rotation  | bool  | 0  |  | if 1, image animation emission will be rotated based on entity rotation   
ignore_transform_updated_msg  | bool  | 0  |  | if 1, mExPosition and m_last_emit_position will not be updated when receiving Message_TransformUpdated   
Custom data types   
color  | uint32  | 0  |  |   
offset  | vec2  |  |  |   
area_circle_radius  | ValueRange  |  |  | If > 0, the particles will be emitted inside a circular area defined by the min and max bounds of 'area_circle_radius'.   
gravity  | vec2  |  |  |   
count_min  | LensValue<int> |  |  |   
count_max  | LensValue<int> |  |  |   
custom_style  | PARTICLE_EMITTER_CUSTOM_STYLE::Enum  |  |  | NONE or FIRE   
Privates   
mExPosition  | vec2  |  |  | is used with is_trail   
mMaterialInventoryMax  | int  | 1024  |  | this is how we figure out the pressure, when using material_inventory   
m_material_id  | LensValue<int> |  |  |   
m_next_emit_frame  | int  | 0  |  |   
m_has_emitted  | bool  | 0  |  |   
m_last_emit_position  | ivec2  |  |  |   
m_cached_image_animation  | ParticleEmitter_Animation*  |  |  |   
m_image_based_animation_time  | float  | 0  |  |   
m_collision_angles  | float*  |  |  |   
m_particle_attractor_id  | int16  | -1  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
