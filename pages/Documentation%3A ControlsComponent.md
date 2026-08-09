# Documentation: ControlsComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20ControlsComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
polymorph_hax  | bool  | 0  |  |   
polymorph_next_attack_frame  | int  | 0  |  |   
enabled  | bool  | 1  |  |   
gamepad_indirect_aiming_enabled  | bool  | 0  |  |   
gamepad_fire_on_thumbstick_extend  | bool  | 0  |  |   
gamepad_fire_on_thumbstick_extend_threshold  | float  | 0.7  |  |   
Privates   
mButtonDownFire  | bool  | 0  |  |   
mButtonFrameFire  | int  | 0  |  |   
mButtonLastFrameFire  | int  | -2  |  |   
mButtonDownFire2  | bool  | 0  |  |   
mButtonFrameFire2  | int  | 0  |  |   
mButtonDownAction  | bool  | 0  |  |   
mButtonFrameAction  | int  | 0  |  |   
mButtonDownThrow  | bool  | 0  |  |   
mButtonFrameThrow  | int  | 0  |  |   
mButtonDownInteract  | bool  | 0  |  |   
mButtonFrameInteract  | int  | 0  |  |   
mButtonDownLeft  | bool  | 0  |  |   
mButtonFrameLeft  | int  | 0  |  |   
mButtonDownRight  | bool  | 0  |  |   
mButtonFrameRight  | int  | 0  |  |   
mButtonDownUp  | bool  | 0  |  |   
mButtonFrameUp  | int  | 0  |  |   
mButtonDownDown  | bool  | 0  |  |   
mButtonFrameDown  | int  | 0  |  |   
mButtonDownJump  | bool  | 0  |  |   
mButtonFrameJump  | int  | 0  |  |   
mButtonDownRun  | bool  | 0  |  |   
mButtonFrameRun  | int  | 0  |  |   
mButtonDownFly  | bool  | 0  |  |   
mButtonFrameFly  | int  | 0  |  |   
mButtonDownDig  | bool  | 0  |  |   
mButtonFrameDig  | int  | 0  |  |   
mButtonDownChangeItemR  | bool  | 0  |  |   
mButtonFrameChangeItemR  | int  | 0  |  |   
mButtonCountChangeItemR  | int  | 0  |  | note these have special count property   
mButtonDownChangeItemL  | bool  | 0  |  |   
mButtonFrameChangeItemL  | int  | 0  |  |   
mButtonCountChangeItemL  | int  | 0  |  | note these have special count property   
mButtonDownInventory  | bool  | 0  |  |   
mButtonFrameInventory  | int  | 0  |  |   
mButtonDownHolsterItem  | bool  | 0  |  |   
mButtonFrameHolsterItem  | int  | 0  |  |   
mButtonDownDropItem  | bool  | 0  |  |   
mButtonFrameDropItem  | int  | 0  |  |   
mButtonDownKick  | bool  | 0  |  |   
mButtonFrameKick  | int  | 0  |  |   
mButtonDownEat  | bool  | 0  |  |   
mButtonFrameEat  | int  | 0  |  |   
mButtonDownLeftClick  | bool  | 0  |  | NOTE! Ignores gamepad, if mouse is pressed this will be true.   
mButtonFrameLeftClick  | int  | 0  |  | NOTE! Ignores gamepad, if mouse is pressed this will be true.   
mButtonDownRightClick  | bool  | 0  |  | NOTE! Ignores gamepad, if mouse is pressed this will be true.   
mButtonFrameRightClick  | int  | 0  |  | NOTE! Ignores gamepad, if mouse is pressed this will be true.   
mButtonDownTransformLeft  | bool  | 0  |  | NOT IN USE!   
mButtonFrameTransformLeft  | int  | 0  |  | NOT IN USE!   
mButtonDownTransformRight  | bool  | 0  |  | NOT IN USE!   
mButtonFrameTransformRight  | int  | 0  |  | NOT IN USE!   
mButtonDownTransformUp  | bool  | 0  |  | NOT IN USE!   
mButtonFrameTransformUp  | int  | 0  |  | NOT IN USE!   
mButtonCountTransformUp  | int  | 0  |  | NOT IN USE!   
mButtonDownTransformDown  | bool  | 0  |  | NOT IN USE!   
mButtonFrameTransformDown  | int  | 0  |  | NOT IN USE!   
mButtonCountTransformDown  | int  | 0  |  | NOT IN USE!   
mFlyingTargetY  | float  | 0  |  |   
mAimingVector  | vec2  |  |  |   
mAimingVectorNormalized  | vec2  |  |  | Aiming vector normalized to unit sphere.   
mAimingVectorNonZeroLatest  | vec2  |  |  |   
mGamepadAimingVectorRaw  | vec2  |  |  |   
mJumpVelocity  | vec2  |  |  | used mostly by AI only?   
mMousePosition  | vec2  |  |  |   
mMousePositionRaw  | vec2  |  |  |   
mMousePositionRawPrev  | vec2  |  |  |   
mMouseDelta  | vec2  |  |  |   
mGamepadIndirectAiming  | vec2  |  |  |   
mGamePadCursorInWorld  | vec2  |  |  | where the aiming cursor is in the world, updated by platformshooterplayer_system   
mButtonDownDelayLineFire  | uint32_t  | 0  |  | Used to delay input for some game effects   
mButtonDownDelayLineFire2  | uint32_t  | 0  |  | Used to delay input for some game effects   
mButtonDownDelayLineRight  | uint32_t  | 0  |  | Used to delay input for some game effects   
mButtonDownDelayLineLeft  | uint32_t  | 0  |  | Used to delay input for some game effects   
mButtonDownDelayLineUp  | uint32_t  | 0  |  | Used to delay input for some game effects   
mButtonDownDelayLineDown  | uint32_t  | 0  |  | Used to delay input for some game effects   
mButtonDownDelayLineKick  | uint32_t  | 0  |  | Used to delay input for some game effects   
mButtonDownDelayLineThrow  | uint32_t  | 0  |  | Used to delay input for some game effects   
mButtonDownDelayLineJump  | uint32_t  | 0  |  | Used to delay input for some game effects   
mButtonDownDelayLineFly  | uint32_t  | 0  |  | Used to delay input for some game effects   
input_latency_frames  | LensValue<int> |  |  | Adds latency to some inputs. Used by some game effects. Max 31. 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
