# Documentation: GhostComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20GhostComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
speed  | float  | 5  |  | pixels per second   
new_hunt_target_check_every  | int  | 0  |  | how often do we look for targets   
hunt_box_radius  | float  | 512  |  |   
aggressiveness  | float  | 100  |  | if higher than relations then will attack   
max_distance_from_home  | float  | 300  |  | how far from home can we go?   
die_if_no_home  | bool  | 1  |  | if set to false will die, if it can't find home   
target_tag  | std::string  | player_unit  |  | if something else (like mortal), will attack the home   
Custom data types   
velocity  | vec2  |  |  |   
Privates   
mEntityHome  | EntityID  | 0  |  | where is our home?   
mFramesWithoutHome  | int  | 0  |  |   
mTargetPosition  | vec2  |  |  |   
mTargetEntityId  | int  | 0  |  |   
mRandomTarget  | vec2  |  |  |   
mNextTargetCheckFrame  | int  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
