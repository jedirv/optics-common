from opics_common.opics_logging.log_constants import (
    error_string,
    exception_string,
)
from opics_common.results.stats_output import express_results_summary, header
from opics_common.scene_type.type_constants import cubes_for_type


class LogStats:
    def __init__(self, opics_logs, proj):
        self.proj = proj
        self.logs_by_type = opics_logs.logs[proj]
        self.logs_by_type_and_cube = opics_logs.logs_for_cubes[proj]

    def results_summary(self):
        header("summary")
        scene_count = 0
        success_count = 0
        missing_results_count = 0
        exception_count = 0
        broken_scene_count = 0

        for scene_type, logs_for_type in self.logs_by_type.items():
            for scene_log in logs_for_type:
                if scene_log.is_broken:
                    broken_scene_count += 1
                else:
                    scene_count += 1
                    if scene_log.exception_thrown():
                        exception_count += 1
                    correctness = scene_log.is_correct()
                    if correctness == "?":
                        missing_results_count += 1
                    elif correctness == True:
                        success_count += 1

        express_results_summary(
            success_count,
            scene_count,
            missing_results_count,
            exception_count,
            broken_scene_count,
        )

    def init_counts(self, abbrev_category_types):
        counts = {}
        for scene_type in abbrev_category_types:
            counts[scene_type]                            = {}
            counts[scene_type]["scene_count"]             = 0
            counts[scene_type]["success_count"]           = 0
            counts[scene_type]["exception_count"]         = 0
            counts[scene_type]["missing_results_count"]   = 0
            counts[scene_type]["broken_log_count"]        = 0
            counts[scene_type]["broken_log_scenes"] = []
            counts[scene_type]["success_scene_classifier_count"] = 0
            counts[scene_type]["incorrect_classifier_scenes"] = []
            for cube in cubes_for_type[self.proj][scene_type]:
                counts[scene_type + "_" + cube]                             = {}
                counts[scene_type + "_" + cube]["scene_count"]              = 0
                counts[scene_type + "_" + cube]["success_count"]            = 0
                counts[scene_type + "_" + cube]["exception_count"]          = 0
                counts[scene_type + "_" + cube]["missing_results_count"]    = 0
                counts[scene_type + "_" + cube]["broken_log_count"]         = 0
                counts[scene_type + "_" + cube]["success_scene_classifier_count"] = 0
        return counts

    # def results_for_class_summary(self, scene_class):
    #     scene_count = 0
    #     success_count = 0
    #     missing_results_count = 0

    #     for scene_log in self.log_loader.scene_logs:
    #         if scene_log.get_scene_class() == scene_class:
    #             scene_count += 1
    #             correctness =  scene_log.is_correct()
    #             if correctness == '?':
    #                 missing_results_count += 1
    #             elif correctness == True:
    #                 success_count += 1
    #     express_class_results_summary(success_count, scene_count, scene_class, missing_results_count)

    def use_scene(self, plausibility_requested, scene_plausibility):
        if plausibility_requested == "*":
            return True
        if plausibility_requested == scene_plausibility:
            return True
        return False

    # def tabulate_counts_for_type(self, counts, scene_class, plausibility_requested):
    #     for scene_log in self.log_loader.scene_logs:
    #         scene_plausibility = scene_log.get_scene_plausibility()
    #         if not self.use_scene(plausibility_requested, scene_plausibility):
    #             continue
    #         if scene_class == scene_log.get_scene_class():
    #             type = scene_log.scene_type.split('.')[1]
    #             type_counts = counts[type]
    #             type_counts['scene_count'] += 1
    #             correctness =  scene_log.is_correct()
    #             if correctness == '?':
    #                 type_counts['missing_results_count'] += 1
    #             elif correctness == True:
    #                 type_counts['success_count'] += 1

    def incr_success_or_failure_as_per_log(self, scene_log, counts):
        counts["scene_count"] += 1
        if scene_log.is_broken:
            counts["missing_results_count"] += 1
        else:
            correctness = scene_log.is_correct()
            if correctness == "?":
                counts["missing_results_count"] += 1
            elif correctness == True:
                counts["success_count"] += 1
            
    def incr_outcome_count(self, scene_log, counts):
        scene_name = scene_log.scene_name
        scene_type = scene_log.scene_type
        if scene_log.is_broken:
            counts["broken_log_count"] += 1
            if "broken_log_scenes" in counts: # won't be present in the cubeid counts
                counts["broken_log_scenes"].append(scene_name)
        else:
            counts["scene_count"] += 1
            if scene_log.has_scene_classifier():
                classifier_correctness = scene_log.is_scene_classifier_correct()
                if classifier_correctness == True:
                    counts["success_scene_classifier_count"] +=1
                else:
                    if "incorrect_classifier_scenes" in counts: # won't be present in the cubeid counts
                        counts["incorrect_classifier_scenes"].append(scene_name)
            if (
                scene_log.result == error_string
                or scene_log.result == exception_string
            ):
                counts["exception_count"] += 1
            else:
                correctness = scene_log.is_correct()
                if correctness == "?":
                    counts["missing_results_count"] += 1
                elif correctness == True:
                    counts["success_count"] += 1

    def pvoe_scenes_by_category(self, scene_plausibility, correctness):
        print("scenes by catagory not yet implemented")

    def get_answer_key_scene_id_from_scene_name(self, scene_name):
        # coll_alpha_0005_22_G2_implaus -> alpha_0005_22
        parts = scene_name.split("_")
        return parts[1] + "_" + parts[2] + "_" + parts[3]
