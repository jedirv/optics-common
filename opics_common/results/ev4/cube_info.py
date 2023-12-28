pvoe                                  = {}
pvoe_op                               = {}
pvoe["object permanence"]             = pvoe_op
pvoe_op["A1"]                         = "novelty_none   movement_linear       move_behind_occluder   implausibly_disappear"
pvoe_op["B1"]                         = "novelty_size   movement_linear       move_behind_occluder   implausibly_disappear"
pvoe_op["C1"]                         = "novelty_shape  movement_linear       move_behind_occluder   implausibly_disappear"
pvoe_op["D1"]                         = "novelty_none   movement_linearDepth  move_behind_occluder   implausibly_disappear"
pvoe_op["E1"]                         = "novelty_size   movement_linearDepth  move_behind_occluder   implausibly_disappear"
pvoe_op["F1"]                         = "novelty_shape  movement_linearDepth  move_behind_occluder   implausibly_disappear"
pvoe_op["G1"]                         = "novelty_none   movement_arced        move_behind_occluder   implausibly_disappear"
pvoe_op["H1"]                         = "novelty_size   movement_arced        move_behind_occluder   implausibly_disappear"
pvoe_op["I1"]                         = "novelty_shape  movement_arced        move_behind_occluder   implausibly_disappear"
pvoe_op["J1"]                         = "novelty_none   movement_linear       move_behind_occluder   plausible"
pvoe_op["K1"]                         = "novelty_size   movement_linear       move_behind_occluder   plausible"
pvoe_op["L1"]                         = "novelty_shape  movement_linear       move_behind_occluder   plausible"
pvoe_op["M1"]                         = "novelty_none   movement_linearDepth  move_behind_occluder   plausible"
pvoe_op["N1"]                         = "novelty_size   movement_linearDepth  move_behind_occluder   plausible"
pvoe_op["O1"]                         = "novelty_shape  movement_linearDepth  move_behind_occluder   plausible"
pvoe_op["P1"]                         = "novelty_none   movement_arced        move_behind_occluder   plausible"
pvoe_op["Q1"]                         = "novelty_size   movement_arced        move_behind_occluder   plausible"
pvoe_op["R1"]                         = "novelty_shape  movement_arced        move_behind_occluder   plausible"

pvoe_op["A2"]                         = "novelty_none   movement_linear       no_occluder   implausibly_appear"
pvoe_op["B2"]                         = "novelty_size   movement_linear       no_occluder   implausibly_appear"
pvoe_op["C2"]                         = "novelty_shape  movement_linear       no_occluder   implausibly_appear"
pvoe_op["D2"]                         = "novelty_none   movement_linearDepth  no_occluder   implausibly_appear"
pvoe_op["E2"]                         = "novelty_size   movement_linearDepth  no_occluder   implausibly_appear"
pvoe_op["F2"]                         = "novelty_shape  movement_linearDepth  no_occluder   implausibly_appear"
pvoe_op["G2"]                         = "novelty_none   movement_arced        no_occluder   implausibly_appear"
pvoe_op["H2"]                         = "novelty_size   movement_arced        no_occluder   implausibly_appear"
pvoe_op["I2"]                         = "novelty_shape  movement_arced        no_occluder   implausibly_appear"
pvoe_op["J2"]                         = "novelty_none   movement_linear       no_occluder   plausible"
pvoe_op["K2"]                         = "novelty_size   movement_linear       no_occluder   plausible"
pvoe_op["L2"]                         = "novelty_shape  movement_linear       no_occluder   plausible"
pvoe_op["M2"]                         = "novelty_none   movement_linearDepth  no_occluder   plausible"
pvoe_op["N2"]                         = "novelty_size   movement_linearDepth  no_occluder   plausible"
pvoe_op["O2"]                         = "novelty_shape  movement_linearDepth  no_occluder   plausible"
pvoe_op["P2"]                         = "novelty_none   movement_arced        no_occluder   plausible"
pvoe_op["Q2"]                         = "novelty_size   movement_arced        no_occluder   plausible"
pvoe_op["R2"]                         = "novelty_shape  movement_arced        no_occluder   plausible"

pvoe_sc                               = {}
pvoe["shape constancy"]               = pvoe_sc
pvoe_sc["A1"]                         = "one_obj          obj_trained_yes   change_in_obj_A_none"
pvoe_sc["B1"]                         = "one_obj          obj_trained_no    change_in_obj_A_none"
pvoe_sc["E1"]                         = "one_obj          obj_trained_yes   change_in_obj_A_to_trained"
pvoe_sc["F1"]                         = "one_obj          obj_trained_no    change_in_obj_A_to_trained"
pvoe_sc["I1"]                         = "one_obj          obj_trained_yes   change_in_obj_A_to_untrained"
pvoe_sc["J1"]                         = "one_obj          obj_trained_no    change_in_obj_A_to_untrained"

pvoe_sc["A2"]                         = "obj_A_trained    obj_B_trained     change_in_obj_A_none           change_in_obj_B_none"
pvoe_sc["B2"]                         = "obj_A_untrained  obj_B_trained     change_in_obj_A_none           change_in_obj_B_none"
pvoe_sc["E2"]                         = "obj_A_trained    obj_B_trained     change_in_obj_A_to_trained     change_in_obj_B_none"
pvoe_sc["F2"]                         = "obj_A_untrained  obj_B_trained     change_in_obj_A_to_trained     change_in_obj_B_none"
pvoe_sc["I2"]                         = "obj_A_trained    obj_B_trained     change_in_obj_A_to_untrained   change_in_obj_B_none"
pvoe_sc["J2"]                         = "obj_A_untrained  obj_B_trained     change_in_obj_A_to_untrained   change_in_obj_B_none"

pvoe_sc["C2"]                         = "obj_A_trained    obj_B_untrained   change_in_obj_A_none           change_in_obj_B_none"
pvoe_sc["D2"]                         = "obj_A_untrained  obj_B_untrained   change_in_obj_A_none           change_in_obj_B_none"
pvoe_sc["G2"]                         = "obj_A_trained    obj_B_untrained   change_in_obj_A_to_trained     change_in_obj_B_none"
pvoe_sc["H2"]                         = "obj_A_untrained  obj_B_untrained   change_in_obj_A_to_trained     change_in_obj_B_none"
pvoe_sc["K2"]                         = "obj_A_trained    obj_B_untrained   change_in_obj_A_to_untrained   change_in_obj_B_none"
pvoe_sc["L2"]                         = "obj_A_untrained  obj_B_untrained   change_in_obj_A_to_untrained   change_in_obj_B_none"


pvoe_sc["A3"]                         = "obj_A_trained    obj_B_trained     change_in_obj_A_none           obj_B_changes_to_trained_shape"
pvoe_sc["B3"]                         = "obj_A_untrained  obj_B_trained     change_in_obj_A_none           obj_B_changes_to_trained_shape"
pvoe_sc["E3"]                         = "obj_A_trained    obj_B_trained     change_in_obj_A_to_trained     obj_B_changes_to_trained_shape"
pvoe_sc["F3"]                         = "obj_A_untrained  obj_B_trained     change_in_obj_A_to_trained     obj_B_changes_to_trained_shape"
pvoe_sc["I3"]                         = "obj_A_trained    obj_B_trained     change_in_obj_A_to_untrained   obj_B_changes_to_trained_shape"
pvoe_sc["J3"]                         = "obj_A_untrained  obj_B_trained     change_in_obj_A_to_untrained   obj_B_changes_to_trained_shape"

pvoe_sc["C3"]                         = "obj_A_trained    obj_B_untrained   change_in_obj_A_none           obj_B_changes_to_trained_shape"
pvoe_sc["D3"]                         = "obj_A_untrained  obj_B_untrained   change_in_obj_A_none           obj_B_changes_to_trained_shape"
pvoe_sc["G3"]                         = "obj_A_trained    obj_B_untrained   change_in_obj_A_to_trained     obj_B_changes_to_trained_shape"
pvoe_sc["H3"]                         = "obj_A_untrained  obj_B_untrained   change_in_obj_A_to_trained     obj_B_changes_to_trained_shape"
pvoe_sc["K3"]                         = "obj_A_trained    obj_B_untrained   change_in_obj_A_to_untrained   obj_B_changes_to_trained_shape"
pvoe_sc["L3"]                         = "obj_A_untrained  obj_B_untrained   change_in_obj_A_to_untrained   obj_B_changes_to_trained_shape"

pvoe_sc["A4"]                         = "obj_A_trained    obj_B_trained     change_in_obj_A_none           obj_B_changes_to_untrained_shape"
pvoe_sc["B4"]                         = "obj_A_untrained  obj_B_trained     change_in_obj_A_none           obj_B_changes_to_untrained_shape"
pvoe_sc["E4"]                         = "obj_A_trained    obj_B_trained     change_in_obj_A_to_trained     obj_B_changes_to_untrained_shape"
pvoe_sc["F4"]                         = "obj_A_untrained  obj_B_trained     change_in_obj_A_to_trained     obj_B_changes_to_untrained_shape"
pvoe_sc["I4"]                         = "obj_A_trained    obj_B_trained     change_in_obj_A_to_untrained   obj_B_changes_to_untrained_shape"
pvoe_sc["J4"]                         = "obj_A_untrained  obj_B_trained     change_in_obj_A_to_untrained   obj_B_changes_to_untrained_shape"

pvoe_sc["C4"]                         = "obj_A_trained    obj_B_untrained   change_in_obj_A_none           obj_B_changes_to_untrained_shape"
pvoe_sc["D4"]                         = "obj_A_untrained  obj_B_untrained   change_in_obj_A_none           obj_B_changes_to_untrained_shape"
pvoe_sc["G4"]                         = "obj_A_trained    obj_B_untrained   change_in_obj_A_to_trained     obj_B_changes_to_untrained_shape"
pvoe_sc["H4"]                         = "obj_A_untrained  obj_B_untrained   change_in_obj_A_to_trained     obj_B_changes_to_untrained_shape"
pvoe_sc["K4"]                         = "obj_A_trained    obj_B_untrained   change_in_obj_A_to_untrained   obj_B_changes_to_untrained_shape"
pvoe_sc["L4"]                         = "obj_A_untrained  obj_B_untrained   change_in_obj_A_to_untrained   obj_B_changes_to_untrained_shape"


pvoe_stc                              = {}
pvoe["spatio temporal continuity"]    = pvoe_stc
pvoe_stc["A1"]                        = "obj_trained    2_occluders   no_movement_in_depth       plausible"
pvoe_stc["B1"]                        = "obj_untrained  2_occluders   no_movement_in_depth       plausible"
pvoe_stc["E1"]                        = "obj_trained    0_occluders   no_movement_in_depth       plausible"
pvoe_stc["F1"]                        = "obj_untrained  0_occluders   no_movement_in_depth       plausible"
pvoe_stc["C1"]                        = "obj_trained    2_occluders   no_movement_in_depth       implausible"
pvoe_stc["D1"]                        = "obj_untrained  2_occluders   no_movement_in_depth       implausible"
pvoe_stc["G1"]                        = "obj_trained    0_occluders   no_movement_in_depth       implausible"
pvoe_stc["H1"]                        = "obj_untrained  0_occluders   no_movement_in_depth       implausible"

pvoe_stc["A2"]                        = "obj_trained    2_occluders   linear_movement_in_depth   plausible"
pvoe_stc["B2"]                        = "obj_untrained  2_occluders   linear_movement_in_depth   plausible"
pvoe_stc["E2"]                        = "obj_trained    0_occluders   linear_movement_in_depth   plausible"
pvoe_stc["F2"]                        = "obj_untrained  0_occluders   linear_movement_in_depth   plausible"
pvoe_stc["C2"]                        = "obj_trained    2_occluders   linear_movement_in_depth   implausible"
pvoe_stc["D2"]                        = "obj_untrained  2_occluders   linear_movement_in_depth   implausible"
pvoe_stc["G2"]                        = "obj_trained    0_occluders   linear_movement_in_depth   implausible"
pvoe_stc["H2"]                        = "obj_untrained  0_occluders   linear_movement_in_depth   implausible"

pvoe_stc["A3"]                        = "obj_trained    2_occluders   toss_arc                   plausible"
pvoe_stc["B3"]                        = "obj_untrained  2_occluders   toss_arc                   plausible"
pvoe_stc["E3"]                        = "obj_trained    0_occluders   toss_arc                   plausible"
pvoe_stc["F3"]                        = "obj_untrained  0_occluders   toss_arc                   plausible"
pvoe_stc["C3"]                        = "obj_trained    2_occluders   toss_arc                   implausible"
pvoe_stc["D3"]                        = "obj_untrained  2_occluders   toss_arc                   implausible"
pvoe_stc["G3"]                        = "obj_trained    0_occluders   toss_arc                   implausible"
pvoe_stc["H3"]                        = "obj_untrained  0_occluders   toss_arc                   implausible"

pvoe_grav                             = {}
pvoe["gravity support"]               = pvoe_grav
pvoe_grav["A1"]                       = "symm                     support_0pc     plausible"
pvoe_grav["I1"]                       = "symm                     support_25pc    plausible"
pvoe_grav["EE1"]                      = "symm                     support_49pc    plausible"
pvoe_grav["AA1"]                      = "symm                     support_75pc    plausible"
pvoe_grav["M1"]                       = "symm                     support_100pc   plausible"

pvoe_grav["B1"]                       = "heavy_side_unsupported   support_0pc     plausible"
pvoe_grav["J1"]                       = "heavy_side_unsupported   support_25pc    plausible"
pvoe_grav["FF1"]                      = "heavy_side_unsupported   support_49pc    plausible"
pvoe_grav["BB1"]                      = "heavy_side_unsupported   support_75pc    plausible"
pvoe_grav["N1"]                       = "heavy_side_unsupported   support_100pc   plausible"

pvoe_grav["Y1"]                       = "heavy_side_supported     support_0pc     plausible"
pvoe_grav["W1"]                       = "heavy_side_supported     support_25pc    plausible"
pvoe_grav["UU1"]                      = "heavy_side_supported     support_49pc    plausible"
pvoe_grav["SS1"]                      = "heavy_side_supported     support_75pc    plausible"
pvoe_grav["S1"]                       = "heavy_side_supported     support_100pc   plausible"


pvoe_grav["C1"]                       = "symm                     support_0pc     implausible"
pvoe_grav["K1"]                       = "symm                     support_25pc    implausible"
pvoe_grav["GG1"]                      = "symm                     support_49pc    implausible"
pvoe_grav["CC1"]                      = "symm                     support_75pc    implausible"
pvoe_grav["O1"]                       = "symm                     support_100pc   implausible"

pvoe_grav["D1"]                       = "heavy_side_unsupported   support_0pc     implausible"
pvoe_grav["L1"]                       = "heavy_side_unsupported   support_25pc    implausible"
pvoe_grav["HH1"]                      = "heavy_side_unsupported   support_49pc    implausible"
pvoe_grav["DD1"]                      = "heavy_side_unsupported   support_75pc    implausible"
pvoe_grav["P1"]                       = "heavy_side_unsupported   support_100pc   implausible"

pvoe_grav["Z1"]                       = "heavy_side_supported     support_0pc     implausible"
pvoe_grav["X1"]                       = "heavy_side_supported     support_25pc    implausible"
pvoe_grav["VV1"]                      = "heavy_side_supported     support_49pc    implausible"
pvoe_grav["TT1"]                      = "heavy_side_supported     support_75pc    implausible"
pvoe_grav["T1"]                       = "heavy_side_supported     support_100pc   implausible"


pvoe_coll                             = {}
pvoe["collisions"]                    = pvoe_coll
pvoe_coll["A1"]                       = "objects_trained     obj_A_moves_offscreen   occluder_raises_to_reveal_empty_stage"
pvoe_coll["B1"]                       = "objects_trained     obj_A_moves_offscreen   occluder_raises_to_reveal_obj_B_on_path"
pvoe_coll["C1"]                       = "objects_trained     obj_A_moves_offscreen   occluder_raises_to_reveal_obj_B_behind_path"

pvoe_coll["G1"]                       = "objects_trained     obj_B_moves_offscreen   occluder_raises_to_reveal_empty_stage"
pvoe_coll["H1"]                       = "objects_trained     obj_B_moves_offscreen   occluder_raises_to_reveal_obj_B_on_path"
pvoe_coll["I1"]                       = "objects_trained     obj_B_moves_offscreen   occluder_raises_to_reveal_obj_B_behind_path"

pvoe_coll["D1"]                       = "objects_untrained   obj_A_moves_offscreen   occluder_raises_to_reveal_empty_stage"
pvoe_coll["E1"]                       = "objects_untrained   obj_A_moves_offscreen   occluder_raises_to_reveal_obj_B_on_path"
pvoe_coll["F1"]                       = "objects_untrained   obj_A_moves_offscreen   occluder_raises_to_reveal_obj_B_behind_path"

pvoe_coll["J1"]                       = "objects_untrained   obj_B_moves_offscreen   occluder_raises_to_reveal_empty_stage"
pvoe_coll["K1"]                       = "objects_untrained   obj_B_moves_offscreen   occluder_raises_to_reveal_obj_B_on_path"
pvoe_coll["L1"]                       = "objects_untrained   obj_B_moves_offscreen   occluder_raises_to_reveal_obj_B_behind_path"


pvoe_coll["A2"]                       = "objects_trained     obj_A_moves_offscreen   start_of_scene_empty_stage"
pvoe_coll["B2"]                       = "objects_trained     obj_A_moves_offscreen   start_of_scene_obj_B_on_path"
pvoe_coll["C2"]                       = "objects_trained     obj_A_moves_offscreen   start_of_scene_obj_B_behind_path"

pvoe_coll["G2"]                       = "objects_trained     obj_B_moves_offscreen   start_of_scene_empty_stage"
pvoe_coll["H2"]                       = "objects_trained     obj_B_moves_offscreen   start_of_scene_obj_B_on_path"
pvoe_coll["I2"]                       = "objects_trained     obj_B_moves_offscreen   start_of_scene_obj_B_behind_path"

pvoe_coll["D2"]                       = "objects_untrained   obj_A_moves_offscreen   start_of_scene_empty_stage"
pvoe_coll["E2"]                       = "objects_untrained   obj_A_moves_offscreen   start_of_scene_obj_B_on_path"
pvoe_coll["F2"]                       = "objects_untrained   obj_A_moves_offscreen   start_of_scene_obj_B_behind_path"

pvoe_coll["J2"]                       = "objects_untrained   obj_B_moves_offscreen   start_of_scene_empty_stage"
pvoe_coll["K2"]                       = "objects_untrained   obj_B_moves_offscreen   start_of_scene_obj_B_on_path"
pvoe_coll["L2"]                       = "objects_untrained   obj_B_moves_offscreen   start_of_scene_obj_B_behind_path"


ir                                    = {}
ir_container                          = {}
ir["container"]                       = ir_container
ir_container["A1"]                    = "3_containers  container_familiar   target_in_container"
ir_container["A2"]                    = "3_containers  container_novel      target_in_container"
ir_container["G1"]                    = "2_containers  container_familiar   target_in_container"
ir_container["G2"]                    = "2_containers  container_novel      target_in_container"
ir_container["M1"]                    = "1_containers  container_familiar   target_in_container"
ir_container["M2"]                    = "1_containers  container_novel      target_in_container"

ir_container["D1"]                    = "3_containers  container_familiar   target_outside_container"
ir_container["D2"]                    = "3_containers  container_novel      target_outside_container"
ir_container["J1"]                    = "2_containers  container_familiar   target_outside_container"
ir_container["J2"]                    = "2_containers  container_novel      target_outside_container"
ir_container["P1"]                    = "1_containers  container_familiar   target_outside_container"
ir_container["P2"]                    = "1_containers  container_novel      target_outside_container"

ir_obstacle                           = {}
ir["obstacle"]                        = ir_obstacle
ir_obstacle["A1"]                     = "target_behind_robot      obstacle_between_robot_and_target       obstacle_familiar"
ir_obstacle["B1"]                     = "target_behind_robot      obstacle_not_between_robot_and_target   obstacle_familiar"
ir_obstacle["C1"]                     = "target_not_behind_robot  obstacle_between_robot_and_target       obstacle_familiar"
ir_obstacle["D1"]                     = "target_not_behind_robot  obstacle_not_between_robot_and_target   obstacle_familiar"

ir_obstacle["A2"]                     = "target_behind_robot      obstacle_between_robot_and_target       obstacle_novel_from_familiar_category"
ir_obstacle["B2"]                     = "target_behind_robot      obstacle_not_between_robot_and_target   obstacle_novel_from_familiar_category"
ir_obstacle["C2"]                     = "target_not_behind_robot  obstacle_between_robot_and_target       obstacle_novel_from_familiar_category"
ir_obstacle["D2"]                     = "target_not_behind_robot  obstacle_not_between_robot_and_target   obstacle_novel_from_familiar_category"

ir_occlusion                          = {}
ir["occluder"]                        = ir_occlusion
ir_occlusion["A1"]                    = "target_behind_robot       target_hidden_by_occluder_on_frame_1        3_objects_that_could_occlude_target   occluder_familiar"
ir_occlusion["B1"]                    = "target_behind_robot       target_not_hidden_by_occluder_on_frame_1    3_objects_that_could_occlude_target   occluder_familiar"
ir_occlusion["C1"]                    = "target_not_behind_robot   target_hidden_by_occluder_on_frame_1        3_objects_that_could_occlude_target   occluder_familiar"
ir_occlusion["D1"]                    = "target_not_behind_robot   target_not_hidden_by_occluder_on_frame_1    3_objects_that_could_occlude_target   occluder_familiar"

ir_occlusion["E1"]                    = "target_behind_robot       target_hidden_by_occluder_on_frame_1        2_objects_that_could_occlude_target   occluder_familiar"
ir_occlusion["F1"]                    = "target_behind_robot       target_not_hidden_by_occluder_on_frame_1    2_objects_that_could_occlude_target   occluder_familiar"
ir_occlusion["G1"]                    = "target_not_behind_robot   target_hidden_by_occluder_on_frame_1        2_objects_that_could_occlude_target   occluder_familiar"
ir_occlusion["H1"]                    = "target_not_behind_robot   target_not_hidden_by_occluder_on_frame_1    2_objects_that_could_occlude_target   occluder_familiar"

ir_occlusion["I1"]                    = "target_behind_robot       target_hidden_by_occluder_on_frame_1        1_objects_that_could_occlude_target   occluder_familiar"
ir_occlusion["J1"]                    = "target_behind_robot       target_not_hidden_by_occluder_on_frame_1    1_objects_that_could_occlude_target   occluder_familiar"
ir_occlusion["K1"]                    = "target_not_behind_robot   target_hidden_by_occluder_on_frame_1        1_objects_that_could_occlude_target   occluder_familiar"
ir_occlusion["L1"]                    = "target_not_behind_robot   target_not_hidden_by_occluder_on_frame_1    1_objects_that_could_occlude_target   occluder_familiar"


ir_occlusion["A2"]                    = "target_behind_robot       target_hidden_by_occluder_on_frame_1        3_objects_that_could_occlude_target   occluder_novel"
ir_occlusion["B2"]                    = "target_behind_robot       target_not_hidden_by_occluder_on_frame_1    3_objects_that_could_occlude_target   occluder_novel"
ir_occlusion["C2"]                    = "target_not_behind_robot   target_hidden_by_occluder_on_frame_1        3_objects_that_could_occlude_target   occluder_novel"
ir_occlusion["D2"]                    = "target_not_behind_robot   target_not_hidden_by_occluder_on_frame_1    3_objects_that_could_occlude_target   occluder_novel"

ir_occlusion["E2"]                    = "target_behind_robot       target_hidden_by_occluder_on_frame_1        2_objects_that_could_occlude_target   occluder_novel"
ir_occlusion["F2"]                    = "target_behind_robot       target_not_hidden_by_occluder_on_frame_1    2_objects_that_could_occlude_target   occluder_novel"
ir_occlusion["G2"]                    = "target_not_behind_robot   target_hidden_by_occluder_on_frame_1        2_objects_that_could_occlude_target   occluder_novel"
ir_occlusion["H2"]                    = "target_not_behind_robot   target_not_hidden_by_occluder_on_frame_1    2_objects_that_could_occlude_target   occluder_novel"

ir_occlusion["I2"]                    = "target_behind_robot       target_hidden_by_occluder_on_frame_1        1_objects_that_could_occlude_target   occluder_novel"
ir_occlusion["J2"]                    = "target_behind_robot       target_not_hidden_by_occluder_on_frame_1    1_objects_that_could_occlude_target   occluder_novel"
ir_occlusion["K2"]                    = "target_not_behind_robot   target_hidden_by_occluder_on_frame_1        1_objects_that_could_occlude_target   occluder_novel"
ir_occlusion["L2"]                    = "target_not_behind_robot   target_not_hidden_by_occluder_on_frame_1    1_objects_that_could_occlude_target   occluder_novel"

ir_obj_perm                           = {}
ir["interactive object permanence"]   = ir_obj_perm
ir_obj_perm["A1"]                     = "ai_not_frozen   opposite_side_toss    target_occluded"
ir_obj_perm["B1"]                     = "ai_frozen       opposite_side_toss    target_occluded"
ir_obj_perm["A2"]                     = "ai_not_frozen   opposite_side_toss    target_not_occluded"
ir_obj_perm["B2"]                     = "ai_frozen       opposite_side_toss    target_not_occluded"

ir_obj_perm["C1"]                     = "ai_not_frozen   same_side_drop        target_occluded"
ir_obj_perm["D1"]                     = "ai_frozen       same_side_drop        target_occluded"
ir_obj_perm["C2"]                     = "ai_not_frozen   same_side_drop        target_not_occluded"
ir_obj_perm["D2"]                     = "ai_frozen       same_side_drop        target_not_occluded"

ir_reorient                           = {}
ir["reorientation"]                   = ir_reorient
ir_reorient["A1"]                     = "prior_experience_explore   rotation_90    wall_colored"
ir_reorient["B1"]                     = "prior_experience_explore   rotation_180   wall_colored"
ir_reorient["C1"]                     = "prior_experience_explore   rotation_270   wall_colored"
ir_reorient["D1"]                     = "prior_experience_explore   rotation_360   wall_colored"
ir_reorient["I1"]                     = "prior_experience_visual    rotation_90    wall_colored"
ir_reorient["J1"]                     = "prior_experience_visual    rotation_180   wall_colored"
ir_reorient["K1"]                     = "prior_experience_visual    rotation_270   wall_colored"
ir_reorient["L1"]                     = "prior_experience_visual    rotation_360   wall_colored"

ir_reorient["E1"]                     = "prior_experience_explore   rotation_90    wall_not_colored"
ir_reorient["F1"]                     = "prior_experience_explore   rotation_180   wall_not_colored"
ir_reorient["G1"]                     = "prior_experience_explore   rotation_270   wall_not_colored"
ir_reorient["H1"]                     = "prior_experience_explore   rotation_360   wall_not_colored"
ir_reorient["M1"]                     = "prior_experience_visual    rotation_90    wall_not_colored"
ir_reorient["N1"]                     = "prior_experience_visual    rotation_180   wall_not_colored"
ir_reorient["O1"]                     = "prior_experience_visual    rotation_270   wall_not_colored"
ir_reorient["P1"]                     = "prior_experience_visual    rotation_360   wall_not_colored"
