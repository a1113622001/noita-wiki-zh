# Documentation: ItemChestComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20ItemChestComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
item_count_min  | int  | 0  | [0,1e+006]  |   
item_count_max  | int  | 0  | [0,1e+006]  |   
level  | int  | 0  | [0,1e+006]  |   
enemy_drop  | bool  | 0  |  | enemy_drop, if set will modify the item_count_min, item_count_max...   
actions  | std::string  |  |  | e.g. 'bullet,bullet,damage' ... actions are parsed into a string   
action_uses_remaining  | std::string  |  |  | e.g. '10,10,-1' ... action uses remaining counts are parsed into a string   
other_entities_to_spawn  | std::string  |  |  | file names of other entities we should spawn from this chest, comma separated   
mSeed  | unsigned int  | 0  |  | this is used to figure out what we spawn from this chest 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
