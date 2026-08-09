# Documentation: PathFindingComponent

**分类:** [Category:Documentation](Category%3ADocumentation.md)
**来源:** https://noita.wiki.gg/zh/wiki/Documentation%3A%20PathFindingComponent
---

字段名  | 类型  | 默认值  | 示例范围  | 描述   
---|---|---|---|---  
Members   
search_depth_max_no_goal  | int  | 20  | [0,1e+006]  | TODO: Comment   
iterations_max_no_goal  | int  | 1500  | [0,1e+006]  | TODO: Comment   
search_depth_max_with_goal  | int  | 2500  | [0,1e+006]  | TODO: Comment   
iterations_max_with_goal  | int  | 1500  | [0,1e+006]  | TODO: Comment   
cost_of_flying  | float  | 20  | [0,100000]  | TODO: Comment   
distance_to_reach_node_x  | int  | 2  | [0,200]  | TODO: Comment   
distance_to_reach_node_y  | int  | 6  | [0,200]  | TODO: Comment   
frames_to_get_stuck  | int  | 60  | [0,600]  | TODO: Comment   
frames_between_searches  | int  | 30  | [0,300]  | TODO: Comment   
y_walking_compensation  | float  | 0  | [-100,100]  | TODO: Comment   
can_fly  | bool  | 1  |  | TODO: Comment   
can_walk  | bool  | 1  |  | TODO: Comment   
can_jump  | bool  | 0  |  | TODO: Comment   
can_dive  | bool  | 0  |  | TODO: Comment   
can_swim_on_surface  | bool  | 0  |  | TODO: Comment   
never_consider_line_of_sight  | bool  | 0  |  | if 1, we require a path to have an entity at the goal, having line of sight to the entity is not enough   
space_required  | float  | 0  | [0,20]  | how far (in cells) must a point on our route be from the nearest wall to consider it passable?   
max_jump_distance_from_camera  | float  | 400  | [0,400]  | TODO: Comment   
jump_speed  | float  | 200  | [0,1000]  | TODO: Comment   
initial_jump_lob  | float  | 1  | [0,5]  | TODO: Comment   
initial_jump_max_distance_x  | float  | 100  | [0,1000]  | TODO: Comment   
initial_jump_max_distance_y  | float  | 80  | [0,1000]  | TODO: Comment   
read_state  | int  | 0  |  | Read only value to get mState as an integer. Used to detect when the worst cheesers are trying to cheese our beloved squidward.   
Custom data types   
jump_trajectories  | VECTOR_JUMPPARAMS  |  |  | TODO: Comment   
Privates   
input  | PathFindingInput  |  |  | TODO: Comment   
job_result_receiver  | MSG_QUEUE_PATH_FINDING_RESULT  |  |  | TODO: Comment   
waiting_for  | bool  | 0  |  | TODO: Comment   
next_search_frame  | int  | 0  |  | TODO: Comment   
path  | VECTOR_PATHNODE  |  |  | TODO: Comment   
path_next_node  | PathFindingResultNode  |  |  | TODO: Comment   
path_next_node_vector_to  | vec2  |  |  | TODO: Comment   
path_next_node_distance_to  | float  | 0  |  | TODO: Comment   
path_previous_node  | PathFindingNodeHandle  |  |  | TODO: Comment   
path_frames_stuck  | int  | 0  |  | TODO: Comment   
path_is_stuck  | bool  | 0  |  | TODO: Comment   
path_last_frame_with_job  | int  | 0  |  | TODO: Comment   
mLogic  | PathFindingLogic*  |  |  | this defines what is an acceptable path   
mFallbackLogic  | PathFindingLogic*  |  |  | we use this to define an acceptable path if mLogic doesn't return one   
mSelectedLogic  | PathFindingLogic*  |  |  | TODO: Comment   
mEnabled  | bool  | 0  |  | TODO: Comment   
mState  | PathFindingComponentState::Enum  |  |  | TODO: Comment   
mTimesStuck  | int  | 0  |  | TODO: Comment   
mNextClearDontApproachListFrame  | int  | 0  |  | TODO: Comment   
mNodeProximityCheckCorrectionY  | float  | 0  |  | TODO: Comment   
debug_path  | VECTOR_PATHNODE  |  |  | TODO: Comment   
jump_velocity_multiplier  | LensValue<float> |  |  | TODO: Comment 
  *[没有对应音频]: no audio file named Neva-Aave.mp3 was found
  *[1/820]: 0.121%
  *[1/598]: 0.167%
