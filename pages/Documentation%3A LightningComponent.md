# Documentation: LightningComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20LightningComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
sprite_lightning_file  | std::string  | data/particles/lightning_ray.png  |  | particle effect, from where the file is loaded that lightning is generated from   
is_projectile  | bool  | 0  |  | if this is true, it's a projectile lightning and looks for ProjectileComponent and uses the data from there to move it   
explosion_type  | int  | 1  |  | 1 = lightning trail   
arc_lifetime  | int  | 60  |  | remaining number of frames the arc exists   
Objects   
config_explosion  | ConfigExplosion  |  |  |   
Privates   
mExPosition  | vec2  |  |  | stores the ex position of this entity   
mArcTarget  | EntityID  | 0  |  | if 'mArcTarget' points to an existing entity a lighting arc will be created between this entity and 'mArcTarget' 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
