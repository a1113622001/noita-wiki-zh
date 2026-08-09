# Documentation: PhysicsJoint2Component

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PhysicsJoint2Component
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
joint_id  | uint16  | 0  | [0,1000]  | Use this to create a relation between PhysicsJointMutator and a joint. The PhysicsJointMutator must exist when the physics objects are initialized for the first time. This id should be unique inside one entity. Defaults to 0   
break_force  | float  | 1.3  |  | if > 0, will break if theres a force too strong.   
break_distance  | float  | 1.4142  |  | if > 0, will break if the anchors on the bodies get further than this.   
break_on_body_modified  | bool  | 0  |  | if > 1, will break if an attached body is modified   
break_on_shear_angle_deg  | float  | 0  |  | if > 0, will break if the angle between the linked bodies becomes greater than this   
body1_id  | int  | 0  |  |   
body2_id  | int  | 0  |  |   
offset_x  | float  | 0  |  |   
offset_y  | float  | 0  |  |   
ray_x  | float  | 0  |  |   
ray_y  | float  | -10  |  |   
surface_attachment_offset_x  | float  | 0  |  |   
surface_attachment_offset_y  | float  | 2.5  |  |   
Custom data types   
type  | JOINT_TYPE::Enum  |  |  | Enum - REVOLUTE_JOINT, WELD_JOINT, REVOLUTE_JOINT_ATTACH_TO_NEARBY_SURFACE or WELD_JOINT_ATTACH_TO_NEARBY_SURFACE 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
