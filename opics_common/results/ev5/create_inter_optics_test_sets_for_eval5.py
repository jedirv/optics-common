import json
import os
import random
import sys
from pathlib import Path

home_dir = str(Path.home())
root = os.path.join(home_dir, "eval6_systest/inter/scenes/")


class RoomSizeSorter:
    def __init__(self, scene_type, cube_id, scenes_for_cube_id):
        self.scenes = scenes_for_cube_id
        self.scene_type = scene_type

    def get_area_for_scene(self, scene_name):
        path = os.path.join(root, scene_type, scene_name)
        print(f"loading path {path}")
        f = open(path, "r")
        data = json.load(f)
        f.close()
        width = int(data["roomDimensions"]["x"])
        depth = int(data["roomDimensions"]["z"])
        area = width * depth
        return area

    def get_size_sorted_scenes(self):
        if not self.scene_type in ["lava", "ramps", "holes", "tool"]:
            return self.scenes
        scene_infos = []
        print(" BEFORE SORTING")
        for scene in self.scenes:
            area = self.get_area_for_scene(scene)
            scene_info = {}
            scene_info["name"] = scene
            scene_info["area"] = area
            scene_infos.append(scene_info)
        for scene_info in scene_infos:
            print(
                f'area for scene {scene_info["name"]} is {scene_info["area"]}'
            )

        sorted_scene_infos = sorted(scene_infos, key=lambda d: d["area"])
        print(" AFTER SORTING")
        sorted_scenes = []
        for scene_info in sorted_scene_infos:
            print(
                f'area for scene {scene_info["name"]} is {scene_info["area"]}'
            )
            sorted_scenes.append(scene_info["name"])
        return sorted_scenes


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
root = os.path.join(home_dir, "eval6_systest/inter/scenes/")


def get_full_scene_path(scene_fname):
    scene_type = scene_fname.split("_")[0]
    return os.path.join("inter/scenes", scene_type, scene_fname)


if __name__ == "__main__":
    if not "OPICS_HOME" in os.environ:
        print("")
        print(
            "      ERROR - OPICS_HOME not defined.  Please 'export OPICS_HOME=<parent_of_opics_dir>'"
        )
        print("")
        sys.exit()

    types = os.listdir(root)

    # isolate scenes by type
    scenes_for_type = {}
    for scene_type in types:
        scenes_for_type[scene_type] = os.listdir(
            os.path.join(root, scene_type)
        )

    # get hypercubes for each type
    cube_ids_per_type = {}
    for scene_type in types:
        cube_ids_per_type[scene_type] = set()
        for scene in scenes_for_type[scene_type]:
            cube_id = scene.split("_")[4]
            cube_ids_per_type[scene_type].add(cube_id)

    # isolate hypercube scenes
    scenes_for_type_with_cube_id = {}
    for scene_type in types:
        scenes_for_type_with_cube_id[scene_type] = {}
        for cube_id in cube_ids_per_type[scene_type]:
            scenes_for_cube_id = []
            for scene in scenes_for_type[scene_type]:
                if scene.split("_")[4] == cube_id:
                    scenes_for_cube_id.append(scene)
            rss = RoomSizeSorter(scene_type, cube_id, scenes_for_cube_id)
            scenes_for_cube_id = rss.get_size_sorted_scenes()
            scenes_for_type_with_cube_id[scene_type][
                cube_id
            ] = scenes_for_cube_id
            print(
                f"count of scenes for {scene_type} {cube_id} is {len(scenes_for_cube_id)}"
            )

    for scene_type in types:
        for cube_id in cube_ids_per_type[scene_type]:
            # accomplish randomizing the color palette
            if not scene_type in ["lava", "ramps", "holes", "tool"]:
                random.shuffle(
                    scenes_for_type_with_cube_id[scene_type][cube_id]
                )

    final_sets_weighted = {}
    final_sets_unweighted = {}
    for i in range(50):
        final_sets_weighted[i] = []
        final_sets_unweighted[i] = []
        for scene_type in types:
            for cube_id in cube_ids_per_type[scene_type]:
                if cube_id in weighted_codes_for_type[scene_type]:
                    final_sets_weighted[i].append(
                        scenes_for_type_with_cube_id[scene_type][cube_id][i]
                    )
                else:
                    final_sets_unweighted[i].append(
                        scenes_for_type_with_cube_id[scene_type][cube_id][i]
                    )
    for i in range(25):
        final_sets_weighted[i] = sorted(final_sets_weighted[i])
        final_sets_unweighted[i] = sorted(final_sets_unweighted[i])

    for i in range(25):
        print(
            f"length of set {i} in weighted is {len(final_sets_weighted[i])}"
        )
    for i in range(25):
        print(
            f"length of set {i} in unweighted is {len(final_sets_unweighted[i])}"
        )

    print("....final_sets_weighted[0]")
    for i in range(70):
        print(final_sets_weighted[0][i])

    print("....final_sets_unweighted[0]")
    for i in range(52):
        print(final_sets_unweighted[0][i])

    # reconsitute as check

    test_num_counts = {}
    for i in range(25):
        for scene_file in final_sets_weighted[i]:
            test_num = scene_file.split("_")[2]
            if test_num not in test_num_counts:
                test_num_counts[test_num] = 0
            test_num_counts[test_num] += 1

    for test_num in test_num_counts:
        print(f"weighted:  {test_num} {test_num_counts[test_num]}")

    test_num_counts = {}
    for i in range(25):
        for scene_file in final_sets_unweighted[i]:
            test_num = scene_file.split("_")[2]
            if test_num not in test_num_counts:
                test_num_counts[test_num] = 0
            test_num_counts[test_num] += 1

    for test_num in test_num_counts:
        print(f"unweighted:  {test_num} {test_num_counts[test_num]}")

    weighted_dir = os.path.join(
        home_dir, "eval6_systest", "inter_mod", "test_sets", "eval5_weighted"
    )
    unweighted_dir = os.path.join(
        home_dir, "eval6_systest", "inter_mod", "test_sets", "eval5_unweighted"
    )
    os.makedirs(weighted_dir, exist_ok=True)
    os.makedirs(unweighted_dir, exist_ok=True)
    for i in range(25):
        two_digit_number = "{:02d}".format(i)
        test_set_path = os.path.join(
            weighted_dir, f"test_set_ev5_weighted_{two_digit_number}.txt"
        )
        f = open(test_set_path, "w")
        for scene_path in final_sets_weighted[i]:
            full_scene_path = get_full_scene_path(scene_path)
            f.write(full_scene_path + "\n")
        f.close()

    for i in range(25):
        two_digit_number = "{:02d}".format(i)
        test_set_path = os.path.join(
            unweighted_dir, f"test_set_ev5_unweighted_{two_digit_number}.txt"
        )
        f = open(test_set_path, "w")
        for scene_path in final_sets_unweighted[i]:
            full_scene_path = get_full_scene_path(scene_path)
            f.write(full_scene_path + "\n")
        f.close()
