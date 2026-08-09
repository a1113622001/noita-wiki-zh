# Documentation: Inventory2Component

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20Inventory2Component
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
quick_inventory_slots  | int  | 10  | [0,30]  |   
full_inventory_slots_x  | int  | 8  | [0,30]  |   
full_inventory_slots_y  | int  | 8  | [0,30]  |   
mSavedActiveItemIndex  | uint32  | 0  |  | Used to retain active item across save/load. Don't touch this unless you know what you're doing!   
Privates   
mActiveItem  | EntityID  | 0  |  | NOTE: Don't attempt to directly change the value of this field via lua code. It will probably break the game logic in obvious or subtle ways.   
mActualActiveItem  | EntityID  | 0  |  | NOTE: Don't attempt to directly change the value of this field via lua code. It will probably break the game logic in obvious or subtle ways.   
mActiveStash  | EntityID  | 0  |  |   
mThrowItem  | EntityID  | 0  |  | Is used to store the item that is being thrown, instead of mActiveItem, since the player can switch items (mActiveItem) during the throwing animation   
mItemHolstered  | bool  | 0  |  |   
mInitialized  | bool  | 0  |  |   
mForceRefresh  | bool  | 0  |  |   
mDontLogNextItemEquip  | bool  | 0  |  |   
mSmoothedItemXOffset  | float  | 0  |  |   
mLastItemSwitchFrame  | int  | 0  |  |   
mIntroEquipItemLerp  | float  | 1  |  |   
mSmoothedItemAngleVec  | vec2  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
