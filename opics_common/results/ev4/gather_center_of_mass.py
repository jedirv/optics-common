import argparse
import json
import os
import sys

from header_val_indices import val_index


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene_dir", default="junk1")
    parser.add_argument("--answer_key", default="junk2")
    return parser


value_map = {}


def note_value_of(data, key, success):
    if key in data:
        val = data[key]
        if not val in value_map:
            value_map[val] = {}
            value_map[val]["Correct"] = 0
            value_map[val]["Incorrect"] = 0
        value_map[val][success] += 1


if __name__ == "__main__":
    args = make_parser().parse_args()
    scene_dir = args.scene_dir
    answer_key = args.answer_key

    if not os.path.isdir(scene_dir):
        print("scene_dir dir {} doesn't exist.".format(scene_dir))
        print(
            "usage:  python gather_center_of_mass.py --scene_dir <scene_dir> --answer_key <answer_key_path>"
        )
        sys.exit()
    if not os.path.isfile(answer_key):
        print("answer_key {} not valid.".format(answer_key))
        print(
            "usage:  python gather_center_of_mass.py --scene_dir <scene_dir> --answer_key <answer_key_path>"
        )
        sys.exit()

    f = open(answer_key)
    lines = f.readlines()
    f.close()
    print("# scene_dir {}".format(scene_dir))
    print("# answer_key {}".format(answer_key))
    print("# failed scenes with center of mass change:")
    for i in range(2, len(lines)):
        line = lines[i]
        parts = line.split(",")
        scene_name = parts[val_index["TEST NAME"]]
        success = parts[val_index["EVALUATION SCORE ACCURACY"]]
        if success == "Incorrect":
            scene_filename = scene_name + ".json"
            scene_path = os.path.join(scene_dir, scene_filename)
            if not os.path.isfile(scene_path):
                print("error - cannot find file {}".format(scene_path))
                sys.exit()
            f = open(scene_path)
            data = json.load(f)
            f.close()
            if "resetCenterOfMass" in data["objects"][0]:
                print(scene_filename)
