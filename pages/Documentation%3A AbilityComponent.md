# Documentation: AbilityComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20AbilityComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
cooldown_frames  | int  | 0  | [0,60000]  |   
entity_file  | std::string  |  |  | the projectile entity file   
sprite_file  | std::string  |  |  |   
entity_count  | int  | 1  | [0,60000]  |   
never_reload  | bool  | 0  |  |   
reload_time_frames  | int  | 0  |  |   
mana  | float  | 0  |  |   
mana_max  | float  | 100  |  |   
mana_charge_speed  | float  | 10  |  |   
rotate_in_hand  | bool  | 1  |  |   
rotate_in_hand_amount  | float  | 1  |  | [0-1], how much does the item rotate related to the actual aiming angle   
rotate_hand_amount  | float  | 0.7  |  | [0-1], how much does hand sprite rotate related to the actual aiming angle   
fast_projectile  | bool  | 0  |  | if 1, then the velocity of the bullet is increased quite a bit. Lightning requires this   
swim_propel_amount  | float  | 0  | [-1000,1000]  |   
max_charged_actions  | int  | 0  |  |   
charge_wait_frames  | int  | 10  |  |   
item_recoil_recovery_speed  | float  | 15  |  | How quickly does the item return to resting state after getting recoil   
item_recoil_max  | float  | 1  |  | Maximum distance moved by recoil   
item_recoil_offset_coeff  | float  | 1  |  | Item distance moved by recoil = mItemRecoil * item_recoil_offset_coeff   
item_recoil_rotation_coeff  | float  | 5  |  | Item rotation by recoil = mItemRecoil * item_recoil_rotation_coeff   
base_item_file  | std::string  | data/entities/base_item.xml  |  | when dropping / throwing the item, this is the base_item that we add the ability component to   
use_entity_file_as_projectile_info_proxy  | bool  | 0  |  |   
click_to_use  | bool  | 1  |  |   
stat_times_player_has_shot  | int  | 0  |  | used to track how many times player has shot this 'ability'   
stat_times_player_has_edited  | int  | 0  |  | used to track how many times this has been edited   
shooting_reduces_amount_in_inventory  | bool  | 0  |  |   
throw_as_item  | bool  | 0  |  |   
simulate_throw_as_item  | bool  | 0  |  | If 1, the item will be work as normal ability, but throwing animation is played by the user   
max_amount_in_inventory  | int  | 1  |  |   
amount_in_inventory  | int  | 1  |  |   
drop_as_item_on_death  | bool  | 1  |  |   
ui_name  | std::string  | [NOT_SET]  |  | way to name the weapons   
use_gun_script  | bool  | 0  |  | If 1, the default ability behaviour is replaced with one that uses the lua gun system.   
is_petris_gun  | bool  | 0  |  | if 1, TODO( PETRI)   
gun_level  | int  | 1  | [1,10]  | the level of the wand, set in gun_procedural.lua   
add_these_child_actions  | std::string  |  |  | e.g. 'bullet,bullet,damage' ... actions are parsed into a string. These are added as actual entities when the item is initialized   
current_slot_durability  | int  | -1  |  | After this many slots the last slot of the gun is removed. -1 means not initialized/infinite.   
slot_consumption_function  | std_string  | _get_gun_slot_durability_default  |  | Name of the lua function in 'gun.lua' that is called to calculate durability of the last slot in the gun   
mNextFrameUsable  | int  | 0  |  | hax, don't touch!   
mCastDelayStartFrame  | int  | 0  |  | hax, don't touch!   
mReloadFramesLeft  | int  | 0  |  | hax, don't touch!   
mReloadNextFrameUsable  | int  | 0  |  | hax, don't touch!   
mChargeCount  | int  | 0  |  | hax, don't touch!   
mIsInitialized  | bool  | 0  |  |   
Objects   
gun_config  | ConfigGun  |  |  | Constants for gun script   
gunaction_config  | ConfigGunActionInfo  |  |  | Constants for gun script   
Privates   
mAmmoLeft  | int  | 0  |  |   
mNextChargeFrame  | int  | 0  |  |   
mItemRecoil  | float  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
