import os

from opics_common.opics_logging.log_constants import error_string
from opics_common.results.ev5.eval_results_pvoe_ev5 import EvalResultsPvoe
from opics_common.results.log_stats import LogStats
from opics_common.results.stats_output import (
    express_results_by_cube_ids,
    express_results_by_scene_type,
    header,
)
from opics_common.scene_type.type_constants import abbrev_types, cubes_for_type


class StatsPvoe(LogStats):
    def __init__(self, opics_logs, proj):
        super(StatsPvoe, self).__init__(opics_logs, proj)

    def results_by_scene_type_and_cube_id(self):
        header("summary for pvoe scenes by type and cube id")
        counts_dict = self.init_counts(abbrev_types["pvoe"])
        self.tabulate_counts_for_cube_ids(counts_dict, "*")
        express_results_by_cube_ids(counts_dict, "pvoe", abbrev_types["pvoe"])

    def results_by_scene_type(self):
        header("summary for pvoe scenes by type")
        counts_dict = self.init_counts(abbrev_types["pvoe"])
        self.tabulate_counts_for_types(counts_dict, "*")
        express_results_by_scene_type(counts_dict, abbrev_types["pvoe"])

    def results_plausible_by_scene_type(self):
        header("summary for plausible pvoe scenes")
        counts_dict = self.init_counts(abbrev_types["pvoe"])
        self.tabulate_counts_for_types(counts_dict, "plausible")
        express_results_by_scene_type(counts_dict, abbrev_types["pvoe"])

    def results_implausible_by_scene_type(self):
        header("summary for implausible pvoe scenes")
        counts_dict = self.init_counts(abbrev_types["pvoe"])
        self.tabulate_counts_for_types(counts_dict, "implausible")
        express_results_by_scene_type(counts_dict, abbrev_types["pvoe"])

    def compare_results_to_ta2_eval5_runs(self, answer_key_root):
        files = os.listdir(answer_key_root)
        print("")

        for file in files:
            type = file.split(".")[0].split("__")[1]
            print(f"comparing results to eval5 run for {type}")
            answer_key_for_type = os.path.join(answer_key_root, file)
            if not os.path.exists(answer_key_for_type):
                print("")
                print(
                    f"       ! ERROR could not find answer key for type {type} {answer_key_for_type}"
                )
                print("")
                continue
                print("")
                continue
            f = open(answer_key_for_type, "r")
            lines = f.readlines()
            f.close()
            eval_results = EvalResultsPvoe(lines)

            if type in self.logs_by_type:
                same_count = 0
                for scene_log in self.logs_by_type[type]:
                    if scene_log.result == error_string:
                        continue
                    answer_key_scene_id = (
                        self.get_answer_key_scene_id_from_scene_name(
                            scene_log.scene_name
                        )
                    )
                    answer_key_correctness = (
                        eval_results.correctness_for_scene[
                            answer_key_scene_id
                        ].lower()
                    )
                    is_run_correct = scene_log.is_correct()
                    if answer_key_correctness == "correct" and is_run_correct:
                        same_count += 1
                    elif (
                        answer_key_correctness == "correct"
                        and not is_run_correct
                    ):
                        print(
                            f"   {scene_log.scene_name}\tCHANGE correct->incorrect"
                        )
                    elif (
                        answer_key_correctness == "incorrect"
                        and is_run_correct
                    ):
                        print(
                            f"   {scene_log.scene_name}\tCHANGE incorrect->correct"
                        )
                    elif (
                        answer_key_correctness == "incorrect"
                        and not is_run_correct
                    ):
                        same_count += 1
                print(
                    f"   {same_count} of {len(self.logs_by_type[type])} scenes are the same"
                )

    def use_scene(self, plausibility_requested, scene_plausibility):
        if plausibility_requested == "*":
            return True
        if plausibility_requested == scene_plausibility:
            return True
        return False

    # for each type and cube_id combo, if that type has a logs present, got through each log,
    # decide whether to use it based on proj-specific criteria, get the counts for that type and cube_id combo,
    # and pass it to the base class to increment the success or failure as per log
    def tabulate_counts_for_cube_ids(self, counts, plausibility_requested):
        for scene_type in abbrev_types["pvoe"]:
            if not scene_type in self.logs_by_type_and_cube:
                continue
            for cube_id in cubes_for_type["pvoe"][scene_type]:
                if cube_id in self.logs_by_type_and_cube[scene_type]:
                    for scene_log in self.logs_by_type_and_cube[scene_type][
                        cube_id
                    ]:
                        if not self.use_scene(
                            plausibility_requested,
                            scene_log.scene_plausibility,
                        ):
                            continue
                        cube_counts = counts[scene_type + "_" + cube_id]
                        self.incr_outcome_count(scene_log, cube_counts)

    # for each type, if that type has a logs present, got through each log,
    # decide whether to use it based on proj-specific criteria, get the counts for that type,
    # and pass it to the base class to increment the success or failure count as per log
    def tabulate_counts_for_types(self, counts, plausibility_requested):
        for scene_type in abbrev_types["pvoe"]:
            if not scene_type in self.logs_by_type:
                continue
            for scene_log in self.logs_by_type[scene_type]:
                if scene_log.result == error_string:
                    continue
                if not self.use_scene(
                    plausibility_requested, scene_log.scene_plausibility
                ):
                    continue
                type_counts = counts[scene_type]
                self.incr_outcome_count(scene_log, type_counts)

    def pvoe_scenes_by_category(self, scene_plausibility, correctness):
        print("scenes by catagory not yet implemented")
