# Documentation: TorchComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20TorchComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
probability_of_ignition_attempt  | int  | 15  | [0,100]  | how likely are we to ignite colliding cells   
suffocation_check_offset_y  | float  | -2  | [-10,10]  | check offset in world coordinates from our position   
frames_suffocated_to_extinguish  | int  | 5  | [0,30]  | how many frames the torch needs to be suffocated before it stops emitting fire   
extinguishable  | bool  | 1  |  | if 1, the torch needs to be re-ignited in case it is turned off   
fire_audio_weight  | float  | 0  | [0,2]  | how loud is the sound of our fire? 0 = no sound   
Privates   
mFlickerOffset  | float  | 0  |  |   
mFramesSuffocated  | int  | 0  |  |   
mIsOn  | bool  | 1  |  |   
mFireIsBurningPrev  | bool  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
