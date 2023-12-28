from opics_common.results.header_val_indices import val_index

metadata_abbrev                             = {}
metadata_abbrev["level1"]                   = "L1"
metadata_abbrev["level2"]                   = "L2"
metadata_abbrev["oracle"]                   = "oracle"

type_abbrev                                 = {}
type_abbrev["object permanence"]            = "op"
type_abbrev["spatio temporal continuity"]   = "stc"
type_abbrev["shape constancy"]              = "sc"
type_abbrev["collisions"]                   = "coll"
type_abbrev["gravity support"]              = "grav"


plausibility_abbrev                         = {}
plausibility_abbrev["plausible"]            = "plaus"
plausibility_abbrev["implausible"]          = "implaus"


def get_articulate_scene_name(root, entry_fields):
    # scene files were copied into names of this form:  grav_L1_A1_plaus_correct_oscar_0003_01
    correctness = entry_fields[val_index["EVALUATION SCORE ACCURACY"]]
    level = metadata_abbrev[entry_fields[val_index["METADATA LEVEL"]]]
    type = type_abbrev[entry_fields[val_index["TERTIARY TYPE"]]]
    cube = entry_fields[val_index["CUBE/SCENE GOAL ID"]]
    plaus_abbrev = plausibility_abbrev[
        entry_fields[val_index["GOAL ANSWER CHOICE"]]
    ]
    return (
        type
        + "_"
        + level
        + "_"
        + cube
        + "_"
        + plaus_abbrev
        + "_"
        + correctness.lower()
        + "_"
        + root
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
            scene_name_root = parts[val_index["TEST NAME"]]

            correctness = parts[val_index["EVALUATION SCORE ACCURACY"]]
            plausibility = parts[val_index["GOAL ANSWER CHOICE"]]
            type = parts[val_index["TERTIARY TYPE"]]
            self.scene_name_roots.append(scene_name_root)
            self.scene_filename_for_root[
                scene_name_root
            ] = get_articulate_scene_name(scene_name_root, parts)
            self.correctness_for_scene[scene_name_root] = correctness
            self.plausibility_for_scene[scene_name_root] = plausibility
            self.scene_type_for_scene[scene_name_root] = type
