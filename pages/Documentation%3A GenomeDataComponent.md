# Documentation: GenomeDataComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20GenomeDataComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
is_predator  | bool  | 0  |  | Predators are considered threats by other species and hunt for food.   
food_chain_rank  | float  | 0  | [0,200]  | 0 means king of the hill. Greater number = more likely to get eaten by other species.   
berserk_dont_attack_friends  | bool  | 0  |  | if 1, this animal will not try to attack player who would normally be its friend   
Custom data types   
herd_id  | LensValue<int> |  |  | This is used for example to separate people in different tribes.   
Privates   
friend_thundermage  | LensValue<bool> |  |  | if 1, thunder mage doesn't attack this   
friend_firemage  | LensValue<bool> |  |  | if 1, fire mage doesn't attack this 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
