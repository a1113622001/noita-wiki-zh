# Documentation: PlatformShooterPlayerComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PlatformShooterPlayerComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
aiming_reticle_distance_from_character  | float  | 40  | [0,1000]  |   
camera_max_distance_from_character  | float  | 25  | [0,1000]  |   
alcohol_drunken_speed  | float  | 0.005  | [0,1000]  |   
blood_fungi_drunken_speed  | float  | 0.006  | [0,1000]  |   
blood_worm_drunken_speed  | float  | 0.006  | [0,1000]  |   
eating_cells_per_frame  | int  | 1  | [0,100]  |   
eating_probability  | int  | 5  | [0,100]  |   
eating_delay_frames  | int  | 30  | [0,100]  |   
stoned_speed  | float  | 0.1  | [0,1000]  |   
center_camera_on_this_entity  | bool  | 1  |  |   
move_camera_with_aim  | bool  | 1  |  | if true, moves camera with the aim.   
Custom data types   
eating_area_min  | ivec2  |  |  |   
eating_area_max  | ivec2  |  |  |   
Privates   
mSmoothedCameraPosition  | vec2  |  |  |   
mSmoothedAimingVector  | vec2  |  |  |   
mCameraRecoil  | float  | 0  |  |   
mCameraRecoilTarget  | float  | 0  |  |   
mCrouching  | bool  | 0  |  |   
mCameraDistanceLerped  | float  | 0  |  |   
mRequireTriggerPull  | bool  | 0  |  |   
mWarpDelay  | int  | 0  |  |   
mItemTemporarilyHidden  | int  | 0  |  |   
mDesiredCameraPos  | vec2  |  |  |   
mHasGamepadControlsPrev  | bool  | 0  |  |   
mForceFireOnNextUpdate  | bool  | 0  |  |   
mFastMovementParticlesAlphaSmoothed  | float  | 0  |  |   
mTeleBoltFramesDuringLastSecond  | uint64  | 0  |  |   
mCamCorrectionTeleSmoothed  | float  | 0  |  |   
mCamCorrectionGainSmoothed  | vec2  |  |  |   
mCameraErrorPrev  | Vec2ArrayInline  |  |  |   
mCamErrorAveraged  | vec2  |  |  |   
mCamMovingFastPrev  | bool  | 0  |  |   
mCamFrameStartedMovingFast  | int  | 0  |  |   
mCamFrameLastMovingFastExplosion  | int  | 0  |  |   
mCessationDo  | bool  | 0  |  |   
mCessationLifetime  | int  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
