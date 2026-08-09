# Documentation: InheritTransformComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20InheritTransformComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
use_root_parent  | bool  | 0  |  | if 1, we use the root of our entity hierarchy instead of the immediate parent   
only_position  | bool  | 0  |  | if 1, we only inherit position. it is calculated as follows: parent_position + parent_offset * parent_scale   
parent_hotspot_tag  | std::string  |  |  | if set, we apply the offset of parent HotSpot with this tag   
parent_sprite_id  | int  | -1  |  | if >= 0, the Nth sprite transform in parent entity is inherited   
always_use_immediate_parent_rotation  | bool  | 0  |  | if 1, we use the immediate parent for rotation, no matter what other properties say   
rotate_based_on_x_scale  | bool  | 0  |  | if 1, the rotation is set to 0 deg if scale >= 0 else to 180 deg   
Custom data types   
Transform  | types::xform  |  |  |   
Privates   
mUpdateFrame  | int  | -1  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
