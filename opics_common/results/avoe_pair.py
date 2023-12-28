

#example scene filename : socimit_charlie_0002_01_000000i2e_expected_6c.json

#example TA2_test_name : charlie_0002_01

class AvoePair():
    def __init__(self,log_numbered_01,log_numbered_02):
        self.log_01 = log_numbered_01
        self.log_02 = log_numbered_02
        #self.avoe_results = avoe_results
        parts = self.log_01.scene_name.split('_')
        self.log_01_TA2_test_name = parts[1] + '_' + parts[2] + '_' + parts[3]

    def is_scene_01_more_expected_in_ground_truth(self):
        #expectedness = self.avoe_results.expectedness_for_scene[self.log_01_TA2_test_name]
        expectedness = self.log_01.scene_name.split('_')[5]
        #print(f'expectedness of scene_01 {self.log_01.scene_name} is {expectedness}, 02 is {self.log_02.scene_name}')
        if expectedness == 'mexpected':
            return True
        else:
            return False

    def is_osu_agent_correct_for_training_scene(self):
        #print(f'self.log_01.score {self.log_01.score}')
        if self.log_01.score == None:
            print(f'training scene had None for score : {self.log_01.scene_name}')
            return False
        if self.log_01.score > 0.5:
            return True
        return False

    def is_osu_agent_correct_for_pair(self):
        # each log has a score that is not None, since None scored logs are filtered out prior
        # print('')
        # print(f' log 1 is {self.log_01_TA2_test_name}')
        # print(f'++ self.log_01.score {self.log_01.score}')
        # print(f'++ self.log_02.score {self.log_02.score}')

        # if either scene threw exception, return False
        if self.log_01.exception_occurred or self.log_02.exception_occurred:
            return False
        log_01_is_more_expected = False
        if self.log_01.score > self.log_02.score:
            log_01_is_more_expected = True
        
        if self.is_scene_01_more_expected_in_ground_truth() and log_01_is_more_expected:
            #print(f'++ correct')
            return True
        elif not self.is_scene_01_more_expected_in_ground_truth() and not log_01_is_more_expected:
            #print(f'++ correct')
            return True
        #print(f'++ incorrect')
        return False

    def is_osu_agent_correct(self):
        if self.log_02 == None:
            return self.is_osu_agent_correct_for_training_scene()
        else:
            return self.is_osu_agent_correct_for_pair()

    def is_exception_scene(self, scene_name):
        #print(f'scene name for exception check {scene_name}')
        if self.log_01.scene_name == scene_name:
            #print(f'exception check for log_01 : {self.log_01.exception_occurred}')
            return self.log_01.exception_occurred
        elif self.log_02.scene_name == scene_name:
            #print(f'exception check for log_02 : {self.log_02.exception_occurred}')
            return self.log_02.exception_occurred
        return False

