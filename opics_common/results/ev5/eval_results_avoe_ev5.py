import opics_common.scene_type.type_constants as tc
from opics_common.results.ev5.header_val_indices_ev5 import val_index

type_abbrev                                                           = {}
type_abbrev["agents efficient action irrational"]                     = tc.ABBREV_INEFFICIENT_ACTION_IRRATIONAL
type_abbrev["agents efficient action path lure"]                      = tc.ABBREV_INEFFICIENT_ACTION_PATH
type_abbrev["agents efficient action time control"]                   = tc.ABBREV_INEFFICIENT_ACTION_TIME
type_abbrev["agents inaccessible goal"]                               = tc.ABBREV_INACCESSIBLE_GOAL
type_abbrev["agents instrumental action blocking barriers"]           = tc.ABBREV_INSTRUMENTAL_ACTION_BLOCKING_BARRIERS
type_abbrev["agents instrumental action inconsequential barriers"]    = tc.ABBREV_INSTRUMENTAL_ACTION_INCONSEQUENTIAL_BARRIERS
type_abbrev["agents instrumental action no barriers"]                 = tc.ABBREV_INSTRUMENTAL_ACTION_NO_BARRIERS
type_abbrev["agents object preference"]                               = tc.ABBREV_OBJECT_PREFERENCE
type_abbrev["agents multiple agents"]                                 = tc.ABBREV_MULTIPLE_AGENTS


def get_scene_name_including_answer(scene_id, entry_fields):
    # get names of form   <type>_<scene_id>_<cube>_<answer>.json   where scene_id breaks out to <ta2code>_<testnum>_<scenenum>
    correctness = entry_fields[val_index["EVALUATION SCORE ACCURACY"]]
    if correctness == "Correct":
        result = "5c"
    else:
        result = "5i"
    type = type_abbrev[entry_fields[val_index["TERTIARY TYPE"]]]
    cube = entry_fields[val_index["CUBE/SCENE GOAL ID"]]
    expectedness = entry_fields[val_index["GOAL ANSWER CHOICE"]]
    return (
        type
        + "_"
        + scene_id
        + "_"
        + cube
        + "_"
        + expectedness
        + "_"
        + result
        + ".json"
    )


class EvalResultsAvoe:
    def __init__(self, answer_key_lines):
        self.scene_name_roots = []
        self.scene_filename_for_root = {}
        self.expectedness_for_scene = {}
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
            expectedness = parts[val_index["GOAL ANSWER CHOICE"]]
            type = parts[val_index["TERTIARY TYPE"]]
            self.scene_name_roots.append(scene_id)
            self.scene_filename_for_root[
                scene_id
            ] = get_scene_name_including_answer(scene_id, parts)
            self.correctness_for_scene[scene_id] = correctness
            self.expectedness_for_scene[scene_id] = expectedness
            self.scene_type_for_scene[scene_id] = type
