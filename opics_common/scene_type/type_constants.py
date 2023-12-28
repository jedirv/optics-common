# PVOE
ABBREV_COLLISION                                      = "coll"
ABBREV_OBJECT_PERMANENCE                              = "op"
ABBREV_SPATIO_TEMPORAL_CONTINUITY                     = "stc"
ABBREV_SHAPE_CONSTANCY                                = "sc"
ABBREV_GRAVITY                                        = "grav"

# AVOE
ABBREV_HELPER_HINDERER                                = "helphind"
ABBREV_TRUE_BELIEF                                    = "tbelief"
ABBREV_FALSE_BELIEF                                   = "fbelief"
ABBREV_INACCESSIBLE_GOAL                              = "igoal"
ABBREV_INSTRUMENTAL_ACTION_BLOCKING_BARRIERS          = "blockb"
ABBREV_INSTRUMENTAL_ACTION_INCONSEQUENTIAL_BARRIERS   = "inconsb"
ABBREV_INSTRUMENTAL_ACTION_NO_BARRIERS                = "nobarr"
ABBREV_INEFFICIENT_ACTION_IRRATIONAL                  = "irrat"
ABBREV_INEFFICIENT_ACTION_PATH                        = "path"
ABBREV_INEFFICIENT_ACTION_TIME                        = "time"
ABBREV_MULTIPLE_AGENTS                                = "multa"
ABBREV_OBJECT_PREFERENCE                              = "opref"
# agent/non_agent eval6
# ABBREV_AGENT_ONE_GOAL                                 = "agoal"
# ABBREV_AGENT_PREFERENCE                               = "apref"
# ABBREV_COLLECT                                        = "acol"
# ABBREV_NON_AGENT_ONE_GOAL                             = "ngoal"
# ABBREV_NON_AGENT_PREFERENCE                           = "npref"
ABBREV_AGENT_NON_AGENT                                = "anona"
# social eval6
#ABBREV_INSTRUMENTAL_APPROACH                          = "instrapp"
#ABBREV_INSTRUMENTAL_IMITATION                         = "instrim"
ABBREV_SOCIAL_APPROACH                                = "socapp"
ABBREV_SOCIAL_IMITATION                               = "socimit"

# INTER
ABBREV_HIDDEN_SET_ROTATION                            = "hsetrot"
ABBREV_KNOWLEDGEABLE_AGENTS                           = "kagents"
ABBREV_MULTI_TOOL                                     = "mtool"
ABBREV_AGENT_IDENTIFICATION                           = "agentid"
ABBREV_CONTAINERS                                     = "cont"
ABBREV_LAVA                                           = "lava"
ABBREV_HOLES                                          = "holes"
ABBREV_MOVING_TARGET                                  = "movtarg"
ABBREV_OBSTACLES                                      = "obst"
ABBREV_OCCLUDERS                                      = "occl"
ABBREV_RAMP                                           = "ramps"
ABBREV_SOLIDITY                                       = "solid"
ABBREV_SPATIAL_ELIMINATION                            = "spelim"
ABBREV_SUPPORT_RELATIONS                              = "suprel"
ABBREV_TOOL                                           = "tool"
ABBREV_INTERACTIVE_OBJECT_PERMENANCE                  = "iop"

ABBREV_ARITHMETIC                                     = "math"
ABBREV_NUMBER_COMPARISON                              = "numcomp"
ABBREV_IMITATION                                      = "imit"
ABBREV_SET_ROTATION                                   = "setrot"
ABBREV_SPATIAL_REFERENCE                              = "spatref"
ABBREV_REORIENT                                       = "reor"
ABBREV_TOOL_CHOICE                                    = "tlch"
ABBREV_ASYMMETRIC_TOOL                                = "tlas"
ABBREV_HIDDEN_TRAJECTORY                              = "hidtraj"
ABBREV_COLLISION_TRAJECTORY                           = "coltraj"
ABBREV_SEEING_LEADS_TO_KNOWING                        = "sltk"
ABBREV_SHELL_GAME                                     = "shell"

abbrev_types = {}
abbrev_types["pvoe"] = []
abbrev_types["pvoe"].append(ABBREV_COLLISION)
abbrev_types["pvoe"].append(ABBREV_OBJECT_PERMANENCE)
abbrev_types["pvoe"].append(ABBREV_SPATIO_TEMPORAL_CONTINUITY)
abbrev_types["pvoe"].append(ABBREV_SHAPE_CONSTANCY)
abbrev_types["pvoe"].append(ABBREV_GRAVITY)

abbrev_types["inter"] = []
abbrev_types["inter"].append(ABBREV_AGENT_IDENTIFICATION)
abbrev_types["inter"].append(ABBREV_CONTAINERS)
abbrev_types["inter"].append(ABBREV_LAVA)
abbrev_types["inter"].append(ABBREV_HOLES)
abbrev_types["inter"].append(ABBREV_MOVING_TARGET)
abbrev_types["inter"].append(ABBREV_INTERACTIVE_OBJECT_PERMENANCE)
abbrev_types["inter"].append(ABBREV_OBSTACLES)
abbrev_types["inter"].append(ABBREV_OCCLUDERS)
abbrev_types["inter"].append(ABBREV_RAMP)
abbrev_types["inter"].append(ABBREV_SOLIDITY)
abbrev_types["inter"].append(ABBREV_SPATIAL_ELIMINATION)
abbrev_types["inter"].append(ABBREV_SUPPORT_RELATIONS)
abbrev_types["inter"].append(ABBREV_TOOL)

abbrev_types["inter"].append(ABBREV_ARITHMETIC)
abbrev_types["inter"].append(ABBREV_NUMBER_COMPARISON)
abbrev_types["inter"].append(ABBREV_IMITATION)
abbrev_types["inter"].append(ABBREV_SET_ROTATION)
abbrev_types["inter"].append(ABBREV_SPATIAL_REFERENCE)
abbrev_types["inter"].append(ABBREV_REORIENT)
abbrev_types["inter"].append(ABBREV_TOOL_CHOICE)
abbrev_types["inter"].append(ABBREV_ASYMMETRIC_TOOL)
abbrev_types["inter"].append(ABBREV_HIDDEN_TRAJECTORY)
abbrev_types["inter"].append(ABBREV_COLLISION_TRAJECTORY)
abbrev_types["inter"].append(ABBREV_SEEING_LEADS_TO_KNOWING)
abbrev_types["inter"].append(ABBREV_SHELL_GAME)
abbrev_types["inter"].append(ABBREV_HIDDEN_SET_ROTATION)
abbrev_types["inter"].append(ABBREV_KNOWLEDGEABLE_AGENTS)
abbrev_types["inter"].append(ABBREV_MULTI_TOOL)


abbrev_types["avoe"] = []
# abbrev_types['avoe'].append(ABBREV_INACCESSIBLE_GOAL)
# abbrev_types['avoe'].append(ABBREV_INSTRUMENTAL_ACTION_BLOCKING_BARRIERS)
# abbrev_types['avoe'].append(ABBREV_INSTRUMENTAL_ACTION_INCONSEQUENTIAL_BARRIERS)
# abbrev_types['avoe'].append(ABBREV_INSTRUMENTAL_ACTION_NO_BARRIERS)
abbrev_types["avoe"].append(ABBREV_INEFFICIENT_ACTION_IRRATIONAL)
# abbrev_types['avoe'].append(ABBREV_INEFFICIENT_ACTION_PATH)
# abbrev_types['avoe'].append(ABBREV_INEFFICIENT_ACTION_TIME)
abbrev_types["avoe"].append(ABBREV_MULTIPLE_AGENTS)
abbrev_types["avoe"].append(ABBREV_OBJECT_PREFERENCE)
# abbrev_types["avoe"].append(ABBREV_AGENT_ONE_GOAL)
# abbrev_types["avoe"].append(ABBREV_AGENT_PREFERENCE)
# abbrev_types["avoe"].append(ABBREV_COLLECT)
# abbrev_types["avoe"].append(ABBREV_NON_AGENT_ONE_GOAL)
# abbrev_types["avoe"].append(ABBREV_NON_AGENT_PREFERENCE)
# abbrev_types["avoe"].append(ABBREV_INSTRUMENTAL_APPROACH)
# abbrev_types["avoe"].append(ABBREV_INSTRUMENTAL_IMITATION)
abbrev_types["avoe"].append(ABBREV_SOCIAL_APPROACH)
abbrev_types["avoe"].append(ABBREV_SOCIAL_IMITATION)
abbrev_types["avoe"].append(ABBREV_AGENT_NON_AGENT)
abbrev_types["avoe"].append(ABBREV_HELPER_HINDERER)
abbrev_types["avoe"].append(ABBREV_TRUE_BELIEF)
abbrev_types["avoe"].append(ABBREV_FALSE_BELIEF)


abbrev_project_names                                                = ["pvoe", "inter", "avoe"]

formal_type                                                         = {}
formal_type[ABBREV_COLLISION]                                       = "collision"
formal_type[ABBREV_GRAVITY]                                         = "gravity"
formal_type[ABBREV_OBJECT_PERMANENCE]                               = "passive_object_permanence"
formal_type[ABBREV_SHAPE_CONSTANCY]                                 = "shape_constancy"
formal_type[ABBREV_SPATIO_TEMPORAL_CONTINUITY]                      = "spatio_temporal_continuity"

formal_type[ABBREV_AGENT_IDENTIFICATION]                            = "agent_identification"
formal_type[ABBREV_CONTAINERS]                                      = "containers"
formal_type[ABBREV_LAVA]                                            = "lava"
formal_type[ABBREV_HOLES]                                           = "holes"
formal_type[ABBREV_MOVING_TARGET]                                   = "moving_target_prediction"
formal_type[
    ABBREV_INTERACTIVE_OBJECT_PERMENANCE
]                                                                   = "interactive_object_permanence"
formal_type[ABBREV_OBSTACLES]                                       = "obstacles"
formal_type[ABBREV_OCCLUDERS]                                       = "occluders"
formal_type[ABBREV_RAMP]                                            = "ramps"
formal_type[ABBREV_SOLIDITY]                                        = "solidity"
formal_type[ABBREV_SPATIAL_ELIMINATION]                             = "spatial_elimination"
formal_type[ABBREV_SUPPORT_RELATIONS]                               = "support_relations"
formal_type[ABBREV_TOOL]                                            = "tool_use"

formal_type[ABBREV_ARITHMETIC]                                      = "interactive_arithmetic"
formal_type[ABBREV_NUMBER_COMPARISON]                               = "interactive_number_comparison"
formal_type[ABBREV_IMITATION]                                       = "interactive_imitation"
formal_type[ABBREV_SET_ROTATION]                                    = "interactive_set_rotation"
formal_type[ABBREV_SPATIAL_REFERENCE]                               = "interactive_spatial_reference"
formal_type[ABBREV_REORIENT]                                        = "interactive_spatial_reorientation"
formal_type[ABBREV_TOOL_CHOICE]                                     = "interactive_tool_choice"
formal_type[ABBREV_ASYMMETRIC_TOOL]                                 = "interactive_asymmetric_tool"
formal_type[ABBREV_HIDDEN_TRAJECTORY]                               = "interactive_trajectory"
formal_type[ABBREV_COLLISION_TRAJECTORY]                            = "interactive_collisions"
formal_type[ABBREV_SEEING_LEADS_TO_KNOWING]                         = "passive_seeing_leads_to_knowing"
formal_type[ABBREV_SHELL_GAME]                                      = "interactive_shell_game"

formal_type[ABBREV_INEFFICIENT_ACTION_IRRATIONAL]                   = "efficient_action_irrational"
formal_type[ABBREV_INEFFICIENT_ACTION_PATH]                         = "efficient_action_path"
formal_type[ABBREV_INEFFICIENT_ACTION_TIME]                         = "efficient_action_time"
formal_type[ABBREV_INACCESSIBLE_GOAL]                               = "inaccessible_goal"
formal_type[ABBREV_INSTRUMENTAL_ACTION_BLOCKING_BARRIERS]           = "instrumental_action_blocking_barriers"
formal_type[ABBREV_INSTRUMENTAL_ACTION_INCONSEQUENTIAL_BARRIERS]    = "instrumental_action_inconsequential_barriers"
formal_type[ABBREV_INSTRUMENTAL_ACTION_NO_BARRIERS]                 = "instrumental_action_no_barriers"
formal_type[ABBREV_OBJECT_PREFERENCE]                               = "object_preference"
formal_type[ABBREV_MULTIPLE_AGENTS]                                 = "multiple_agents"

# formal_type[ABBREV_AGENT_ONE_GOAL]                                  = "agent_one_goal"
# formal_type[ABBREV_AGENT_PREFERENCE]                                = "agent_preference"
# formal_type[ABBREV_COLLECT]                                         = "collect"
# formal_type[ABBREV_NON_AGENT_ONE_GOAL]                              = "non_agent_one_goal"
# formal_type[ABBREV_NON_AGENT_PREFERENCE]                            = "non_agent_preference"
# formal_type[ABBREV_INSTRUMENTAL_APPROACH]                           = "instrumental_approach"
# formal_type[ABBREV_INSTRUMENTAL_IMITATION]                          = "instrumental_imitation"
formal_type[ABBREV_SOCIAL_APPROACH]                                 = "social_approach"
formal_type[ABBREV_SOCIAL_IMITATION]                                = "social_imitation"
formal_type[ABBREV_AGENT_NON_AGENT]                                 = "agent_non_agent"
formal_type[ABBREV_HELPER_HINDERER]                                 = "helper_hinderer"
formal_type[ABBREV_TRUE_BELIEF]                                     = "true_belief"
formal_type[ABBREV_FALSE_BELIEF]                                    = "false_belief"
formal_type[ABBREV_HIDDEN_SET_ROTATION]                             = "hidden_set_rotation"
formal_type[ABBREV_KNOWLEDGEABLE_AGENTS]                            = "knowledgeable_agents"
formal_type[ABBREV_MULTI_TOOL]                                      = "multi_tool"
formal_type[""]                                                     = ""


UNKNOWN_SCENE_TYPE_ABBREVIATION   = "unknown_scene_type_abbreviation"
SCENE_TYPE_NOT_RECOGNIZED         = "scene_type_not_recognized"


def get_formal_scene_type_from_filename(name):
    # first see if its an osu named file
    scene_type = get_formal_scene_type_from_osu_scene_filename(name)
    if scene_type != UNKNOWN_SCENE_TYPE_ABBREVIATION:
        return scene_type
    # then see if its a validation scene file
    scene_type = get_formal_scene_type_from_validation_scene_filename(name)
    return scene_type


def get_formal_scene_type_from_osu_scene_filename(name):
    # prefix should be scene type abbreviation
    abbrev = name.split("_")[0]
    if not abbrev in formal_type:
        return UNKNOWN_SCENE_TYPE_ABBREVIATION
    return formal_type[abbrev]


def get_formal_scene_type_from_validation_scene_filename(name):
    # assumes that the names embedded in the validation scene files match the formal type declarations in this file
    # PVOE
    if formal_type[ABBREV_COLLISION] in name:
        return formal_type[ABBREV_COLLISION]
    elif formal_type[ABBREV_OBJECT_PERMANENCE] in name:
        return formal_type[ABBREV_OBJECT_PERMANENCE]
    elif formal_type[ABBREV_SHAPE_CONSTANCY] in name:
        return formal_type[ABBREV_SHAPE_CONSTANCY]
    elif formal_type[ABBREV_SPATIO_TEMPORAL_CONTINUITY] in name:
        return formal_type[ABBREV_SPATIO_TEMPORAL_CONTINUITY]
    elif formal_type[ABBREV_GRAVITY] in name:
        return formal_type[ABBREV_GRAVITY]
    # INTERACTIVE
    elif formal_type[ABBREV_HIDDEN_SET_ROTATION] in name:
        return formal_type[ABBREV_HIDDEN_SET_ROTATION]
    elif formal_type[ABBREV_KNOWLEDGEABLE_AGENTS] in name:
        return formal_type[ABBREV_KNOWLEDGEABLE_AGENTS]
    elif formal_type[ABBREV_MULTI_TOOL] in name:
        return formal_type[ABBREV_MULTI_TOOL]
    elif formal_type[ABBREV_AGENT_IDENTIFICATION] in name:
        return formal_type[ABBREV_AGENT_IDENTIFICATION]
    elif formal_type[ABBREV_CONTAINERS] in name:
        return formal_type[ABBREV_CONTAINERS]
    elif formal_type[ABBREV_LAVA] in name:
        return formal_type[ABBREV_LAVA]
    elif formal_type[ABBREV_HOLES] in name:
        return formal_type[ABBREV_HOLES]
    elif formal_type[ABBREV_MOVING_TARGET] in name:
        return formal_type[ABBREV_MOVING_TARGET]
    elif formal_type[ABBREV_INTERACTIVE_OBJECT_PERMENANCE] in name:
        return formal_type[ABBREV_INTERACTIVE_OBJECT_PERMENANCE]
    elif formal_type[ABBREV_OBSTACLES] in name:
        return formal_type[ABBREV_OBSTACLES]
    elif formal_type[ABBREV_OCCLUDERS] in name:
        return formal_type[ABBREV_OCCLUDERS]
    elif formal_type[ABBREV_RAMP] in name:
        return formal_type[ABBREV_RAMP]
    elif formal_type[ABBREV_SOLIDITY] in name:
        return formal_type[ABBREV_SOLIDITY]
    elif formal_type[ABBREV_SPATIAL_ELIMINATION] in name:
        return formal_type[ABBREV_SPATIAL_ELIMINATION]
    elif formal_type[ABBREV_SUPPORT_RELATIONS] in name:
        return formal_type[ABBREV_SUPPORT_RELATIONS]
    elif formal_type[ABBREV_TOOL] in name:
        return formal_type[ABBREV_TOOL]

    elif formal_type[ABBREV_ARITHMETIC] in name:
        return formal_type[ABBREV_ARITHMETIC]
    elif formal_type[ABBREV_NUMBER_COMPARISON] in name:
        return formal_type[ABBREV_NUMBER_COMPARISON]
    elif formal_type[ABBREV_IMITATION] in name:
        return formal_type[ABBREV_IMITATION]
    elif formal_type[ABBREV_SET_ROTATION] in name:
        return formal_type[ABBREV_SET_ROTATION]
    elif formal_type[ABBREV_SPATIAL_REFERENCE] in name:
        return formal_type[ABBREV_SPATIAL_REFERENCE]
    elif formal_type[ABBREV_REORIENT] in name:
        return formal_type[ABBREV_REORIENT]
    elif formal_type[ABBREV_TOOL_CHOICE] in name:
        return formal_type[ABBREV_TOOL_CHOICE]
    elif formal_type[ABBREV_ASYMMETRIC_TOOL] in name:
        return formal_type[ABBREV_ASYMMETRIC_TOOL]
    elif formal_type[ABBREV_HIDDEN_TRAJECTORY] in name:
        return formal_type[ABBREV_HIDDEN_TRAJECTORY]
    elif formal_type[ABBREV_COLLISION_TRAJECTORY] in name:
        return formal_type[ABBREV_COLLISION_TRAJECTORY]
    elif formal_type[ABBREV_SEEING_LEADS_TO_KNOWING] in name:
        return formal_type[ABBREV_SEEING_LEADS_TO_KNOWING]
    elif formal_type[ABBREV_SHELL_GAME] in name:
        return formal_type[ABBREV_SHELL_GAME]
    # #AVOE
    elif formal_type[ABBREV_HELPER_HINDERER] in name:
        return formal_type[ABBREV_HELPER_HINDERER]
    elif formal_type[ABBREV_TRUE_BELIEF] in name:
        return formal_type[ABBREV_TRUE_BELIEF]
    elif formal_type[ABBREV_FALSE_BELIEF] in name:
        return formal_type[ABBREV_FALSE_BELIEF]
    elif formal_type[ABBREV_INEFFICIENT_ACTION_IRRATIONAL] in name:
        return formal_type[ABBREV_INEFFICIENT_ACTION_IRRATIONAL]
    elif formal_type[ABBREV_INEFFICIENT_ACTION_PATH] in name:
        return formal_type[ABBREV_INEFFICIENT_ACTION_PATH]
    elif formal_type[ABBREV_INEFFICIENT_ACTION_TIME] in name:
        return formal_type[ABBREV_INEFFICIENT_ACTION_TIME]
    elif formal_type[ABBREV_INACCESSIBLE_GOAL] in name:
        return formal_type[ABBREV_INACCESSIBLE_GOAL]
    elif formal_type[ABBREV_INSTRUMENTAL_ACTION_BLOCKING_BARRIERS] in name:
        return formal_type[ABBREV_INSTRUMENTAL_ACTION_BLOCKING_BARRIERS]
    elif (
        formal_type[ABBREV_INSTRUMENTAL_ACTION_INCONSEQUENTIAL_BARRIERS]
        in name
    ):
        return formal_type[ABBREV_INSTRUMENTAL_ACTION_INCONSEQUENTIAL_BARRIERS]
    elif formal_type[ABBREV_INSTRUMENTAL_ACTION_NO_BARRIERS] in name:
        return formal_type[ABBREV_INSTRUMENTAL_ACTION_NO_BARRIERS]
    elif formal_type[ABBREV_OBJECT_PREFERENCE] in name:
        return formal_type[ABBREV_OBJECT_PREFERENCE]
    elif formal_type[ABBREV_MULTIPLE_AGENTS] in name:
        return formal_type[ABBREV_MULTIPLE_AGENTS]
    # elif formal_type[ABBREV_AGENT_ONE_GOAL] in name:
    #     return formal_type[ABBREV_AGENT_ONE_GOAL]
    # elif formal_type[ABBREV_AGENT_PREFERENCE] in name:
    #     return formal_type[ABBREV_AGENT_PREFERENCE]
    # elif formal_type[ABBREV_COLLECT] in name:
    #     return formal_type[ABBREV_COLLECT]
    # elif formal_type[ABBREV_NON_AGENT_ONE_GOAL] in name:
    #     return formal_type[ABBREV_NON_AGENT_ONE_GOAL]
    # elif formal_type[ABBREV_NON_AGENT_PREFERENCE] in name:
    #     return formal_type[ABBREV_NON_AGENT_PREFERENCE]
    # elif formal_type[ABBREV_INSTRUMENTAL_APPROACH] in name:
    #     return formal_type[ABBREV_INSTRUMENTAL_APPROACH]
    # elif formal_type[ABBREV_INSTRUMENTAL_IMITATION] in name:
    #     return formal_type[ABBREV_INSTRUMENTAL_IMITATION]
    elif formal_type[ABBREV_SOCIAL_APPROACH] in name:
        return formal_type[ABBREV_SOCIAL_APPROACH]
    elif formal_type[ABBREV_SOCIAL_IMITATION] in name:
        return formal_type[ABBREV_SOCIAL_IMITATION]
    elif formal_type[ABBREV_AGENT_NON_AGENT] in name:
        return formal_type[ABBREV_AGENT_NON_AGENT]
    else:
        return SCENE_TYPE_NOT_RECOGNIZED


def get_abbrev_scene_type_from_filename(name):
    # first see if its an osu named file
    scene_type = get_abbrev_scene_type_from_osu_scene_filename(name)
    if scene_type != UNKNOWN_SCENE_TYPE_ABBREVIATION:
        return scene_type
    # then see if its a validation scene file
    scene_type = get_abbrev_scene_type_from_validation_scene_filename(name)
    return scene_type


def get_abbrev_scene_type_from_osu_scene_filename(name):
    # prefix should be scene type abbreviation
    abbrev = name.split("_")[0]
    if abbrev in abbrev_types["pvoe"]:
        return abbrev
    if abbrev in abbrev_types["inter"]:
        return abbrev
    if abbrev in abbrev_types["avoe"]:
        return abbrev
    return UNKNOWN_SCENE_TYPE_ABBREVIATION


def get_abbrev_scene_type_from_validation_scene_filename(name):
    # assumes that the names embedded in the validation scene files match the formal type declarations in this file
    # PVOE
    if formal_type[ABBREV_COLLISION] in name:
        return ABBREV_COLLISION
    elif formal_type[ABBREV_OBJECT_PERMANENCE] in name:
        return ABBREV_OBJECT_PERMANENCE
    elif formal_type[ABBREV_SHAPE_CONSTANCY] in name:
        return ABBREV_SHAPE_CONSTANCY
    elif formal_type[ABBREV_SPATIO_TEMPORAL_CONTINUITY] in name:
        return ABBREV_SPATIO_TEMPORAL_CONTINUITY
    elif formal_type[ABBREV_GRAVITY] in name:
        return ABBREV_GRAVITY
    # INTERACTIVE
    elif formal_type[ABBREV_INTERACTIVE_OBJECT_PERMENANCE] in name:
        return ABBREV_INTERACTIVE_OBJECT_PERMENANCE
    elif formal_type[ABBREV_AGENT_IDENTIFICATION] in name:
        return ABBREV_AGENT_IDENTIFICATION
    elif formal_type[ABBREV_CONTAINERS] in name:
        return ABBREV_CONTAINERS
    elif formal_type[ABBREV_LAVA] in name:
        return ABBREV_LAVA
    elif formal_type[ABBREV_HOLES] in name:
        return ABBREV_HOLES
    elif formal_type[ABBREV_MOVING_TARGET] in name:
        return ABBREV_MOVING_TARGET
    elif formal_type[ABBREV_INTERACTIVE_OBJECT_PERMENANCE] in name:
        return ABBREV_INTERACTIVE_OBJECT_PERMENANCE
    elif formal_type[ABBREV_OBSTACLES] in name:
        return ABBREV_OBSTACLES
    elif formal_type[ABBREV_OCCLUDERS] in name:
        return ABBREV_OCCLUDERS
    elif formal_type[ABBREV_RAMP] in name:
        return ABBREV_RAMP
    elif formal_type[ABBREV_SOLIDITY] in name:
        return ABBREV_SOLIDITY
    elif formal_type[ABBREV_SPATIAL_ELIMINATION] in name:
        return ABBREV_SPATIAL_ELIMINATION
    elif formal_type[ABBREV_SUPPORT_RELATIONS] in name:
        return ABBREV_SUPPORT_RELATIONS
    elif formal_type[ABBREV_TOOL] in name:
        return ABBREV_TOOL

    elif formal_type[ABBREV_ARITHMETIC] in name:
        return ABBREV_ARITHMETIC
    elif formal_type[ABBREV_NUMBER_COMPARISON] in name:
        return ABBREV_NUMBER_COMPARISON
    elif formal_type[ABBREV_IMITATION] in name:
        return ABBREV_IMITATION
    elif formal_type[ABBREV_SET_ROTATION] in name:
        return ABBREV_SET_ROTATION
    elif formal_type[ABBREV_SPATIAL_REFERENCE] in name:
        return ABBREV_SPATIAL_REFERENCE
    elif formal_type[ABBREV_REORIENT] in name:
        return ABBREV_REORIENT
    elif formal_type[ABBREV_TOOL_CHOICE] in name:
        return ABBREV_TOOL_CHOICE
    elif formal_type[ABBREV_ASYMMETRIC_TOOL] in name:
        return ABBREV_ASYMMETRIC_TOOL
    elif formal_type[ABBREV_HIDDEN_TRAJECTORY] in name:
        return ABBREV_HIDDEN_TRAJECTORY
    elif formal_type[ABBREV_COLLISION_TRAJECTORY] in name:
        return ABBREV_COLLISION_TRAJECTORY
    elif formal_type[ABBREV_SEEING_LEADS_TO_KNOWING] in name:
        return ABBREV_SEEING_LEADS_TO_KNOWING
    elif formal_type[ABBREV_SHELL_GAME] in name:
        return ABBREV_SHELL_GAME

    elif formal_type[ABBREV_HIDDEN_SET_ROTATION] in name:
        return ABBREV_HIDDEN_SET_ROTATION
    elif formal_type[ABBREV_KNOWLEDGEABLE_AGENTS] in name:
        return ABBREV_KNOWLEDGEABLE_AGENTS
    elif formal_type[ABBREV_MULTI_TOOL] in name:
        return ABBREV_MULTI_TOOL
    # #AVOE
    elif formal_type[ABBREV_HELPER_HINDERER] in name:
        return ABBREV_HELPER_HINDERER
    elif formal_type[ABBREV_TRUE_BELIEF] in name:
        return ABBREV_TRUE_BELIEF
    elif formal_type[ABBREV_FALSE_BELIEF] in name:
        return ABBREV_FALSE_BELIEF
    elif formal_type[ABBREV_INEFFICIENT_ACTION_IRRATIONAL] in name:
        return ABBREV_INEFFICIENT_ACTION_IRRATIONAL
    elif formal_type[ABBREV_INEFFICIENT_ACTION_PATH] in name:
        return ABBREV_INEFFICIENT_ACTION_PATH
    elif formal_type[ABBREV_INEFFICIENT_ACTION_TIME] in name:
        return ABBREV_INEFFICIENT_ACTION_TIME
    elif formal_type[ABBREV_INACCESSIBLE_GOAL] in name:
        return ABBREV_INACCESSIBLE_GOAL
    elif formal_type[ABBREV_INSTRUMENTAL_ACTION_BLOCKING_BARRIERS] in name:
        return ABBREV_INSTRUMENTAL_ACTION_BLOCKING_BARRIERS
    elif (
        formal_type[ABBREV_INSTRUMENTAL_ACTION_INCONSEQUENTIAL_BARRIERS]
        in name
    ):
        return ABBREV_INSTRUMENTAL_ACTION_INCONSEQUENTIAL_BARRIERS
    elif formal_type[ABBREV_INSTRUMENTAL_ACTION_NO_BARRIERS] in name:
        return ABBREV_INSTRUMENTAL_ACTION_NO_BARRIERS
    elif formal_type[ABBREV_OBJECT_PREFERENCE] in name:
        return ABBREV_OBJECT_PREFERENCE
    elif formal_type[ABBREV_MULTIPLE_AGENTS] in name:
        return ABBREV_MULTIPLE_AGENTS

    # elif formal_type[ABBREV_AGENT_ONE_GOAL] in name:
    #     return ABBREV_AGENT_ONE_GOAL
    # elif formal_type[ABBREV_AGENT_PREFERENCE] in name:
    #     return ABBREV_AGENT_PREFERENCE
    # elif formal_type[ABBREV_COLLECT] in name:
    #     return ABBREV_COLLECT
    # elif formal_type[ABBREV_NON_AGENT_ONE_GOAL] in name:
    #     return ABBREV_NON_AGENT_ONE_GOAL
    # elif formal_type[ABBREV_NON_AGENT_PREFERENCE] in name:
    #     return ABBREV_NON_AGENT_PREFERENCE
    # elif formal_type[ABBREV_INSTRUMENTAL_APPROACH] in name:
    #     return ABBREV_INSTRUMENTAL_APPROACH
    # elif formal_type[ABBREV_INSTRUMENTAL_IMITATION] in name:
    #     return ABBREV_INSTRUMENTAL_IMITATION
    elif formal_type[ABBREV_SOCIAL_APPROACH] in name:
        return ABBREV_SOCIAL_APPROACH
    elif formal_type[ABBREV_SOCIAL_IMITATION] in name:
        return ABBREV_SOCIAL_IMITATION
    elif formal_type[ABBREV_AGENT_NON_AGENT] in name:
        return ABBREV_AGENT_NON_AGENT
    else:
        return SCENE_TYPE_NOT_RECOGNIZED


cubes_for_type                                                              = {}
cubes_for_type["pvoe"]                                                      = {}
cubes_for_type["pvoe"][ABBREV_COLLISION]                                    = ["C1","D2","F1","C2","A1","F2","G1","B1","I1","E2","L2","J2","E1","J1","H2","I2","L1","A2","K2","D1","K1","G2","B2","H1",]
cubes_for_type["pvoe"][ABBREV_OBJECT_PERMANENCE]                            = ["F3","C1","M2","R2","C2","A2","D2","I1","G1","D3","D1","P1","O1","L1","F1","F2","A1","R1","L2","I2","J1","J2","A3","G3","P2","I3","M1","O2","C3","G2",]
cubes_for_type["pvoe"][ABBREV_SHAPE_CONSTANCY]                              = ["E1","J1","L2","E2","L4","D2","A2","E3","A1","B1",]
cubes_for_type["pvoe"][ABBREV_SPATIO_TEMPORAL_CONTINUITY]                   = ["B2","C1","H2","B3","F1","A1","E1","D1","G2","D2","G1","A2","A3","H1","D3","G3","F3","E3","F2","C3","C2","B1","E2","H3",]
cubes_for_type["pvoe"][ABBREV_GRAVITY]                                      = ["S1","GG1","CC1","Z1","EE1","P1","N1","T1","J1","B1","M1","AA1","BB1","SS1","DD1","TT1","Y1","L1","VV1","D1","HH1","I1","X1","W1","K1","C1","O1","UU1","A1","FF1",]

cubes_for_type["inter"]                                                     = {}
cubes_for_type["inter"]["weighted"]                                         = {}
cubes_for_type["inter"]["weighted"][ABBREV_AGENT_IDENTIFICATION]            = ["F1","A2","E1","F2","B2","B1","E2","A1",]
cubes_for_type["inter"]["weighted"][ABBREV_CONTAINERS]                      = ["M2","G2","A1","G1","A2","M1",]
cubes_for_type["inter"]["weighted"][ABBREV_LAVA]                            = ["C1", "B1"]
cubes_for_type["inter"]["weighted"][ABBREV_HOLES]                           = ["B1", "C1"]
cubes_for_type["inter"]["weighted"][ABBREV_MOVING_TARGET]                   = ["A1","E1","I1","B1","F1","J1",]
cubes_for_type["inter"]["weighted"][ABBREV_INTERACTIVE_OBJECT_PERMENANCE]   = ["C1","A1",]
cubes_for_type["inter"]["weighted"][ABBREV_OBSTACLES]                       = ["A1","C2","C1","A2",]
cubes_for_type["inter"]["weighted"][ABBREV_OCCLUDERS]                       = ["E1","I1","A1","K2","K1","G2","E2","G1","C2","I2","C1","A2",]
cubes_for_type["inter"]["weighted"][ABBREV_RAMP]                            = ["L1","H1","F1","C1","K1","E1","B1","I1",]
cubes_for_type["inter"]["weighted"][ABBREV_SOLIDITY]                        = ["B1", "A1", "C1"]
cubes_for_type["inter"]["weighted"][ABBREV_SPATIAL_ELIMINATION]             = ["C1","A1","A2","C2",]
cubes_for_type["inter"]["weighted"][ABBREV_SUPPORT_RELATIONS]               = ["B1","H1","C1","E1","F1","I1","A1","G1","D1",]
cubes_for_type["inter"]["weighted"][ABBREV_TOOL]                            = ["G1", "A1", "C1", "E1_"]

cubes_for_type["inter"]["unweighted"]                                       = {}
cubes_for_type["inter"]["unweighted"][ABBREV_AGENT_IDENTIFICATION]          = []
cubes_for_type["inter"]["unweighted"][ABBREV_CONTAINERS]                    = ["D2","D1","P2","P1","J2","J1",]
cubes_for_type["inter"]["unweighted"][ABBREV_LAVA]                          = ["A1"]
cubes_for_type["inter"]["unweighted"][ABBREV_HOLES]                         = ["A1"]
cubes_for_type["inter"]["unweighted"][ABBREV_MOVING_TARGET]                 = ["G1","D1","L1","K1","H1","C1",]
cubes_for_type["inter"]["unweighted"][ABBREV_INTERACTIVE_OBJECT_PERMENANCE] = ["A2","C2",]
cubes_for_type["inter"]["unweighted"][ABBREV_OBSTACLES]                     = ["D1","D2","B1","B2",]
cubes_for_type["inter"]["unweighted"][ABBREV_OCCLUDERS]                     = ["J2","D2","F2","B1","F1","H1","J1","D1","L2","H2","B2","L1",]
cubes_for_type["inter"]["unweighted"][ABBREV_RAMP]                          = ["G1", "A1", "D1", "J1"]
cubes_for_type["inter"]["unweighted"][ABBREV_SOLIDITY]                      = ["B2","B3","D2","C3","B4","A4","D3","A3","D4","C4","D1","B1",]
cubes_for_type["inter"]["unweighted"][ABBREV_SPATIAL_ELIMINATION]           = []
cubes_for_type["inter"]["unweighted"][ABBREV_SUPPORT_RELATIONS]             = []
cubes_for_type["inter"]["unweighted"][ABBREV_TOOL]                          = ["F1", "H1", "D1", "B1"]

# NOTE for our eval6 testing, we first added new_scene_types dataset where we didn't do the work of verifying 
# that all hypercube variants were present, hoping that the default yaml files generated a representative set.
cubes_for_type["inter"][ABBREV_ARITHMETIC]                                  = ["zz"]
cubes_for_type["inter"][ABBREV_NUMBER_COMPARISON]                           = ["zz"]
cubes_for_type["inter"][ABBREV_IMITATION]                                   = ["zz"]
cubes_for_type["inter"][ABBREV_SET_ROTATION]                                = ["zz"]
cubes_for_type["inter"][ABBREV_SPATIAL_REFERENCE]                           = ["zz"]
cubes_for_type["inter"][ABBREV_REORIENT]                                    = ["zz"]
cubes_for_type["inter"][ABBREV_TOOL_CHOICE]                                 = ["zz"]
cubes_for_type["inter"][ABBREV_ASYMMETRIC_TOOL]                             = ["zz"]
cubes_for_type["inter"][ABBREV_HIDDEN_TRAJECTORY]                           = ["zz"]
cubes_for_type["inter"][ABBREV_COLLISION_TRAJECTORY]                        = ["zz"]
cubes_for_type["inter"][ABBREV_SEEING_LEADS_TO_KNOWING]                     = ["zz"]
cubes_for_type["inter"][ABBREV_SHELL_GAME]                                  = ["zz"]

cubes_for_type["inter"][ABBREV_HIDDEN_SET_ROTATION]                         = ["zz"]
cubes_for_type["inter"][ABBREV_KNOWLEDGEABLE_AGENTS]                        = ["zz"]
cubes_for_type["inter"][ABBREV_MULTI_TOOL]                                  = ["zz"]

# WARNING ASSUMES weighted AND unweighted NEVER TESTED TOGETHER!!!
for inter_type in abbrev_types["inter"]:
    if inter_type in cubes_for_type["inter"]["weighted"] or inter_type in cubes_for_type["inter"]["unweighted"]:
        cubes_for_type["inter"][inter_type] = []
        # pull the cube ids up from the weighted and unweighed sub dictionaries into the top level dictionary
        if inter_type in cubes_for_type["inter"]["weighted"]:
            #print(f'{inter_type} is in weighted set ')
            cubes_for_type["inter"][inter_type].extend(
                cubes_for_type["inter"]["weighted"][inter_type]
            )
        if inter_type in cubes_for_type["inter"]["unweighted"]:
            #print(f'{inter_type} is in UNweighted set ')
            cubes_for_type["inter"][inter_type].extend(
                cubes_for_type["inter"]["unweighted"][inter_type]
            )
    

cubes_for_type["avoe"]                                          = {}
cubes_for_type["avoe"][ABBREV_INEFFICIENT_ACTION_IRRATIONAL]    = ["nyi"]
cubes_for_type["avoe"][ABBREV_MULTIPLE_AGENTS]                  = ["nyi"]
cubes_for_type["avoe"][ABBREV_OBJECT_PREFERENCE]                = ["nyi"]

#cubes_for_type["avoe"][ABBREV_AGENT_ONE_GOAL]                   = ["nyi"]
# cubes_for_type["avoe"][ABBREV_AGENT_PREFERENCE]                 = ["nyi"]
# cubes_for_type["avoe"][ABBREV_COLLECT]                          = ["nyi"]
# cubes_for_type["avoe"][ABBREV_NON_AGENT_ONE_GOAL]               = ["nyi"]
# cubes_for_type["avoe"][ABBREV_NON_AGENT_PREFERENCE]             = ["nyi"]
# cubes_for_type["avoe"][ABBREV_INSTRUMENTAL_APPROACH]            = ["nyi"]
# cubes_for_type["avoe"][ABBREV_INSTRUMENTAL_IMITATION]           = ["nyi"]
cubes_for_type["avoe"][ABBREV_SOCIAL_APPROACH]                 = ["nyi"]
cubes_for_type["avoe"][ABBREV_SOCIAL_IMITATION]                = ["nyi"]
cubes_for_type["avoe"][ABBREV_AGENT_NON_AGENT]                 = ["nyi"]

cubes_for_type["avoe"][ABBREV_HELPER_HINDERER]                 = ["nyi"]
cubes_for_type["avoe"][ABBREV_TRUE_BELIEF]                     = ["nyi"]
cubes_for_type["avoe"][ABBREV_FALSE_BELIEF]                    = ["nyi"]
