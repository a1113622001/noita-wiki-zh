# Documentation: GameStatsComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20GameStatsComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
name  | std::string  |  |  | no one uses the name variable on entity, so we have to do this to make it happen   
stats_filename  | std::string  |  |  | also generated from the gunk   
is_player  | bool  | 0  |  | if true, will use the session file for loading stats   
extra_death_msg  | std::string  |  |  | set when e.g. polymorphed   
dont_do_logplayerkill  | bool  | 0  |  | if 1, StatsLogPlayerKill must be manually called from lua   
player_polymorph_count  | int  | 0  |  | skip loading of stats if this higher than 0 and decrament this by one 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
