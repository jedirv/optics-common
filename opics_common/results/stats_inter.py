from opics_common.results.log_stats import LogStats
from opics_common.results.stats_output import (
    express_results_by_cube_ids,
    express_results_by_scene_type,
    express_scene_classifier_results, 
    header,
)
from opics_common.scene_type.type_constants import abbrev_types, cubes_for_type


class StatsInter(LogStats):
    def __init__(self, opics_logs, proj):
        super(StatsInter, self).__init__(opics_logs, proj)

    def results_scene_classifier(self):
        header("scene classifier scores")
        counts_dict = self.init_counts(abbrev_types["inter"])
        self.tabulate_counts_for_type(counts_dict)
        express_scene_classifier_results(counts_dict, abbrev_types["inter"])

    def results_by_scene_type_and_cube_id(self):
        header("summary for inter scenes by type and cube id")
        counts_dict = self.init_counts(abbrev_types["inter"])
        self.tabulate_counts_for_cube_ids(counts_dict)
        express_results_by_cube_ids(
            counts_dict, "inter", abbrev_types["inter"]
        )

    def results_by_scene_type(self):
        header("summary for inter scenes by type")
        counts_dict = self.init_counts(abbrev_types["inter"])
        self.tabulate_counts_for_type(counts_dict)
        express_results_by_scene_type(counts_dict, abbrev_types["inter"])

    def use_scene(self, expectation_requested, scene_expectation):
        if expectation_requested == "*":
            return True
        if expectation_requested == scene_expectation:
            return True
        return False

    # for each type and cube_id combo, if that type has a logs present, got through each log,
    # get the counts for that type and cube_id combo,
    # and pass it to the base class to increment the success or failure as per log
    def tabulate_counts_for_cube_ids(self, counts):
        for scene_type in abbrev_types["inter"]:
            if not scene_type in self.logs_by_type_and_cube:
                continue
            for cube_id in cubes_for_type["inter"][scene_type]:
                # the following if statement is needed because we divide up the inter scenes into weighted and unweighted
                # and a particular run will be one or the other or both
                if cube_id in self.logs_by_type_and_cube[scene_type]:
                    for scene_log in self.logs_by_type_and_cube[scene_type][cube_id]:
                        # if scene_log.result == inter_error_string:
                        #    continue
                        cube_counts = counts[scene_type + "_" + cube_id]
                        self.incr_outcome_count(scene_log, cube_counts)

    def tabulate_counts_for_type(self, counts):
        for scene_type in abbrev_types["inter"]:
            if not scene_type in self.logs_by_type:
                continue
            for scene_log in self.logs_by_type[scene_type]:
                type_counts = counts[scene_type]
                self.incr_outcome_count(scene_log, type_counts)
