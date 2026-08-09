# Documentation: TelekinesisComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20TelekinesisComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
min_size  | uint32  | 7  |  | Minimum size of physics body that can be grabbed, in cells/pixels   
max_size  | uint32  | 1500  |  | Maximum size of physics body that can be grabbed, in cells/pixels   
radius  | float  | 250  | [0,300]  | Maximum object search distance   
throw_speed  | float  | 25  | [0,300]  | Affects object speed when it is thrown   
target_distance  | float  | 6  | [0,30]  | Affects how far objects float from owner when held. Object size will also affect the floating distance.   
kick_to_use  | bool  | 1  |  | If 1, telekinesis interaction will occur when kick input is detected in root entity's ControlsComponent   
mState  | int32  | 0  |  |   
mBodyID  | uint64  | 0  |  |   
mStartBodyMaxExtent  | float  | 0  |  |   
mStartAimAngle  | float  | 0  |  |   
mStartBodyAngle  | float  | 0  |  |   
mStartBodyDistance  | float  | 0  |  |   
mStartTime  | float  | 0  |  |   
mMinBodyDistance  | float  | 3.40282e+038  |  |   
mInteract  | bool  | 0  |  | If set to true, telekinesis interaction will occur. Will automatically turn to false at the end of component update. 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
