
import os


if __name__ == '__main__':
    dest_root = os.path.join('/home','ubuntu','eval6_systest','unweighted_scene_jsons')
    if not os.path.exists(dest_root):
        os.mkdir(dest_root)
    uw_test_sets_dir = os.path.join('/home','ubuntu','eval6_systest','inter','test_sets','eval5_unweighted')
    if not os.path.exists(uw_test_sets_dir):
        print(f'bad path {uw_test_sets_dir}')
    files = os.listdir(uw_test_sets_dir)
    for fname in files:
        fpath = os.path.join(uw_test_sets_dir,fname)
        f = open(fpath,'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            abs_path = os.path.join('/home','ubuntu','eval6_systest',line.rstrip())
            fname = os.path.basename(abs_path)
            scene_type = fname.split('_')[0]
            dest_scene_type_dir = os.path.join(dest_root,scene_type)
            if not os.path.exists(dest_scene_type_dir):
                os.mkdir(dest_scene_type_dir)
            dest_path = os.path.join(dest_scene_type_dir,fname)
            
            command = f'cp {abs_path} {dest_path}'
            os.system(command)
