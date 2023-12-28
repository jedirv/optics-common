import argparse
import json
import os
import random
import sys

answer_options    = ["plaus", "implaus"]
score_options     = ["0", "1"]


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", default="junk1")
    parser.add_argument("--outdir", default="junk2")
    parser.add_argument("--wrongs", default="junk3")
    return parser


def get_plausibility():
    return random.choice(answer_options)


def get_score():
    return random.choice(score_options)


if __name__ == "__main__":
    args = make_parser().parse_args()
    indir = args.indir
    outdir = args.outdir
    wrongs = args.wrongs
    if wrongs == "junk3":
        print("wrongs-file must be specified")
        print(
            "usage:  python rename_as_per_results.py --indir <input_dir>  --outdir <output_dir> --wrongs <wrongs_file>"
        )
        sys.exit()
    if not os.path.isfile(wrongs):
        print("wrongs-file {} does not exist".format(wrongs))
        print(
            "usage:  python rename_as_per_results.py --indir <input_dir>  --outdir <output_dir> --wrongs <wrongs_file>"
        )
        sys.exit()
    if outdir == "junk2":
        print("outdir must be specified")
        print(
            "usage:  python rename_as_per_results.py --indir <input_dir>  --outdir <output_dir> --wrongs <wrongs_file>"
        )
        sys.exit()
    if not os.path.isdir(indir):
        print("input dir {} doesn't exist.".format(indir))
        print(
            "usage:  python rename_as_per_results.py --indir <input_dir>  --outdir <output_dir> --wrongs <wrongs_file>"
        )
        sys.exit()
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    wrongs_fd = open(wrongs)
    wrong_scenes = wrongs_fd.readlines()
    wrongs_fd.close()
    for scene in sorted(os.listdir(indir)):
        if scene.endswith(".json"):  # All scene config files are JSON files
            inputpath = os.path.join(indir, scene)
            f = open(inputpath)
            data = json.load(f)
            f.close()
            parts = scene.split(".")
            plausibility = get_plausibility()
            score = get_score()
            suffix = "_" + plausibility + "_" + score
            new_name = parts[0] + suffix + ".json"
            out_path = os.path.join(outdir, new_name)
            data["plausibility"] = plausibility
            data["score"] = score
            f2 = open(out_path, "w")
            json.dump(data, f2, indent=4)
            f2.close()
