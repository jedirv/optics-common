import os
import sys


def get_rel_scene_paths_of_type(
    test_sets_dir, test_set_files, scene_type, cube_ids
):
    rel_scene_paths_for_type = []
    for test_set_file in test_set_files:
        f = open(os.path.join(test_sets_dir, test_set_file), "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            if scene_type + "_" in line:
                cube_id = line.split("_")[4]
                if cube_id in cube_ids:
                    rel_scene_paths_for_type.append(line)
    return rel_scene_paths_for_type


# coll scenes have 12 different situations, when novelty is ignored
# ...these representative cube_ids have been chosen: ['A1', 'G1', 'B1', 'H1', 'C1', 'L1', 'A2', 'G2', 'B2', 'C2', 'L2', 'K2']
# ...to reach 100, need 10 each
# ...for a total of 120 coll scenes
def generate_manifest_lines(rel_scene_paths, scene_type, cubes):
    lines = []
    lines.append(
        f"{scene_type} scenes have {len(cubes)} different situations, (novelty is ignored as a factor if it is relevant to scene type)"
    )
    lines.append(f"...these representative cube_ids have been chosen: {cubes}")
    lines.append(f"...10 each as per test_set split")
    lines.append(f"...for a total of {len(cubes) * 10} {scene_type} scenes")
    for cube in cubes:
        lines.append(f"[{cube}]")
        filename_lines = []
        for rel_scene_path in rel_scene_paths:
            cube_string = "_" + cube + "_"
            if cube_string in rel_scene_path:
                filename_lines.append(rel_scene_path.split("/")[-1].rstrip())
        filename_lines.sort()
        lines.extend(filename_lines)
    return lines


def copy_scenes(dest_dir, root_dir, rel_scene_paths_coll):
    print(f"dest_dir: {dest_dir}")
    for rel_scene_path in rel_scene_paths_coll:
        src = os.path.join(root_dir, rel_scene_path.rstrip())
        command = f"cp {src} {dest_dir}"
        os.system(command)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: python create_pvoe_rule_based_dev_set_from_test_sets.py <test_sets_dir> <target_dir>"
        )
        sys.exit(1)
    test_sets_dir = sys.argv[1]
    target_dir = sys.argv[2]
    if not os.path.isdir(test_sets_dir):
        print(f"Error: {test_sets_dir} is not a directory")
        sys.exit(1)

    test_set_files = os.listdir(test_sets_dir)
    test_set_files = [f for f in test_set_files if f.endswith(".txt")]

    coll_cubes_no_novelty = [
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
    op_cubes_no_novelty = [
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
    grav_cubes = [
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
    sc_cubes_no_novelty = ["L4", "L2", "J1", "B1", "D2"]
    stc_no_novelty = [
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

    rel_scene_paths_coll = get_rel_scene_paths_of_type(
        test_sets_dir, test_set_files, "coll", coll_cubes_no_novelty
    )
    rel_scene_paths_op = get_rel_scene_paths_of_type(
        test_sets_dir, test_set_files, "op", op_cubes_no_novelty
    )
    rel_scene_paths_sc = get_rel_scene_paths_of_type(
        test_sets_dir, test_set_files, "sc", sc_cubes_no_novelty
    )
    rel_scene_paths_stc = get_rel_scene_paths_of_type(
        test_sets_dir, test_set_files, "stc", stc_no_novelty
    )
    rel_scene_paths_grav = get_rel_scene_paths_of_type(
        test_sets_dir, test_set_files, "grav", grav_cubes
    )

    manifest_lines = []
    coll_manifest_lines = generate_manifest_lines(
        rel_scene_paths_coll, "coll", coll_cubes_no_novelty
    )
    manifest_lines.extend(coll_manifest_lines)
    op_manifest_lines = generate_manifest_lines(
        rel_scene_paths_op, "op", op_cubes_no_novelty
    )
    manifest_lines.extend(op_manifest_lines)
    sc_manifest_lines = generate_manifest_lines(
        rel_scene_paths_sc, "sc", sc_cubes_no_novelty
    )
    manifest_lines.extend(sc_manifest_lines)
    stc_manifest_lines = generate_manifest_lines(
        rel_scene_paths_stc, "stc", stc_no_novelty
    )
    manifest_lines.extend(stc_manifest_lines)
    grav_manifest_lines = generate_manifest_lines(
        rel_scene_paths_grav, "grav", grav_cubes
    )
    manifest_lines.extend(grav_manifest_lines)

    f = open("ruleBasedDevSet_V2_fileList.txt", "w")
    for line in manifest_lines:
        f.write(line + "\n")
    f.close()

    os.makedirs(target_dir, exist_ok=True)
    coll_dir = os.path.join(target_dir, "coll")
    os.makedirs(coll_dir, exist_ok=True)
    op_dir = os.path.join(target_dir, "op")
    os.makedirs(op_dir, exist_ok=True)
    sc_dir = os.path.join(target_dir, "sc")
    os.makedirs(sc_dir, exist_ok=True)
    stc_dir = os.path.join(target_dir, "stc")
    os.makedirs(stc_dir, exist_ok=True)
    grav_dir = os.path.join(target_dir, "grav")
    os.makedirs(grav_dir, exist_ok=True)

    copy_scenes(coll_dir, "/home/ubuntu/eval6_systest", rel_scene_paths_coll)
    copy_scenes(op_dir, "/home/ubuntu/eval6_systest", rel_scene_paths_op)
    copy_scenes(sc_dir, "/home/ubuntu/eval6_systest", rel_scene_paths_sc)
    copy_scenes(stc_dir, "/home/ubuntu/eval6_systest", rel_scene_paths_stc)
    copy_scenes(grav_dir, "/home/ubuntu/eval6_systest", rel_scene_paths_grav)
