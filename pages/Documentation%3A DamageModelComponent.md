# Documentation: DamageModelComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20DamageModelComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
hp  | double  | 1  | [0,4]  | hit points at the moment   
max_hp  | double  | 0  | [0,4]  | the maximum hp that this can have, we'll set this when loading   
max_hp_cap  | double  | 0  | [0,12]  | the maximum 'max_hp' that this can have, <= 0 means no limits. Used by perks such as GLASS_CANNON   
max_hp_old  | double  | 0  |  | used for UI rendering   
critical_damage_resistance  | float  | 0  |  | 0.0 = all critical damage multiplier is applied. 1.0 = no critical damage multiplier is applied   
invincibility_frames  | int  | 0  | [0,1024]  | if positive, doesn't take damage   
falling_damages  | bool  | 1  |  | do we take fall damage   
falling_damage_height_min  | float  | 70  |  | how far do we need to fall to take damage, we start with this height, the peasant takes min damage from this   
falling_damage_height_max  | float  | 250  |  | after this the peasant always takes the maximum fall damage   
falling_damage_damage_min  | float  | 0.1  |  | when we fall over height_min we take this much, lineary ramping to damage_max   
falling_damage_damage_max  | float  | 1.2  |  | when we fall over height_min we take this much, lineary ramping to damage_max   
air_needed  | bool  | 1  |  | Do we breath, can we take damage from not breathing?   
air_in_lungs  | float  | 5  |  | How much air do we have in our lungs? - after the air runs out we take damage   
air_in_lungs_max  | float  | 5  |  | how much air can we have in our lungs, it's filled to this point if we're not in water   
air_lack_of_damage  | float  | 0.2  |  | (* dt)... damage in a second if we're in the water   
minimum_knockback_force  | float  | 0  |  | Minimum knockback force required to do the knockback   
materials_damage  | bool  | 1  |  | should materials do damage or not?   
material_damage_min_cell_count  | int  | 4  |  | if material damage is received from less than 'material_damage_min_cell_count' this frame, it is ignored   
materials_that_damage  | std::string  | acid  |  | list of materials that do damage, separated by ',' e.g. 'acid, fire, smoke'   
materials_how_much_damage  | std::string  | 0.1  |  | list of damage amount per material in materials_that_damage, separated by ','   
materials_damage_proportional_to_maxhp  | bool  | 0  |  | if damage from materials is proportional to max hp, instead of just damage   
physics_objects_damage  | bool  | 0  |  | if true, will take damage from physics objects that hit it   
materials_create_messages  | bool  | 0  |  | should collisions with certain materials create messages or not?   
materials_that_create_messages  | std::string  | meat  |  | list of materials that generate CollisionWithCell messages, separated by ',' e.g. 'acid, fire, smoke'   
ragdoll_filenames_file  | std::string  | data/temp/ragdoll/filenames.txt  |  | the file from which to load a ragdoll on death'   
ragdoll_material  | std::string  | meat  |  | what material is the ragdoll made out of   
ragdoll_offset_x  | float  | 0  |  | where should the ragdoll be created relative to our entity position'   
ragdoll_offset_y  | float  | 0  |  | where should the ragdoll be created relative to our entity position'   
blood_material  | std::string  | blood_fading  |  | this is the material that gets thrown as particles when this entity takes damage   
blood_spray_material  | std::string  |  |  | this is the material that gets thrown as particles when this entity sprays blood on death   
blood_spray_create_some_cosmetic  | bool  | 0  |  | if true, we force some blood spray particles to be cosmetic (can be enabled to avoid making a huge mess of blood spray)   
blood_multiplier  | float  | 1  | [0,10]  | how much blood, this is the multiplier used for sprouting lots or little blood   
ragdoll_blood_amount_absolute  | int  | -1  | [-1,1000]  | if > -1, this is the absolute amount of blood we share between particle emitters in the ragdoll   
blood_sprite_directional  | std::string  |  |  | this sprite is loaded at damage position if we take damage that creates a blood effect   
blood_sprite_large  | std::string  |  |  | this sprite is loaded at damage position if we take explosion/heavy damage   
healing_particle_effect_entity  | std::string  |  |  | if this is set, will load this entity as a child of this entity, when this entity is healed   
create_ragdoll  | bool  | 1  |  | if 0, we skip ragdoll creation on death   
ragdollify_child_entity_sprites  | bool  | 0  |  | if 1, we ragdollify child entity sprites   
ragdollify_root_angular_damping  | float  | 0  |  | If ragdoll_filenames_file= and > 0, the angular damping of the first ragdoll body is set to this value.   
ragdollify_disintegrate_nonroot  | bool  | 0  |  | If ragdoll_filenames_file= and true, all but the first sprite on the root entity will be disintegrated instead of being turned into physics bodies.   
wait_for_kill_flag_on_death  | bool  | 0  |  | if 1, we wont kill the entity along with kill fx and ragdoll until 'kill' is 1   
kill_now  | bool  | 0  |  | if 1, we wont kill the entity along with kill fx and ragdoll until 'kill_now' is 1   
drop_items_on_death  | bool  | 1  |  | drop the abilities as items on death?   
ui_report_damage  | bool  | 1  |  | If 1, damage numbers are displayed when this entity is damaged   
ui_force_report_damage  | bool  | 0  |  | If 1, damage numbers are displayed when this entity is damaged, even if the numbers are disabled in settings   
in_liquid_shooting_electrify_prob  | int  | 0  | [0,100]  | when shooting underwater how likely are we to electrify the water   
wet_status_effect_damage  | float  | 0  | [0,0.1]  | how much damage per 10 frames is done if entity has 'wet' status effect   
is_on_fire  | bool  | 0  |  | Tells us we're on fire or not   
fire_probability_of_ignition  | float  | 0.5  |  | what is the probability that we'll ignite, 0 means won't ever ignite   
fire_how_much_fire_generates  | int  | 4  | [0,10]  | how many fire particles do we generate each frame   
fire_damage_ignited_amount  | float  | 0.0003  | [0,2]  | how much damage does being ignited do?   
fire_damage_amount  | float  | 0.2  | [0,2]  | how much damage does fire do?, 0.2 is pretty good   
mLastElectricityResistanceFrame  | int  | -2147483648  |  | Last frame electricity has no effect. Should not be private!   
mLastFrameReportedBlock  | int  | -2147483648  |  | Last frame a damage block message was displayed for this entity   
mLastMaxHpChangeFrame  | int  | -10000  |  | used for UI rendering   
Objects   
damage_multipliers  | ConfigDamagesByType  |  |  | the multipliers applied to different types of damage   
Custom data types   
ragdoll_fx_forced  | RAGDOLL_FX::Enum  |  |  | if set, will force this ragdoll fx to happen everytime   
Privates   
mIsOnFire  | bool  | 0  |  | private variable to check when we're on fire and not   
mFireProbability  | int  | 100  |  | this gets decreased if we can't ignite anything else   
mFireFramesLeft  | int  | 0  |  | this is the remaining frames we're on fire   
mFireDurationFrames  | int  | 0  |  | this is the total duration in frames we're on fire   
mFireTriedIgniting  | bool  | 0  |  | private variable to check when we could have been ignited or not   
mLastCheckX  | int  | 0  |  | an optimization, so we don't have to check everything every frame   
mLastCheckY  | int  | 0  |  | an optimization, so we don't have to check everything every frame   
mLastCheckTime  | int  | 0  |  | an optimization, so we don't have to check everything every frame   
mLastMaterialDamageFrame  | int  | 0  |  | this is the last frame we took material damage   
mFallIsOnGround  | bool  | 0  |  | for fall damage, keeps a private variable about if we're on ground or not   
mFallHighestY  | float  | 3.40282e+038  |  | private var to keep track of how high have we flown to   
mFallCount  | int  | 0  |  | how many times have we fallen? This is used to make sure we don't take damage from the first fall   
mAirAreWeInWater  | bool  | 0  |  | a private variable to track our state in drowning   
mAirFramesNotInWater  | int  | 0  |  | how many frames have been with air to breathe   
mAirDoWeHave  | bool  | 0  |  | a private variable to track our state in drowning   
mTotalCells  | int  | 0  |  | how many cells are there total   
mLiquidCount  | int  | 0  |  | how many of the cells are liquid   
mLiquidMaterialWeAreIn  | int  | -1  |  | stores the liquid material we're in... may not be the most accurate   
mDamageMaterials  | std::vector< int > |  |  | NOTE! Sorted! a list of materials that do damage (materials_that_damage)   
mDamageMaterialsHowMuch  | std::vector< float > |  |  | NOTE! Sorted! a list of materials that do damage (materials_that_damage)   
mCollisionMessageMaterials  | std::vector< int > |  |  | NOTE! Sorted! a list of materials that create messages (materials_that_create_messages)   
mCollisionMessageMaterialCountsThisFrame  | std::vector< int > |  |  | Number of cells per collided with this frame. Order matches mCollisionMessageMaterials   
mMaterialDamageThisFrame  | std::vector< float > |  |  | A list of damage per material that damages us. In same order as materials   
mFallDamageThisFrame  | float  | 0  |  | Amount of fall damage received this frame   
mElectricityDamageThisFrame  | float  | 0  |  | Amount of electricity damage received this frame   
mPhysicsDamageThisFrame  | float  | 0  |  | max physics damage we have taken this round   
mPhysicsDamageVecThisFrame  | vec2  |  |  | direction of physics damage   
mPhysicsDamageLastFrame  | int  | 0  |  | frame number when we took physics damage   
mPhysicsDamageEntity  | EntityTypeID  | 0  |  | the physics entity that hit us   
mPhysicsDamageTelekinesisCasterEntity  | EntityTypeID  | 0  |  | who moved an object that hit us via telekinesis   
mLastDamageFrame  | int  | -120  |  | frame number when we took any damage   
mHpBeforeLastDamage  | double  | 0  |  | how much hp did we have a while ago?   
mFireDamageBuffered  | float  | 0  |  | used to optimized cases where lots of entities are taking fire damage   
mFireDamageBufferedNextDeliveryFrame  | int32  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
