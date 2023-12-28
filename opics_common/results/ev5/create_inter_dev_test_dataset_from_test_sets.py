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


def get_cubes_for_scenes(scene_paths):
    cubes = []
    for scene_path in scene_paths:
        scene_name = os.path.basename(scene_path)
        cube = scene_name.split("_")[4]
        if cube not in cubes:
            cubes.append(cube)
    return cubes


def usage():
    print(
        "Usage: python create_inter_dev_test_dataset_from_test_sets.py weighted|unweighted <test_sets_dir> <target_dir>"
    )


#
#  The assumption in play is that the test_sets that have already been created for inter capture all the thinking about
#  which cube codes should be in play, so this script is merely
#    - scanning the test_sets,
#    - sorting the rel paths by scene_type
#    - copying the corresponding scene json files into the appropr scene_type dir
#

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
        sys.exit(1)
    weighting = sys.argv[1]
    test_sets_dir = sys.argv[2]
    target_dir = sys.argv[3]
    if not os.path.isdir(test_sets_dir):
        print(f"Error: {test_sets_dir} is not a directory")
        usage()
        sys.exit(1)

    if not os.path.isdir(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    systest_dir = "/home/ubuntu/eval6_systest"

    test_set_files = os.listdir(test_sets_dir)
    test_set_files = [f for f in test_set_files if f.endswith(".txt")]

    paths_for_scene_type = {}

    for test_set_file in test_set_files:
        print(f"Processing {test_set_file}")
        f = open(os.path.join(test_sets_dir, test_set_file), "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            full_path = os.path.join(systest_dir, line.rstrip())
            print(f"full_path: {full_path}")
            fname = os.path.basename(full_path)
            scene_type = fname.split("_")[0]
            if scene_type not in paths_for_scene_type:
                paths_for_scene_type[scene_type] = []
            paths_for_scene_type[scene_type].append(full_path)
    for scene_type in paths_for_scene_type:
        paths_for_scene_type[scene_type].sort()

    # copy the files

    for scene_type in paths_for_scene_type:
        dest_dir = os.path.join(target_dir, scene_type)
        if not os.path.isdir(dest_dir):
            os.mkdir(dest_dir)
        for full_path in paths_for_scene_type[scene_type]:
            print(f"Copying {full_path} to {dest_dir}")
            command = f"cp {full_path} {dest_dir}"
            os.system(command)

    # create manifest which lists filenames by type by cube
    # xyz scenes have <n> different situations for <weighting> scenes
    # ...represented by these cubes: [...]
    # ...to reach 100, need 10 each
    # ...for a total of 120 coll scenes
    manifest_lines = []
    for scene_type in paths_for_scene_type:
        cubes_for_type = get_cubes_for_scenes(paths_for_scene_type[scene_type])
        cubes_for_type.sort()
        manifest_lines.append(
            f"{scene_type} scenes have {len(cubes_for_type)} different situations (for {weighting} scenes)"
        )
        manifest_lines.append(
            f"...represented by these cubes: {cubes_for_type}"
        )
        manifest_lines.append(
            f"...totaling {len(paths_for_scene_type[scene_type])} scenes"
        )

        for cube in cubes_for_type:
            manifest_lines.append(f"[{cube}]")
            for full_path in paths_for_scene_type[scene_type]:
                fname = os.path.basename(full_path)
                if cube in fname:
                    manifest_lines.append(fname)

    target_dir_parent = os.path.dirname(target_dir)
    target_dir_name = os.path.basename(target_dir)
    manifest_path = os.path.join(
        target_dir_parent, f"{target_dir_name}_fileList.txt"
    )
    print(f"Writing manifest to {manifest_path}")
    f = open(manifest_path, "w")
    for line in manifest_lines:
        print(line)
        f.write(f"{line}" + "\n")
    f.close()

    # rel_scene_paths_coll = get_rel_scene_paths_of_type(test_sets_dir, test_set_files, 'coll', coll_cubes_no_novelty)
    # rel_scene_paths_op   = get_rel_scene_paths_of_type(test_sets_dir, test_set_files, 'op',   op_cubes_no_novelty)
    # rel_scene_paths_sc   = get_rel_scene_paths_of_type(test_sets_dir, test_set_files, 'sc',   sc_cubes_no_novelty)
    # rel_scene_paths_stc  = get_rel_scene_paths_of_type(test_sets_dir, test_set_files, 'stc',  stc_no_novelty)
    # rel_scene_paths_grav = get_rel_scene_paths_of_type(test_sets_dir, test_set_files, 'grav', grav_cubes)

    # manifest_lines = []
    # coll_manifest_lines = generate_manifest_lines(rel_scene_paths_coll, 'coll', coll_cubes_no_novelty)
    # manifest_lines.extend(coll_manifest_lines)
    # op_manifest_lines = generate_manifest_lines(rel_scene_paths_op, 'op', op_cubes_no_novelty)
    # manifest_lines.extend(op_manifest_lines)
    # sc_manifest_lines = generate_manifest_lines(rel_scene_paths_sc, 'sc', sc_cubes_no_novelty)
    # manifest_lines.extend(sc_manifest_lines)
    # stc_manifest_lines = generate_manifest_lines(rel_scene_paths_stc, 'stc', stc_no_novelty)
    # manifest_lines.extend(stc_manifest_lines)
    # grav_manifest_lines = generate_manifest_lines(rel_scene_paths_grav, 'grav', grav_cubes)
    # manifest_lines.extend(grav_manifest_lines)

    # f = open('ruleBasedDevSet_V2_fileList.txt', 'w')
    # for line in manifest_lines:
    #     f.write(line + '\n')
    # f.close()

    # os.makedirs(target_dir, exist_ok=True)
    # coll_dir = os.path.join(target_dir, 'coll')
    # os.makedirs(coll_dir, exist_ok=True)
    # op_dir = os.path.join(target_dir, 'op')
    # os.makedirs(op_dir, exist_ok=True)
    # sc_dir = os.path.join(target_dir, 'sc')
    # os.makedirs(sc_dir, exist_ok=True)
    # stc_dir = os.path.join(target_dir, 'stc')
    # os.makedirs(stc_dir, exist_ok=True)
    # grav_dir = os.path.join(target_dir, 'grav')
    # os.makedirs(grav_dir, exist_ok=True)

    # copy_scenes(coll_dir, '/home/ubuntu/eval6_systest', rel_scene_paths_coll )
    # copy_scenes(op_dir,   '/home/ubuntu/eval6_systest', rel_scene_paths_op )
    # copy_scenes(sc_dir,   '/home/ubuntu/eval6_systest', rel_scene_paths_sc )
    # copy_scenes(stc_dir,  '/home/ubuntu/eval6_systest', rel_scene_paths_stc )
    # copy_scenes(grav_dir, '/home/ubuntu/eval6_systest', rel_scene_paths_grav )
