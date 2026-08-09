# Documentation: PixelSpriteComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PixelSpriteComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
image_file  | std::string  |  |  | loads pixelsprite based on this file   
anchor_x  | int  | 0  | [0,3.5]  | the anchor and center_offset   
anchor_y  | int  | 0  | [0,3.5]  | the anchor and center_offset   
material  | std::string  | wood_loose  |  | what's the material that things are made out of, TODO - change this into MetaCustom   
diggable  | bool  | 1  |  | if 1, this can be broken with digger   
clean_overlapping_pixels  | bool  | 1  |  | cleans up the pixels that are ovelapping in the world   
kill_when_sprite_dies  | bool  | 1  |  | kills the entity, if the pixel sprite is dead (empty)   
create_box2d_bodies  | bool  | 0  |  | if true, will create new pixel sprites with box2d bodies, instead of gridworld cells   
Custom data types   
mPixelSprite  | PixelSprite*  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
