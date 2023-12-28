import argparse
import os
import sys

from header_val_indices import val_index

# not_answered = []
# cube_ids = []
# cube_result = {}
# cube_result["Correct"] = {}
# cube_result["Incorrect"] = {}
pretty_type                                 = {}
pretty_type["gravity support"]              = "grav"
pretty_type["object permanence"]            = "op"
pretty_type["shape constancy"]              = "sc"
pretty_type["spatio temporal continuity"]   = "stc"
pretty_type["collisions"]                   = "coll"


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--answer_key_dir", default="junk2")
    return parser


def note_result(cube_ids, cube_result, not_answered, cube_id, success):
    if not cube_id in cube_ids:
        cube_ids.append(cube_id)
        cube_result["Correct"][cube_id] = 0
        cube_result["Incorrect"][cube_id] = 0
    if success == "No answer":
        not_answered.append(cube_id + " ")
    else:
        cube_result[success][cube_id] += 1


def get_percent_string(val, boldness):
    remainder = 100 - val
    marker = "="
    if boldness == "bold":
        marker = "#"
    result = ""
    for i in range(0, val):
        result = result + marker
    for i in range(0, remainder):
        result = result + "."
    return result


def process_answer_key_lines(lines):
    not_answered                = []
    cube_ids                    = []
    cube_result                 = {}
    correct_plaus               = []
    correct_implaus             = []
    level_choice                = {}
    level_choice["grav"]        = "L1"
    level_choice["op"]          = "L1"
    level_choice["sc"]          = "L1"
    level_choice["stc"]         = "L1"
    level_choice["coll"]        = "L2"
    cube_result["Correct"]      = {}
    cube_result["Incorrect"]    = {}
    for i in range(0, len(lines)):
        line = lines[i].rstrip()
        if line.startswith("Total"):
            continue
        if line.startswith("CATEGORY"):
            continue
        parts = line.split(",")
        scene_name = parts[val_index["TEST NAME"]]  # i.e. oscar_0001_01
        scene_type = parts[val_index["TEST TYPE"]]  # i.e. gravity support
        success = parts[val_index["EVALUATION SCORE ACCURACY"]]
        level = parts[val_index["METADATA LEVEL"]]
        plausibility = parts[val_index["GOAL ANSWER CHOICE"]]
        # cube_id = parts[val_index["CUBE ID"]]
        cube_id = parts[val_index["CUBE/SCENE GOAL ID"]]
        # print('noting cube_id {}  success  {}  scene_type {}'.format(cube_id, success, scene_type))
        combo = pretty_type[scene_type] + "_" + level
        if success:
            if (
                combo == "coll_level2"
                or combo == "op_level1"
                or combo == "sc_level1"
                or combo == "stc_level1"
                or combo == "grav_level1"
            ):

                if plausibility == "implausible":
                    our_scene_name = "{}_{}_{}_implaus_correct_{}".format(
                        pretty_type[scene_type],
                        level_choice[pretty_type[scene_type]],
                        cube_id,
                        scene_name,
                    )
                    if len(correct_implaus) < 10:
                        correct_implaus.append(our_scene_name)

                else:
                    our_scene_name = "{}_{}_{}_plaus_correct_{}".format(
                        pretty_type[scene_type],
                        level_choice[pretty_type[scene_type]],
                        cube_id,
                        scene_name,
                    )
                    if len(correct_plaus) < 10:
                        correct_plaus.append(our_scene_name)

    for plaus in correct_plaus:
        print(plaus)
    for implaus in correct_implaus:
        print(implaus)


if __name__ == "__main__":
    args = make_parser().parse_args()
    answer_key_dir = args.answer_key_dir

    if not os.path.isdir(answer_key_dir):
        print("answer_key_dir {} not valid.".format(answer_key_dir))
        print(
            "usage:  python success_by_cube.py --answer_key_dir <answer_key_dir>"
        )
        sys.exit()

    print("answer key dir: {}".format(answer_key_dir))

    print("--------------------------------------------")
    type_levels = [
        "coll_oracle",
        "coll_L2",
        "op_L2",
        "op_L1",
        "grav_L2",
        "grav_L1",
        "stc_L2",
        "stc_L1",
        "sc_L2",
        "sc_L1",
    ]
    # NOTE: type_levels = ['interactReorientation_oracle','interactReorientation_L2','interactObjectPerm_oracle','interactObjectPerm_L2','interactContainer_L2','interactContainer_L1','interactObstacle_L2','interactObstacle_L1','interactOccluder_L2','interactOccluder_L1']
    for type_level in type_levels:
        fname = "answerkey_cube_" + type_level + ".csv"
        print(
            "-----------------------------------------------------------------------"
        )
        print(
            "PROCESSING    {}    as per answer file    {}".format(
                type_level, fname
            )
        )
        print(
            "-----------------------------------------------------------------------"
        )
        print("")
        path = os.path.join(answer_key_dir, fname)
        f = open(path)
        lines = f.readlines()
        f.close()
        process_answer_key_lines(lines)
        print("\n........finished {}\n\n".format(type_level))
