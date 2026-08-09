# Documentation: PhysicsImageShapeComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PhysicsImageShapeComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
is_root  | bool  | 0  |  | if 1, PhysicsBody2Component will use this to figure out where the entity is located   
body_id  | int  | 0  | [0,1000]  | used to figure out which bodies are attached to each other when creating joints   
use_sprite  | bool  | 0  |  | will try to find the SpriteComponent and use that   
is_circle  | bool  | 0  |  | tries to fit this into a circle, looks at bounding box of the pixels and sets the circle to the center of that with radius being the line from there to a straight edge   
centered  | bool  | 0  |  | if this is true, moves offset to be in the center of the image, overwrites the offset_x, offset_y   
offset_x  | float  | 0  |  | offset x in pixels   
offset_y  | float  | 0  |  | offset y in pixels   
z  | float  | 0  |  | offset in the z direction   
image_file  | std::string  |  |  | the png file from which the body is created from   
Custom data types   
material  | int  | 0  |  | the material from which the body is created   
Privates   
mBody  | b2Body*  |  |  | used in joint creation phase 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
