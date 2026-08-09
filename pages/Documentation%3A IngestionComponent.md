# Documentation: IngestionComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20IngestionComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
ingestion_size  | int64  | 0  |  | How many units of material we currently store   
ingestion_capacity  | int64  | 7500  |  | How many units of material we can store   
ingestion_cooldown_delay_frames  | uint32  | 600  |  | How many frames is ingestion_size retained after last time eating?   
ingestion_reduce_every_n_frame  | uint32  | 5  |  | One unit of ingestion_size is removed every N frame   
overingestion_damage  | float  | 0.002  |  | How much damage per overingested cell is applied   
blood_healing_speed  | float  | 0.0008  | [0,1000]  | affects healing speed if entity has HEALING_BLOOD game effect. The amount of hp restored per one blood cell.   
ingestion_satiation_material_tag  | std::string  |  |  | If set, only materials with this tag will increase satiation level   
m_ingestion_cooldown_frames  | int32  | 0  |  | Next frame ingestion_size cooldown can occur   
Privates   
m_next_overeating_msg_frame  | int32  | 0  |  |   
m_ingestion_satiation_material_tag_cached  | std::string  |  |  |   
m_ingestion_satiation_material_cache  | std::set<int32> |  |  |   
m_damage_effect_lifetime  | int32  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
