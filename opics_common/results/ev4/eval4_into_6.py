import argparse
import os
import sys

types = ["sc", "op", "stc", "coll", "grav"]
files_for_type = {}


def usage_and_quit():
    print(
        "usage:  python eval5_training_set_rename.py --scene_dir <parent_scene_dir>"
    )
    sys.exit()


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene_dir", default="junk")
    return parser


if __name__ == "__main__":
    args = make_parser().parse_args()
    scene_dir = args.scene_dir
    if scene_dir == "junk":
        usage_and_quit()
    if not os.path.isdir(scene_dir):
        print("scene_dir dir {} doesn't exist.".format(scene_dir))

    print("scene_dir {}".format(scene_dir))

    for type in types:
        files_for_type[type] = {}
        for i in range(6):
            files_for_type[type][i] = []

    print("one 1300 file dataset will have...")
    for type in types:
        dirname = "eval4_" + type
        type_dir = os.path.join(scene_dir, dirname)
        filenames = os.listdir(type_dir)
        filecount = len(filenames)
        filecount_per_set = int(len(filenames) / 6)
        cur_set_count = 0
        cur_set = 0
        max_test_num = 0
        for i in range(filecount):
            filename = filenames[i]
            test_num = int(filename.split("_")[2])
            if test_num > max_test_num:
                max_test_num = test_num
            files_for_type[type][cur_set].append(filename)
            cur_set_count += 1
            if cur_set_count == filecount_per_set:
                cur_set += 1
                cur_set_count = 0
        scenes_per_test = int(filecount / max_test_num)
        # print('there are {} tests for type {} ...and {} scenes per test'.format(max_test_num, type, scenes_per_test))
        print(
            "    {} {}\tscenes, which is comprosed of {} tests of {} scenes each".format(
                filecount_per_set,
                type,
                filecount_per_set / max_test_num,
                scenes_per_test,
            )
        )
    for type in types:
        for i in range(6):
            print(
                "set {} type {} : {}".format(
                    i, type, len(files_for_type[type][i])
                )
            )
    for i in range(6):
        num = i + 1
        dataset_name = "eval4_dataset_" + str(num) + "_of_6.txt"

        f = open(dataset_name, "w")
        names_to_write = []
        for type in types:
            files = files_for_type[type][i]
            for file in files:
                names_to_write.append(file + "\n")
        f.writelines(names_to_write)
        f.close()
