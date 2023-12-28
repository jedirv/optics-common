import os, sys

def trim_set_to_500(dir):
    print(f' trimming {dir} to 500 scenes')
    os.system(f'cd {dir};ls -1 | tail -n 500')
    answer = input("continue? (y/n): ")
    if answer == 'y':
        os.system(f'cd {dir};ls -1 | tail -n 500 | xargs rm')
    else:
        sys.exit()



if __name__ == '__main__':
    #dir_socimit       = '/home/jedirv/mcs/eval6_socimit_scenes_renamed/socimit'
    #dir_socimit_instr = '/home/jedirv/mcs/eval6_instrimit_scenes_renamed/socimit'
    dir_socapp        = '/home/jedirv/mcs/eval6_socapp_scenes_renamed/socapp'
    dir_socapp_instr  = '/home/jedirv/mcs/eval6_instrapp_scenes_renamed/socapp'

    # if not os.path.exists(dir_socimit):
    #     print(f' {dir_socimit} does not exist')
    #     sys.exit()
    # if not os.path.exists(dir_socimit_instr):
    #     print(f' {dir_socimit_instr} does not exist')
    #     sys.exit()
    if not os.path.exists(dir_socapp):
        print(f' {dir_socapp} does not exist')
        sys.exit()
    if not os.path.exists(dir_socapp_instr):
        print(f' {dir_socapp_instr} does not exist')
        sys.exit()

    # trim_set_to_500(dir_socimit)
    # trim_set_to_500(dir_socimit_instr)
    trim_set_to_500(dir_socapp)
    trim_set_to_500(dir_socapp_instr)