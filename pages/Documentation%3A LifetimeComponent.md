# Documentation: LifetimeComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20LifetimeComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
lifetime  | int  | -1  |  | if anything else than -1 will kill this entity when this many frames have passed   
fade_sprites  | bool  | 0  |  | if 1, sprites will be faded as lifetime gets lower   
kill_parent  | bool  | 0  |  | if 1, will kill the parent entity   
kill_all_parents  | bool  | 0  |  | if 1, will kill all the parents entity   
serialize_duration  | bool  | 0  |  | if 1, will retain kill_frame and creation_frame over serialization   
kill_frame_serialized  | int  | 0  |  | frame that this is killed at   
creation_frame_serialized  | int  | 0  |  | frame that this is killed at   
Custom data types   
randomize_lifetime  | ValueRange  |  |  | this is added to the lifetime   
Privates   
creation_frame  | int  | 0  |  | we'll set this to GG.GetFrameNum() when this component is created   
kill_frame  | int  | 0  |  | frame that this is killed at 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
