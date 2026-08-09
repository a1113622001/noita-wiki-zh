# Documentation: LuaComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20LuaComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
script_source_file  | std::string  |  |  |   
execute_on_added  | bool  | 0  |  |   
execute_on_removed  | bool  | 0  |  |   
execute_every_n_frame  | int  | 1  | [1,150]  | 1 = execute every frame. 2 = execute every second frame. 3 = execute every third frame and so on. -1 = execute only on add/remove/event   
execute_times  | int  | 0  |  | How many times should the script be executed? < 1 means infinite   
limit_how_many_times_per_frame  | int  | -1  |  | -1 = infinite. Use this to limit how many times this can be executed per frame. Currently only used to limit script_shot from being executed forever.   
limit_to_every_n_frame  | int  | -1  |  | -1 = no limit. Currently only used to limit script_shot from being executed every frame.   
limit_all_callbacks  | bool  | 0  |  | NOTE( Petri ): 19.8.2023 - by default limit_how_many_times_per_frame and limit_to_every_n_frame only works for script_shot. If this is set to true, will limit all callbacks. Also note that this limit is shared within this component. So if this is true and both script_shot and script_damage_received and both are called within limit_to_every_n_frame frames, only one of them will be called.   
remove_after_executed  | bool  | 0  |  |   
enable_coroutines  | bool  | 0  |  |   
call_init_function  | bool  | 0  |  | if 1, calls function init( entity_id:int ) after running the code in the file scope of script_source_file along with all mod appends. Does nothing if execute_on_added is 0   
script_enabled_changed  | std::string  |  |  | if set, calls function 'enabled_changed( entity_id:int, is_enabled:bool )' when the IsEnabled status of this LuaComponent is changed   
script_damage_received  | std::string  |  |  | if set, calls function 'damage_received( damage:number, message:string, entity_thats_responsible:int, is_fatal:bool, projectile_thats_responsible:int )' when we receive a message about damage (Message_DamageReceived)   
script_damage_about_to_be_received  | std::string  |  |  | if set, calls function 'damage_about_to_be_received( damage:number, x:number, y:number, entity_thats_responsible:int, critical_hit_chance:int )' when we receive a message (Message_DamageAboutToBeReceived) -> new_damage:number,new_critical_hit_chance:int   
script_item_picked_up  | std::string  |  |  | if set, calls function 'item_pickup( int entity_item, int entity_pickupper, string item_name )' when message 'Message_ItemPickUp' is called   
script_shot  | std::string  |  |  | if set, calls function 'shot( projectile_entity_id )' when we receive Message_Shot   
script_collision_trigger_hit  | std::string  |  |  | if set, calls function 'collision_trigger( colliding_entity_id )' when we receive Message_CollisionTriggerHit   
script_collision_trigger_timer_finished  | std::string  |  |  | if set, calls function 'collision_trigger_timer_finished()' when we receive Message_CollisionTriggerTimerFinished   
script_physics_body_modified  | std::string  |  |  | if set, calls function 'physics_body_modified( is_destroyed )' when physics body has been modified   
script_pressure_plate_change  | std::string  |  |  | if set, calls function 'pressure_plate_change( new_state )' when PressurePlateComponent decides that things have change   
script_inhaled_material  | std::string  |  |  | if set, calls function 'inhaled_material( material_name, count )' once per second for each inhaled material   
script_death  | std::string  |  |  | if set, calls function 'death( int damage_type_bit_field, string damage_message, int entity_thats_responsible, bool drop_items )' when we receive message Message_Death   
script_throw_item  | std::string  |  |  | if set, calls function 'throw_item( from_x, from_y, to_x, to_y )' when we receive message Message_ThrowItem   
script_material_area_checker_failed  | std::string  |  |  | if set, calls function 'material_area_checker_failed( pos_x, pos_y, )' when we receive message Message_MaterialAreaCheckerFailed   
script_material_area_checker_success  | std::string  |  |  | if set, calls function 'material_area_checker_success( pos_x, pos_y, )' when we receive message Message_MaterialAreaCheckerSuccess   
script_electricity_receiver_switched  | std::string  |  |  | if set, calls function 'electricity_receiver_switched( bool is_electrified )' when we receive message Message_ElectricityReceiverSwitched   
script_electricity_receiver_electrified  | std::string  |  |  | if set, calls function 'electricity_receiver_electrified()' when we receive message Message_ElectricityReceiverElectrified   
script_kick  | std::string  |  |  | if set, calls function 'kick( entity_who_kicked )' when we receive message Message_Kick   
script_interacting  | std::string  |  |  | if set, calls function 'interacting( entity_who_interacted, entity_interacted, interactable_name )' when we receive message Message_Interaction   
script_audio_event_dead  | std::string  |  |  | if set, calls function 'audio_event_dead( bank_file, event_root )' when we receive message Message_AudioEventDead   
script_wand_fired  | std::string  |  |  | if set, calls function 'wand_fired( gun_entity_id )' when we receive Message_WandFired   
script_teleported  | std::string  |  |  | if set, calls function 'teleported( from_x, from_y, to_x, to_y, bool portal_teleport )' when we receive Message_Teleported   
script_portal_teleport_used  | std::string  |  |  | if set, calls function 'portal_teleport_used( entity_that_was_teleported, from_x, from_y, to_x, to_y )' when we receive Message_PortalTeleportUsed   
script_polymorphing_to  | std::string  |  |  | if set, calls function 'polymorphing_to( string_entity_we_are_about_to_polymorph_to )' when we receive Message_PolymorphingTo   
script_biome_entered  | std::string  |  |  | if set, calls function 'biome_entered( string_biome_name, string_biome_old_name )' when this entity changes biomes. Requires BiomeTrackerComponent   
mLastExecutionFrame  | int  | -1  |  |   
mTimesExecutedThisFrame  | int  | 0  |  | tracks how many times we've executed this frame. This will linger on and store the old value of the old frames. Used internally.   
mModAppendsDone  | bool  | 0  |  |   
Custom data types   
vm_type  | LUA_VM_TYPE::Enum  |  |  | Do we share a single Lua virtual machine for everyone who runs 'script_source_file' ('SHARED_BY_MANY_COMPONENTS'), create one VM per one LuaComponent and reuse the VM in case the component runs the script multiple times ('ONE_PER_COMPONENT_INSTANCE'), or create a new VM every time the script is executed ('CREATE_NEW_EVERY_EXECUTION', deprecated)?   
Privates   
mNextExecutionTime  | int  | -1  |  |   
mTimesExecuted  | int  | 0  |  |   
mLuaManager  | LuaManager*  |  |  |   
mPersistentValues  | ValueMap  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
