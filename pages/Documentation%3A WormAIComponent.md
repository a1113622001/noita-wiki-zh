# Documentation: WormAIComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20WormAIComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
speed  | float  | 1  | [0,10000]  |   
speed_hunt  | float  | 3  | [0,10000]  |   
direction_adjust_speed  | float  | 1  | [0,10000]  |   
direction_adjust_speed_hunt  | float  | 1  | [0,10000]  |   
random_target_box_radius  | float  | 512  | [0,10000]  |   
new_hunt_target_check_every  | int  | 30  | [0,10000]  |   
new_random_target_check_every  | int  | 120  | [0,10000]  |   
hunt_box_radius  | float  | 512  | [0,10000]  |   
cocoon_food_required  | int  | 30  |  | how much food do we need to consume before we can cocoon   
cocoon_entity  | std::string  |  |  | if empty, won't cocoon, if set it'll spawn this after it's eaten enough   
give_up_area_radius  | float  | 50  | [0,10000]  |   
give_up_time_frames  | int  | 300  | [0,10000]  |   
debug_follow_mouse  | bool  | 0  |  |   
Privates   
mRandomTarget  | vec2  |  |  |   
mTargetEntityId  | int  | 0  |  |   
mNextTargetCheckFrame  | int  | 0  |  |   
mNextHuntTargetCheckFrame  | int  | 0  |  |   
mGiveUpStarted  | int  | 0  |  |   
mGiveUpAreaMinX  | int  | 0  |  |   
mGiveUpAreaMinY  | int  | 0  |  |   
mGiveUpAreaMaxX  | int  | 0  |  |   
mGiveUpAreaMaxY  | int  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
