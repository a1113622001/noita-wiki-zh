# Documentation: HitEffectComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20HitEffectComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
value  | int  | 0  | [0,100]  | Usage depends on selected 'effect_hit'   
value_string  | std::string  |  |  | Usage depends on selected 'effect_hit'   
Custom data types   
condition_effect  | GAME_EFFECT::Enum  |  |  | Hit entity needs to have this 'GAME_EFFECT' for effects to apply. If both 'condition_effect' and 'condition_status' are set, they are combined with AND logic   
condition_status  | StatusEffectType  | 0  |  | Hit entity needs to have this 'STATUS_EFFECT' for effects to apply   
effect_hit  | HIT_EFFECT::Enum  |  |  | What kind of 'HIT_EFFECT' is applied to hit entity if condition is true 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
