import os

# TODO(Mazen): this doesn't seems to exist anywhere
from opics_common.opics_logging.log_constants import delim
from opics_common.results.header_val_indices import (
    inter_results_idx,
    val_index,
)

metadata_abbrev                                 = {}
metadata_abbrev["level1"]                       = "L1"
metadata_abbrev["level2"]                       = "L2"
metadata_abbrev["oracle"]                       = "oracle"

type_abbrev                                     = {}
type_abbrev["interactive object permanence"]    = "iop"
type_abbrev["container"]                        = "cont"
type_abbrev["occluder"]                         = "occl"
type_abbrev["obstacle"]                         = "obst"


def get_articulate_scene_name(root, entry_fields):
    # scene files were copied into names of this form:  iop_L2_A1_correct_alpha_0003_01
    correctness = entry_fields[val_index["EVALUATION SCORE ACCURACY"]]
    level = metadata_abbrev[entry_fields[val_index["METADATA LEVEL"]]]
    type = type_abbrev[entry_fields[val_index["TERTIARY TYPE"]]]
    cube = entry_fields[val_index["CUBE/SCENE GOAL ID"]]
    return (
        type
        + "_"
        + level
        + "_"
        + cube
        + "_"
        + correctness.lower()
        + "_"
        + root
    )


class EvalResultsInt:
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
            scene_name_root = parts[val_index["TEST NAME"]]

            correctness = parts[val_index["EVALUATION SCORE ACCURACY"]]
            type = parts[val_index["TERTIARY TYPE"]]
            self.scene_name_roots.append(scene_name_root)
            self.scene_filename_for_root[
                scene_name_root
            ] = get_articulate_scene_name(scene_name_root, parts)
            self.correctness_for_scene[scene_name_root] = correctness
            self.scene_type_for_scene[scene_name_root] = type


class CurrentRunInt:
    def __init__(self, result_lines):
        self.scene_info = {}
        for result in result_lines:
            all_info = result.split(delim)
            full_scene_name = all_info[inter_results_idx["SCENE NAME"]]
            curr_scene_name = full_scene_name.split("/")[-1]
            curr_scene_name = curr_scene_name.split(".")[0]
            result = all_info[inter_results_idx["RESULT"]]
            result = result.split("=")[-1][:-1]
            steps = all_info[inter_results_idx["STEPS"]]
            # print (cur)
            self.scene_info[curr_scene_name] = (result, steps)


def compare_results(eval4_result, curr_result):
    if (
        eval4_result.lower() == "correct"
        and curr_result.lower() == "succeeded"
    ):
        return True
    if eval4_result.lower() == "iccorrect" and curr_result.lower() == "failed":
        return True
    return False


def compare_int(answer_key_file, opics_results_file):

    with open(answer_key_file) as f:
        answer_key_lines = f.readlines()
    f.close()

    with open(opics_results_file) as f:
        result_lines = f.readlines()
    f.close()

    eval_results_info = EvalResultsInt(answer_key_lines)
    curr_run_info = CurrentRunInt(result_lines)
    number_same_result = 0
    number_correct_results_curr_run = 0
    total_results = len(result_lines)
    for key, values in eval_results_info.correctness_for_scene.items():
        if key in curr_run_info.scene_info:
            print(key, values)
            print(curr_run_info.scene_info[key])
            same_result = compare_results(
                values, curr_run_info.scene_info[key][0]
            )
            if curr_run_info.scene_info[key][0] == "succeeded":
                number_correct_results_curr_run += 1
            if same_result == True:
                number_same_result += 1

    # print (eval_results_info.__dict__)
    # print (curr_run_info.__dict__)

    print(f"Number of results matching eval 4 : {number_same_result}")
    print(
        f"Number of successes : {number_correct_results_curr_run}/{total_results}"
    )
    return


root_dir            = os.environ("OPICS_HOME")
results_dir         = os.path.join(root_dir, "opics_common/results")
results_file        = "eval4_results_level2_int_obstacle.csv"
results_file_path   = os.path.join(results_dir, results_file)
log_dir             = os.path.join(root_dir, "logs")
log_filename        = "opics_log_2022_05_23-05_11_59_715745_AM.txt"
log_filename        = "opics_log_2022_05_23-04_31_22_134458_PM.txt"
log_path            = os.path.join(log_dir, log_filename)
compare_int(results_file_path, log_path)
