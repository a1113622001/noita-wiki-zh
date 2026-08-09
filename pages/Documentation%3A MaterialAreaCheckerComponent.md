# Documentation: MaterialAreaCheckerComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20MaterialAreaCheckerComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
update_every_x_frame  | int  | 0  |  | if something other than 0 or 1, will only update_every_x_frames   
look_for_failure  | bool  | 1  |  | if true, will send message Message_MaterialAreaCheckerFailed if the material doesn't exist. If false, will send a message Message_MaterialAreaCheckerSuccess if the aabb is full of material and material2   
count_min  | int  | 0  |  | If > 0, and look_for_failure=0, will send message if material count exceeds this number of cells   
always_check_fullness  | bool  | 0  |  | if 1, and look_for_failure=0, will always check the whole area for cells   
kill_after_message  | bool  | 1  |  | will kill this entity after sending the message   
Custom data types   
area_aabb  | types::aabb  |  |  | aabb offset, we check that this aabb contains only material   
material  | int  | 0  |  | String name of material that we check that the aabb contains   
material2  | int  | 0  |  | String name of material2 that we check that the aabb contains   
Privates   
mPosition  | int  | 0  |  | keeps track where we are   
mLastFrameChecked  | int  | 0  |  | keeps track of how often we've checked 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
