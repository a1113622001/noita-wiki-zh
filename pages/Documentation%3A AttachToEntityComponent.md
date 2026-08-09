# Documentation: AttachToEntityComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20AttachToEntityComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
only_position  | bool  | 0  |  | if 1, we only inherit position. it is calculated as follows: target_position + target_offset * target_scale   
target_hotspot_tag  | std::string  |  |  | if set, we apply the offset of target HotSpot with this tag   
target_sprite_id  | int  | -1  |  | if >= 0, the Nth sprite transform in target entity is inherited   
rotate_based_on_x_scale  | bool  | 0  |  | if 1, the rotation is set to 0 deg if scale >= 0 else to 180 deg   
destroy_component_when_target_is_gone  | bool  | 1  |  | should probably be on by default   
Custom data types   
Transform  | types::xform  |  |  |   
Privates   
target  | EntityID  | 0  |  | EntityID of the entity we're attached to. This will fail after save/load, unfortunately   
mUpdateFrame  | int  | -1  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
