
import os

if __name__ == '__main__':
    inter_dir = '/home/ubuntu/eval6_systest/inter/scenes/eval6'
    type_dirs = os.listdir(inter_dir)
    for scene_type in type_dirs:
        cube_ids = []
        type_dir = os.path.join(inter_dir, scene_type)
        files = os.listdir(type_dir)
        for file in files:
            cube_id = file.split('_')[4]
            if not cube_id in cube_ids:
                cube_ids.append(cube_id)
                
        cube_ids = sorted(cube_ids)
       
        s = ''
        for cube_id in cube_ids:
            s += f"'{cube_id}', "
        print(f'weighted_codes_for_type["{scene_type}"] = [{s}]')
        print(f'unweighted_codes_for_type["{scene_type}"] = []')
        print('')
        print('')
        
