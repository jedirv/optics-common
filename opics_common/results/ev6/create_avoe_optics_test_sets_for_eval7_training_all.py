import sys, os

def load_fnames(dir):
    files = os.listdir(dir)
    sorted_files = sorted(files)
    return sorted_files

scene_types = ['helphind', 'tbelief','fbelief']
if __name__ == "__main__":
    helphind_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval7_training/helphind'
    tbelief_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval7_training/tbelief'
    fbelief_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval7_training/fbelief'

    files = {}
    files['helphind']   = load_fnames(helphind_dir)
    files['tbelief']   = load_fnames(tbelief_dir)
    files['fbelief']   = load_fnames(fbelief_dir)

    # 15000 scenes total
    # 5000 training of each type
    # 100 each per set  , 100x3 = 300 /set
    # 50 sets of 300
    root_of_path = 'avoe/scenes/eval7_training'
    test_sets = {}
    test_set_count = 50
    scenes_per_test_set_from_each = 100
    for i in range(test_set_count):
        test_sets[i] = []
        for j in range(scenes_per_test_set_from_each):
            #print(f'test_set {i} getting info from index {test_set_count ')
            for scene_type in scene_types:
            
                test_sets[i].append(root_of_path + '/' + scene_type + '/' + files[scene_type][ scenes_per_test_set_from_each * i + j])
            
    # for i in range(100):
    #    print(f'{test_sets[0][i]}')
    for i in range(test_set_count):
        two_digit_num = f'{i:02d}'
        test_set_pathname = f'/home/ubuntu/eval6_systest/avoe/test_sets/eval7_training_all/test_set_{two_digit_num}.txt'
        f = open(test_set_pathname, 'w')
        for fname in test_sets[i]:
            f.write(fname + '\n')
        f.close()
        

