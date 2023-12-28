import os

from opics_common.results.ev5.eval_results_avoe_ev5 import EvalResultsAvoe
from opics_common.results.ev5.eval_results_inter_ev5 import EvalResultsInter
from opics_common.results.ev5.eval_results_pvoe_ev5 import EvalResultsPvoe
from opics_common.results.ev5.scene_type_for_codeword import codeword_for_type
from opics_common.scene_type.type_constants import abbrev_types

projects                              = ["pvoe", "avoe", "inter"]

# to account for missing answers that prevented cube id lookup...
cube_for_scene_id                     = {}
# lava
cube_for_scene_id["victor_0002_03"]   = "A1"
cube_for_scene_id["victor_0011_02"]   = "C1"
cube_for_scene_id["victor_0002_02"]   = "B1"
cube_for_scene_id["victor_0011_01"]   = "B1"
cube_for_scene_id["victor_0011_03"]   = "A1"
cube_for_scene_id["victor_0002_01"]   = "C1"
# holes
cube_for_scene_id["uniform_0002_01"]  = "B1"
cube_for_scene_id["uniform_0002_02"]  = "C1"
cube_for_scene_id["uniform_0002_03"]  = "A1"
cube_for_scene_id["uniform_0017_01"]  = "B1"
# obst
cube_for_scene_id["papa_0049_01"]     = "C2"
# occl
cube_for_scene_id["quebec_0012_23"]   = "E1"
# ramps
cube_for_scene_id["whiskey_0010_02"]  = "B1"
cube_for_scene_id["whiskey_0018_06"]  = "B1"
cube_for_scene_id["whiskey_0007_05"]  = "K1"
cube_for_scene_id["whiskey_0011_10"]  = "L1"
cube_for_scene_id["whiskey_0016_11"]  = "B1"
cube_for_scene_id["whiskey_0016_04"]  = "L1"
cube_for_scene_id["whiskey_0002_11"]  = "F1"
cube_for_scene_id["whiskey_0024_11"]  = "C1"
cube_for_scene_id["whiskey_0011_04"]  = "K1"
# tool
cube_for_scene_id["omega_0019_03"]    = "G1"


def get_new_name_using_cube_lookup(scene_id, type):
    cube = cube_for_scene_id[scene_id]
    return type + "_" + scene_id + "_" + cube + "_5u.json"


if __name__ == "__main__":
    # PVOE gravity no bounce scene filenames of the form bravo_0001_01
    do_pvoe_gravity_no_bounce = True
    if do_pvoe_gravity_no_bounce:
        proj                            = "pvoe"
        src_scene_files_dir             = (
            "/home/jedirv/mcs/scenes_eval5/" + proj + "_gravity_no_bounce/"
        )
        renamed_scene_files_dir         = (
            "/home/jedirv/mcs/scenes_eval5/"
            + proj
            + "_renamed_with_correctness_gravity_no_bounce/"
        )
        renamed_plaus_scene_files_dir   = (
            "/home/jedirv/mcs/scenes_eval5/"
            + proj
            + "_renamed_with_correctness_plaus_gravity_no_bounce/"
        )
        renamed_implaus_scene_files_dir = (
            "/home/jedirv/mcs/scenes_eval5/"
            + proj
            + "_renamed_with_correctness_implaus_gravity_no_bounce/"
        )

        os.makedirs(renamed_scene_files_dir, exist_ok=True)
        os.makedirs(renamed_plaus_scene_files_dir, exist_ok=True)
        os.makedirs(renamed_implaus_scene_files_dir, exist_ok=True)
        for type in abbrev_types[proj]:
            print(f"...working type {type}...")
            target_type_dir = renamed_scene_files_dir + type + "/"
            target_type_dir_plaus = renamed_plaus_scene_files_dir + type + "/"
            target_type_dir_implaus = (
                renamed_implaus_scene_files_dir + type + "/"
            )
            os.makedirs(target_type_dir, exist_ok=True)
            os.makedirs(target_type_dir_plaus, exist_ok=True)
            os.makedirs(target_type_dir_implaus, exist_ok=True)
            code = codeword_for_type[type]
            answer_key_path = (
                "/home/jedirv/mcs/scenes_eval5/answer_keys/"
                + proj
                + "/"
                + proj
                + "__"
                + type
                + ".csv"
            )
            f = open(answer_key_path, "r")
            answer_key_lines = f.readlines()
            f.close()
            pvoe_results = EvalResultsPvoe(answer_key_lines)
            files = os.listdir(src_scene_files_dir)
            for file in files:
                if code in file:
                    file_root = file.split(".")[0]
                    parts = file_root.split("_")
                    scene_id = parts[0] + "_" + parts[1] + "_" + parts[2]
                    print(f"...scene_id {scene_id}...")
                    new_name = pvoe_results.scene_filename_for_root[scene_id]
                    os.system(
                        "cp "
                        + src_scene_files_dir
                        + file
                        + " "
                        + target_type_dir
                        + new_name
                    )
                    if "implaus" in new_name:
                        os.system(
                            "cp "
                            + src_scene_files_dir
                            + file
                            + " "
                            + target_type_dir_implaus
                            + new_name
                        )
                    else:
                        os.system(
                            "cp "
                            + src_scene_files_dir
                            + file
                            + " "
                            + target_type_dir_plaus
                            + new_name
                        )

    # PVOE
    do_pvoe = False
    if do_pvoe:  # scene filenames of the form alpha_0001_01_A2_debug.json
        proj                            = "pvoe"
        src_scene_files_dir             = "/home/jedirv/mcs/scenes_eval5/" + proj + "/"
        renamed_scene_files_dir         = (
            "/home/jedirv/mcs/scenes_eval5/"
            + proj
            + "_renamed_with_correctness/"
        )
        renamed_plaus_scene_files_dir   = (
            "/home/jedirv/mcs/scenes_eval5/"
            + proj
            + "_renamed_with_correctness_plaus/"
        )
        renamed_implaus_scene_files_dir = (
            "/home/jedirv/mcs/scenes_eval5/"
            + proj
            + "_renamed_with_correctness_implaus/"
        )
        os.makedirs(renamed_scene_files_dir, exist_ok=True)
        os.makedirs(renamed_plaus_scene_files_dir, exist_ok=True)
        os.makedirs(renamed_implaus_scene_files_dir, exist_ok=True)
        for type in abbrev_types[proj]:
            print(f"...working type {type}...")
            target_type_dir = renamed_scene_files_dir + type + "/"
            target_type_dir_plaus = renamed_plaus_scene_files_dir + type + "/"
            target_type_dir_implaus = (
                renamed_implaus_scene_files_dir + type + "/"
            )
            os.makedirs(target_type_dir, exist_ok=True)
            os.makedirs(target_type_dir_plaus, exist_ok=True)
            os.makedirs(target_type_dir_implaus, exist_ok=True)
            code = codeword_for_type[type]
            answer_key_path = (
                "/home/jedirv/mcs/scenes_eval5/answer_keys/"
                + proj
                + "/"
                + proj
                + "__"
                + type
                + ".csv"
            )
            f = open(answer_key_path, "r")
            answer_key_lines = f.readlines()
            f.close()
            pvoe_results = EvalResultsPvoe(answer_key_lines)
            files = os.listdir(src_scene_files_dir)
            for file in files:
                if code in file:
                    parts = file.split("_")
                    scene_id = parts[0] + "_" + parts[1] + "_" + parts[2]
                    print(f"...scene_id {scene_id}...")
                    new_name = pvoe_results.scene_filename_for_root[scene_id]
                    os.system(
                        "cp "
                        + src_scene_files_dir
                        + file
                        + " "
                        + target_type_dir
                        + new_name
                    )
                    if "implaus" in new_name:
                        os.system(
                            "cp "
                            + src_scene_files_dir
                            + file
                            + " "
                            + target_type_dir_implaus
                            + new_name
                        )
                    else:
                        os.system(
                            "cp "
                            + src_scene_files_dir
                            + file
                            + " "
                            + target_type_dir_plaus
                            + new_name
                        )

    # AVOE
    do_avoe = False
    if do_avoe:
        proj                                = "avoe"
        src_scene_files_dir                 = "/home/jedirv/mcs/scenes_eval5/" + proj + "/"
        renamed_scene_files_dir             = (
            "/home/jedirv/mcs/scenes_eval5/"
            + proj
            + "_renamed_with_correctness/"
        )
        renamed_expected_scene_files_dir    = (
            "/home/jedirv/mcs/scenes_eval5/"
            + proj
            + "_renamed_with_correctness_expected/"
        )
        renamed_unexpected_scene_files_dir  = (
            "/home/jedirv/mcs/scenes_eval5/"
            + proj
            + "_renamed_with_correctness_unexpected/"
        )
        os.makedirs(renamed_scene_files_dir, exist_ok=True)
        os.makedirs(renamed_expected_scene_files_dir, exist_ok=True)
        os.makedirs(renamed_unexpected_scene_files_dir, exist_ok=True)
        for type in abbrev_types[proj]:
            print(f"...working type {type}...")
            target_type_dir = renamed_scene_files_dir + type + "/"
            target_type_dir_expected = (
                renamed_expected_scene_files_dir + type + "/"
            )
            target_type_dir_unexpected = (
                renamed_unexpected_scene_files_dir + type + "/"
            )
            os.makedirs(target_type_dir, exist_ok=True)
            os.makedirs(target_type_dir_expected, exist_ok=True)
            os.makedirs(target_type_dir_unexpected, exist_ok=True)
            code = codeword_for_type[type]
            answer_key_path = (
                "/home/jedirv/mcs/scenes_eval5/answer_keys/"
                + proj
                + "/"
                + proj
                + "__"
                + type
                + ".csv"
            )
            f = open(answer_key_path, "r")
            answer_key_lines = f.readlines()
            f.close()
            avoe_results = EvalResultsAvoe(answer_key_lines)
            files = os.listdir(src_scene_files_dir)
            for file in files:
                if code in file:
                    parts = file.split("_")
                    scene_id = parts[0] + "_" + parts[1] + "_" + parts[2]
                    new_name = avoe_results.scene_filename_for_root[scene_id]
                    os.system(
                        "cp "
                        + src_scene_files_dir
                        + file
                        + " "
                        + target_type_dir
                        + new_name
                    )
                    # if 'unexpected' in new_name:
                    #     os.system('cp ' + src_scene_files_dir + file + ' ' + target_type_dir_unexpected + new_name)
                    # else:
                    #     os.system('cp ' + src_scene_files_dir + file + ' ' + target_type_dir_expected + new_name)

    # INTER
    do_inter = False
    if do_inter:
        proj                      = "inter"
        src_scene_files_dir       = "/home/jedirv/mcs/scenes_eval5/" + proj + "/"
        renamed_scene_files_dir   = (
            "/home/jedirv/mcs/scenes_eval5/" + proj + "_renamed/"
        )
        os.makedirs(renamed_scene_files_dir, exist_ok=True)
        for type in abbrev_types[proj]:
            print(f"...working type {type}...")
            target_type_dir = renamed_scene_files_dir + type + "/"
            os.makedirs(target_type_dir, exist_ok=True)
            code = codeword_for_type[type]
            answer_key_path = (
                "/home/jedirv/mcs/scenes_eval5/answer_keys/"
                + proj
                + "/"
                + proj
                + "__"
                + type
                + ".csv"
            )
            f = open(answer_key_path, "r")
            answer_key_lines = f.readlines()
            f.close()
            inter_results = EvalResultsInter(answer_key_lines)
            files = os.listdir(src_scene_files_dir)
            for file in files:
                if code in file:
                    parts = file.split("_")
                    scene_id = parts[0] + "_" + parts[1] + "_" + parts[2]
                    if scene_id in inter_results.scene_filename_for_root:
                        new_name = inter_results.scene_filename_for_root[
                            scene_id
                        ]
                    else:
                        print(
                            f"...{scene_id} not found in answer key... renaming using workaround..."
                        )
                        new_name = get_new_name_using_cube_lookup(
                            scene_id, type
                        )
                    os.system(
                        "cp "
                        + src_scene_files_dir
                        + file
                        + " "
                        + target_type_dir
                        + new_name
                    )
