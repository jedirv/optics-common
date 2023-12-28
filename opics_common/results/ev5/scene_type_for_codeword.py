import opics_common.scene_type.type_constants as tc

type_for_codeword                                                           = {}
# INTER
type_for_codeword["sierra"]                                                 = tc.ABBREV_AGENT_IDENTIFICATION  # agent_identification
type_for_codeword["oscar"]                                                  = tc.ABBREV_CONTAINERS  # container
type_for_codeword["uniform"]                                                = tc.ABBREV_HOLES  #
type_for_codeword["romeo"]                                                  = tc.ABBREV_INTERACTIVE_OBJECT_PERMENANCE  # interactive_object_permenance
type_for_codeword["victor"]                                                 = tc.ABBREV_LAVA  #
type_for_codeword["tango"]                                                  = tc.ABBREV_MOVING_TARGET  # moving target
type_for_codeword["papa"]                                                   = tc.ABBREV_OBSTACLES  # obstacle
type_for_codeword["quebec"]                                                 = tc.ABBREV_OCCLUDERS  # occluders
type_for_codeword["whiskey"]                                                = tc.ABBREV_RAMP  #
type_for_codeword["xray"]                                                   = tc.ABBREV_SOLIDITY  # solidity
type_for_codeword["yankee"]                                                 = tc.ABBREV_SPATIAL_ELIMINATION  # spatial_elimination
type_for_codeword["zulu"]                                                   = tc.ABBREV_SUPPORT_RELATIONS  # support_relations
type_for_codeword["omega"]                                                  = tc.ABBREV_TOOL  #

# AVOE
type_for_codeword["india"]                                                  = tc.ABBREV_INEFFICIENT_ACTION_IRRATIONAL  # efficient_action_irrational
type_for_codeword["juliett"]                                                = tc.ABBREV_INEFFICIENT_ACTION_PATH  # efficient_action_path
type_for_codeword["kilo"]                                                   = tc.ABBREV_INEFFICIENT_ACTION_TIME  # efficient_action_time
type_for_codeword["lima"]                                                   = tc.ABBREV_INACCESSIBLE_GOAL  # inaccessible_goal
type_for_codeword["foxtrot"]                                                = tc.ABBREV_INSTRUMENTAL_ACTION_BLOCKING_BARRIERS # instrumental_action_blocking_barriers
type_for_codeword["golf"]                                                   = tc.ABBREV_INSTRUMENTAL_ACTION_INCONSEQUENTIAL_BARRIERS # instrumental_action_inconsequential_barriers
type_for_codeword["hotel"]                                                  = tc.ABBREV_INSTRUMENTAL_ACTION_NO_BARRIERS # instrumental_action_no_barriers
type_for_codeword["mike"]                                                   = tc.ABBREV_MULTIPLE_AGENTS  # multiple_agents
type_for_codeword["november"]                                               = tc.ABBREV_OBJECT_PREFERENCE  # object_preference

# PVOE
type_for_codeword["alpha"]                                                  = tc.ABBREV_COLLISION  # collision
type_for_codeword["bravo"]                                                  = tc.ABBREV_GRAVITY  # gravity
type_for_codeword["charlie"]                                                = tc.ABBREV_OBJECT_PERMANENCE  # object_permenance
type_for_codeword["delta"]                                                  = tc.ABBREV_SHAPE_CONSTANCY  # shape_constancy
type_for_codeword["echo"]                                                   = tc.ABBREV_SPATIO_TEMPORAL_CONTINUITY  # spartio_temporal_continuity

#####################################################################################

codeword_for_type                                                           = {}
# INTER
codeword_for_type[tc.ABBREV_AGENT_IDENTIFICATION]                           = "sierra"  # agent_identification
codeword_for_type[tc.ABBREV_CONTAINERS]                                     = "oscar"  # container
codeword_for_type[tc.ABBREV_HOLES]                                          = "uniform"  #
codeword_for_type[tc.ABBREV_INTERACTIVE_OBJECT_PERMENANCE]                  = "romeo"  # interactive_object_permenance
codeword_for_type[tc.ABBREV_LAVA]                                           = "victor"  #
codeword_for_type[tc.ABBREV_MOVING_TARGET]                                  = "tango"  # moving target
codeword_for_type[tc.ABBREV_OBSTACLES]                                      = "papa"  # obstacle
codeword_for_type[tc.ABBREV_OCCLUDERS]                                      = "quebec"  # occluders
codeword_for_type[tc.ABBREV_RAMP]                                           = "whiskey"  #
codeword_for_type[tc.ABBREV_SOLIDITY]                                       = "xray"  # solidity
codeword_for_type[tc.ABBREV_SPATIAL_ELIMINATION]                            = "yankee"  # spatial_elimination
codeword_for_type[tc.ABBREV_SUPPORT_RELATIONS]                              = "zulu"  # support_relations
codeword_for_type[tc.ABBREV_TOOL]                                           = "omega"  #

# AVOE
codeword_for_type[tc.ABBREV_INEFFICIENT_ACTION_IRRATIONAL]                  = "india"  # efficient_action_irrational
codeword_for_type[tc.ABBREV_INEFFICIENT_ACTION_PATH]                        = "juliett"  # efficient_action_path
codeword_for_type[tc.ABBREV_INEFFICIENT_ACTION_TIME]                        = "kilo"  # efficient_action_time
codeword_for_type[tc.ABBREV_INACCESSIBLE_GOAL]                              = "lima"  # inaccessible_goal
codeword_for_type[tc.ABBREV_INSTRUMENTAL_ACTION_BLOCKING_BARRIERS]          = "foxtrot"  # instrumental_action_blocking_barriers
codeword_for_type[tc.ABBREV_INSTRUMENTAL_ACTION_INCONSEQUENTIAL_BARRIERS]   = "golf"  # instrumental_action_inconsequential_barriers
codeword_for_type[tc.ABBREV_INSTRUMENTAL_ACTION_NO_BARRIERS]                = "hotel"  # instrumental_action_no_barriers
codeword_for_type[tc.ABBREV_MULTIPLE_AGENTS]                                = "mike"  # multiple_agents
codeword_for_type[tc.ABBREV_OBJECT_PREFERENCE]                              = "november"  # object_preference

# PVOE
codeword_for_type[tc.ABBREV_COLLISION]                                      = "alpha"  # collision
codeword_for_type[tc.ABBREV_GRAVITY]                                        = "bravo"  # gravity
codeword_for_type[tc.ABBREV_OBJECT_PERMANENCE]                              = "charlie"  # object_permenance
codeword_for_type[tc.ABBREV_SHAPE_CONSTANCY]                                = "delta"  # shape_constancy
codeword_for_type[tc.ABBREV_SPATIO_TEMPORAL_CONTINUITY]                     = "echo"  # spartio_temporal_continuity
