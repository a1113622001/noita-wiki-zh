# Documentation: AreaDamageComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20AreaDamageComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
circle_radius  | float  | 0  |  | if > 0, will only damage entities inside the aabb rectangle which are closer than 'circle_radius' to the aabb center.   
damage_per_frame  | float  | 10  | [0,256]  |   
update_every_n_frame  | int  | 1  | [0,60]  |   
entity_responsible  | EntityID  | 0  |  | if NULL, will try to figure out who to blame   
death_cause  | std::string  | $damage_curse  | [0,60]  |   
entities_with_tag  | std::string  | mortal  |  | damage entities with this tag   
Custom data types   
aabb_min  | vec2  |  |  |   
aabb_max  | vec2  |  |  |   
damage_type  | DAMAGE_TYPES::Enum  |  |  | the damage type 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
