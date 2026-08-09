# Documentation: CharacterPlatformingComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20CharacterPlatformingComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
jump_velocity_x  | float  | 0  | [0,500]  |   
jump_velocity_y  | float  | -175  | [-500,0]  |   
jump_keydown_buffer  | int  | 2  | [0,10]  |   
fly_speed_mult  | float  | 0  | [-100,100]  | AI stuff   
fly_speed_change_spd  | float  | 5  | [0,1000]  | player   
fly_model_player  | bool  | 0  |  | if true, uses player fly model   
fly_smooth_y  | bool  | 1  |  | if true, smooths out the AI fly model   
accel_x  | float  | 1  | [0,1000]  |   
accel_x_air  | float  | 0.1  | [0,1000]  |   
pixel_gravity  | float  | 600  | [0,1000]  |   
swim_idle_buoyancy_coeff  | float  | 1.2  | [0,2]  |   
swim_down_buoyancy_coeff  | float  | 0.7  | [0,2]  |   
swim_up_buoyancy_coeff  | float  | 0.9  | [0,2]  |   
swim_drag  | float  | 0.95  | [0,2]  | when in water velocity *= swim_drag   
swim_extra_horizontal_drag  | float  | 0.9  | [0,2]  | when in water velocity.x *= swim_extra_horizontal_drag   
mouse_look  | bool  | 1  |  |   
mouse_look_buffer  | float  | 1  | [0,5]  |   
keyboard_look  | bool  | 0  |  | if true, turns based on if left or right has been pressed down   
turning_buffer  | float  | 0.1  | [0,2]  |   
animation_to_play  | std::string  |  |  |   
animation_to_play_next  | std::string  |  |  |   
run_animation_velocity_switching_threshold  | float  | 45  | [0,1000]  |   
run_animation_velocity_switching_enabled  | bool  | 0  |  |   
turn_animation_frames_between  | int  | 20  | [0,100]  |   
precision_jumping_max_duration_frames  | int  | -1  |  | maximum duration of precision jump or knockback. -1 = infinite   
audio_liquid_splash_intensity  | float  | 1  |  |   
Custom data types   
velocity_min_x  | LensValue<float> |  |  |   
velocity_max_x  | LensValue<float> |  |  |   
velocity_min_y  | LensValue<float> |  |  |   
velocity_max_y  | LensValue<float> |  |  |   
run_velocity  | LensValue<float> |  |  |   
fly_velocity_x  | LensValue<float> |  |  |   
fly_speed_max_up  | LensValue<float> |  |  |   
fly_speed_max_down  | LensValue<float> |  |  |   
Privates   
mExAnimationPos  | vec2  |  |  |   
mFramesInAirCounter  | int  | -1  |  |   
mIsPrecisionJumping  | bool  | 0  |  |   
mPrecisionJumpingTime  | int  | 0  |  |   
mPrecisionJumpingSpeedX  | float  | 0  |  |   
mPrecisionJumpingTimeLeft  | int  | 0  |  |   
mFlyThrottle  | float  | 0  |  |   
mSmoothedFlyingTargetY  | float  | 0  |  |   
mJetpackEmitting  | int  | -1  |  | -1 = undefined, 0 = not emitting, 1 = emitting   
mNextTurnAnimationFrame  | int  | 0  |  |   
mFramesNotSwimming  | int  | 10  |  | 0 = currently swimming   
mFramesSwimming  | int  | 0  |  | 0 = not currently swimming   
mShouldCrouch  | bool  | 0  |  |   
mShouldCrouchPrev  | bool  | 0  |  |   
mLastPostureSwitchFrame  | int  | -1  |  |   
mLookOverrideLastFrame  | int  | 0  |  |   
mLookOverrideDirection  | int  | 0  |  |   
  
## Turning

This component implements the turning functionality for entities based on the values in their [ControlsComponent](Documentation%3A ControlsComponent.md). If you want to disable this behaviour and replace it with your own, you can do that by specifying these values: `mouse_look="0"`, `keyboard_look="0"`, and `turning_buffer="5000"`. 

Turning works by flipping the x-scale of the entity between a positive value and a negative value, usually +1 and -1. 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
