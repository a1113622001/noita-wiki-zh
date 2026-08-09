# Documentation: PhysicsBody2Component

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PhysicsBody2Component
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
mBodyId  | b2ObjectID  | 0  |  | this is mBody->GetBodyId() - not to be confused with uid, has to be tracked separately, since the mBody pointer is not unique   
linear_damping  | float  | 0  |  |   
angular_damping  | float  | 0  |  |   
allow_sleep  | bool  | 1  |  |   
fixed_rotation  | bool  | 0  |  |   
is_bullet  | bool  | 0  |  |   
is_static  | bool  | 0  |  |   
buoyancy  | float  | 0.7  |  |   
hax_fix_going_through_ground  | bool  | 0  |  | if 1, will lift the body upwards if it is inside ground   
hax_fix_going_through_sand  | bool  | 0  |  | hax_fix_going_through_ground has to be set, if set will lift the body upwards if it is inside sand   
hax_wait_till_pixel_scenes_loaded  | bool  | 0  |  |   
go_through_sand  | bool  | 0  |  | if 1, will go through sand PhysicsBridge::mGoThroughSand = 1   
auto_clean  | bool  | 1  |  | if 1, the simulation might destroy this body if it's hidden under sand. Problematic if you have a small piece with joint attached to something like the wheels of minecart. Set to 0 in cases like that   
force_add_update_areas  | bool  | 1  |  | if 1, we will mark our predicted aabb as a box2d update area.   
update_entity_transform  | bool  | 1  |  |   
kill_entity_if_body_destroyed  | bool  | 1  |  | if 1, will kill the entity when physics body is destroyed   
kill_entity_after_initialized  | bool  | 0  |  | if 1, will destroy the entity after initialization has been done based the entity's PhysicsBodyComponents and JointComponents   
manual_init  | bool  | 0  |  | if 1, initialization occurs only when done via for example lua component and Physic2InitFromComponents()   
destroy_body_if_entity_destroyed  | bool  | 0  |  | if 1, root body is destroyed if the entity is destroyed   
root_offset_x  | float  | 0  |  | TODO   
root_offset_y  | float  | 0  |  | TODO   
init_offset_x  | float  | 0  |  | TODO   
init_offset_y  | float  | 0  |  | TODO   
mActiveState  | bool  | 0  |  | private variable, please don't mess around with this   
mPixelCountOrig  | uint32  | 0  |  | the number of pixels the body had when it was originally created   
Custom data types   
mLocalPosition  | vec2  |  |  | private variable, please don't mess around with this   
Privates   
mBody  | b2Body*  |  |  |   
mInitialized  | bool  | 0  |  | private variable, please don't mess around with this   
mPixelCount  | uint32  | 0  |  | if set, tracks the number of csolidcells the body has   
mRefreshed  | bool  | 0  |  | this is sure the bodies are only parsed once 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
