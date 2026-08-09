# Documentation: PhysicsJoint2MutatorComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PhysicsJoint2MutatorComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
joint_id  | uint16  | 0  | [0,1000]  | Use this to create a relation between PhysicsJointMutator and a joint created by PhysicsJoint2Component. The PhysicsJoint2Mutator must exist when the physics objects are initialized for the first time.   
destroy  | bool  | 0  |  | if 1, the joint will break and this component will be destroyed.   
motor_speed  | float  | 0  |  | if != 0 and this is linked to a revolute joint, the joint motor will be enabled at this speed   
motor_max_torque  | float  | 1  |  | max torque for motor   
mBox2DJointId  | uint64  | 0  |  | Private, don't touch this! Stores the joint's id in the physics engine.   
Privates   
mPreviousMotorSpeed  | float  | 0  |  |   
mPreviousMotorMaxTorque  | float  | 0  |  | 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
