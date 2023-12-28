import os
import sys
from pathlib import Path


def usage():
    print("python create_avoe_optics_test_sets_for_eval6.py")




def get_full_scene_path(scene_fname):
    scene_type = scene_fname.split("_")[0]
    return os.path.join("avoe/scenes/eval6", scene_type, scene_fname)


if __name__ == "__main__":

    home_dir = str(Path.home())
    root = os.path.join(home_dir, "eval6_systest/avoe/scenes/eval6")
    types = ["irrat", "multa", "opref", "anona", "socapp", "socimit"]

    # isolate scenes by type
    scenes_for_type = {}
    for scene_type in types:
        scenes_for_type[scene_type] = sorted(os.listdir(os.path.join(root, scene_type)))

    # sort them
    # for scene_type in types:
    #     scenes_for_type[scene_type] = sorted(scenes_for_type[scene_type])

    for scene_type in types:
        print(
            f"len scenes for {scene_type} {len(scenes_for_type[scene_type])}"
        )
    #
    # avoe has tests in pairs - one expected and one unexpected in each "test", both the same color scheme
    # there are 1000 pairs of each scene type for the eval5 vintage scenes, but 
    # 4348/2    anona
    # 4200/2    socapp
    # 4232/2    socimit

    # test set approach, until we add the new scene types in:
    # test_set_ev5_00 - test_set_ev5_??
    # each test set has 10 pairs of each scene type, so 10 * 2 * 3 = 60/test set       1000/20 = 50
    #
    test_set_count = 99
    scenes_per_set_per_type = 10 * 2  # (10 pairs)
    test_sets = {}
    for test_set_num in range(test_set_count):
        test_sets[test_set_num] = []
        for scene_count in range(scenes_per_set_per_type):
            for scene_type in types:
                index_for_type = (
                    test_set_num * scenes_per_set_per_type + scene_count
                )
                # print(f'pulling index_for_type {index_for_type} for {scene_type}')
                test_sets[test_set_num].append(
                    scenes_for_type[scene_type][index_for_type]
                )

    # for test_set_num in range(test_set_count):
    #     print(f'test_set_{test_set_num}')
    #     for item in test_sets[test_set_num]:
    #         print(f'    {item}')

    eval6_dir = os.path.join(home_dir, "eval6_systest", "avoe", "test_sets", "eval6")
    os.makedirs(eval6_dir, exist_ok=True)
    for test_set_num in range(test_set_count):
        two_digit_number = "{:02d}".format(test_set_num)
        test_set_path = os.path.join(
            eval6_dir, f"test_set_ev6_{two_digit_number}.txt"
        )
        print(f"...writing test set {test_set_path}")
        f = open(test_set_path, "w")
        for scene_path in test_sets[test_set_num]:
            full_scene_path = get_full_scene_path(scene_path)
            f.write(full_scene_path + "\n")
        f.close()
