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
    header = '?"'
    for line in lines:
        if line.startswith('CATEGORY'):
            header = line
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
    return header, lines_pvoe, lines_inter, lines_avoe

def create_file(name, header, lines):
    f = open(name, 'w')
    f.write(header)
    for line in lines:
        f.write(line)
    f.close()

if __name__ == '__main__':
    header, lines_pvoe, lines_inter, lines_avoe = load_answer_key()

    create_file('eval6_results_pvoe.csv', header, lines_pvoe)
    create_file('eval6_results_inter.csv',header, lines_inter)
    create_file('eval6_results_avoe.csv',header, lines_avoe)