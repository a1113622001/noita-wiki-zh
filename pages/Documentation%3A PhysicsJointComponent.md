# Documentation: PhysicsJointComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PhysicsJointComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
nail_to_wall  | bool  | 0  |  |   
grid_joint  | bool  | 0  |  | if 1, will do a grid joint that works correctly with a body when it is destroyed / chipped away   
breakable  | bool  | 0  |  | if 1, will break if theres a force too strong   
body1_id  | int  | 0  |  |   
body2_id  | int  | 0  |  |   
pos_x  | float  | 0  | [0,3.5]  |   
pos_y  | float  | 0  | [0,3.5]  |   
delta_x  | float  | 0  | [-10,10]  | For mouse joint only ... moves the mouse joint by *dt   
delta_y  | float  | 0  | [-10,10]  | For mouse joint only ... moves the mouse joint by *dt   
mMotorEnabled  | bool  | 0  |  | enable motor, by setting this to true   
mMotorSpeed  | float  | 0  | [0,20]  | if enabled this gets set to speed   
mMaxMotorTorque  | float  | 1  |  | max torque for motor   
Custom data types   
type  | JOINT_TYPE::Enum  |  |  | Enum - JOINT_TYPE   
Privates   
mJoint  | b2Joint*  |  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
