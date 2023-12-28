import random

from opics_common.opics_logging.scene_logger import get_scene_logger
from opics_common.scene_type.type_constants import abbrev_types


def pick_plaus_implaus():
    choice = random.choice(range(0, 2))
    if choice == 0:
        return "plaus"
    else:
        return "implaus"


if __name__ == "__main__":

    logger = get_scene_logger(__name__, logfile_path="test_log_pvoe.txt")

    for i in range(1, 200):
        scene_type = random.choice(abbrev_types["pvoe"])
        scene_name = (
            scene_type
            + "_"
            + str(i).zfill(6)
            + "_"
            + pick_plaus_implaus()
            + ".json"
        )

        #
        # tell the logger what scene it is - this will be done in run_opics.py
        logger.set_scene_name(scene_name)

        #
        # log any assumptions the code is making - this will emit once per run
        #
        # 'tracker'          is a component declared in cfg/unified_log_config.txt
        # 'filter_tracklets' is a task      declared in cfg/unified_log_config.txt
        logger.log_assumption(
            "tracker",
            "filter_tracklets",
            "focus objects that appear for too few frames before occlusion won't be detected",
        )

        #
        # log any thresholds the code is using - this will emit once per run
        #
        logger.log_threshold(
            "tracker", "filter_tracklets", "toss tracklets shorter than 3"
        )

        # for generic debug and info messages
        logger.debug("tracker", "filter_tracklets", "some debug message")
        logger.info("tracker", "filter_tracklets", "some info message")

        #
        # log any summary findings
        #
        logger.log_finding(
            "tracker", "filter_tracklets", "35 short tracklets ignored"
        )

        #
        # for when  plausible is determined
        #
        choice = random.choice(range(0, 2))
        if choice == 0:
            logger.log_result_plausible()
        else:
            logger.log_result_implausible()
