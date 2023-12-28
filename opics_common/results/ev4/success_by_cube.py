import argparse
import os
import sys

from cube_info import ir
from header_val_indices import val_index

# not_answered = []
# cube_ids = []
# cube_result = {}
# cube_result["Correct"] = {}
# cube_result["Incorrect"] = {}


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
    not_answered = []
    cube_ids = []
    cube_result = {}
    cube_result["Correct"] = {}
    cube_result["Incorrect"] = {}
    for i in range(0, len(lines)):
        line = lines[i].rstrip()
        if line.startswith("Total"):
            continue
        if line.startswith("CATEGORY"):
            continue
        parts = line.split(",")
        scene_name = parts[val_index["TEST NAME"]]
        scene_type = parts[val_index["TEST TYPE"]]
        success = parts[val_index["EVALUATION SCORE ACCURACY"]]
        # cube_id = parts[val_index["CUBE ID"]]
        cube_id = parts[60]
        # print('noting cube_id {}  success  {}  scene_type {}'.format(cube_id, success, scene_type))
        note_result(cube_ids, cube_result, not_answered, cube_id, success)
    percents = []
    print("   %  cube_id\tcube characteritics...")
    print("--------------------------------------------------------------")
    for cube_id in cube_ids:
        right = cube_result["Correct"][cube_id]
        wrong = cube_result["Incorrect"][cube_id]
        # context = pvoe[scene_type][cube_id]
        # print('scene type {}  id  {}'.format(scene_type, cube_id))
        context = ir[scene_type][cube_id]
        percent = "  {:03d}\t{}\t{}".format(
            int(100 * (float(right) / float(right + wrong))), cube_id, context
        )
        percents.append(percent)
    percents.sort(reverse=True)
    for percent in percents:
        print("{}".format(percent))
    print("")
    print("")
    print("")
    print("   % per cube characteritic")
    print("--------------------------------------------------------------")
    pc_register = {}
    for percent in percents:
        parts = percent.split()
        field_count = len(parts)
        for i in range(2, field_count):
            aspect = parts[i]
            if not aspect in pc_register:
                pc_register[aspect] = []
            score = parts[0]
            pc_register[aspect].append(score)
    averages = []
    for aspect in pc_register:
        total = 0
        score_strings = pc_register[aspect]
        count = len(score_strings)
        for score_string in score_strings:
            score_num = int(score_string)
            total += score_num
        average = int(float(total) / float(count))
        averages.append("  {:03d}\t{}".format(average, aspect))
    averages.sort(reverse=True)
    for average in averages:
        print(average)

    unanswered_counts = {}
    for unanswered_cube_id in not_answered:
        if not unanswered_cube_id in unanswered_counts:
            unanswered_counts[unanswered_cube_id] = 0
        unanswered_counts[unanswered_cube_id] += 1
    print("")
    for unanswered_cube_id in unanswered_counts:
        print(
            "not answered: {}  {}".format(
                unanswered_cube_id, unanswered_counts[unanswered_cube_id]
            )
        )


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
    # NOTE: type_levels = ['coll_oracle','coll_L2','op_L2','op_L1','grav_L2','grav_L1','stc_L2','stc_L1','sc_L2','sc_L1']
    type_levels = [
        "interactReorientation_oracle",
        "interactReorientation_L2",
        "interactObjectPerm_oracle",
        "interactObjectPerm_L2",
        "interactContainer_L2",
        "interactContainer_L1",
        "interactObstacle_L2",
        "interactObstacle_L1",
        "interactOccluder_L2",
        "interactOccluder_L1",
    ]
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
