
import os


if __name__ == '__main__':
    scenes_root_dir = '/home/ubuntu/eval6_systest/inter/scenes/eval6_new_ile'
    scene_types = sorted(os.listdir(scenes_root_dir))
    datasets = {}
    scenes_for_type = {}
    for scene_type in scene_types:
        type_dir = os.path.join(scenes_root_dir, scene_type)
        scenes = sorted(os.listdir(type_dir))
        scenes_for_type[scene_type] = scenes
    # for scene_type in scenes_for_type:
    #     print(f' {scene_type} has this many : {len(scenes_for_type[scene_type])}')
    test_set_count = 20
    scenes_of_type_per_set = 10
    for i in range(test_set_count):
        two_digit_number = "{:02d}".format(i)
        dataset_name = f'test_set_ev6_new_types_{two_digit_number}.txt'
        datasets[dataset_name] = []
        for j in range(scenes_of_type_per_set):
            for scene_type in scenes_for_type:
                cur_index = i * scenes_of_type_per_set + j
                scene = scenes_for_type[scene_type][cur_index]
                scene_path = os.path.join('inter', 'scenes','eval6_new_ile', scene_type, scene)
                datasets[dataset_name].append(scene_path)    
    for dataset_name in datasets:
        print(f' {dataset_name} has this many : {len(datasets[dataset_name])}')

    datasets_dir = '/home/ubuntu/eval6_systest/inter/test_sets/eval6_new_ile'
    os.makedirs(datasets_dir, exist_ok=True)

    for dataset_name in datasets:
        dataset_path = os.path.join(datasets_dir, dataset_name)
        f = open(dataset_path, 'w')
        for scene_path in datasets[dataset_name]:
            f.write(scene_path + '\n')
        f.close()

    