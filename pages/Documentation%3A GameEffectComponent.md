# Documentation: GameEffectComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20GameEffectComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
custom_effect_id  | std::string  |  |  | if 'effect' is set to 'CUSTOM', this will define effect uniqueness.   
frames  | int  | -1  |  | how many frames does it affect -1 = forever   
exclusivity_group  | int  | 0  |  | if > 0, previous game effects with the same exclusivity group as new one will be removed when calling LoadGameEffectEntityTo   
report_block_msg  | bool  | 1  |  | to disable the block message that rises   
disable_movement  | bool  | 0  |  | if set, will disable movement   
ragdoll_effect_custom_entity_file  | std::string  |  |  | an entity that is loaded to each ragdoll part if 'ragdoll_effect' is set to 'CUSTOM_RAGDOLL_ENTITY'   
ragdoll_fx_custom_entity_apply_only_to_largest_body  | bool  | 0  |  | if 1, 'ragdoll_effect_custom_entity_file' is loaded only to the largest piece in the ragdoll   
polymorph_target  | std::string  |  |  | when doing a polymorph, this is what we convert it to   
mSerializedData  | USTRING  |  |  | polymorph stores the serialized entity here...   
mCaster  | EntityID  | 0  |  | Contains a handle to the caster of this GameEffect   
mCasterHerdId  | int  | 0  |  | Contains the herd if of the caster of this GameEffect   
teleportation_probability  | int  | 600  |  | How likely is it that we teleport, larger = less often   
teleportation_delay_min_frames  | int  | 30  |  | Never teleports more often that this   
teleportation_radius_min  | float  | 128  |  |   
teleportation_radius_max  | float  | 1024  |  |   
teleportations_num  | int  | 0  |  | How many times has this GameEffectComponent teleported the owner?   
no_heal_max_hp_cap  | double  | 3.40282e+038  |  | If current hp is less than this, we store it here. Then we make sure the hp never exceeds this.   
caused_by_ingestion_status_effect  | bool  | 0  |  | Did this effect occur because someone ate something?   
caused_by_stains  | bool  | 0  |  | was this caused by stains   
mCharmDisabledCameraBound  | bool  | 0  |  | When charmed, will try to disable CameraBound. This keeps track if we've done it, so we can enable it back   
mCharmEnabledTeleporting  | bool  | 0  |  | When charmed, will try to enable teleporting (tag:teleportable_NOT). This keeps track if we've done it, so we can disable it again   
mInvisible  | bool  | 0  |  | Are we invisible?   
mCounter  | int  | 0  |  | Counts stuff   
mCooldown  | int  | 0  |  | Counts cooldown   
mIsExtension  | bool  | 0  |  | If 1, this is an effect extension and shouldn't create an extension when removed   
mIsSpent  | bool  | 0  |  | NOTE( Petri ): 29.4.2024 - this is used internally to make RESPAWN perk disabled in the UI   
Custom data types   
effect  | GAME_EFFECT::Enum  |  |  | GAME_EFFECT   
ragdoll_effect  | RAGDOLL_FX::Enum  |  |  | if set, will use this for ragdoll effect   
ragdoll_material  | int  | 0  |  | converts to string name of the material that ragdoll is made out of   
causing_status_effect  | StatusEffectType  | 0  |  | Status effect that caused this game effect, if any 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
