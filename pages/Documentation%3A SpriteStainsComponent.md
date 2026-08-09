# Documentation: SpriteStainsComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20SpriteStainsComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
sprite_id  | int  | 0  | [0,10]  | which sprite (in the order in which they appear in the entity) are we going to stain?   
fade_stains_towards_srite_top  | bool  | 1  |  | if 1, shades get less opaque near the top of the sprite   
Custom data types   
stain_shaken_drop_chance_multiplier  | LensValue<int> |  |  | how quickly stains are dropped relative to normal drop speed   
mData  | SpriteStains*  |  |  |   
Privates   
mTextureHandle  | VirtualTextureHandle  |  |  |   
mState  | SpriteStainsState  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
