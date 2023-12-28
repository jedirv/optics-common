import os, sys
from pathlib import Path
from opics_common.results.ev6.eval_results_avoe_ev6 import EvalResultsAvoe
from opics_common.results.avoe_pair import AvoePair
from opics_common.scene_type.type_constants import abbrev_types
from opics_common.results.stats_output import express_results_by_scene_type, express_results_summary

#example scene filename : socimit_charlie_0002_01_000000i2e_expected_6c.json

class AvoePairs():
    def __init__(self, stdout_logs):
        if not'OPTICS_HOME' in os.environ:
            print('...must set OPTICS_HOME')
            sys.exit()
        optics_home = os.environ['OPTICS_HOME']
        #answers_path = os.path.join(optics_home, 'opics_common', 'opics_common', 'results','ev6','eval6_results_avoe.csv')
        #f = open(answers_path, 'r')
        #lines = f.readlines()
        #f.close()
        #self.avoe_results = EvalResultsAvoe(lines)
        self.exception_pairs = 0
        self.stdout_logs = stdout_logs
        self.pairs_for_type = {}
        self.skipped_pairs = 0
        for scene_type in stdout_logs.logs['avoe']:
            avoe_logs = stdout_logs.logs['avoe'][scene_type]
            logs_numbered_01 = self.gather_logs_numbered_01(avoe_logs)
            for log_numbered_01 in logs_numbered_01:
                log_numbered_02 = self.get_matching_log_numbered_02(log_numbered_01, avoe_logs)
                if log_numbered_02 == None:
                    if '_training_' in log_numbered_01.scene_name:
                        pair = AvoePair(log_numbered_01,None)
                        #scene_type = log_numbered_01.scene_type
                        if not scene_type in self.pairs_for_type:
                            self.pairs_for_type[scene_type] = []
                        self.pairs_for_type[scene_type].append(pair)
                    else:
                        print(f'WARNING - could not find matching log numbered 02 for log_numbered_01 {log_numbered_01.scene_name} - skipping pair for avoe scoring')
                        self.skipped_pairs += 1
                elif self.did_either_log_contain_exception(log_numbered_01, log_numbered_02):
                    self.exception_pairs += 1
                    pair = AvoePair(log_numbered_01,log_numbered_02)
                    #scene_type = log_numbered_01.scene_type
                    if not scene_type in self.pairs_for_type:
                        self.pairs_for_type[scene_type] = []
                    self.pairs_for_type[scene_type].append(pair)

                elif self.is_either_log_missing_score(log_numbered_01, log_numbered_02):
                    print(f'WARNING - missing score in at least one of the pair {log_numbered_01.scene_name} - skipping for avoe scoring')
                    self.skipped_pairs += 1
                else:
                    pair = AvoePair(log_numbered_01,log_numbered_02)
                    #scene_type = log_numbered_01.scene_type
                    if not scene_type in self.pairs_for_type:
                        self.pairs_for_type[scene_type] = []
                    self.pairs_for_type[scene_type].append(pair)


    def did_either_log_contain_exception(self, l1, l2):
        if l1.exception_occurred or l2.exception_occurred :
            return True
        return False


    def is_either_log_missing_score(self, l1, l2):
        if l1.score == None or l2.score == None:
            return True
        return False

    def gather_logs_numbered_01(self, avoe_logs):
        logs_numbered_01 = []
        for avoe_log in avoe_logs:
            number_string = avoe_log.scene_name.split('_')[3]
            if number_string == '01':
                logs_numbered_01.append(avoe_log)
        return logs_numbered_01

    def get_test_name_from_filename(self, avoe_log):
        parts = avoe_log.scene_name.split('_')
        test_name = parts[0] + '_' + parts[1] + '_' + parts[2] + '_' + parts[3]
        return  test_name

    def get_matching_log_numbered_02(self, log_numbered_01, avoe_logs):
        test_name = self.get_test_name_from_filename(log_numbered_01)
        parts = test_name.split('_')
        ta2_scene_name = parts[0] + '_' + parts[1] + '_' + parts[2] + '_02'
        #print(f'ta2_scene_name is {ta2_scene_name}')
        for avoe_log in avoe_logs:
            
            if ta2_scene_name in avoe_log.scene_name:
                return avoe_log
        return None

    def results_pairwise_by_scene_type(self):
        scene_type_counts = {}
        scene_types_present = []
        total_pair_count = 0
        total_pair_success_count = 0
        for scene_type in self.pairs_for_type:
            scene_types_present.append(scene_type)
            counts = {}
            scene_type_counts[scene_type] = counts
            counts["missing_results_count"] = 0
            counts["exception_count"] = 0
            counts["success_count"] = 0
            counts["scene_count"] = 0
            if scene_type in self.pairs_for_type:
                pairs = self.pairs_for_type[scene_type]
                for pair in pairs:
                    counts["scene_count"] += 1
                    total_pair_count += 1
                    if pair.is_osu_agent_correct():
                        total_pair_success_count += 1
                        counts["success_count"] += 1
                    else:
                        print(f'incorrect pair: {pair.log_01_TA2_test_name}')
                        print(f'    log1 {pair.log_01.scene_name}\t\twe scored: {pair.log_01.score}')
                        if not pair.log_02 == None:
                            print(f'    log2 {pair.log_02.scene_name}\twe scored: {pair.log_02.score}')
                        print('')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print('                    summary')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print('')
        express_results_summary(total_pair_success_count, total_pair_count,self.skipped_pairs,self.exception_pairs,0)
        print('')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print('                    summary for avoe scenes by type')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print('')
        express_results_by_scene_type(scene_type_counts, scene_types_present)
        print('')

if __name__ == '__main__':
    pass
