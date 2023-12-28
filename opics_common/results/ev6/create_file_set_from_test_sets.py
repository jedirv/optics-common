import os
import sys


def get_rel_scene_paths_of_type(
    test_sets_dir, test_set_files, scene_type
):
    rel_scene_paths_for_type = []
    for test_set_file in test_set_files:
        f = open(os.path.join(test_sets_dir, test_set_file), "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            if scene_type + "_" in line:
                rel_scene_paths_for_type.append(line)
    return rel_scene_paths_for_type


# coll scenes have 12 different situations, when novelty is ignored
# ...these representative cube_ids have been chosen: ['A1', 'G1', 'B1', 'H1', 'C1', 'L1', 'A2', 'G2', 'B2', 'C2', 'L2', 'K2']
# ...to reach 100, need 10 each
# ...for a total of 120 coll scenes
def generate_manifest_lines(rel_scene_paths, scene_type):
    lines = []
    lines.append(f"\n{scene_type} file count is {len(rel_scene_paths)}\n")
    filename_lines = []
    for rel_scene_path in rel_scene_paths:
        filename_lines.append(rel_scene_path.split("/")[-1].rstrip())
    filename_lines.sort()
    lines.extend(filename_lines)
    return lines


def copy_scenes(dest_dir, root_dir, rel_scene_paths_coll):
    print(f"dest_dir: {dest_dir}")
    for rel_scene_path in rel_scene_paths_coll:
        print(f'rel_scene_path is {rel_scene_path}')
        src = os.path.join(root_dir, rel_scene_path.rstrip())
        command = f"cp {src} {dest_dir}"
        os.system(command)

def get_scene_types_from_test_set_file(test_set_path):
    f = open(test_set_path, 'r')
    lines = f.readlines()
    f.close()
    scene_types = set()
    for line in lines:
        parts = line.split('/')
        print(parts)
        scene_type = parts[3]
        scene_types.add(scene_type)
    return scene_types

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: python create_file_set_from_test_sets.py <test_sets_dir> <target_dir>"
        )
        sys.exit(1)
    test_sets_dir = sys.argv[1]
    target_dir = sys.argv[2]
    if not os.path.isdir(test_sets_dir):
        print(f"Error: {test_sets_dir} is not a directory")
        sys.exit(1)

    test_set_files = os.listdir(test_sets_dir)
    test_set_files = [f for f in test_set_files if f.endswith(".txt")]

    first_test_set_path = os.path.join(test_sets_dir, test_set_files[0])
    scene_types = get_scene_types_from_test_set_file(first_test_set_path)
    for scene_type in sorted(scene_types):
        print(f'scene_type : {scene_type}')

    test_sets_name = os.path.basename(test_sets_dir)
    if 'inter' in test_sets_dir:
        proj = 'inter'
    elif 'pvoe' in test_sets_dir:
        proj = 'pvoe'
    elif 'avoe' in test_sets_dir:
        proj = 'avoe'
    else:
        print('could not find avoe, inter, or pvoe in test_sets_dir to help name manifest file')
    file_list_fname = f"{proj}_{test_sets_name}_fileList.txt"

    f = open(file_list_fname, "w")
    f.write(f'File manifest for fileset based on test_sets {test_sets_name}\n')
    # for line in manifest_lines:
    #     f.write(line + "\n")
    f.close()
    os.makedirs(target_dir, exist_ok=True)
    for scene_type in sorted(scene_types):
        rel_scene_paths = get_rel_scene_paths_of_type(test_sets_dir, test_set_files, scene_type)
        type_manifest_lines = generate_manifest_lines(rel_scene_paths, scene_type)
        f = open(file_list_fname, "a")
        f.write('\n')
        f.write(f' -- {scene_type} --')
        for line in type_manifest_lines:
            f.write(line + "\n")
        f.close()

        type_dir = os.path.join(target_dir, scene_type)
        os.makedirs(type_dir, exist_ok=True)
        copy_scenes(type_dir, "/home/ubuntu/eval6_systest", rel_scene_paths)
