# Documentation: PotionComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PotionComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
spray_velocity_coeff  | float  | 1  | [0,2]  |   
spray_velocity_normalized_min  | float  | 0.5  |  |   
body_colored  | bool  | 0  |  |   
throw_bunch  | bool  | 0  |  |   
throw_how_many  | int  | 5  |  |   
dont_spray_static_materials  | bool  | 0  |  | NOTE( Petri ): 15.8.2023 - if this is set to true, will only spray dynamic materials, that dont cause bugs (i.e. will not spray hard rock, box2d materials)   
dont_spray_just_leak_gas_materials  | bool  | 0  |  | NOTE( Petri ): 15.8.2023 - if this is set to true, will only leak gas materials instead of 'spraying' them.   
never_color  | bool  | 0  |  | Petri: body_colored didn't seem to work, so I added never_color. It can be set to true if you never want the potion to be colored   
Custom data types   
custom_color_material  | int  | 0  |  | if set, will always use the color from this material 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
