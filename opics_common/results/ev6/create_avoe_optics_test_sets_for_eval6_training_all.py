import sys, os

def load_fnames(dir):
    files = os.listdir(dir)
    sorted_files = sorted(files)
    return sorted_files

scene_types = ['anona', 'irrat','multa','opref','socapp','socimit']
if __name__ == "__main__":
    anona_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval6_training/anona'
    multa_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval6_training/multa'
    opref_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval6_training/opref'
    irrat_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval6_training/irrat'
    socapp_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval6_training/socapp'
    socimit_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval6_training/socimit'

    files = {}
    files['anona']   = load_fnames(anona_dir)
    files['multa']   = load_fnames(multa_dir)
    files['opref']   = load_fnames(opref_dir)
    files['irrat']   = load_fnames(irrat_dir)
    files['socapp']  = load_fnames(socapp_dir)
    files['socimit'] = load_fnames(socimit_dir)

    # 6000 scenes total
    # 1000 training of each type
    # 50 each per set  , 50 * 6 = 300 /set
    # 20 sets of 300
    root_of_path = 'avoe/scenes/eval6_training'
    test_sets = {}
    test_set_count = 20
    scenes_per_test_set_from_each = 50
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
        test_set_pathname = f'/home/ubuntu/eval6_systest/avoe/test_sets/eval6_training_all/test_set_{two_digit_num}.txt'
        f = open(test_set_pathname, 'w')
        for fname in test_sets[i]:
            f.write(fname + '\n')
        f.close()
        

