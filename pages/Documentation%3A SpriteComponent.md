# Documentation: SpriteComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20SpriteComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
image_file  | std::string  | data/temp/temp_gun.png  |  |   
ui_is_parent  | bool  | 0  |  | Adds this to the GG.GetUISprite() as a child, instead of the mSpriteContainer   
is_text_sprite  | bool  | 0  |  | if you want to load a text sprite, set this to true and image_file to a font file   
offset_x  | float  | 0  | [-24,24]  |   
offset_y  | float  | 0  | [-24,24]  |   
alpha  | float  | 1  |  |   
visible  | bool  | 1  |  |   
emissive  | bool  | 0  |  |   
additive  | bool  | 0  |  |   
fog_of_war_hole  | bool  | 0  |  | if 1, the alpha channel of this texture punctures a hole in the fog of war   
smooth_filtering  | bool  | 0  |  |   
rect_animation  | std::string  |  |  |   
next_rect_animation  | std::string  |  |  |   
text  | std::string  |  |  |   
z_index  | float  | 1  | [-256,256]  | 0 = world grid, -1 = enemies, -1.5 = items in world, player = 0.6   
update_transform  | bool  | 1  |  |   
update_transform_rotation  | bool  | 1  |  |   
kill_entity_after_finished  | bool  | 0  |  |   
has_special_scale  | bool  | 0  |  | if this is set, sets special_scale_x and _y to scale   
special_scale_x  | float  | 1  |  | this overrides the scale of the entity, if has_special_scale   
special_scale_y  | float  | 1  |  | this overrides the scale of the entity, if has_special_scale   
never_ragdollify_on_death  | bool  | 0  |  |   
Custom data types   
transform_offset  | vec2  |  |  |   
offset_animator_offset  | vec2  |  |  | used by SpriteOffsetAnimator   
Privates   
mSprite  | as::Sprite*  |  |  |   
mRenderList  | SpriteRenderList*  |  |  |   
mRenderListHandle  | int32  | -1  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
