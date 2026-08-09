# Documentation: ItemComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20ItemComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
item_name  | std::string  |  |  | the name of the item   
is_stackable  | bool  | 0  |  | does this item stack on other items the same 'item_name' in the inventory?   
is_consumable  | bool  | 0  |  | if 1, using this item will reduce 'uses_remaining'. When it reaches zero the item is destroyed   
stats_count_as_item_pick_up  | bool  | 1  |  | does this count as an item that was picked up in the stats   
auto_pickup  | bool  | 0  |  | if 1, item will be automatically picked up, no pickup hint is shown   
permanently_attached  | bool  | 0  |  | if 1, this item can't be removed from a container once it is put inside one   
uses_remaining  | int  | -1  |  | how many times can this item be used? -1 = unlimited, will be reset to gun_actions.lua max_uses by inventorygui_system, -2 = unlimited unlimited   
is_identified  | bool  | 1  |  | is it known what this item does?   
is_frozen  | bool  | 0  |  | if 1, this item can't be modified or moved from a wand   
collect_nondefault_actions  | bool  | 0  |  | does player keep this item when respawning?   
remove_on_death  | bool  | 0  |  | is this entity destroyed when it's in an inventory and the inventory owner dies?   
remove_on_death_if_empty  | bool  | 0  |  | is this entity destroyed when it's in an inventory, empty and the inventory owner dies?   
remove_default_child_actions_on_death  | bool  | 0  |  | if true, the default AbilityComponent.child_actions in this items will be removed when it dies   
play_hover_animation  | bool  | 0  |  | if 1, the item will play a hovering animation   
play_spinning_animation  | bool  | 1  |  | if 1, the item will play a spinning animation, if player_hover_animation is 0   
is_equipable_forced  | bool  | 0  |  | if 1, the default logic for determining if an item can be equiped in inventory is overridden and this can be always equipped   
play_pick_sound  | bool  | 1  |  | if 1, plays a default sound when picked   
drinkable  | bool  | 1  |  | if 0 you cannot drink this, default is 1, because that's how it was implemented and backwards compatibility   
max_child_items  | int  | 0  |  | number of items this can hold inside itself. TODO: get rid of all uses of 'ability->gun_config.deck_capacity' and replace them with this!   
ui_sprite  | std::string  |  |  | sprite displayed for the item in various UIs. If not empty overrides sprites declared by Ability and ItemAction   
ui_description  | std::string  |  |  | item description displayed in various UIs   
enable_orb_hacks  | bool  | 0  |  |   
is_all_spells_book  | bool  | 0  |  |   
always_use_item_name_in_ui  | bool  | 0  |  |   
custom_pickup_string  | std::string  |  |  | if set, this is used for the 'Press $0 to pick $1' message   
ui_display_description_on_pick_up_hint  | bool  | 0  |  |   
next_frame_pickable  | int  | 0  |  |   
npc_next_frame_pickable  | int  | 0  |  | NPC have their own next_frame_pickable, because this is used to make NPCs not pick up gold, which also meant player couldn't pick up that gold   
is_pickable  | bool  | 1  |  | can this be picked up and placed on someone's inventory   
is_hittable_always  | bool  | 0  |  | to override the weirdness that is is_pickable, which affects if this is hittable or not. If true, will always be hittable regardless of is_pickable   
item_pickup_radius  | float  | 14.1  |  | how many pixels away can this item be picked up from   
camera_max_distance  | float  | 50  |  | how far can we move the camera from the player when this item is equipped   
camera_smooth_speed_multiplier  | float  | 1  |  | how quickly does the camera follow player?   
has_been_picked_by_player  | bool  | 0  |  |   
mFramePickedUp  | int  | 0  |  |   
Custom data types   
spawn_pos  | vec2  |  |  | the position where this item spawned   
preferred_inventory  | INVENTORY_KIND::Enum  |  |  | Which inventory do we go to when we're picked up, if it's not full.   
inventory_slot  | ivec2  |  |  | our preferred slot (x,y) in the inventory   
Privates   
mItemUid  | int  | 0  |  |   
mIsIdentified  | bool  | 1  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
