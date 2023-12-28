import os


type_map = {}
type_map['avoe'] = {}
type_map['avoe']['inter'] = {}
type_map['avoe']['tbelief'] = 'true_false_belief'
type_map['avoe']['fbelief'] = 'true_false_belief'
type_map['avoe']['socimit'] = 'imitation'
type_map['avoe']['helphind'] = 'helper_hinderer'
type_map['avoe']['socapp'] = 'approach'
type_map['avoe']['anona'] = 'non_agent'
type_map['inter'] = {}
type_map['inter']['hidtraj'] = 'trajectory'
type_map['inter']['tool'] = 'tool_use'
type_map['inter']['suprel'] = 'support_relations'
type_map['inter']['reor'] = 'reorientation'
type_map['inter']['spatref'] = 'spatial_reference'
type_map['inter']['spelim'] = 'spatial_elimination'
type_map['inter']['solid'] = 'solidity'
type_map['inter']['shell'] = 'shell_game'
type_map['inter']['hsetrot'] = 'set_rotation'
type_map['inter']['setrot'] = 'set_rotation'
type_map['inter']['mtool'] = 'secondary_tool'
type_map['inter']['ramps'] = 'ramps'
type_map['inter']['occl'] = 'occluders'
type_map['inter']['iop'] = 'object_permanence'
type_map['inter']['movtarg'] = 'target_prediction'
type_map['inter']['lava'] = 'lava'
type_map['inter']['kagents'] = 'knowledgeable_agents'
type_map['inter']['imit'] = 'imitation'
type_map['inter']['holes'] = 'holes'
type_map['inter']['cont'] = 'containers'
type_map['inter']['coltraj'] = 'collisions'

#ta2_results_dir_inter = '/home/ubuntu/opics_eval7_validation_run1_log/inter'
#osu_results_dir_inter = '/home/ubuntu/eval6_systest/inter/versions/101823_val7/stdout_logs'

#ta2_results_dir_inter = '/home/ubuntu/opics_eval7_validation_run1_log/inter'
#osu_results_dir_inter = '/home/ubuntu/eval6_systest/inter/versions/110923_val_ec2d_only/stdout_logs'

#ta2_results_dir_inter = '/home/ubuntu/opics_eval7_validation_run2_log/inter'
#osu_results_dir_inter = '/home/ubuntu/eval6_systest/inter/versions/111623_val7/stdout_logs'

#ta2_results_dir_inter = '/home/ubuntu/opics_eval7_validation_run2_log/inter'
#osu_results_dir_inter = '/home/ubuntu/eval6_systest/inter/versions/112023_val7_ec2d_only/stdout_logs'

#diverse hardware vs TA2 with delay
# ta2_results_dir_inter = '/home/ubuntu/opics_eval7_validation_run3_log'
# osu_results_dir_inter = '/home/ubuntu/eval6_systest/inter/versions/111623_val7/stdout_logs'

#ec2d only vs TA2 with delay
#ta2_results_dir_inter = '/home/ubuntu/opics_eval7_validation_run3_log'
#osu_results_dir_inter = '/home/ubuntu/eval6_systest/inter/versions/112023_val7_ec2d_only/stdout_logs'


#ec2d only vs TA2 with 1200x800
#ta2_results_dir_inter = '/home/ubuntu/opics_eval7_validation_run4_log'
#osu_results_dir_inter = '/home/ubuntu/eval6_systest/inter/versions/111623_val7/stdout_logs'

#ta2_results_dir_inter = '/home/ubuntu/opics_eval7_validation_run4_log'
#osu_results_dir_inter = '/home/ubuntu/eval6_systest/inter/versions/112023_val7_ec2d_only/stdout_logs'


#ta2_results_dir_inter = '/home/ubuntu/opics_eval7_validation_run5_log/inter'
#osu_results_dir_inter = '/home/ubuntu/eval6_systest/inter/versions/120123_val7/stdout_logs'

#ta2_results_dir_avoe  = '/home/ubuntu/opics_eval7_validation_run1_log/avoe'
#osu_results_dir_avoe  = '/home/ubuntu/eval6_systest/avoe/versions/110723_val7hh/stdout_logs'

#ta2_results_dir_avoe  = '/home/ubuntu/opics_eval7_validation_run2_log/avoe'


#ta2_results_dir_avoe  = '/home/ubuntu/opics_eval7_validation_run5_log/avoe'
#osu_results_dir_avoe  = '/home/ubuntu/eval6_systest/avoe/versions/120123_val7/stdout_logs'


ta2_results_dir_avoe  = '/home/ubuntu/opics_eval7_validation_run6_log/'
osu_results_dir_avoe  = '/home/ubuntu/eval6_systest/avoe/versions/120323_full2/stdout_logs'

def get_osu_files_of_type(osu_results_dir, scene_type):
    result = []
    type_dir = os.path.join(osu_results_dir, scene_type)
    if not os.path.isdir(type_dir):
        print(f'WARNING - dir {type_dir} does not exist')
        return []
    files = os.listdir(type_dir)
    for fname in files:
        if fname.startswith(scene_type):
            result.append(fname)
    return result

def get_scene_num_from_osu_fname(fname):
    parts = fname.split('_')
    return parts[2] + '_' + parts[3]

def get_file_with_scene_num(scene_num_prefix_match, ta2_results_dir):
    files = os.listdir(ta2_results_dir)
    for fname in files:
        if scene_num_prefix_match in fname:
            return fname
    return None

def compare_inter_results(osu_result_path, ta2_result_path):
    osu_file = os.path.basename(osu_result_path)
    ta2_file = os.path.basename(ta2_result_path)
    #2023-11-08 14:56:33 ; RESULT ; True ; InterAgent:run_scene ;  inter_agent.py:241
    osu_result_string = get_inter_result_string(osu_result_path)
    ta2_result_string = get_inter_result_string(ta2_result_path)
    if osu_result_string != ta2_result_string:
        print(f'       DIFFERENCE: {osu_file}:{osu_result_string}   {ta2_file}:{ta2_result_string}')
    else:
        print(f'       match {osu_result_string}  {osu_file} {ta2_file} ') 


def compare_avoe_results(osu_result_path, ta2_result_path):
    osu_file = os.path.basename(osu_result_path)
    ta2_file = os.path.basename(ta2_result_path)
    #Final choice:  expected , Answer:  expected
    osu_result_string = get_avoe_result_string(osu_result_path)
    ta2_result_string = get_avoe_result_string(ta2_result_path)
    if osu_result_string != ta2_result_string:
        print(f'DIFFERENCE: {osu_file}:{osu_result_string}   {ta2_file}:{ta2_result_string}')
    else:
        print(f'match: {osu_file} {osu_result_string}') 


def get_avoe_result_string(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        #print(f'checking line {line}')
        if 'RESULT' in line:
            parts = line.split(' ')
            print 
            return parts[4]

    return '???'

def get_inter_result_string(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        #print(f'checking line {line}')
        if 'RESULT' in line:
            parts = line.split(' ')
            return parts[5]

    return '???'

if __name__ == '__main__':
   
    # inter_type_map = type_map['inter']
    # for itype in inter_type_map:
    #     print(f'{itype}')
    #     itype_files = sorted(get_osu_files_of_type(osu_results_dir_inter, itype))
    #     for itype_file in itype_files:
    #         scene_num = get_scene_num_from_osu_fname(itype_file)
    #         corresponding_ta2_file = get_file_with_scene_num(inter_type_map[itype] + '_' + scene_num, ta2_results_dir_inter)
    #         if None == corresponding_ta2_file:
    #             print(f'Error - no matching file found for {itype_file}')
    #         else:
    #             osu_result_path = os.path.join(osu_results_dir_inter, itype, itype_file)
    #             ta2_result_path = os.path.join(ta2_results_dir_inter, corresponding_ta2_file)
    #             compare_inter_results(osu_result_path, ta2_result_path)
    # print('')
    # print(f'TA2 data used: {ta2_results_dir_inter}')
    # print('')
    # print(f'osu data used: {osu_results_dir_inter}')
    # print('')


    avoe_type_map = type_map['avoe']
    for atype in avoe_type_map:
        print(f'{atype}')
        atype_files = sorted(get_osu_files_of_type(osu_results_dir_avoe, atype))
        for atype_file in atype_files:
            scene_num = get_scene_num_from_osu_fname(atype_file)
            corresponding_ta2_file = get_file_with_scene_num(avoe_type_map[atype] + '_' + scene_num, ta2_results_dir_avoe)
            if None == corresponding_ta2_file:
                print(f'Error - no matching file found for {atype_file}')
            else:
                osu_result_path = os.path.join(osu_results_dir_avoe, atype, atype_file)
                ta2_result_path = os.path.join(ta2_results_dir_avoe, corresponding_ta2_file)
                compare_avoe_results(osu_result_path, ta2_result_path)
    print('')
    print(f'TA2 data used: {ta2_results_dir_avoe}')
    print('')
    print(f'osu data used: {osu_results_dir_avoe}')
    print('')
