import sys, os

if __name__ == "__main__":
    scene_dir = '/home/ubuntu/eval6_systest/avoe/scenes/eval6_training/anona'
    test_set_dir = '/home/ubuntu/eval6_systest/avoe/test_sets/eval6_training'
    # 1000 training apref
    # 1000 training napref
    # 20 test sets of 100
    fnames = os.listdir(scene_dir)
    fnames.sort()
    apref_scenes = []
    napref_scenes = []
    for fname in fnames:
        if 'napref' in fname:
            napref_scenes.append(fname)
        else:
            apref_scenes.append(fname)

    test_sets = {}
    test_set_count = 20
    scenes_per_test_set_from_each = 50
    for i in range(test_set_count):
        test_sets[i] = []
        for j in range(scenes_per_test_set_from_each):
            #print(f'test_set {i} getting info from index {test_set_count ')
            root_of_path = 'avoe/scenes/eval6_training/anona/'
            test_sets[i].append(root_of_path + apref_scenes[ scenes_per_test_set_from_each * i + j])
            test_sets[i].append(root_of_path + napref_scenes[scenes_per_test_set_from_each * i + j])
    #for i in range(100):
    #    print(f'{test_sets[0][i]}')
    for i in range(test_set_count):
        two_digit_num = f'{i:02d}'
        test_set_pathname = f'/home/ubuntu/eval6_systest/avoe/test_sets/eval6_training/test_set_{two_digit_num}.txt'
        f = open(test_set_pathname, 'w')
        for fname in test_sets[i]:
            f.write(fname + '\n')
        f.close()
        

# SKIP agent_one_goal.json       (no paddle contact)  omit these as these are just training data
# agent_preference.json    (no paddle contact)  rename all with  "_expected"
# SKIP collect.json                omit these as these are just training data
# SKIP non_agent_one_goal.json     (paddle contact - sometimes contacts goal) omit these because no way to know without reviewing scenes whether contact was made 
# non_agent_preference.json    (paddle contact - always contacts goal)    rename all with "_noexpectation"