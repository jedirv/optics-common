import opics_common.scene_type.type_constants as tc
from opics_common.results.ev5.header_val_indices_ev5 import val_index

type_abbrev                                 = {}
type_abbrev["object permanence"]            = tc.ABBREV_OBJECT_PERMANENCE
type_abbrev["spatio temporal continuity"]   = tc.ABBREV_SPATIO_TEMPORAL_CONTINUITY
type_abbrev["shape constancy"]              = tc.ABBREV_SHAPE_CONSTANCY
type_abbrev["collisions"]                   = tc.ABBREV_COLLISION
type_abbrev["gravity support"]              = tc.ABBREV_GRAVITY

plausibility_abbrev                         = {}
plausibility_abbrev["plausible"]            = "plaus"
plausibility_abbrev["implausible"]          = "implaus"


def get_scene_name_including_answer(scene_id, entry_fields):
    # get names of form   <type>_<scene_id>_<cube>_<answer>.json   where scene_id breaks out to <ta2code>_<testnum>_<scenenum>
    correctness = entry_fields[val_index["EVALUATION SCORE ACCURACY"]]
    if correctness == "Correct":
        result = "6c"
    else:
        result = "6i"
    type = type_abbrev[entry_fields[val_index["TERTIARY TYPE"]]]
    cube = entry_fields[val_index["CUBE/SCENE GOAL ID"]]
    plaus_abbrev = plausibility_abbrev[
        entry_fields[val_index["GOAL ANSWER CHOICE"]]
    ]
    return (
        type
        + "_"
        + scene_id
        + "_"
        + cube
        + "_"
        + plaus_abbrev
        + "_"
        + result
        + ".json"
    )


class EvalResultsPvoe:
    def __init__(self, answer_key_lines):
        self.scene_name_roots = []
        self.scene_filename_for_root = {}
        self.plausibility_for_scene = {}
        self.correctness_for_scene = {}
        self.scene_type_for_scene = {}
        for answer_key_line in answer_key_lines:
            if answer_key_line.startswith("Total"):
                continue
            if answer_key_line.startswith("CATEGORY"):
                continue
            parts = answer_key_line.split(",")
            scene_id = parts[val_index["TEST NAME"]]
            print(f'loading scene {scene_id}')

            correctness = parts[val_index["EVALUATION SCORE ACCURACY"]]
            plausibility = parts[val_index["GOAL ANSWER CHOICE"]]
            type = parts[val_index["TERTIARY TYPE"]]
            self.scene_name_roots.append(scene_id)
            self.scene_filename_for_root[
                scene_id
            ] = get_scene_name_including_answer(scene_id, parts)
            self.correctness_for_scene[scene_id] = correctness
            self.plausibility_for_scene[scene_id] = plausibility
            self.scene_type_for_scene[scene_id] = type

    def get_type_abbrev(self, tertiary_type):
        return type_abbrev[tertiary_type]
