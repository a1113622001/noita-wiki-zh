# Documentation: LightComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20LightComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
update_properties  | bool  | 0  |  | turn this on if you expect this to function like the other components   
radius  | float  | 0  | [0,3000]  | The radius of the light in world pixels.   
r  | unsigned int  | 255  | [0,255]  | Color red 0-255   
g  | unsigned int  | 178  | [0,255]  | Color green 0-255   
b  | unsigned int  | 118  | [0,255]  | Color blue 0-255   
offset_x  | float  | 0  | [-3000,3000]  | Offset from the center of entity.   
offset_y  | float  | 0  | [-3000,3000]  | Offset from the center of entity.   
fade_out_time  | float  | 0  | [0,5]  | time in seconds, if not 0, this is how long this takes to die, when the component is destroyed   
blinking_freq  | float  | 1  |  | if less than 1, will blink randomly when rand() < blinking_freq   
Privates   
mAlpha  | float  | 1  |  |   
mSprite  | as::Sprite*  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
