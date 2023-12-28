import opics_common.scene_type.type_constants as tc
from opics_common.results.ev5.header_val_indices_ev5 import val_index

type_abbrev                                     = {}
type_abbrev["agent identification"]             = tc.ABBREV_AGENT_IDENTIFICATION
type_abbrev["container"]                        = tc.ABBREV_CONTAINERS
type_abbrev["lava"]                             = tc.ABBREV_LAVA
type_abbrev["holes"]                            = tc.ABBREV_HOLES
type_abbrev["moving target prediction"]         = tc.ABBREV_MOVING_TARGET
type_abbrev["interactive object permanence"]    = tc.ABBREV_INTERACTIVE_OBJECT_PERMENANCE
type_abbrev["obstacle"]                         = tc.ABBREV_OBSTACLES
type_abbrev["occluder"]                         = tc.ABBREV_OCCLUDERS
type_abbrev["ramp"]                             = tc.ABBREV_RAMP
type_abbrev["solidity"]                         = tc.ABBREV_SOLIDITY
type_abbrev["spatial elimination"]              = tc.ABBREV_SPATIAL_ELIMINATION
type_abbrev["support relations"]                = tc.ABBREV_SUPPORT_RELATIONS
type_abbrev["symmetric tool use"]               = tc.ABBREV_TOOL

type_abbrev["arithmetic"]                       = tc.ABBREV_ARITHMETIC
type_abbrev["number comparison"]                = tc.ABBREV_NUMBER_COMPARISON
type_abbrev["imitation task"]                   = tc.ABBREV_IMITATION
type_abbrev["set rotation"]                     = tc.ABBREV_SET_ROTATION
type_abbrev["spatial reference"]                = tc.ABBREV_SPATIAL_REFERENCE
type_abbrev["spatial reorientation"]            = tc.ABBREV_REORIENT
type_abbrev["asymmetric tool use"]              = tc.ABBREV_ASYMMETRIC_TOOL
type_abbrev["tool choice"]                      = tc.ABBREV_TOOL_CHOICE
type_abbrev["trajectory"]                       = tc.ABBREV_HIDDEN_TRAJECTORY
type_abbrev["interactive collision"]            = tc.ABBREV_COLLISION_TRAJECTORY
type_abbrev["seeing leads to knowing"]          = tc.ABBREV_SEEING_LEADS_TO_KNOWING
type_abbrev["shell game"]                       = tc.ABBREV_SHELL_GAME


def get_scene_name_including_answer(scene_id, entry_fields):
    # get names of form   <type>_<scene_id>_<cube>_<answer>.json   where scene_id breaks out to <ta2code>_<testnum>_<scenenum>
    correctness = entry_fields[val_index["EVALUATION SCORE ACCURACY"]]
    if correctness == "Correct":
        result = "6c"
    else:
        result = "6i"
    type = type_abbrev[entry_fields[val_index["TERTIARY TYPE"]]]
    cube = entry_fields[val_index["CUBE/SCENE GOAL ID"]]
    return type + "_" + scene_id + "_" + cube + "_" + result + ".json"


class EvalResultsInter:
    def __init__(self, answer_key_lines):
        self.scene_name_roots = []
        self.scene_filename_for_root = {}
        self.correctness_for_scene = {}
        self.scene_type_for_scene = {}
        for answer_key_line in answer_key_lines:
            if answer_key_line.startswith("Total"):
                continue
            if answer_key_line.startswith("CATEGORY"):
                continue
            parts = answer_key_line.split(",")
            scene_id = parts[val_index["TEST NAME"]]

            correctness = parts[val_index["EVALUATION SCORE ACCURACY"]]
            type = parts[val_index["TERTIARY TYPE"]]
            self.scene_name_roots.append(scene_id)
            self.scene_filename_for_root[
                scene_id
            ] = get_scene_name_including_answer(scene_id, parts)
            self.correctness_for_scene[scene_id] = correctness
            self.scene_type_for_scene[scene_id] = type

    def get_type_abbrev(self, tertiary_type):
        return type_abbrev[tertiary_type]
