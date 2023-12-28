import os, json, sys
   
#scene_history_dir = '/home/ubuntu/test__inter_111623_val7/scripts/SCENE_HISTORY'
scene_history_dir = '/home/ubuntu/opics_eval7_validation_run2_history'
scene_files_dir = '/home/ubuntu/eval6_systest/inter/scenes/eval7_validation'

def get_matching_hist_file_for_scene(fname_root):
    fnames = os.listdir(scene_history_dir)
    for fname in fnames:
        if fname.startswith(fname_root):
            hist_path = os.path.join(scene_history_dir, fname)
            if os.path.getsize(hist_path) > 0:
                return hist_path
    return None


 
counts = {}
if __name__ == '__main__':

    scene_type_names = os.listdir(scene_files_dir)
    
    for scene_type in scene_type_names:
        print('')
        scene_type_dir = os.path.join(scene_files_dir, scene_type)
        scene_type_files = os.listdir(scene_type_dir)
        for scene_fname in scene_type_files:
            scene_path = os.path.join(scene_type_dir, scene_fname)
            f = open(scene_path, 'r')
            data = json.load(f)
            f.close()
            if len(data['lava']) != 0 or scene_type == 'movtarg':
                #print(f'{scene_fname} lava YES ')
                fname_root = scene_fname.split('.')[0]
                matching_hist_path = get_matching_hist_file_for_scene(fname_root)
                if matching_hist_path != None:
                    f = open(matching_hist_path, 'r')
                    hist_data = json.load(f)
                    f.close()
                    steps = hist_data['steps']
                    final_step_info = steps[len(steps) - 1]
                    final_step_output = final_step_info['output']
                    print(f"{fname_root} steps on lava: {final_step_output['steps_on_lava']}")

                    #print(json.dumps(final_step_output, indent=4))
                    #sys.exit()
                    #print(f'final step lava: {fname_root} {final_step_info["steps_on_lava"]}')
    # hist_files = os.list_dir(scene_history_dir)
    # for fname in hist_files:
    #     hist_path = os.path.join(scene_history_dir,fname)
    #     scene_type = fname.split('_')[0]
    #     if not scene_type in counts:
    #         counts[scene_type] = {}
        