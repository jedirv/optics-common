import argparse
import json
import os
import sys

import eval_results


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene_dir", default="junk")
    parser.add_argument("--answer_key", default="junk")
    parser.add_argument("--out_dir", default="junk")
    return parser


if __name__ == "__main__":
    args = make_parser().parse_args()
    scene_dir = args.scene_dir
    answer_key = args.answer_key
    out_dir = args.out_dir
    if scene_dir == "junk" or answer_key == "junk" or out_dir == "junk":
        print(
            "usage:  python eval5_training_set_rename.py --scene_dir <scene_dir> --answer_key <answer_key_path> --out_dir <output_dir>"
        )
        sys.exit()
    if not os.path.isdir(scene_dir):
        print("scene_dir dir {} doesn't exist.".format(scene_dir))
        print(
            "usage:  python eval5_training_set_rename.py --scene_dir <scene_dir> --answer_key <answer_key_path> --out_dir <output_dir>"
        )
        sys.exit()
    if not os.path.isfile(answer_key):
        print("answer_key {} not valid.".format(answer_key))
        print(
            "usage:  python eval5_training_set_rename.py --scene_dir <scene_dir> --answer_key <answer_key_path> --out_dir <output_dir>"
        )
        sys.exit()
    if os.path.isdir(out_dir):
        print("out_dir{} already exists.".format(out_dir))
        print(
            "usage:  python eval5_training_set_rename.py --scene_dir <scene_dir> --answer_key <answer_key_path> --out_dir <output_dir>"
        )
        sys.exit()

    os.makedirs(out_dir)
    print("scene_dir {}".format(scene_dir))
    print("answer_key {}".format(answer_key))
    print("out_dir {}".format(out_dir))

    f = open(answer_key)
    lines = f.readlines()
    f.close()
    # copy scene november_0001_01.json to eval 5 format
    print(lines[0])
    er = eval_results.EvalResults(lines)
    for scene_root in er.scene_name_roots:
        print("processing {}".format(scene_root))
        path = os.path.join(scene_dir, scene_root + ".json")
        f = open(path, "r")
        json_data = json.load(f)
        f.close()

        new_name = er.scene_filename_for_root[scene_root] + ".json"
        out_path = os.path.join(out_dir, new_name)
        f = open(out_path, "w")
        json.dump(json_data, f, indent=4)
        f.close()
