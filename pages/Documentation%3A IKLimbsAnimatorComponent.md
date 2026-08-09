# Documentation: IKLimbsAnimatorComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20IKLimbsAnimatorComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
future_state_samples  | int  | 10  |  | The number of future animation states evaluated to find the next state   
ground_attachment_ray_length_coeff  | float  | 1.15  |  | Limb raycast length is (ground_attachment_ray_length_coeff * limb length)   
leg_velocity_coeff  | float  | 15  |  | Limbs are moved towards target position at a pace affected by this value.   
affect_flying  | bool  | 0  |  | If set, will cause the mFlyingTime (in CharacterDataComponent) of the entity to be 0 or 1 depending on if the limbs are touching ground   
large_movement_penalty_coeff  | float  | 0.25  |  | The movement score is multiplied by this value if a large move would occur   
no_ground_attachment_penalty_coeff  | float  | 0.75  |  | If a limb movement would make it not collide with ground, the movement score is multiplied with this value. Use lower values to make the limbs prioritize attaching to walls.   
is_limp  | bool  | 0  |  | If 1, will apply verlet animation to simulate ragdoll-like limbs   
Custom data types   
ray_skip_material  | int  | 0  |  | String name of material to not cast rays against. Defaults to 'aluminium'   
mPrevBodyPosition  | vec2  |  |  |   
Privates   
mLimbStates  | IKLimbStateVec  |  |  |   
mHasGroundAttachmentOnAnyLeg  | bool  | 0  |  | Will be set to true if at least one leg is attached to ground. 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
