import os, sys


# anona

# agent_one_goal.json       (no paddle contact)  rename all with  "_expected"   omit these as these are just training data
# agent_preference.json    (no paddle contact)  rename all with  "_expected"
# collect.json                        (no occluder so not like scenes we will be tested on)   omit these as these are just training data
# non_agent_one_goal.json     (paddle contact - sometimes contacts goal) omit these because no way to know without reviewing scenes whether contact was made 
# non_agent_preference.json    (paddle contact - always contacts goal)    rename all with "_noexpectation"

scenes = {}
scenes['anona'] = {}
#scenes['anona']['agent_one_goal']      = []
scenes['anona']['agent_preference']    = []
#scenes['anona']['collect']             = []
#scenes['anona']['non_agent_one_goal']   = []
scenes['anona']['non_agent_preference'] = []

def rename_anona_scenes():
    anona_src_dir    = '/home/jedirv/mcs/eval_6_passive_agent_training_agent_nonagent_tasks'
    trap_target_dir  = '/home/jedirv/mcs/eval6_anona_trap_scenes_renamed'
    trnap_target_dir = '/home/jedirv/mcs/eval6_anona_trnap_scenes_renamed'
    os.makedirs(trap_target_dir, exist_ok=True)
    os.makedirs(trnap_target_dir, exist_ok=True)
    fnames = os.listdir(anona_src_dir)
    # order is important because some names within others
    for fname in fnames:
        # if 'non_agent_one_goal' in fname:
        #     scenes['anona']['non_agent_one_goal'].append(fname)
        if 'non_agent_preference' in fname:
            scenes['anona']['non_agent_preference'].append(fname)
        # elif 'agent_one_goal' in fname:
        #     scenes['anona']['agent_one_goal'].append(fname)
        elif 'agent_preference' in fname:
            scenes['anona']['agent_preference'].append(fname)
        # elif 'collect' in fname:
        #     scenes['anona']['collect'].append(fname)
        else:
            pass
    scenes['anona']['agent_preference'].sort()
    scenes['anona']['non_agent_preference'].sort()
    #print(f'agent_one_goal: {len(scenes["anona"]["agent_one_goal"])}')
    print(f'anona agent_preference: {len(scenes["anona"]["agent_preference"])}')
    #print(f'collect: {len(scenes["anona"]["collect"])}')
    #print(f'non_agent_one_goal: {len(scenes["anona"]["non_agent_one_goal"])}')
    print(f'anona non_agent_preference: {len(scenes["anona"]["non_agent_preference"])}')

    count = 0
    for fname in scenes['anona']['agent_preference']: 
        if count < 1000:
            # from passive_agent_training_agent_preference_<test>_<scene>.json
            # want anona_trap_<test_num>_<scene_num>_zz_expected.json
            parts = fname.split('.')[0].split('_')
            test_num = parts[5]
            scene_num = parts[6]
            # NOTE scene_num is always 1 in these training scenes, only the tes number increments
            # so, we assign 01 to apref scenes and 02 to napref scenes below so that we 
            # continue the norm of having the abbrev_type+test+scene_num being unique.
            # If we retained the scene num and had both being 1, then we would have duplicate numberings
            new_fname = f'anona_training_{test_num}_01_apref_expected.json'
            orig_path = os.path.join(anona_src_dir, fname)
            new_path = os.path.join(trap_target_dir, new_fname)
            if count == 0:
                print(f'cp {orig_path} {new_path}')
            os.system(f'cp {orig_path} {new_path}')
            count += 1

    count = 0
    for fname in scenes['anona']['non_agent_preference']: 
        if count < 1000:
            # from passive_agent_training_non_agent_preference_<test>_<scene>.json
            # want anona_trap_<test_num>_<scene_num>_zz_expected.json
            parts = fname.split('.')[0].split('_')
            test_num = parts[6]
            scene_num = parts[7]
            new_fname = f'anona_training_{test_num}_02_napref_noexpectation.json'
            orig_path = os.path.join(anona_src_dir, fname)
            new_path = os.path.join(trnap_target_dir, new_fname)
            if count == 0:
                print(f'cp {orig_path} {new_path}')
            os.system(f'cp {orig_path} {new_path}')
            count += 1

# social scenes
#     social approach    test trial imitates thing it approached in past
#     social imitation   test trial approaches thing it imitated in past
#     instrumental approach  test trial imitates thing it approached in past but possible confound of noexpectation
#     instrtumental imitation test trial approaches thing it imitated in past but possible confound of noexpectation


scenes['socimit'] = []
scenes['socapp']  = []
scenes['instrimit'] = []
scenes['instrapp']  = []

def rename_social_scenes():
    social_src_dir    = '/home/jedirv/mcs/eval_6_passive_agent_training_approach_imitation_tasks'
    socimit_target_dir  = '/home/jedirv/mcs/eval6_socimit_scenes_renamed'
    socapp_target_dir = '/home/jedirv/mcs/eval6_socapp_scenes_renamed'
    instrimit_target_dir  = '/home/jedirv/mcs/eval6_instrimit_scenes_renamed'
    instrapp_target_dir = '/home/jedirv/mcs/eval6_instrapp_scenes_renamed'
    os.makedirs(socimit_target_dir, exist_ok=True)
    os.makedirs(socapp_target_dir, exist_ok=True)
    os.makedirs(instrimit_target_dir, exist_ok=True)
    os.makedirs(instrapp_target_dir, exist_ok=True)
    fnames = os.listdir(social_src_dir)
    # order is important because some names within others
    for fname in fnames:
        if 'social_approach' in fname:
            scenes['socapp'].append(fname)
        elif 'social_imitation' in fname:
            scenes['socimit'].append(fname)
        elif 'instrumental_approach' in fname:
            scenes['instrapp'].append(fname)
        elif 'instrumental_imitation' in fname:
            scenes['instrimit'].append(fname)
        else:
            pass
    scenes['socapp'].sort()
    scenes['socimit'].sort()
    scenes['instrapp'].sort()
    scenes['instrimit'].sort()
    print(f'socapp: {len(scenes["socapp"])}')
    print(f'socimit: {len(scenes["socimit"])}')
    print(f'instrapp: {len(scenes["instrapp"])}')
    print(f'instrimit: {len(scenes["instrimit"])}')

    count = 0
    for fname in scenes['socapp']: 
        if count < 1000:
            # from passive_agent_training_social_approach_<test>_<scene>.json
            # want socapp_zzz_<test_num>_<scene_num>_zz_expected.json
            parts = fname.split('.')[0].split('_')
            test_num = parts[5]
            scene_num = parts[6]
            new_fname = f'socapp_training_{test_num}_{scene_num}_stand_expected.json'
            orig_path = os.path.join(social_src_dir, fname)
            new_path = os.path.join(socapp_target_dir, new_fname)
            if count == 0:
                print(f'cp {orig_path} {new_path}')
            os.system(f'cp {orig_path} {new_path}')
            count += 1

    count = 0
    for fname in scenes['socimit']: 
        if count < 1000:
            # from passive_agent_training_social_imitation_<test>_<scene>.json
            # want anona_trap_<test_num>_<scene_num>_zz_expected.json
            parts = fname.split('.')[0].split('_')
            test_num = parts[5]
            scene_num = parts[6]
            new_fname = f'socimit_training_{test_num}_{scene_num}_stand_expected.json'
            orig_path = os.path.join(social_src_dir, fname)
            new_path = os.path.join(socimit_target_dir, new_fname)
            if count == 0:
                print(f'cp {orig_path} {new_path}')
            os.system(f'cp {orig_path} {new_path}')
            count += 1

    count = 0
    for fname in scenes['instrapp']: 
        if count < 1000:
            # from passive_agent_training_instrumental_approach_<test>_<scene>.json
            # want socapp_instrumental_<test_num>_<scene_num>_zz_expected.json
            parts = fname.split('.')[0].split('_')
            test_num = parts[5]
            scene_num = parts[6]
            new_fname = f'socapp_training_{test_num}_{scene_num}_instr_noexpectation.json'
            orig_path = os.path.join(social_src_dir, fname)
            new_path = os.path.join(instrapp_target_dir, new_fname)
            if count == 0:
                print(f'cp {orig_path} {new_path}')
            os.system(f'cp {orig_path} {new_path}')
            count += 1

    count = 0
    for fname in scenes['instrimit']: 
        if count < 1000:
            # from passive_agent_training_instrumental_approach_<test>_<scene>.json
            # want socapp_instrumental_<test_num>_<scene_num>_zz_expected.json
            parts = fname.split('.')[0].split('_')
            test_num = parts[5]
            scene_num = parts[6]
            new_fname = f'socimit_training_{test_num}_{scene_num}_instr_noexpectation.json'
            orig_path = os.path.join(social_src_dir, fname)
            new_path = os.path.join(instrimit_target_dir, new_fname)
            if count == 0:
                print(f'cp {orig_path} {new_path}')
            os.system(f'cp {orig_path} {new_path}')
            count += 1

def rename_to_expected(cue, abbrev, source_dir):
    target_dir  = f'/home/jedirv/mcs/eval6_{abbrev}_scenes_renamed'
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
        if count < 1000:
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
    rename_anona_scenes()
    rename_social_scenes()
    rename_to_expected('multiple_agents'   , 'multa', '/home/jedirv/mcs/eval_6_passive_agent_training_multiple_agents')
    rename_to_expected('single_object'     , 'irrat', '/home/jedirv/mcs/eval_6_passive_agent_training_single_object')
    rename_to_expected('object_preference' , 'opref', '/home/jedirv/mcs/eval_6_passive_agent_training_object_preference')


