# Documentation: InventoryComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20InventoryComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
ui_container_type  | int  | 1  |  | UI_CONTAINER_TYPES enum   
ui_element_sprite  | std::string  | data/ui_gfx/inventory/inventory_box.png  |  | ui back sprite   
actions  | std::string  |  |  | list of actions, used for serialization   
Custom data types   
ui_container_size  | ivec2  |  |  | ui size, how many items x*y we can fit in   
ui_element_size  | ivec2  |  |  | ui size   
ui_position_on_screen  | ivec2  |  |  | where do we load this on screen   
Privates   
update_listener  | InvenentoryUpdateListener*  |  |  | listener to keep ui up with ability changes   
items  | INVENTORYITEM_VECTOR  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
