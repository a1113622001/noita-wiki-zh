# Documentation: AnimalAIComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20AnimalAIComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
ai_state  | int  | 0  | [0,20]  | Current state of ai, defines what the animal is doing   
ai_state_timer  | int  | 0  | [0,1000]  | If not 0, then we wait till this frame to pop current state from our state stack   
keep_state_alive_when_enabled  | bool  | 0  |  | if 1, will ensure state timer keeps current state alive for a while when Component is Enabled   
preferred_job  | std::string  |  |  | We always do this job, unless interrupted (i.e. by taking fire damage)   
escape_if_damaged_probability  | int  | 30  |  | the chance of escaping if someone damages us. only works if 'can_fly = 0 '   
attack_if_damaged_probability  | int  | 100  |  | the chance of counter-attacking if someone damages us, and we didn't escape   
eye_offset_x  | int  | 0  | [-100,100]  | We cast rays from our position + eye_offset to check if we can see something   
eye_offset_y  | int  | 0  | [-100,100]  | We cast rays from our position + eye_offset to check if we can see something   
attack_only_if_attacked  | bool  | 0  |  | If 1, we never attack anyone unless attacked before by someone   
dont_counter_attack_own_herd  | bool  | 0  |  | If 1, we don't attack members of our herd even if they accidentally attack us   
creature_detection_range_x  | float  | 50  | [0,2000]  | When looking for threats/prey this is the max distance from us on the X axis we scan   
creature_detection_range_y  | float  | 20  | [0,2000]  | When looking for threats/prey this is the max distance from us on the Y axis we scan   
creature_detection_angular_range_deg  | float  | 90  | [0,90]  | When looking for threats/prey this is our field of view around the X axis. 90 means we scan the whole 180 degrees around the X axis, to the left and right   
creature_detection_check_every_x_frames  | int  | 120  | [0,5000]  | Checks for threats/prey take place at least this many frames apart from each other   
max_distance_to_cam_to_start_hunting  | float  | 300  | [0,2000]  | JobDefault idles before we've been once at least this close to the camera   
pathfinding_max_depth_no_target  | int  | 50  | [0,5000]  | The maximum depth (in nodes) path search use when we have not found prey yet   
pathfinding_max_depth_has_target  | int  | 120  | [0,5000]  | The maximum depth (in nodes) path search use when we have found prey   
aggressiveness_min  | float  | 80  | [0,100]  | what's the initial random aggressiveness of this creature   
aggressiveness_max  | float  | 100  | [0,100]  | what's the initial random aggressiveness of this creature   
tries_to_ranged_attack_friends  | bool  | 0  |  | if 1, the AI tries to attack whoever it considers a friend based on herd_ids, CHARMED and BERSERK status etc. useful e.g. for healers.   
attack_melee_enabled  | bool  | 1  |  | If 1, and melee attack has been configured, we can perform melee attacks   
attack_dash_enabled  | bool  | 0  |  | If 1, and dash attack has been configured, we can perform dash attacks (a long-distance melee attack where we dash towards the enemy)   
attack_landing_ranged_enabled  | bool  | 0  |  | If 1, and ranged attack has been configured, we can perform ranged attacks   
attack_ranged_enabled  | bool  | 0  |  | If 1, and ranged attack has been configured, we can perform ranged attacks   
attack_knockback_multiplier  | float  | 100  | [-100,100]  | If not 0, melee and dash attacks cause knockback to target   
is_static_turret  | bool  | 0  |  | If 1, we can only attack in one fixed direction   
attack_melee_max_distance  | int  | 20  | [0,400]  | Maximum distance at which we can perform a melee attack   
attack_melee_action_frame  | int  | 2  | [0,1000]  | The animation frame during which the melee attack damage is inflicted and visual effects are created   
attack_melee_frames_between  | int  | 10  | [0,1000]  | The minimum number of frames we wait between melee attacks   
attack_melee_damage_min  | float  | 0.4  | [0,100]  | Melee attack damage inclusive minimum amount. The damage is randomized between melee attack_damage_min and attack_melee_damage_max   
attack_melee_damage_max  | float  | 0.6  | [0,100]  | Melee attack damage inclusive maximum amount. The damage is randomized between melee attack_damage_min and attack_melee_damage_max   
attack_melee_impulse_vector_x  | float  | 0  | [-100,100]  | The x component of the impulse that is applied to damaged entities   
attack_melee_impulse_vector_y  | float  | 0  | [-100,100]  | The y component of the impulse that is applied to damaged entities   
attack_melee_impulse_multiplier  | float  | 0  | [-100,100]  | A multiplier applied to attack_melee_impulse   
attack_melee_offset_x  | float  | 0  | [-1000,1000]  | Melee attack particle effects are created here   
attack_melee_offset_y  | float  | 0  | [-1000,1000]  | Melee attack particle effects are created here   
attack_melee_finish_enabled  | bool  | 0  |  | If 1, we perform a finishing move when our attack would kill the target using the 'attack_finish' animation   
attack_melee_finish_action_frame  | int  | 2  | [0,1000]  | The animation frame during which the melee attack finishing move damage is inflicted and visual effects are created   
attack_dash_distance  | float  | 50  | [0,10000]  | The maximum distance from enemy at which we can perform a dash attack. If a normal melee attack is possible we always do that instead   
attack_dash_frames_between  | int  | 120  | [0,1200]  | The minimum number of frames we wait between dash attacks   
attack_dash_damage  | float  | 0.25  | [0,20]  | The amount of damage inflicted by the dash attack   
attack_dash_speed  | float  | 200  | [0,5000]  | The speed at which we dash   
attack_dash_lob  | float  | 0.9  | [0,6]  | The smaller this value is the more curved our dash attack trajectory is   
attack_ranged_min_distance  | float  | 10  | [0,10000]  | The minimum distance from enemy at which we can perform a ranged attack.   
attack_ranged_max_distance  | float  | 160  | [0,10000]  | The maximum distance from enemy at which we can perform a ranged attack.   
attack_ranged_action_frame  | int  | 2  | [0,1000]  | The frame of the 'attack_ranged' animation during which the ranged attack actually occurs   
attack_ranged_offset_x  | float  | 0  | [-1000,1000]  | 'attack_ranged_entity_file' is created here when performing a ranged attack   
attack_ranged_offset_y  | float  | 0  | [-1000,1000]  | 'attack_ranged_entity_file' is created here when performing a ranged attack   
attack_ranged_use_message  | bool  | 0  |  | If 1, we do ranged attacks by sending a Message_UseItem   
attack_ranged_predict  | bool  | 0  |  | If 1, we attempt to predict target movement and shoot accordingly   
attack_ranged_entity_file  | std::string  | data/entities/projectiles/spear.xml  |  | File to projectile entity that is created when performing a ranged attack   
attack_ranged_entity_count_min  | int  | 1  | [0,1000]  | Minimum number of projectiles shot when performing a ranged attack   
attack_ranged_entity_count_max  | int  | 1  | [0,1000]  | Maximum number of projectiles shot when performing a ranged attack   
attack_ranged_use_laser_sight  | bool  | 0  |  | If 1, we draw a laser sight to our target. Requires entity to have a sprite with tag 'laser_sight'   
attack_ranged_laser_sight_beam_kind  | bool  | 0  |  | 0 = red, 1 = blue   
attack_ranged_aim_rotation_enabled  | bool  | 0  |  |   
attack_ranged_aim_rotation_speed  | float  | 3  |  |   
attack_ranged_aim_rotation_shooting_ok_angle_deg  | float  | 10  |  |   
attack_ranged_state_duration_frames  | int  | 45  | [0,1000]  | How long do we stay in the attack state, before other states are allowed?   
hide_from_prey  | bool  | 0  |  | If 1, we attempt to hide from our target after a succesful attack   
hide_from_prey_target_distance  | float  | 200  | [0,10000]  | The minimum distance from our target where we should move when hiding   
hide_from_prey_time  | int  | 300  |  | The number of frames we spend hiding and staying hiding   
food_eating_create_particles  | bool  | 1  |  | If 1, we replace eaten cells with particles made of this material   
eating_area_radius_x  | int  | 3  | [-100,100]  | 1/2 width of the area from which we eat food   
eating_area_radius_y  | int  | 8  | [-100,100]  | 1/2 height of the area from which we eat food   
mouth_offset_x  | int  | 0  | [-100,100]  | The center of the area from which we eat food   
mouth_offset_y  | int  | 0  | [-100,100]  | The center of the area from which we eat food   
defecates_and_pees  | bool  | 0  |  | If 1, we occasionally take a leak or a dump   
butt_offset_x  | int  | 0  | [-100,100]  | Bodily wastes are created here   
butt_offset_y  | int  | 0  | [-100,100]  | Bodily wastes are created here   
pee_velocity_x  | float  | 0  | [-1000,1000]  | The velocity at which our piss gets shot   
pee_velocity_y  | float  | 0  | [-1000,1000]  | The velocity at which our piss gets shot   
needs_food  | bool  | 1  |  | If 1, we stop to eat if we encounter 'food_material' cells   
sense_creatures  | bool  | 1  |  | If 1, we occasionally search our surroundings for prey and threats   
sense_creatures_through_walls  | bool  | 0  |  | If 1, will see creatures even if the wall raycast fails   
can_fly  | bool  | 1  |  | If 1, we can fly. Please set 'PathFindingComponent.can_fly' to 1 as well if this is 1   
can_walk  | bool  | 1  |  | If 1, we can walk. Please set 'PathFindingComponent.can_walk' to 1 as well if this is 1   
path_distance_to_target_node_to_turn_around  | int  | 0  | [0,1000]  | If we're further than this from target path finding node on the X-axis we turn to face it   
path_cleanup_explosion_radius  | float  | 6  | [0,1000]  | If we get stuck on ground we create an explosion this big to clear our surroundings a bit   
max_distance_to_move_from_home  | float  | 0  |  |   
Objects   
attack_melee_finish_config_explosion  | ConfigExplosion  |  |  | If we have explosion, it's the setup for it   
Custom data types   
attack_ranged_frames_between  | LensValue<int> |  |  | The minimum number of frames we wait between ranged attacks   
food_material  | int  | 0  |  | The cell material we eat if encountering said material and 'needs_food' is 1   
food_particle_effect_material  | int  | 0  |  | We create particles made of this material when eating if 'food_eating_create_particles' is 1   
mAggression  | LensValue<float> |  |  | the greater this value the more likely we're to attack creatures from other herds   
Privates   
mAiStateStack  | AI_STATE_STACK  |  |  | a stack of actions and times they take, we can push new actions to the front and pop them from there   
mAiStateLastSwitchFrame  | int  | 0  |  | when was the last time we switched a state   
mAiStatePrev  | int  | 0  |  | previous AI state   
mCreatureDetectionNextCheck  | int  | 0  |  | threat/prey check, next time we check for threat/prey   
mGreatestThreat  | EntityID  | 0  |  | the entity we consider to be our greatest threat   
mGreatestPrey  | EntityID  | 0  |  | the entity we consider to be our most important prey   
mSelectedMultiAttack  | int  | -1  |  | which AIAttackComponent attack are we using?   
mHasFoundPrey  | bool  | 0  |  | 1, if we have ever found prey   
mHasBeenAttackedByPlayer  | bool  | 0  |  | 1, if we have been ever attacked   
mHasStartedAttacking  | bool  | 0  |  | 1, if we have ever started attacking anyone   
mNearbyFoodCount  | int  | 0  |  | amount of 'food_material' near us   
mEatNextFrame  | int  | 0  |  | next frame we can eat   
mEatTime  | int  | 0  |  | time we've been constantly eating   
mFrameNextGiveUp  | int  | 0  |  | next frame we consider ourselves to be stuck   
mLastFramesMovementAreaMin  | vec2  |  |  | AABB min of the area where we've been since the last time we got stuck   
mLastFramesMovementAreaMax  | vec2  |  |  | AABB max of the area where we've been since the last time we got stuck   
mFoodMaterialId  | int  | -1  |  | cached id of 'food_material'   
mFoodParticleEffectMaterialId  | int  | -1  |  | cached id of 'food_particle_effect_material'   
mNextJumpLob  | float  | 1  |  | we use this for next jump   
mNextJumpTarget  | vec2  |  |  | we use this for next jump   
mNextJumpHasVelocity  | bool  | 0  |  | we use this for next jump   
mLastFrameJumped  | int  | -1  |  | previous frame we launched into a jump   
mFramesWithoutTarget  | int  | 0  |  |   
mLastFrameCanDamageOwnHerd  | int  | -1  |  |   
mHomePosition  | vec2  |  |  | where our home is located   
mLastFrameAttackWasDone  | int  | 0  |  | when was the last time we did an attack (not necessarily did damage to anyone though)   
mNextFrameCanCallFriend  | int  | 0  |  |   
mNextFrameRespondFriend  | int  | -1  |  |   
mHasNoticedPlayer  | bool  | 0  |  | if 1, we have noticed player or player projectile   
mRangedAttackCurrentAimAngle  | float  | 0  |  | which direction does our gun currently point at, physically saying?   
mRangedAttackNextFrame  | int  | 0  |  | next frame we can perform a ranged attack   
mMeleeAttackNextFrame  | int  | 0  |  | next frame we can perform a melee attack   
mNextMeleeAttackDamage  | float  | 0  |  | the amount of damage our next melee attack will cause. used by finishing move logic   
mMeleeAttacking  | bool  | 0  |  | 1, if we're doing a melee attack   
mMeleeAttackDashNextFrame  | int  | 0  |  | the next frame we can perform a melee attack   
mCurrentJob  | RtsUnitGoal  |  |  | info about our current job. sorta legacy and could be simplified because the RTS logic is not used anywhere but doesn't have much overhead either. 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
