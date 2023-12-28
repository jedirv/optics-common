import argparse
import os
import random
import sys

from header_val_indices import val_index

#
# for each cube id, get:
#  1 correct plaus
#  1 correct implaus
#  1 + more_incorrect incorrect plaus
#  1 + more_incorrect incorrect implaus
# so if more_incorrect == 2, each cube will have 8, if == 3, it would be 10
more_incorrect = 3


def make_parser():
    parser = argparse.ArgumentParser()
    # parser.add_argument('--scene_dir', default='junk1')
    parser.add_argument("--answer_key", default="junk2")
    return parser


def get_non_header_lines(lines):
    result = []
    for line in lines:
        if line.startswith("Total"):
            continue
        if line.startswith("CATEGORY"):
            continue
        result.append(line)
    return result


def choose_files(file_list, count):
    result = []
    if len(file_list) == count:
        result.extend(file_list)
    else:
        while len(result) < count:
            rand_index = random.randint(0, count - 1)
            rand_file = file_list[rand_index]
            if not rand_file in result:
                result.append(rand_file)
    return result


def create_entries_from_files(level, cube, files, plausibility, correctness):
    entries = []
    for file in files:
        entry = (
            file
            + ","
            + level
            + "_"
            + cube
            + "_"
            + abbrev[plausibility]
            + "_"
            + correctness
        )
        entries.append(entry)
    return entries


def get_cubes(lines):
    result = []
    for line in lines:
        parts = line.split(",")
        cube_name = parts[val_index["CUBE/SCENE GOAL ID"]]
        if not cube_name in result:
            result.append(cube_name)
    return sorted(result)


abbrev = {}
abbrev["plausible"] = "plaus"
abbrev["implausible"] = "implaus"
files = {}
if __name__ == "__main__":
    args = make_parser().parse_args()
    # scene_dir = args.scene_dir
    answer_key = args.answer_key

    lower_case_answer_key = answer_key.lower()
    if "level1" in lower_case_answer_key:
        level = "L1"
    elif "level2" in lower_case_answer_key:
        level = "L2"
    elif "oracle" in lower_case_answer_key:
        level = "oracle"
    else:
        print("can't find level1, level2, or oracle in answer key name")
    # if not os.path.isdir(scene_dir):
    #     print("scene_dir dir {} doesn't exist.".format(scene_dir))
    #     print("usage:  python fail_set_gather.py --scene_dir <scene_dir> --answer_key <answer_key_path>")
    #     sys.exit()
    if not os.path.isfile(answer_key):
        print("answer_key {} not valid.".format(answer_key))
        print(
            "usage:  python fail_set_gather.py --scene_dir <scene_dir> --answer_key <answer_key_path>"
        )
        sys.exit()
    plausibilities = ["plausible", "implausible"]
    correctness = ["correct", "incorrect"]
    print("# answer_key {}".format(answer_key))
    f = open(answer_key)
    lines = f.readlines()
    f.close()
    lines = get_non_header_lines(lines)
    cubes = get_cubes(lines)
    for cube in cubes:
        # print("{} - sorting files".format(cube))
        files[cube]                               = {}
        files[cube]["plausible"]                  = {}
        files[cube]["plausible"]["Correct"]       = []
        files[cube]["plausible"]["Incorrect"]     = []
        files[cube]["plausible"]["No answer"]     = []
        files[cube]["implausible"]                = {}
        files[cube]["implausible"]["Correct"]     = []
        files[cube]["implausible"]["Incorrect"]   = []
        files[cube]["implausible"]["No answer"]   = []
        for line in lines:
            parts = line.split(",")
            cube_name = parts[val_index["CUBE/SCENE GOAL ID"]]
            if cube_name == cube:
                scene_name = parts[val_index["TEST NAME"]]
                success = parts[val_index["EVALUATION SCORE ACCURACY"]]
                # plausible = parts[val_index["EVALUATION SCORE NUMERICAL GROUND TRUTH"]]
                plausible = parts[val_index["GOAL ANSWER CHOICE"]]
                files[cube][plausible][success].append(scene_name)
                # print('{} {} {} {} '.format(cube, scene_name, plausible, success))
    all_entries = []
    for cube in cubes:
        plaus_correct = len(files[cube]["plausible"]["Correct"])
        plaus_incorrect = len(files[cube]["plausible"]["Incorrect"])
        implaus_correct = len(files[cube]["implausible"]["Correct"])
        implaus_incorrect = len(files[cube]["implausible"]["Incorrect"])
        print(
            "# cube {}\tpc {}\tpi {}\tic {}\tii {}".format(
                cube,
                plaus_correct,
                plaus_incorrect,
                implaus_correct,
                implaus_incorrect,
            )
        )
        desired_plaus_correct = 1
        desired_plaus_incorrect = 1
        desired_implaus_correct = 1
        desired_implaus_incorrect = 1
        total_plaus = plaus_correct + plaus_incorrect
        total_implaus = implaus_correct + implaus_incorrect
        if total_plaus != 0:
            percent_plaus_correct = int(100 * (plaus_correct / (total_plaus)))
            if percent_plaus_correct < 50:
                desired_plaus_incorrect += more_incorrect
        if total_implaus != 0:
            percent_implaus_correct = int(
                100 * (implaus_correct / (implaus_correct + implaus_incorrect))
            )
            if percent_implaus_correct < 50:
                desired_implaus_incorrect += more_incorrect
        if desired_plaus_correct > plaus_correct:
            desired_plaus_correct = plaus_correct
        if desired_plaus_incorrect > plaus_incorrect:
            desired_plaus_incorrect = plaus_incorrect
        if desired_implaus_correct > implaus_correct:
            desired_implaus_correct = implaus_correct
        if desired_implaus_incorrect > implaus_incorrect:
            desired_implaus_incorrect = implaus_incorrect

        chosen_files = choose_files(
            files[cube]["plausible"]["Correct"], desired_plaus_correct
        )
        entries = create_entries_from_files(
            level, cube, chosen_files, "plausible", "correct"
        )
        all_entries.extend(entries)

        chosen_files = choose_files(
            files[cube]["plausible"]["Incorrect"], desired_plaus_incorrect
        )
        entries = create_entries_from_files(
            level, cube, chosen_files, "plausible", "incorrect"
        )
        all_entries.extend(entries)

        chosen_files = choose_files(
            files[cube]["implausible"]["Correct"], desired_implaus_correct
        )
        entries = create_entries_from_files(
            level, cube, chosen_files, "implausible", "correct"
        )
        all_entries.extend(entries)

        chosen_files = choose_files(
            files[cube]["implausible"]["Incorrect"], desired_implaus_incorrect
        )
        entries = create_entries_from_files(
            level, cube, chosen_files, "implausible", "incorrect"
        )
        all_entries.extend(entries)
    for entry in all_entries:
        print(entry)
    print("# {} total entries from {} ".format(len(all_entries), answer_key))
