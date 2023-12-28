import os
import random
import sys
from pathlib import Path


def usage():
    print("python create_systest_sets_from_eval5_scenes.py avoe|pvoe|inter")


if __name__ == "__main__":
    if not "OPICS_HOME" in os.environ:
        print("")
        print(
            "      ERROR - OPICS_HOME not defined.  Please 'export OPICS_HOME=<parent_of_opics_dir>'"
        )
        print("")
        sys.exit()

    if len(sys.argv) < 2:
        usage()
        sys.exit()

    if sys.argv[1] not in ["avoe", "pvoe", "inter"]:
        usage()
        sys.exit()
    proj = sys.argv[1]
    if proj != "pvoe":
        print("only pvoe is supported so far...")
        sys.exit()

    novel_shapes_to_exclude = {}
    # see REASON_FOR_EXCLUDING_SOME_OP_SCENES_FROM_OPTICS_TEST below for reason for excluding these op codes
    novel_shapes_to_exclude["op"] = [
        "H1",
        "E1",
        "B1",
        "Q1",
        "N1",
        "K1",
        "H2",
        "E2",
        "B2",
        "Q2",
        "N2",
        "K2",
        "B3",
        "E3",
        "H3",
    ]
    novel_shapes_to_exclude["sc"] = []
    novel_shapes_to_exclude["stc"] = []
    novel_shapes_to_exclude["coll"] = []
    novel_shapes_to_exclude["grav"] = []
    home_dir = str(Path.home())
    root = os.path.join(home_dir, "eval6_systest/" + proj + "/scenes/full")
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
            if not cube_id in novel_shapes_to_exclude[scene_type]:
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
            scenes_for_type_with_cube_id[scene_type][
                cube_id
            ] = scenes_for_cube_id
            print(
                f"count of scenes for {scene_type} {cube_id} is {len(scenes_for_cube_id)}"
            )

    for scene_type in types:
        for cube_id in cube_ids_per_type[scene_type]:
            random.shuffle(scenes_for_type_with_cube_id[scene_type][cube_id])

    final_sets = {}
    for i in range(50):
        final_sets[i] = []
        for scene_type in types:
            for cube_id in cube_ids_per_type[scene_type]:
                final_sets[i].append(
                    scenes_for_type_with_cube_id[scene_type][cube_id][i]
                )
    for i in range(50):
        final_sets[i] = sorted(final_sets[i])

    for i in range(50):
        print(f"length of set {i} is {len(final_sets[i])}")

    for i in range(118):
        print(final_sets[0][i])

    # reconsitute as check

    test_num_counts = {}
    for i in range(50):
        for scene_file in final_sets[i]:
            test_num = scene_file.split("_")[2]
            if test_num not in test_num_counts:
                test_num_counts[test_num] = 0
            test_num_counts[test_num] += 1

    for test_num in test_num_counts:
        print(f"{test_num} {test_num_counts[test_num]}")

    for i in range(50):
        two_digit_number = "{:02d}".format(i)
        test_set_path = os.path.join(
            home_dir,
            "eval6_systest",
            proj,
            "test_sets",
            f"test_set_{two_digit_number}.txt",
        )
        f = open(test_set_path, "w")
        for scene_path in final_sets[i]:
            f.write(scene_path + "\n")
        f.close()


# From 11/7/22 discord messaging between Jed and Chanho....

# Jed:Looking at test organization another way, it would be the simplifying in a number of aspects if I
# make each test set be equivalent to the situation count, where the color palette is randomly chosen
# for each situation - i.e. just treat novelty as a different situation just like TA2 does.   This would mean,
# just like the eval, we would have 50 test sets where each test has every situation represented , but rather
# than having a consistent color palette, each scene in each test would have it's color palette assigned using
#  a random draw.   The notion of a "test" would remain somewhat consistent with the eval, the size of each set
# would be small enough that running an additional set wouldn't take as long.  So, if the three projects are in
# contention, for example, and we have some hours before the inter tests need to start, for example, we could
# continue running scenes and finish another set.
# So this would mean, regardless of whether or not novelty was represented in the hypercubes for that scene type,
# it would always be:

# for color in random_draw(colors)
#        for situation in all_situations

# to construct each test set, and there would be 50  test sets defined.  Each cycle, we'd get through as many
# of those as we had time for.   Each set would have 133 scenes broken down like this:

# coll    24
# grav   30
# sc       10
# stc     24
# op      45

#  REASON_FOR_EXCLUDING_SOME_OP_SCENES_FROM_OPTICS_TEST
#  The one issue I see is that op scenes are much greater in number than the others - op has three dimensions of
# novelty  -  there are actually only 15 situations where dynamics vary.  I could omit the size novelty scenes,
# which would bring that count down to 30, which would make each set 118.  This would better balance the scene
# counts in each set and still cover all situation dynamics

# Chanho — 11/07/2022
# This sounds good to me. I also agree with your last point to better balance different scene types by decreasing
# the dimensions of novelty for OP.
