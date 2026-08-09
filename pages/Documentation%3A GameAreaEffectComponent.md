# Documentation: GameAreaEffectComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20GameAreaEffectComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
radius  | float  | 0  | [0,3.5]  | what's the radius (in pixels) of the area effect   
collide_with_tag  | std::string  | hittable  |  | the tags we're looking for   
frame_length  | int  | -1  |  | if not 0 will reapply this effect after this many frames have gone by   
Custom data types   
game_effect_entitities  | VECTOR_STR  |  |  | just a vector of the game_effect entities   
Privates   
mEntitiesAppliedOutTo  | VECTOR_ENTITYID  |  |  |   
mEntitiesAppliedFrame  | VECTOR_INT  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
