from opics_common.opics_logging.unified_logger import get_osu_mcs_logger

if __name__ == "__main__":
    logger = get_osu_mcs_logger(__name__, logfile_path="test_log_int.txt")

    logger = get_osu_mcs_logger(__name__, logfile_path="test_log_pvoe.txt")
