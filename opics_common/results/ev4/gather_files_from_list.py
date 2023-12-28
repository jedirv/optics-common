import argparse
import json
import os
import sys


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene_dir", default="junk1")
    parser.add_argument("--file_list", default="junk2")
    parser.add_argument("--target_dir", default="junk3")
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


def get_type_from_codename(fname):
    if "oscar" in fname:
        return "grav"
    if "november" in fname:
        return "coll"
    if "papa" in fname:
        return "op"
    if "quebec" in fname:
        return "sc"
    if "romeo" in fname:
        return "stc"
    return "unknown"


if __name__ == "__main__":
    args = make_parser().parse_args()
    scene_dir = args.scene_dir
    file_list = args.file_list
    target_dir = args.target_dir
    if not os.path.isdir(scene_dir):
        print("scene_dir {} doesn't exist.".format(scene_dir))
        print(
            "usage:  python gather_files_from_list.py --scene_dir <scene_dir> --file_list <file_list_path> --target_dir <target_dir>"
        )
        sys.exit()
    if not os.path.isfile(file_list):
        print("file list {} not valid.".format(file_list))
        print(
            "usage:  python gather_files_from_list.py --scene_dir <scene_dir> --file_list <file_list_path> --target_dir <target_dir>"
        )
        sys.exit()

    if os.path.isdir(target_dir):
        print(
            "target_dir {} exists, delete or pick a new name".format(
                target_dir
            )
        )
        sys.exit()

    os.mkdir(target_dir)

    f = open(file_list)
    lines = f.readlines()
    f.close()
    print("copying from scene_dir {}".format(scene_dir))
    print("to target dir {}".format(target_dir))
    for i in range(0, len(lines)):
        line = lines[i].rstrip()
        if line.startswith("#"):
            continue
        print(line)
        parts = line.split(",")
        source_fname = parts[0] + ".json"
        type = get_type_from_codename(parts[0])
        dest_fname = type + "_" + parts[1] + "_" + parts[0] + ".json"
        scene_path = os.path.join(scene_dir, source_fname)
        target_path = os.path.join(target_dir, dest_fname)
        print("copying {} to {} ".format(scene_path, target_path))
        f_src = open(scene_path)
        data = json.load(f_src)
        f_src.close()
        f_dest = open(target_path, "w")
        json.dump(data, f_dest, indent=4)
        f_dest.close()
