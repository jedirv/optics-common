import json
import os
import random
import sys
from pathlib import Path



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
        if not self.scene_type in ["lava", "ramps", "holes", "tool", "tlas", "tlch"]:
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
    print("python create_inter_optics_test_sets_for_eval6.py")


weighted_codes_for_type               = {}
weighted_codes_for_type["agentid"] = ['A1', 'A2', 'B1', 'B2', 'E1', 'E2', 'F1', 'F2', ]
weighted_codes_for_type["cont"]    = ['A1', 'A2', 'G1', 'G2', 'M1', 'M2']
weighted_codes_for_type["holes"]   = ['B1', 'B2', 'C1', 'C2', 'E1', 'E2', 'F1', 'F2']
weighted_codes_for_type["iop"]     = ['A1', 'C1']
weighted_codes_for_type["lava"]    = ['B1', 'B2', 'C1', 'C2', 'E1', 'E2', 'F1', 'F2']
weighted_codes_for_type["movtarg"] = ['A1', 'B1', 'E1', 'F1','I1', 'J1']
weighted_codes_for_type["obst"]    = ["A1", "C1", "A2", "C2"]
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
weighted_codes_for_type["ramps"]   = ['B1', 'B2', 'C1', 'E1', 'E2', 'F1', 'H1', 'I1', 'K1', 'L1', 'N1', 'N2', 'O1', 'Q1', 'Q2', 'R1', 'T1', 'U1', 'W1', 'X1']

weighted_codes_for_type["solid"]   = ["A1", "B1", "C1"]
weighted_codes_for_type["spelim"]  = ['A1', 'A2']
weighted_codes_for_type["suprel"]  = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', ]
weighted_codes_for_type["tool"]    = ['A1', 'C1', 'E1', 'G1', 'I1', 'K1', 'M1', 'O1', 'Q1', 'S1', 'U1', 'W1' ]
weighted_codes_for_type["imit"]    = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1"]
weighted_codes_for_type["spatref"] = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"]
weighted_codes_for_type["math"]    = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'E1', 'E2', 'F1', 'F2', 'G1', 'G2', 'H1', 'H2', 'I1', 'I2', 'J1', 'J2', 'K1', 'K2', 'L1', 'L2', 'M1', 'M2', 'N1', 'N2', 'O1', 'O2', 'P1', 'P2', 'Q1', 'Q2', 'R1', 'R2', 'S1', 'S2', 'T1', 'T2', ]
weighted_codes_for_type["sltk"]    = ['A1', 'F1' ]
weighted_codes_for_type["shell"]   = ['A1', 'B1', 'E1', 'F1', 'I1', 'J1']
weighted_codes_for_type["tlas"]    = ['E3', 'K3', 'Q3', 'W3']
weighted_codes_for_type["numcomp"] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1', ]
weighted_codes_for_type["setrot"]  = ['B1', 'B2', 'C1', 'C2', 'E1', 'E2', 'F1', 'F2', 'H1', 'H2', 'I1', 'I2', 'K1', 'K2', 'L1', 'L2', ]
weighted_codes_for_type["hidtraj"] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', ]
weighted_codes_for_type["reor"]    = ['B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'E1', 'E2', 'F1', 'F2', 'G1', 'G2', 'H1', 'H2', 'I1', 'I2', 'J1', 'J2', 'K1', 'K2', 'L1', 'L2', 'N1', 'N2', 'O1', 'O2', 'P1', 'P2', 'Q1', 'Q2', 'R1', 'R2']
weighted_codes_for_type["coltraj"] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', ]
weighted_codes_for_type["tlch"]    = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', ]





unweighted_codes_for_type             = {}
unweighted_codes_for_type["agentid"] = []
unweighted_codes_for_type["cont"]     = ['D1', 'D2', 'J1', 'J2', 'P1', 'P2']
unweighted_codes_for_type["holes"] = ['A1', 'A2', 'D1', 'D2']
unweighted_codes_for_type["iop"] = ['A2', 'C2']
unweighted_codes_for_type["lava"] = ['A1', 'A2', 'D1', 'D2']
unweighted_codes_for_type["movtarg"] = ['C1', 'D1', 'G1', 'H1', 'K1', 'L1']
unweighted_codes_for_type["obst"] = ['B1', 'B2', 'D1', 'D2']
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

unweighted_codes_for_type["ramps"] = ['A1', 'D1', 'G1', 'J1', 'M1', 'P1', 'S1', 'V1', 'A2', 'D2', 'M2', 'P2']
unweighted_codes_for_type["solid"]    = []  # none here
unweighted_codes_for_type["spelim"] = ['A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']
unweighted_codes_for_type["suprel"] = []  # none here
unweighted_codes_for_type["tool"]     = ['B1', 'D1', 'F1', 'H1','J1', 'L1', 'N1', 'P1', 'R1', 'T1', 'V1','X1']
unweighted_codes_for_type["imit"]     = []  #none as per Word Doc from Koleen
unweighted_codes_for_type["spatref"]    = ["I3", "J3", "K3", "L3"]
unweighted_codes_for_type["math"]    = [] #none as per Word Doc from Koleen
unweighted_codes_for_type["sltk"] = ['B1', 'C1', 'D1', 'E1', 'G1', 'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1', 'P1']
unweighted_codes_for_type["shell"] = ['C1', 'D1', 'G1', 'H1', 'K1', 'L1']
unweighted_codes_for_type["tlas"] = ['F3', 'L3', 'R3', 'X3']
unweighted_codes_for_type["numcomp"] = []
unweighted_codes_for_type["setrot"] = ['A1', 'D1', 'G1',  'J1', 'A2', 'D2', 'G2', 'J2']
unweighted_codes_for_type["hidtraj"] = []
unweighted_codes_for_type["reor"] = ['A1', 'A2', 'M1', 'M2']
unweighted_codes_for_type["coltraj"] = []
unweighted_codes_for_type["tlch"] = []



home_dir = str(Path.home())
root = os.path.join(home_dir, "eval6_systest/inter/scenes/")


def get_full_scene_path(scene_fname):
    scene_type = scene_fname.split("_")[0]
    return os.path.join("inter/scenes/eval6", scene_type, scene_fname)


if __name__ == "__main__":

    home_dir = str(Path.home())
    root = os.path.join(home_dir, "eval6_systest/inter/scenes/eval6")
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

    #
    #  Looks like for eval5, we made 25 sets for weighted and 25 sets for unweighted
    #  - We made copies of weighted sets 20,21,22,23,24  for the weighted dev test set, presumably since these would be the ones we
    #  rarely get to in an optics run?   (But, wouldn't this mean the dev set would have the biggest rooms for the sorted ones???)
    #  - We made copies of weighted sets 15,16,17,18,19  for the weighted reserved set
    #
    #
    #
    #the numbers here are 50, 25, 70, then 52
    #for eval5, there were 72 weighted and 50 unweighted cube_ids - seems like 70 and 52 were a slight botch of that
    #there are 25 tests (color palettes) for each scene_type

    for i in range(25):
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
    weighted_cube_count = 0
    for scene_type in weighted_codes_for_type:
        cube_ids = weighted_codes_for_type[scene_type]
        weighted_cube_count += len(cube_ids)
    print('')
    print(f'final weighted_cube_count : {weighted_cube_count}')
    print('')
    print("....final_sets_weighted[0]")
    for i in range(weighted_cube_count):                 # 70 was weighted count in eval5
        print(final_sets_weighted[0][i])            

    unweighted_cube_count = 0
    for scene_type in unweighted_codes_for_type:
        cube_ids = unweighted_codes_for_type[scene_type]
        unweighted_cube_count += len(cube_ids)
    print('')
    print(f'final unweighted_cube_count : {unweighted_cube_count}')
    print('')
    print("....final_sets_unweighted[0]")
    for i in range(unweighted_cube_count):                 # 52 was unweighed count in eval5
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
        home_dir, "eval6_systest", "inter", "test_sets", "eval6_weighted"
    )
    unweighted_dir = os.path.join(
        home_dir, "eval6_systest", "inter", "test_sets", "eval6_unweighted"
    )
    os.makedirs(weighted_dir, exist_ok=True)
    os.makedirs(unweighted_dir, exist_ok=True)
    for i in range(25):
        two_digit_number = "{:02d}".format(i)
        test_set_path = os.path.join(
            weighted_dir, f"test_set_ev6_weighted_{two_digit_number}.txt"
        )
        f = open(test_set_path, "w")
        for scene_path in final_sets_weighted[i]:
            full_scene_path = get_full_scene_path(scene_path)
            f.write(full_scene_path + "\n")
        f.close()

    for i in range(25):
        two_digit_number = "{:02d}".format(i)
        test_set_path = os.path.join(
            unweighted_dir, f"test_set_ev6_unweighted_{two_digit_number}.txt"
        )
        f = open(test_set_path, "w")
        for scene_path in final_sets_unweighted[i]:
            full_scene_path = get_full_scene_path(scene_path)
            f.write(full_scene_path + "\n")
        f.close()
