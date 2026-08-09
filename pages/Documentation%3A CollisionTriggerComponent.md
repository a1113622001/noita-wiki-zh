# Documentation: CollisionTriggerComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20CollisionTriggerComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
width  | float  | 32  | [0,100]  |   
height  | float  | 32  | [0,100]  |   
radius  | float  | 32  | [0,100]  |   
required_tag  | std::string  | mortal  |  |   
remove_component_when_triggered  | bool  | 0  |  |   
destroy_this_entity_when_triggered  | bool  | 1  |  |   
timer_for_destruction  | int  | 0  | [0,60]  |   
self_trigger  | bool  | 0  |  | if true, the shooter can trigger it   
skip_self_frames  | int  | 60  |  | skips checks against self during these frames   
Privates   
mTimer  | int  | 0  |  |   
  
## Check Area

This component first collects all entities within the rectangle defined by `width` and `height`, then it goes through those entities and checks whether they are within the defined radius. Only if both checks succeed does it count as a collision. 

Triggers `script_collision_trigger_hit` from [LuaComponent](Documentation%3A LuaComponent.md) when conditions are met, followed by the LuaComponent's `script_collision_trigger_timer_finished` once `timer_for_destruction` has elapsed. 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
