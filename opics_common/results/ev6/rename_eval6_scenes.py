import os
from opics_common.scene_type.type_constants import abbrev_types
from opics_common.results.header_val_indices import val_index_eval6
from opics_common.results.ev6.eval_results_pvoe_ev6 import EvalResultsPvoe
from opics_common.results.ev6.eval_results_inter_ev6 import EvalResultsInter
from opics_common.results.ev6.eval_results_avoe_ev6 import EvalResultsAvoe

type_map = {}
type_map['alpha']    = 'anona'
type_map['bravo']    = 'socapp'
type_map['charlie']  = 'socimit' 
type_map['delta']    = 'math'
type_map['earth']    = 'holes'
type_map['echo']     = 'coltraj'
type_map['foxtrot']  = 'imit'
type_map['golf']     = 'numcomp'
type_map['hotel']    = 'setrot'
type_map['india']    = 'shell'
type_map['juliett']  = 'spatref'
type_map['jupiter']  = 'ramps'
type_map['kilo']     = 'reor'
type_map['lima']     = 'tool'  # tlch? tlas?
type_map['mars']     = 'lava'
type_map['mercury']  = 'agentid'
type_map['mike']     = 'hidtraj'
type_map['neptune']  = 'suprel'
type_map['november'] = 'sltk'
type_map['oscar']    = 'irrat'
type_map['papa']     = 'multa'
type_map['quebec']   = 'opref'
type_map['romeo']    = 'coll'
type_map['saturn']   = 'solid'
type_map['sierra']   = 'grav'
type_map['tango']    = 'op'
type_map['uniform']  = 'sc'
type_map['uranus']   = 'spelim'
type_map['venus']    = 'movtarg'
type_map['victor']   = 'stc'
type_map['whiskey']  = 'cont'
type_map['xray']     = 'obst'
type_map['yankee']   = 'occl'
type_map['zulu']     = 'iop'



def load_answer_key():
    answer_key_path = '/home/jedirv/Downloads/eval6_results.csv'
    f = open(answer_key_path, 'r')
    lines = f.readlines()
    lines_pvoe = []
    lines_inter = []
    lines_avoe = []
    f.close()
    for line in lines:
        if line.startswith('CATEGORY'):
            continue
        fields = line.rstrip().split(',')
        test_name = fields[val_index_eval6['TEST NAME']]
        ta2_code = test_name.split('_')[0]
        osu_code = type_map[ta2_code]
        if osu_code in abbrev_types['pvoe']:
            lines_pvoe.append(line)
        elif osu_code in abbrev_types['inter']:
            lines_inter.append(line)
        elif osu_code in abbrev_types['avoe']:
            lines_avoe.append(line)
        else:
            print(f'unknown type {osu_code}')
    pvoe_results = EvalResultsPvoe(lines_pvoe)
    inter_results = EvalResultsInter(lines_inter)
    avoe_results = EvalResultsAvoe(lines_avoe)
    print(f'pvoe entry count {len(pvoe_results.scene_filename_for_root)}')
    print(f'inter entry count {len(inter_results.scene_filename_for_root)}')
    print(f'avoe entry count {len(avoe_results.scene_filename_for_root)}')
    return pvoe_results, inter_results, avoe_results



def get_proj_for_osu_code(osu_code):
    if osu_code in abbrev_types['pvoe']:
        return 'pvoe'
    elif osu_code in abbrev_types['inter']:
        return 'inter'
    elif osu_code in abbrev_types['avoe']:
        return 'avoe'
    else:
        raise Exception(f'unknown type {osu_code}')

if __name__ == '__main__':
    pvoe_results, inter_results, avoe_results = load_answer_key()
    results_for_project = {}
    results_for_project['pvoe'] = pvoe_results
    results_for_project['inter'] = inter_results
    results_for_project['avoe'] = avoe_results
    input_dirs = []
    input_dirs.append('/home/jedirv/Downloads/eval_6_passive_agent')
    #input_dirs.append('/home/jedirv/Downloads/eval_6_passive_physics')
    #input_dirs.append('/home/jedirv/Downloads/eval_6_interactive_all')
    #input_dirs.append('/home/jedirv/Downloads/eval_6_passive_seeing_leads_to_knowing')

    
    #input_dir = '/home/jedirv/Downloads/eval6eval_scenes_definition/scenes_definition'
    output_root = '/home/jedirv/mcs/eval6_files_renamed'
    os.makedirs(output_root, exist_ok=True)
    for input_dir in input_dirs:
        codes = []
        files = sorted(os.listdir(input_dir))
        for file in files:
            code = file.split('_')[0]
            if not code in codes:
                codes.append(code)
        codes = sorted(codes)
        # for code in codes:
        #     print(f'{type_map[code]}')
        for file in files:
            file_root = file.split('.')[0]
            ta2_code = file_root.split('_')[0]
            test_num = file_root.split('_')[1]
            scene_num = file_root.split('_')[2]
            ta2_test_name = f'{ta2_code}_{test_num}_{scene_num}'
            
            
            osu_code = type_map[ta2_code]
            proj = get_proj_for_osu_code(osu_code)
            results_for_proj = results_for_project[proj]


            # re-calculate osu_code because the TA2 data lumped the three tools types into one internal code, 'lima'
            # If we use results_for_proj.scene_type_for_scene[scene_id], we will get the correct internal code for the 
            # tools variants as well as all the rest. 
            tertiary_type = results_for_proj.scene_type_for_scene[ta2_test_name]
            osu_code = results_for_proj.get_type_abbrev(tertiary_type)
            output_dir = os.path.join(output_root, proj, 'eval6', osu_code)
            os.makedirs(output_dir, exist_ok=True)
            
            new_filename = results_for_proj.scene_filename_for_root[ta2_test_name]
            os.system(f'cp {os.path.join(input_dir, file)} {os.path.join(output_dir, new_filename)}')
            print(f'{ta2_test_name} -> {new_filename}')