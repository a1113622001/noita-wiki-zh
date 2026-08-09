# Documentation: PixelSceneComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PixelSceneComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
pixel_scene  | std::string  |  |  | loads this pixel scene file   
pixel_scene_visual  | std::string  |  |  | this is the colors that get used for the pixels, if empty will use material colors   
pixel_scene_background  | std::string  |  |  | this is the background file that gets loaded, if empty won't do anything   
background_z_index  | int  | 50  |  | the standard z_index of pixel scene backgrounds   
offset_x  | float  | 0  | [-30,30]  | how much off from the entity x,y will this be. Top left corner is where it loads the pixel scene   
offset_y  | float  | 0  | [-30,30]  |   
skip_biome_checks  | bool  | 0  |  | biome check is on by default - it will check that pixel scene is loaded so that every corner is in the same biome   
skip_edge_textures  | bool  | 0  |  | if on - won't do the edge textures for the pixel scene 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
