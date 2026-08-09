# Documentation: PhysicsBodyComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PhysicsBodyComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
is_external  | bool  | 0  |  | if mBody is set from outside, will ignore all the things   
hax_fix_going_through_ground  | bool  | 0  |  | if set will lift the body upwards if it is inside ground   
hax_fix_going_through_sand  | bool  | 0  |  | hax_fix_going_through_ground has to be set, if set will lift the body upwards if it is inside sand   
hax_wait_till_pixel_scenes_loaded  | bool  | 0  |  |   
uid  | int  | 0  | [0,1000]  | if the entity has multiple physics bodies and has specific shapes for those and possible joints, you should use this. 0 is default for shapes   
is_enabled  | bool  | 1  |  | Use this to kill the physics body of. if is_enabled is set to false, will destroy the physics body   
linear_damping  | float  | 0  |  |   
angular_damping  | float  | 0  |  |   
allow_sleep  | bool  | 1  |  |   
fixed_rotation  | bool  | 0  |  |   
buoyancy  | float  | 0.7  |  |   
gravity_scale_if_has_no_image_shapes  | float  | 1  |  |   
is_bullet  | bool  | 0  |  |   
is_static  | bool  | 0  |  |   
is_kinematic  | bool  | 0  |  |   
is_character  | bool  | 0  |  | if it is a character, then we need to few interesting things from time to time   
go_through_sand  | bool  | 0  |  | if set, will go through sand PhysicsBridge::mGoThroughSand = 1   
gridworld_box2d  | bool  | 1  |  | default is 1. You should only change this if you know the body isn't going to touch gridworld   
auto_clean  | bool  | 1  |  | if set, the simulation might destroy this body if it's hidden under sand. Problematic if you have a small piece with joint attached to something like the wheels of minecart. Set to 0 in cases like that   
on_death_leave_physics_body  | bool  | 0  |  | if set, will leave the b2body into the world, even if the entity is killed   
on_death_really_leave_body  | bool  | 0  |  | camera bound... god damn... we need something special when we want to leave the body   
update_entity_transform  | bool  | 1  |  | WARNING! Don't touch this unless you know what you're doing. If false, doesn't update the entitys transform to match the physics body. This is used with multi body entities, to use the correct body to update the entity, e.g. minecart   
force_add_update_areas  | bool  | 0  |  | if 1, we will mark our predicted aabb as a box2d update area.   
kills_entity  | bool  | 1  |  | if set, will kill the entity when physics body is destroyed   
projectiles_rotate_toward_velocity  | bool  | 0  |  | for physics projectiles, if true will initially rotate the body based on the velocity   
randomize_init_velocity  | bool  | 0  |  | randomizes the init velocity   
mActiveState  | bool  | 0  |  | private variable, please don't mess around with this   
Custom data types   
initial_velocity  | vec2  |  |  | if you want a velocity at the start, set it here   
Privates   
mBody  | b2Body*  |  |  |   
mBodyId  | b2ObjectID  | 0  |  | this is mBody->GetBodyId() - not to be confused with uid shit, has to be tracked separately, since the mBody pointer is not unique   
mPixelCount  | int  | 0  |  | if set, tracks the number of csolidcells the body has   
mLocalPosition  | b2Vec2  |  |  |   
mRefreshed  | bool  | 0  |  | this is sure the bodies are only parsed once 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
