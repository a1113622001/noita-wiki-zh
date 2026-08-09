# Documentation: MaterialSuckerComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20MaterialSuckerComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
material_type  | int  | 0  | [0,3]  | 0 = liquid, 1 = sand, 2 = gas (arbitary order)   
barrel_size  | int  | 50  | [0,1024]  | how many pixels can we suck up   
num_cells_sucked_per_frame  | int  | 1  | [0,5]  | How many cells at max can we suck per frame?   
set_projectile_to_liquid  | bool  | 0  |  | if set, will set the projectile what ever we're sucking...?   
last_material_id  | int  | 0  |  | hax... this is set if we use set_projectile_to_liquid   
suck_gold  | bool  | 0  |  | if set will just suck gold and update wallet   
suck_health  | bool  | 0  |  | if set will just suck healthium material and add 1 hp every sucked healthium   
suck_static_materials  | bool  | 0  |  | will suck static materials from the world   
suck_tag  | std::string  |  |  | if set, will only suck materials with this tag. NOTE, will also require the correct material_type to be set   
mAmountUsed  | int  | 0  |  | how full are we   
Custom data types   
randomized_position  | types::iaabb  |  |  | random offset for pos, where we look for pixels   
Privates   
mGoldAccumulator  | int  | 0  |  | accumulates amount of gold picked during consecutive frames   
mLastFramePickedGold  | int  | -2  |  | last frame we picked gold 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
