import os
import sys
from pathlib import Path


def usage():
    print("python create_inter_optics_test_sets_for_eval5.py")


weighted_codes_for_type               = {}
weighted_codes_for_type["agentid"] = [
    "A1",
    "B1",
    "E1",
    "F1",
    "A2",
    "B2",
    "E2",
    "F2",
]
weighted_codes_for_type["cont"]       = ["A1", "G1", "M1", "A2", "G2", "M2"]
weighted_codes_for_type["holes"]      = ["B1", "C1"]
weighted_codes_for_type["iop"]        = ["A1", "C1", "A2", "C2"]
weighted_codes_for_type["lava"]       = ["B1", "C1"]
weighted_codes_for_type["movtarg"]    = ["A1", "B1", "E1", "F1", "I1", "J1"]
weighted_codes_for_type["obst"]       = ["A1", "C1", "A2", "C2"]
weighted_codes_for_type["occl"] = [
    "A1",
    "C1",
    "E1",
    "G1",
    "I1",
    "K1",
    "A2",
    "C2",
    "E2",
    "G2",
    "I2",
    "K2",
]
weighted_codes_for_type["ramps"] = [
    "B1",
    "E1",
    "H1",
    "K1",
    "C1",
    "F1",
    "I1",
    "L1",
]
weighted_codes_for_type["solid"]      = ["A1", "B1", "C1"]
weighted_codes_for_type["spelim"]     = ["A1", "C1", "A2", "C2"]
weighted_codes_for_type["suprel"] = [
    "A1",
    "B1",
    "C1",
    "D1",
    "E1",
    "F1",
    "G1",
    "H1",
    "I1",
]
weighted_codes_for_type["tool"]       = ["A1", "C1", "E1", "G1"]


unweighted_codes_for_type             = {}
unweighted_codes_for_type["agentid"]  = []  # none here
unweighted_codes_for_type["cont"] = [
    "D1",
    "J1",
    "P1",
    "D2",
    "J2",
    "P2",
]  # ball outside container
unweighted_codes_for_type["holes"]    = ["A1"]  # direct path to ball exists
unweighted_codes_for_type["iop"]      = []  # none here
unweighted_codes_for_type["lava"]     = ["A1"]  # direct path to ball exists
unweighted_codes_for_type["movtarg"] = [
    "C1",
    "D1",
    "G1",
    "H1",
    "K1",
    "L1",
]  # no lava
unweighted_codes_for_type["obst"] = [
    "B1",
    "D1",
    "B2",
    "D2",
]  # direct path available
unweighted_codes_for_type["occl"] = [
    "B1",
    "D1",
    "F1",
    "H1",
    "J1",
    "L1",
    "B2",
    "D2",
    "F2",
    "H2",
    "J2",
    "L2",
]  # target not hidden by occluder
unweighted_codes_for_type["ramps"] = [
    "A1",
    "D1",
    "G1",
    "J1",
]  # ball is on floor
unweighted_codes_for_type["solid"]    = []  # none here
unweighted_codes_for_type["spelim"] = [
    "B1",
    "D1",
    "B2",
    "D2",
    "B3",
    "D3",
    "B4",
    "D4",
    "A3",
    "C3",
    "A4",
    "C4",
]  # ball not hidden, could be either(?)
unweighted_codes_for_type["suprel"]   = []  # none here
unweighted_codes_for_type["tool"]     = ["B1", "D1", "F1", "H1"]  # tool not needed

home_dir = str(Path.home())
root = os.path.join(home_dir, "eval6_systest/avoe/scenes/eval5")


def get_full_scene_path(scene_fname):
    scene_type = scene_fname.split("_")[0]
    return os.path.join("avoe/scenes/eval5", scene_type, scene_fname)


if __name__ == "__main__":
    if not "OPICS_HOME" in os.environ:
        print("")
        print(
            "      ERROR - OPICS_HOME not defined.  Please 'export OPICS_HOME=<parent_of_opics_dir>'"
        )
        print("")
        sys.exit()

    types = ["irrat", "multa", "opref"]

    # isolate scenes by type
    scenes_for_type = {}
    for scene_type in types:
        scenes_for_type[scene_type] = os.listdir(
            os.path.join(root, scene_type)
        )

    # sort them
    for scene_type in types:
        scenes_for_type[scene_type] = sorted(scenes_for_type[scene_type])

    for scene_type in types:
        print(
            f"len scenes for {scene_type} {len(scenes_for_type[scene_type])}"
        )
    #
    # avoe has tests in pairs - one expected and one unexpected in each "test", both the same color scheme
    # there are 1000 pairs of each scene type
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

    eval5_dir = os.path.join(
        home_dir, "eval6_systest", "avoe", "test_sets", "eval5"
    )
    os.makedirs(eval5_dir, exist_ok=True)
    for test_set_num in range(test_set_count):
        two_digit_number = "{:02d}".format(test_set_num)
        test_set_path = os.path.join(
            eval5_dir, f"test_set_ev5_{two_digit_number}.txt"
        )
        print(f"...writing test set {test_set_path}")
        f = open(test_set_path, "w")
        for scene_path in test_sets[test_set_num]:
            full_scene_path = get_full_scene_path(scene_path)
            f.write(full_scene_path + "\n")
        f.close()
