# Documentation: PhysicsKeepInWorldComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PhysicsKeepInWorldComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
check_whole_aabb  | bool  | 0  |  | All that is needed is to include one of the components with PhysicsBodyComponent or PhysicsBody2Component and it will be frozen when it hits outer edges of the world. NOTE! This will override the auto_clean variable, auto_clean will be set to false. If this is true, will check all the 4 corners of the bounding box   
predict_aabb  | bool  | 0  |  | Will add the velocity * 1.5 to the aabb to predict where the body will end up at. This will greatly help keep the body inside simulated world.   
keep_at_last_valid_pos  | bool  | 0  |  | Will try to keep the object at the latest valid position   
Privates   
mExPosition  | vec2  |  |  |   
mExRotation  | float  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
