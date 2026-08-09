# Documentation: ProjectileComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20ProjectileComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
lifetime  | int  | -1  |  | lifetime, -1 means it's endless, otherwise it's the frame count   
lifetime_randomness  | int  | 0  |  | final lifetime will be lifetime + random(-lifetime_randomness,lifetime_randomness)   
on_lifetime_out_explode  | bool  | 0  |  | when lifetime runs out, should we explode?   
collide_with_world  | bool  | 1  |  | true by default. Some projectiles you don't want to collide with the world, e.g. blackholes   
speed_min  | float  | 60  | [0,60000]  |   
speed_max  | float  | 60  | [0,60000]  |   
friction  | float  | 0  | [0,60000]  |   
direction_random_rad  | float  | 0  | [0,3.14151]  | when fired, randomizes the velocity -this, this   
direction_nonrandom_rad  | float  | 0  | [-3.14,3.14]  | when fired, multiplies this with projectile_i and adds it to direction   
lob_min  | float  | 0.5  | [0,60000]  |   
lob_max  | float  | 0.8  | [0,60000]  |   
camera_shake_when_shot  | float  | 0  | [0,60000]  |   
shoot_light_flash_radius  | float  | 0  | [0,60000]  |   
shoot_light_flash_r  | unsigned int  | 255  | [0,255]  |   
shoot_light_flash_g  | unsigned int  | 180  | [0,255]  |   
shoot_light_flash_b  | unsigned int  | 150  | [0,255]  |   
create_shell_casing  | bool  | 0  |  | should we create shell casings?   
shell_casing_material  | std::string  | brass  |  | material of the shell casing   
muzzle_flash_file  | std::string  |  |  | this entity is created along with the projectile, oriented along the projectile's path   
bounces_left  | int  | 0  | [0,1e+008]  |   
bounce_energy  | float  | 0.5  |  | when bouncing, velocity is multiplied by this   
bounce_always  | bool  | 0  |  | if true, will do a fake bounce if can't do the proper bounce, but will always try to bounce   
bounce_at_any_angle  | bool  | 0  |  | if true, will bounce at any reflection angle   
attach_to_parent_trigger  | bool  | 0  |  | if true, will attach to the projectile entity that created this projectile via a trigger   
bounce_fx_file  | std::string  |  |  | this entity is created at the bounce position. it gets the bounce angle as rotation.   
angular_velocity  | float  | 0  | [-3.1415,3.1415]  | this is only applied if velocity_sets_rotation == false   
velocity_sets_rotation  | bool  | 1  |  | whether we set the rotation based on velocity, as in spear or if we update the rotation with angular_velocity   
velocity_sets_scale  | bool  | 0  |  | if true, the sprite width is made equal to the distance traveled since last frame   
velocity_sets_scale_coeff  | float  | 1  |  | Larger value means velocity affects the scale more   
velocity_sets_y_flip  | bool  | 0  |  | if true, the sprite is flipped based on which side the projectile is currently traveling   
velocity_updates_animation  | float  | 0  |  | updates the animation based on far the sprite moved   
ground_penetration_coeff  | float  | 0  | [0,5]  | if > 0, this, along with VelocityComponent.mass affects how far we penetrate in materials   
ground_penetration_max_durability_to_destroy  | int  | 0  |  | if 0, will not penetrate into materials with durability greater than this   
go_through_this_material  | std::string  |  |  | if set, we never collide with this material   
do_moveto_update  | bool  | 1  |  | this should probably be true, to get normal projectile behaviour, but you might want to disable this for some physics-based projectiles, like bombs   
on_death_duplicate_remaining  | int  | 0  |  | if greater than 0, the projectile creates two clones of itself on death. 'on_death_duplicate_remaining' on the clones is reduced by one   
on_death_gfx_leave_sprite  | bool  | 1  |  | if true, finds all the sprites and leaves as sand cells into the grid   
on_death_explode  | bool  | 0  |  | if true, does explosion with config_explosion   
on_death_emit_particle  | bool  | 0  |  | if true, emits on_death_emit_particle_type on death   
on_death_emit_particle_count  | int  | 1  |  | how many particles should we emit   
die_on_liquid_collision  | bool  | 0  |  | if true, dies on collision with liquids   
die_on_low_velocity  | bool  | 0  |  | if true, dies when speed goes below die_on_low_velocity_limit   
die_on_low_velocity_limit  | float  | 50  |  | please see die_on_low_velocity   
on_death_emit_particle_type  | std::string  |  |  |   
on_death_particle_check_concrete  | bool  | 0  |  | if you want it to stick as concrete, you should enable this   
ground_collision_fx  | bool  | 1  |  | if 1, spurt some particles when colliding with mortals   
explosion_dont_damage_shooter  | bool  | 0  |  | if true, explosion doesn't damage the entity who shot this   
on_death_item_pickable_radius  | float  | 0  |  | if > 0, makes items closer than this radius pickable on death   
penetrate_world  | bool  | 0  |  | if true, the projectile doesn't collide with ground, liquids, physical objects etc   
penetrate_world_velocity_coeff  | float  | 0.6  |  | if 'penetrate_world' is true, the projectile moves with a velocity multiplied by this value when inside world   
penetrate_entities  | bool  | 0  |  | if true, the projectile doesn't stop when it collides with entities. damages each entity only once   
on_collision_die  | bool  | 1  |  | if true, this is killed as soon as it hits the ground   
on_collision_remove_projectile  | bool  | 0  |  | if true, ProjectileComponent is removed from the entitiy   
on_collision_spawn_entity  | bool  | 1  |  | if true, spawns the spawn_entity   
spawn_entity  | std::string  |  |  | this is spawned if hit something an on_collision_spawn_entity = 1   
spawn_entity_is_projectile  | bool  | 0  |  | if true, will use ShootProjectile instead of LoadEntity()   
physics_impulse_coeff  | float  | 300  |  | projectile applies an impulse to physics bodies it hits. Impulse = physics_impulse_coeff * velocity   
damage_every_x_frames  | int  | -1  |  | if set != -1, will only do damage every x frames, used for fields and such, which would otherwise do damage every frame   
damage_scaled_by_speed  | bool  | 0  |  | if 1, damage is multiplied by (projectile speed / original projectile speed) ratio   
damage_scale_max_speed  | float  | 0  |  | if > 0 and damage_scaled_by_speed = 1, will use this instead of mInitialSpeed when calculating the damage   
collide_with_entities  | bool  | 1  |  | if 1, looks for entities with tag, collide_with_tag and collides with them, giving them damage   
collide_with_tag  | std::string  | hittable  |  | default: mortal, if you needed can be changed to something more specific   
dont_collide_with_tag  | std::string  |  |  | if set will ignore entities with this tag   
collide_with_shooter_frames  | int  | -1  |  | remember friendly_fire 1, if -1 won't collide with shooter at all, otherwise uses the value as frame count and while it's running won't damage the shooter   
friendly_fire  | bool  | 0  |  | if true, will damage same herd id   
damage  | float  | 1  |  | how much Projectile damage does this do when it hits something   
knockback_force  | float  | 0  |  | How far do entities get thrown if a knockback occurs. final_knockback = ProjectileComponent.knockback_force * VelocityComponent.mVelocity * VelocityComponent.mass / who_we_hit.mass   
ragdoll_force_multiplier  | float  | 0.025  |  | velocity * ragdoll_force_multiplier is applied to any ragdolls that are created by entities killed by this   
hit_particle_force_multiplier  | float  | 0.1  |  | hit particle velocity = projectile_velocity * hit_particle_force_multiplier * some randomness   
blood_count_multiplier  | float  | 1  |  | how much blood does this projectile cause   
damage_game_effect_entities  | std::string  |  |  | a list of game_effects entities separated with ','. e.g. 'data/entities/misc/effect_electrocution.xml,data/entities/misc/effect_on_fire.xml'   
never_hit_player  | bool  | 0  |  | If 1, does not hit player no matter what herds this and player belong to   
collect_materials_to_shooter  | bool  | 0  |  | if 1, looks up the 'who_shot' entity and its MaterialInventoryComponent on destruction and updates it based on the cells destroyed on our explosion.   
play_damage_sounds  | bool  | 1  |  |   
mLastFrameDamaged  | int  | -1024  |  |   
Objects   
config  | ConfigGunActionInfo  |  |  |   
config_explosion  | ConfigExplosion  |  |  | if we have explosion, it's the setup for it   
damage_by_type  | ConfigDamagesByType  |  |  | the amounts of different types of damage this does   
damage_critical  | ConfigDamageCritical  |  |  | config for critical hit   
Custom data types   
projectile_type  | PROJECTILE_TYPE::Enum  |  |  |   
shell_casing_offset  | vec2  |  |  | where the shell casing will be created relative to projectile, y is flipped if projectile direction is to the left.   
ragdoll_fx_on_collision  | RAGDOLL_FX::Enum  |  |  | if not NORMAL, do a special ragdoll   
Privates   
mWhoShot  | EntityID  | 0  |  | entity (creature) that shot this   
mWhoShotEntityTypeID  | EntityTypeID  | 0  |  | used for stats   
mShooterHerdId  | int  | 0  |  | the herdid of mWhoShot, unless friendly fire   
mStartingLifetime  | int  | 0  |  |   
mEntityThatShot  | EntityID  | 0  |  | for triggers, if shot from a trigger this should point to the projectile entity that shot this. Otherwise this should be the same as mWhoShot. NOTE! Not really tested properly so might break.   
mTriggers  | ProjectileTriggers  |  |  |   
mDamagedEntities  | VEC_ENTITY  |  |  |   
mInitialSpeed  | float  | -1  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
