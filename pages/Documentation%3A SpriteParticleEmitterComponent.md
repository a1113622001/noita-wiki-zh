# Documentation: SpriteParticleEmitterComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20SpriteParticleEmitterComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
sprite_file  | std::string  |  |  | filepath to the sprite(s), supports the $[0-3] syntax   
sprite_centered  | bool  | 0  |  | sets the offset to the center of the image   
sprite_random_rotation  | bool  | 0  |  | rotates the sprite randomly in 90 degree angles   
render_back  | bool  | 0  |  | if true, will set this particle to be behind entities (won't emit light)   
delay  | float  | 0  |  | delay in seconds...   
lifetime  | float  | 0  |  | lifetime in seconds...   
additive  | bool  | 0  |  | if 1, the sprites will be rendered using additive blending   
emissive  | bool  | 0  |  | if 1, the sprites will be rendered onto the emissive render target   
velocity_slowdown  | float  | 0  |  | what percent of the velocity is slowed by *dt   
rotation  | float  | 0  |  | original rotation in rads   
angular_velocity  | float  | 0  |  | how much rotation there is in a second   
use_velocity_as_rotation  | bool  | 0  |  | do we rotate the sprite based on the velocity   
use_rotation_from_velocity_component  | bool  | 0  |  | if set, will set the initial rotation based on the velocity component's velocity   
use_rotation_from_entity  | bool  | 0  |  | if set, will 'inherit' rotation from the entity   
entity_velocity_multiplier  | float  | 0  |  | 0 = doesn't use the velocity from spawning entity at all, 1 = uses all   
z_index  | float  | 0  |  | Depth of created particles   
randomize_position_inside_hitbox  | bool  | 0  |  | if set, will randomize position inside the hitbox aabb   
velocity_always_away_from_center  | bool  | 0  |  | if set, will make the velocity's rotation always away from center of randomized aabb   
camera_bound  | bool  | 1  |  | if true, will be culled if not near the camera   
camera_distance  | float  | 75  |  | if the distance from camera (edges) is higher than this, this will be culled   
is_emitting  | bool  | 1  |  | disable this from emitting...   
count_min  | int  | 0  |  | how many particles do we spawn at one time   
count_max  | int  | 1  |  | how many particles do we spawn at one time   
emission_interval_min_frames  | int  | 5  | [0,200]  | how often do we emit particles   
emission_interval_max_frames  | int  | 10  | [0,200]  | how often do we emit particles   
entity_file  | std::string  |  |  | if set, this entity is loaded to the emission position by the emitter when it emits   
Custom data types   
color  | types::fcolor  |  |  | original color   
color_change  | types::fcolor  |  |  | how much the color changes in a second   
velocity  | vec2  |  |  | original velocity   
gravity  | vec2  |  |  | gravity   
scale  | vec2  |  |  | original scale   
scale_velocity  | vec2  |  |  | scale velocity per second   
randomize_lifetime  | ValueRange  |  |  | this is added to the lifetime   
randomize_position  | types::aabb  |  |  | random offset for pos   
randomize_velocity  | types::aabb  |  |  | add this randomized velocity inside this o the velocity   
randomize_scale  | types::aabb  |  |  | add this randomized vector2 to scale   
randomize_rotation  | ValueRange  |  |  | this is added to the rotation   
randomize_angular_velocity  | ValueRange  |  |  | this is added to angular_velocity   
randomize_alpha  | ValueRange  |  |  | this is added to the alpha   
randomize_animation_speed_coeff  | ValueRange  |  |  | if set, animation speed is multiplied by a random value inside this range   
expand_randomize_position  | vec2  |  |  | will add dt*this to randomize_position_aabb every frame   
Privates   
mNextEmitFrame  | int  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
