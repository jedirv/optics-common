import os
import sys

from opics_common.opics_logging.opics_logs import OpicsLogs
from opics_common.results.stats_avoe import StatsAvoe
from opics_common.results.stats_inter import StatsInter
from opics_common.results.stats_output import stats_title
from opics_common.results.stats_pvoe import StatsPvoe
from opics_common.scene_type.type_constants import formal_type


def usage():
    print("python results_reader.py <path to logroot> <pvoe|avoe|inter>")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        sys.exit()

    log_root = sys.argv[1]
    if not os.path.isdir(log_root):
        print(f"given path does not exist : {log_root}")
        usage()
        sys.exit()

    target = sys.argv[2]
    if not (
        target == "*"
        or target == "pvoe"
        or target == "avoe"
        or target == "inter"
    ):
        usage()
        sys.exit()

    opics_logs = OpicsLogs()
    category_dir = os.path.join(log_root, target)
    for type in formal_type:
        type_dir = os.path.join(category_dir, type)
        if os.path.exists(type_dir):
            files = os.listdir(type_dir)
            print(type_dir)
            for file in files:
                filepath = os.path.join(type_dir, file)
                if os.path.isfile(filepath):
                    print(f"file:  {filepath}")
                    opics_logs.load_file(filepath, target, type)

    if target == "pvoe":
        pvoe_stats = StatsPvoe(opics_logs, "pvoe")
    elif target == "avoe":
        avoe_stats = StatsAvoe(opics_logs, "avoe")
    else:
        inter_stats = StatsInter(opics_logs, "inter")

    stats_title(log_root)
    if target == "pvoe":
        pvoe_stats.results_summary()
        pvoe_stats.results_by_scene_type()
        pvoe_stats.results_plausible_by_scene_type()
        pvoe_stats.results_implausible_by_scene_type()
        print("")

        # pvoe_stats.outcome_by_category('plausible','correct')
        # pvoe_stats.outcome_by_category('plausible','incorrect')
        # pvoe_stats.outcome_by_category('implausible','correct')
        # pvoe_stats.outcome_by_category('implausible','incorrect')
    elif target == "avoe":
        avoe_stats.results_summary()
        avoe_stats.results_by_scene_type()
        avoe_stats.results_expected_by_scene_type()
        avoe_stats.results_unexpected_by_scene_type()
        print("")
        # avoe_stats.pvoe_outcome_by_category('expected','correct')
        # avoe_stats.pvoe_outcome_by_category('expected','incorrect')
        # avoe_stats.pvoe_outcome_by_category('unexpected','correct')
        # avoe_stats.pvoe_outcome_by_category('unexpected','incorrect')
    else:
        # inter
        inter_stats.results_summary()
        inter_stats.results_by_scene_type()
        print("")
