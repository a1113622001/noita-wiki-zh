# Documentation: TeleportComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20TeleportComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
target_x_is_absolute_position  | bool  | 0  |  | If set, target position x is in world coordinates, otherwise it's an offset   
target_y_is_absolute_position  | bool  | 0  |  | If set, target position y is in world coordinates, otherwise it's an offset   
source_particle_fx_file  | std::string  | data/entities/particles/teleportation_source.xml  |  | This entity is loaded at the source position when teleportation occurs   
target_particle_fx_file  | std::string  | data/entities/particles/teleportation_target.xml  |  | This entity is loaded at the target position when teleportation occurs   
load_collapse_entity  | bool  | 1  |  | if we don't want things to collapse after the teleport   
Custom data types   
target  | vec2  |  |  | Where should we teleport   
Privates   
safety_counter  | int  | 0  |  | used to keep track that we're not stuck in waiting for a pixel scene to load, that is not going to be loaded   
state  | TeleportComponentState::Enum  |  |  |   
teleported_entities  | ENTITY_VEC  |  |  |   
source_location_camera_aabb  | types::aabb  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
