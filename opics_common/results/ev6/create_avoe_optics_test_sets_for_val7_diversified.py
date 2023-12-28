import sys, os

def load_fnames(dir):
    files = os.listdir(dir)
    sorted_files = sorted(files)
    return sorted_files

scene_types = ['helphind', 'tbelief','fbelief']
if __name__ == "__main__":
    helphind_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval7_validation_diversified/helphind'
    tbelief_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval7_validation_diversified/tbelief'
    fbelief_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval7_validation_diversified/fbelief'

    files = {}
    files['helphind']   = load_fnames(helphind_dir) #153
    files['tbelief']   = load_fnames(tbelief_dir) #205
    files['fbelief']   = load_fnames(fbelief_dir) #205

    root_of_path = 'avoe/scenes/eval7_validation_diversified'
    max_count = max([len(files['helphind']), len(files['tbelief']), len(files['fbelief'])])
    all_paths_in_order = []
    for i in range(int(max_count/2)):
        if i*2 < len(files['helphind']):
            all_paths_in_order.append(root_of_path + '/helphind/' + files['helphind'][i*2])
            all_paths_in_order.append(root_of_path + '/helphind/' + files['helphind'][i*2 + 1])
        if i*2 < len(files['tbelief']):
            all_paths_in_order.append(root_of_path + '/tbelief/' + files['tbelief'][i*2])
            all_paths_in_order.append(root_of_path + '/tbelief/' + files['tbelief'][i*2 + 1])
        if i*2 < len(files['fbelief']):
            all_paths_in_order.append(root_of_path + '/fbelief/' + files['fbelief'][i*2])
            all_paths_in_order.append(root_of_path + '/fbelief/' + files['fbelief'][i*2 + 1])
    test_sets = []
    cur_test_set = []
    print(f' length of all_paths_in_order is {len(all_paths_in_order)}')
    for path in all_paths_in_order:
        cur_test_set.append(path)
        if len(cur_test_set) == 50:
            test_sets.append(cur_test_set)
            cur_test_set = []
            continue
    test_sets.append(cur_test_set)


    # for i in range(len(test_sets)):
    #     test_set = test_sets[i]
    #     print(f'test_set {i}  length : {len(test_set)}')
    #     for path in test_set:
    #         print(f'     {path}')


    # 15000 scenes total
    # 5000 training of each type
    # 100 each per set  , 100x3 = 300 /set
    # 50 sets of 300
    # test_sets = {}
    # test_set_count = 50
    # scenes_per_test_set_from_each = 100
    # for i in range(test_set_count):
    #     test_sets[i] = []
    #     for j in range(scenes_per_test_set_from_each):
    #         #print(f'test_set {i} getting info from index {test_set_count ')
    #         for scene_type in scene_types:
            
    #             test_sets[i].append(root_of_path + '/' + scene_type + '/' + files[scene_type][ scenes_per_test_set_from_each * i + j])
            
    # # for i in range(100):
    # #    print(f'{test_sets[0][i]}')
    test_set_dir = '/home/ubuntu/eval6_systest/avoe/test_sets/eval7_validation_diversified'
    cmd = f'rm -rf {test_set_dir}'
    os.system(cmd)
    os.makedirs(test_set_dir, exist_ok=True)
    for i in range(len(test_sets)):
        two_digit_num = f'{i:02d}'
        test_set_pathname = os.path.join(test_set_dir,f'test_set_{two_digit_num}.txt')
        f = open(test_set_pathname, 'w')
        for path in test_sets[i]:
            f.write(path + '\n')
        f.close()
        
