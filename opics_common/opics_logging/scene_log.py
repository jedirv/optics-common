from opics_common.opics_logging.log_constants import (
    avoe_expected_string,
    avoe_unexpected_string,
    avoe_noexpectation_string,
    delim,
    error_string,
    exception_string,
    index_map,
    inter_failed_string,
    inter_succeeded_string,
    line_flag,
    pvoe_implausible_string,
    pvoe_plausible_string,
)
from opics_common.scene_type.type_constants import get_abbrev_scene_type_from_filename


class SceneLog:
    def __init__(self, scene_name, scene_type):
        self.scene_name = scene_name
        self.scene_type = scene_type
        self.lines = []
        self.is_broken = False
        self.result = "unknown"
        self.exception_info = None

    def add_lines(self, lines):
        self.lines = lines

    def get_result_from_result_line(self, line, category):
        parts = line.split(delim)
        result_value_index = index_map[line_flag["result"]][category]["result_value"]
        if result_value_index >= len(parts):
            return "unknown"
        return parts[result_value_index]

    def add_result(self, result_line, category):
        self.result = self.get_result_from_result_line(result_line, category)

    def has_result(self):
        return self.result != "unknown"

    def exception_thrown(self):
        if self.result == error_string:
            return True
        if self.result == exception_string:
            return True
        return False


class PvoeSceneLog(SceneLog):
    def __init__(self, scene_name, scene_type):
        self.scene_plausibility = self.get_scene_plausibility_from_name(
            scene_name
        )
        super(PvoeSceneLog, self).__init__(
            scene_name, scene_type
        )

    def get_scene_plausibility_from_name(self, name):
        if "implaus" in name:
            return pvoe_implausible_string
        elif "plaus" in name:
            return pvoe_plausible_string
        else:
            return "unknown"

    def extract_any_error_info(self, result_line):
        if not self.exception_thrown():
            return
        parts = result_line.split(delim)

        self.exception_info = None
        exception_info_index = index_map[line_flag["result"]]["pvoe"][
            "exception_detail"
        ]
        if exception_info_index < len(parts):
            self.exception_info = parts[exception_info_index]
            #print(f"found exception_info {self.exception_info}")

    def is_correct(self):
        if self.result == error_string or self.result == exception_string:
            return False
        if self.scene_plausibility == "unkown":
            return "?"
        if self.result == "unknown":
            return "?"
        return self.scene_plausibility == self.result

    def get_scene_category(self):
        return "pvoe"

    def has_scene_classifier(self):
        return False 

    def is_scene_classifier_correct(self):
        # only relevant to inter
        return False

# 2022-07-04 02:18:51,588 ; INFO ; root ; SCENE_START ; eval5_validation_avoe_effic_irrat_0001_01_expected ; scene_type_not_recognized
# 2022-07-04 02:28:10,510 ; INFO ; root ; RESULT ; eval5_validation_avoe_effic_irrat_0001_01_expected ; expected
# 2022-07-04 02:28:10,510 ; INFO ; root ; SCORE ; eval5_validation_avoe_effic_irrat_0001_01_expected ; rating:0.5986876601124521 ; score:0.6503642039542142


class AvoeSceneLog(SceneLog):
    def __init__(self, scene_name, scene_type):
        self.scene_expectation = self.get_scene_expectation_from_name(
            scene_name
        )
        super(AvoeSceneLog, self).__init__(scene_name, scene_type)

    def get_scene_expectation_from_name(self, name):
        if "unexpected" in name:
            return avoe_unexpected_string
        elif "expected" in name:
            return avoe_expected_string
        elif "noexpectation" in name:
            return avoe_noexpectation_string
        else:
            return "unknown"

    def is_correct(self):
        if self.scene_expectation == "unkown":
            return "?"
        if self.result == "unknown":
            return "?"
        #print(f'{self.scene_name} is correct() has expectation {self.scene_expectation} and result {self.result}')
        return self.scene_expectation == self.result

    def get_scene_category(self):
        return "avoe"

    def has_scene_classifier(self):
        return False 
        
    def is_scene_classifier_correct(self):
        # only relevant to inter
        return False

    
    def extract_any_error_info(self, result_line):
        if not self.exception_thrown():
            return
        parts = result_line.split(delim)

        self.exception_info = None
        exception_info_index = index_map[line_flag["result"]]["avoe"][
            "exception_detail"
        ]
        if exception_info_index < len(parts):
            self.exception_info = parts[exception_info_index]
            # print(f"found exception_info {self.exception_info}")

class InterSceneLog(SceneLog):
    def __init__(self, scene_name, scene_type):
        super(InterSceneLog, self).__init__(
            scene_name, scene_type
        )

    def extract_step_count(self, result_line):
        parts = result_line.split(delim)
        self.step_count = -1
        step_count_index = index_map[line_flag["result"]]["inter"]["step_count"]
        # if step_count_index < len(parts):
        #     steps_string = parts[step_count_index].split(":")[1]
        #     self.step_count = int(steps_string)
        #     print(f"found step_count {self.step_count}")

    def extract_any_error_info(self, result_line):
        if not self.exception_thrown():
            return
        parts = result_line.split(delim)
        self.step_count = -1
        step_count_index = index_map[line_flag["result"]]["inter"]["step_count"]
        if step_count_index < len(parts):
            steps_string = parts[step_count_index].split(":")[1]
            self.step_count = int(steps_string)
            # print(f"found step_count for exception {self.step_count}")
        self.exception_info = None
        exception_info_index = index_map[line_flag["result"]]["inter"]["exception_detail"]
        if exception_info_index < len(parts):
            self.exception_info = parts[exception_info_index]
            #print(f"found exception_info {self.exception_info}")


    def has_scene_classifier(self):
        return True 
        
    def is_scene_classifier_correct(self):
        for line in self.lines:
            # 2023-03-04 15:14:24 ; CLASSIFIER ; seeing_leads_to_knowing ; InterAgent:try_run_scene ; SCENE_NAME NOT SET ;
            if 'SCENE_CLASSIFIER_ANSWER' in line:
                parts = line.split(delim)
                answer_index = index_map[line_flag["scene_classifier_answer"]]["inter"]["answer_value"]
                answer = parts[answer_index].strip()
                #scene_name_index = index_map[line_flag["scene_classifier_answer"]]["inter"]["scene_name"]
                #scene_name = parts[scene_name_index].strip()
                actual_scene_type = get_abbrev_scene_type_from_filename(self.scene_name)
                if actual_scene_type == answer:
                    return True 
                if answer == 'num':
                    if self.is_math_or_num_comp(actual_scene_type):
                        return True
                if answer == 'traj':
                    if actual_scene_type in ['coltraj','hidtraj']:
                        return True
                if answer == 'xp':
                    if self.is_scene_type_explore_and_pick(actual_scene_type):
                        return True 
                return False
        return False

    def is_math_or_num_comp(self, scene_type):
        if scene_type in ['math','numcomp']:
            return True 
        return False

    def is_scene_type_explore_and_pick(self, scene_type):
        if scene_type in ['obst','cont','lava','holes','occl', 'ramps', 'tool', 'tlas']:
            return True 
        return False 

    def is_correct(self):
        if self.scene_type == 'sltk':
            plausibility = self.get_scene_plausibility_from_sltk_name(self.scene_name)
            if self.result == plausibility:
                return True
            else:
                return False
        if self.result == error_string or self.result == exception_string:
            return False
        if self.result == "unknown":
            return False
        elif self.result == inter_succeeded_string:
            return True
        elif self.result == inter_failed_string:
            return False
        elif self.result == "True":
            return True
        elif self.result == "False":
            return False
        else:
            return "?"

    def get_scene_category(self):
        return "inter"

    def get_scene_plausibility_from_sltk_name(self, name):
        if "implaus" in name:
            return pvoe_implausible_string
        elif "plaus" in name:
            return pvoe_plausible_string
        else:
            return "unknown"

    def is_unknown_result(self):
        return self.result == 'unknown'

    def is_failure(self):
        if self.result == inter_failed_string:
            return True
        if self.result == 'False':
            return True
        return False

    def is_exception(self):
        if self.result == exception_string:
            return True 
        if self.result == 'error':
            return True 
        return False
        
    def is_succeed(self):
        #print(f' self.result of {self.scene_name} is -{self.result}-')
        if self.result == inter_succeeded_string:
            return True
        if self.result == 'True':
            return True
        return False