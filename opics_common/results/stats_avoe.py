from opics_common.results.log_stats import LogStats
from opics_common.results.stats_output import (
    express_results_by_scene_type,
    header,
)
from opics_common.scene_type.type_constants import abbrev_types


class StatsAvoe(LogStats):
    def __init__(self, opics_logs, proj):
        super(StatsAvoe, self).__init__(opics_logs, proj)

    def results_by_scene_type(self):
        header("summary for avoe scenes by type")
        counts_dict = self.init_counts(abbrev_types["avoe"])
        self.tabulate_counts_for_type(counts_dict, "*")
        express_results_by_scene_type(counts_dict, abbrev_types["avoe"])

    def results_expected_by_scene_type(self):
        header("summary for expected avoe scenes")
        counts_dict = self.init_counts(abbrev_types["avoe"])
        self.tabulate_counts_for_type(counts_dict, "expected")
        express_results_by_scene_type(counts_dict, abbrev_types["avoe"])

    def results_unexpected_by_scene_type(self):
        header("summary for unexpected avoe scenes")
        counts_dict = self.init_counts(abbrev_types["avoe"])
        self.tabulate_counts_for_type(counts_dict, "unexpected")
        express_results_by_scene_type(counts_dict, abbrev_types["avoe"])

    def results_noexpectation_by_scene_type(self):
        header("summary for noexpectation avoe scenes")
        counts_dict = self.init_counts(abbrev_types["avoe"])
        self.tabulate_counts_for_type(counts_dict, "noexpectation")
        express_results_by_scene_type(counts_dict, abbrev_types["avoe"])

    def use_scene(self, expectation_requested, scene_expectation):
        #print(f' expectation_requested {expectation_requested}  scene_expectation {scene_expectation}')
        if expectation_requested == "*":
            #print(f' expectation_requested was *, so use - {scene_expectation}')
            return True
        if expectation_requested == scene_expectation:
            #print(f' they matched, so use - {scene_expectation}')
            return True
        #print(f' they did not match, so skip - {scene_expectation}')
        return False

    def tabulate_counts_for_type(self, counts, expectation_requested):
        for scene_type in abbrev_types["avoe"]:
            if not scene_type in self.logs_by_type:
                continue
            for scene_log in self.logs_by_type[scene_type]:
                if self.is_training_scene_filtered_out(scene_log):
                   continue
                if not self.use_scene(
                    expectation_requested, scene_log.scene_expectation
                ):
                    continue
                type_counts = counts[scene_type]
                self.incr_success_or_failure_as_per_log(scene_log, type_counts)

    def is_training_scene_filtered_out(self, scene_log):
        # this is intended to remove trhe eval5 scene types that have been included in the training data
        if '_training_' in scene_log.scene_name and 'multa_' in scene_log.scene_name:
            return True
        return False