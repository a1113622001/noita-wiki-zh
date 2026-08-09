# Documentation: KickComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20KickComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
can_kick  | bool  | 1  |  | e.g. telekinetic kick disables this   
kick_radius  | float  | 3  | [0,3.5]  |   
telekinesis_throw_speed  | float  | 25  |  | this is here, so that STRONG_KICK -perk can affect telekinetic kick as well   
kick_entities  | std::string  |  |  | comma separated list of entities that are loaded when player kicks   
Custom data types   
max_force  | LensValue<float> |  |  |   
player_kickforce  | LensValue<float> |  |  |   
kick_damage  | LensValue<float> |  |  | ( 1.f / 25.f )   
kick_knockback  | LensValue<float> |  |  | knockback force for entities 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
