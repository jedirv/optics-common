import os
import sys

#
# https://docs.google.com/spreadsheets/d/1kFjzills534NYjNBf018kqaFpH3CvnFnZrMvoG2l3Bs/edit#gid=732801562
# has How many different situations there are for each scene type when we ignore novelty as a factor
#
# the hypercube codes below in the *_keys list represent each situation ignoring novelty (the corresponding cubes that involved novel objects are
# omitted because they are redundant given that novelty now has no meaning for this data going forrward - they were onoly novel for eval5)


def usage():
    print("python create_pvoe_rule_based_dev_set.py <renamed_file_root> ")


def collect_scenes_with_codes(type, root_dir, codes, count):
    scene_path_dict = {}

    files = sorted(os.listdir(root_dir))
    for code in codes:
        print(f"[{code}]")
        scene_path_dict[code] = []
        for f in files:
            name = f.split(".")[0]
            parts = name.split("_")
            cube_code = parts[4]
            if cube_code == code:
                path = os.path.join(root_dir, f)
                scene_path_dict[code].append(path)
                print(f"{f}")
                if len(scene_path_dict[code]) == count:
                    break
    return scene_path_dict


def copy_scenes(type, cube_ids, paths_dict, target_root_dir):
    for cube_id in cube_ids:
        for path in paths_dict[cube_id]:
            target_path = f"{target_root_dir}/{type}/{os.path.basename(path)}"
            os.system(f"cp {path} {target_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit()
    target_root_dir = "ruleBasedDevSet"
    if not os.path.exists(target_root_dir):
        os.mkdir(target_root_dir)
    for type in ["coll", "op", "sc", "stc", "grav"]:
        target_type_dir = os.path.join(target_root_dir, type)
        if not os.path.exists(target_type_dir):
            os.mkdir(target_type_dir)

    root_dir = sys.argv[1]
    coll_dir = f"{root_dir}/coll"
    factor_to_reach_100 = 10
    coll_keys = [
        "A1",
        "G1",
        "B1",
        "H1",
        "C1",
        "L1",
        "A2",
        "G2",
        "B2",
        "C2",
        "L2",
        "K2",
    ]
    print(
        f"coll scenes have {len(coll_keys)} different situations, when novelty is ignored"
    )
    print(f"...these representative cube_ids have been chosen: {coll_keys}")
    print(f"...to reach 100, need {factor_to_reach_100} each")
    print(
        f"...for a total of {len(coll_keys)*factor_to_reach_100} coll scenes"
    )
    paths_dict = collect_scenes_with_codes(
        "coll", coll_dir, coll_keys, factor_to_reach_100
    )
    copy_scenes("coll", coll_keys, paths_dict, target_root_dir)

    op_dir = f"{root_dir}/op"
    factor_to_reach_100 = 10
    op_keys = [
        "G1",
        "G2",
        "G3",
        "D1",
        "D2",
        "D3",
        "A1",
        "A2",
        "A3",
        "P1",
        "P2",
        "M1",
        "M2",
        "J1",
        "J2",
    ]
    print("")
    print("")
    print("")
    print(
        f"op scenes have {len(op_keys)} different situations, when novelty is ignored"
    )
    print(f"...these representative cube_ids have been chosen: {op_keys}")
    print(f"...to reach 100, need {factor_to_reach_100} each")
    print(f"...for a total of {len(op_keys)*factor_to_reach_100} op scenes")
    paths_dict = collect_scenes_with_codes(
        "op", op_dir, op_keys, factor_to_reach_100
    )
    copy_scenes("op", op_keys, paths_dict, target_root_dir)

    grav_dir = f"{root_dir}/grav"
    factor_to_reach_100 = 4
    grav_keys = [
        "A1",
        "AA1",
        "B1",
        "BB1",
        "C1",
        "CC1",
        "D1",
        "DD1",
        "EE1",
        "FF1",
        "GG1",
        "HH1",
        "I1",
        "J1",
        "K1",
        "L1",
        "M1",
        "N1",
        "O1",
        "P1",
        "S1",
        "SS1",
        "T1",
        "TT1",
        "UU1",
        "VV1",
        "W1",
        "X1",
        "Y1",
        "Z1",
    ]
    print("")
    print("")
    print("")
    print(f"grav scenes have {len(grav_keys)} different situations")
    print(f"...all cube_ids needed because novelty not in play: {grav_keys}")
    print(f"...to reach 100, need {factor_to_reach_100} each")
    print(
        f"...for a total of {len(grav_keys)*factor_to_reach_100} grav scenes"
    )
    paths_dict = collect_scenes_with_codes(
        "grav", grav_dir, grav_keys, factor_to_reach_100
    )
    copy_scenes("grav", grav_keys, paths_dict, target_root_dir)

    sc_dir = f"{root_dir}/sc"
    factor_to_reach_100 = 20
    sc_keys = ["L4", "L2", "J1", "B1", "D2"]
    print("")
    print("")
    print("")
    print(
        f"sc scenes have {len(sc_keys)} different situations, when novelty is ignored"
    )
    print(f"...these representative cube_ids have been chosen: {sc_keys}")
    print(f"...to reach 100, need {factor_to_reach_100} each")
    print(f"...for a total of {len(sc_keys)*factor_to_reach_100} sc scenes")
    paths_dict = collect_scenes_with_codes("sc", sc_dir, sc_keys, 20)
    copy_scenes("sc", sc_keys, paths_dict, target_root_dir)

    stc_dir = f"{root_dir}/stc"
    factor_to_reach_100 = 10
    stc_keys = [
        "C1",
        "A1",
        "G1",
        "E1",
        "C2",
        "G2",
        "A2",
        "E2",
        "C3",
        "A3",
        "G3",
        "E3",
    ]
    print("")
    print("")
    print("")
    print(
        f"stc scenes have {len(stc_keys)} different situations, when novelty is ignored"
    )
    print(f"...these representative cube_ids have been chosen: {stc_keys}")
    print(f"...to reach 100, need {factor_to_reach_100} each")
    print(f"...for a total of {len(stc_keys)*factor_to_reach_100} stc scenes")
    paths_dict = collect_scenes_with_codes("stc", stc_dir, stc_keys, 10)
    copy_scenes("stc", stc_keys, paths_dict, target_root_dir)
