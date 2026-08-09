# Documentation: MagicConvertMaterialComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20MagicConvertMaterialComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
radius  | int  | 256  | [0,512]  |   
min_radius  | int  | 0  | [0,512]  | allows for convert to happen from x pixels from the center   
is_circle  | bool  | 0  |  |   
steps_per_frame  | int  | 10  | [0,512]  |   
from_material_tag  | std::string  |  |  | the tag of material, e.g. [liquid]   
from_any_material  | bool  | 0  |  | if 1, converts any cells of any material to 'to_materia'   
clean_stains  | bool  | 0  |  |   
extinguish_fire  | bool  | 0  |  |   
fan_the_flames  | int  | 0  |  | if > 0, will call UpdateFire() fan_the_flames times   
temperature_reaction_temp  | int32  | 0  |  | if != 0, will use the 'cold_freezes_to_materials' and 'warmth_melts_to_materials' in CellData to convert cells different materials   
ignite_materials  | int  | 0  |  | if > 0, will call Ignite() with ingite_materials as probability_of_fire   
loop  | bool  | 0  |  |   
kill_when_finished  | bool  | 1  |  |   
convert_entities  | bool  | 0  |  | if 1, kills entities with a damagemodel and converts them to 'to_material'   
stain_frozen  | bool  | 0  |  | petri hax   
reaction_audio_amount  | float  | 0  |  | if > 0, will generate chemical reaction audio at converted cells   
convert_same_material  | bool  | 1  |  | 9.10.2020 - added this because at the end this caused the 'white ring' to appear, set it to false if you don't want constant whiteout   
from_material_array  | std::string  |  |  |   
to_material_array  | std::string  |  |  |   
mRadius  | int  | 0  | [0,512]  |   
Custom data types   
from_material  | int  | 0  |  |   
to_material  | int  | 0  |  |   
Privates   
mUseArrays  | bool  | 0  |  |   
mFromMaterialArray  | std::vector<int> |  |  |   
mToMaterialArray  | std::vector<int> |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
