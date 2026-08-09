# Documentation: CameraBoundComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20CameraBoundComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
enabled  | bool  | 1  |  | If enabled, kills this component if it's outside the camera distance   
distance  | float  | 250  | [0,1024]  | Distance in pixels from the center of camera, if outside this distance the entity is destroyed   
distance_border  | float  | 20  | [0,1024]  | Offset towards camera in pixels from 'distance' where the entity is respawned if it was frozen   
max_count  | int  | 10  | [0,1024]  | If more than 'max_count' entities of this type exist the one furthest from camera is destroyed   
freeze_on_distance_kill  | bool  | 1  |  | If true and the entity went too far - this entity will be stored so we can later respawn it where it was destroyed because it got too far from the camera?   
freeze_on_max_count_kill  | bool  | 1  |  | If true and the entity was one too many of its kind - this entity will be stored so we can later respawn it where it was destroyed because it got too far from the camera? 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
