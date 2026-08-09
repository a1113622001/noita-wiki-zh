# Documentation: LooseGroundComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20LooseGroundComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
probability  | float  | 0  |  | how often do we do this... shoots a ray in random direction and does the loosening   
max_durability  | int  | 2147483647  |  | if material durability > max_durability, it is not loosened   
max_distance  | float  | 256  |  | how far raytraces to find things to loosen up   
max_angle  | float  | 1.57  |  | how much raytraces go to different directions around the up-vector. pi=full circle   
min_radius  | int  | 3  |  | the minimum radius of our loosening of pixels   
max_radius  | int  | 8  |  | the maximum radius of our loosening of pixels   
chunk_probability  | float  | 0  |  | if > 0, will drop box2d chunks of the ceiling   
chunk_max_angle  | float  | 0.7  |  | how much raytraces go to different directions around the up-vector. pi=full circle   
chunk_count  | int  | -1  |  | how many chunks are we allowed to do, -1 = infinite   
collapse_images  | std::string  | data/procedural_gfx/collapse_big/$[0-14].png  |  | loads these files randomly to do the collapse shapes   
Custom data types   
chunk_material  | int  | 0  |  | String name of chunk material   
Privates   
mChunkCount  | int  | 0  |  | how many chunks are we allowed to do, -1 = infinite 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
