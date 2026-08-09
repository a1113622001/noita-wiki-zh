# Documentation: IKLimbWalkerComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20IKLimbWalkerComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
ground_attachment_min_spread  | float  | 16  |  |   
ground_attachment_max_tries  | int  | 10  |  |   
ground_attachment_max_angle  | float  | 0.8  |  |   
ground_attachment_ray_length_coeff  | float  | 1.15  |  |   
leg_velocity_coeff  | float  | 15  |  |   
affect_flying  | bool  | 0  |  | if set, will cause the mFlyingTime (in CharacterDataComponent) of the parent to be 0 or 1 depending on if we're touching anything   
mState  | int  | 0  |  | 0 = detached, 1 = attached   
Custom data types   
ray_skip_material  | int  | 0  |  | String name of material to not cast rays against. Defaults to 'aluminium'   
mTarget  | vec2  |  |  |   
mPrevTarget  | vec2  |  |  |   
mPrevCenterPosition  | vec2  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
