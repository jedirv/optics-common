import os, sys


def rename_to_expected(cue, abbrev, source_dir):
    target_dir  = f'/home/jedirv/mcs/eval7_{abbrev}_scenes_renamed'
    scenes = []
    os.makedirs(target_dir, exist_ok=True)
    fnames = os.listdir(source_dir)
    for fname in fnames:
        if cue in fname:
            scenes.append(fname)
        else:
            pass
    scenes.sort()
    print(f'{abbrev}: {len(scenes)}')
    

    count = 0
    for fname in scenes: 
        if count < 5000:
            # from passive_agent_training_object_prerence_<test>_<scene>.json
            # want opref_zzz_<test_num>_<scene_num>_zz_expected.json
            # from passive_agent_training_multiple_agents_<test>_<scene>.json
            # want multa_zzz_<test_num>_<scene_num>_zz_expected.json
            # from passive_agent_training_single_object_<test>_<scene>.json
            # want irrat_zzz_<test_num>_<scene_num>_zz_expected.json
            parts = fname.split('.')[0].split('_')
            test_num = parts[5]
            scene_num = parts[6]
            new_fname = f'{abbrev}_training_{test_num}_{scene_num}_zz_expected.json'
            orig_path = os.path.join(source_dir, fname)
            new_path = os.path.join(target_dir, new_fname)
            if count == 0:
                print(f'cp {orig_path} {new_path}')
            os.system(f'cp {orig_path} {new_path}')
            count += 1

if __name__ == '__main__':
    #passive_agent_training_helper_hinderer_9999_01.json to  helphind_training_0001_01_zz_mexpected.json
    rename_to_expected('helper_hinderer'   , 'helphind', '/home/jedirv/mcs/passive_agent_training_helper_hinderer')
    rename_to_expected('true_belief'     , 'tbelief', '/home/jedirv/mcs/passive_agent_training_true_belief')
    rename_to_expected('false_belief' , 'fbelief', '/home/jedirv/mcs/passive_agent_training_false_belief')


