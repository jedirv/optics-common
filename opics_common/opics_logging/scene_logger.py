import json
import logging
import os
import sys
from datetime import datetime

from opics_common.opics_logging.log_constants import (
    avoe_expected_string,
    avoe_rating_string,
    avoe_score_string,
    avoe_unexpected_string,
    avoe_noexpectation_string,
    delim,
    exception_string,
    inter_failed_string,
    inter_succeeded_string,
    line_flag,
    pvoe_implausible_string,
    pvoe_plausible_string,
    pvoe_rating_string,
    pvoe_score_string,
)
from opics_common.opics_logging.log_spec import LogSpec
from opics_common.scene_type.type_constants import (
    get_abbrev_scene_type_from_filename,
    get_formal_scene_type_from_filename,
)

dirname_for_category                        = {}
dirname_for_category["intuitive physics"]   = "pvoe"
dirname_for_category["agents"]              = "avoe"
dirname_for_category["retrieval"]           = "inter"
dirname_for_category["imitation"]           = "inter"
dirname_for_category["passive"]             = "inter"
dirname_for_category["multi retrieval"]     = "inter"



def get_proj_from_scene_json(scene_path):
    f = open(scene_path, "r")
    data = json.load(f)
    f.close()
    category = data["goal"]["category"]
    dirname = dirname_for_category[category]
    return dirname


def get_scene_name_from_path(scene_path):
    fname = os.path.basename(scene_path)
    scene_name = fname.split(".")[0]
    return scene_name


def get_log_path(scene_path, scene_name, log_root_dir):
    proj = get_proj_from_scene_json(scene_path)
    current_time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    # name the log file for this scene
    filename = scene_name + "__" + current_time + ".txt"
    if "default" == log_root_dir:
        root_dir = os.getenv("OPTICS_HOME")
        log_root_dir = os.path.join(root_dir, "logs")
    log_proj_dir = os.path.join(log_root_dir, proj)
    type_name = get_abbrev_scene_type_from_filename(scene_name)
    type_dir = os.path.join(log_proj_dir, type_name)
    if not os.path.exists(type_dir):
        os.makedirs(type_dir)
    log_path = os.path.join(type_dir, filename)
    return log_path


class SceneLogger:
    def __init__(self, scene_path, log_spec, log_root_dir):
        self.log_spec = log_spec
        print(f"...setting log level to {log_spec.get_level()}")
        self.logger = logging.getLogger()
        self.logger.setLevel(log_spec.get_level())
        self.scene_name = get_scene_name_from_path(scene_path)

        formatter = logging.Formatter(
            f"%(asctime)s{delim}%(levelname)s{delim}%(name)s{delim}%(message)s"
        )
        log_path = get_log_path(scene_path, self.scene_name, log_root_dir)
        #
        file_handler = logging.FileHandler(filename=log_path)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # stdout_handler = logging.StreamHandler(sys.stdout)
        # stdout_handler.setLevel(log_spec.get_level())
        # self.logger.addHandler(stdout_handler)
        stderr_handler = logging.StreamHandler(sys.stderr)
        self.logger.addHandler(stderr_handler)
        scene_start = line_flag["scene_start"]
        self.logger.info(
            f"{scene_start}{delim}{self.scene_name}{delim}{get_formal_scene_type_from_filename(self.scene_name)}"
        )

    # def set_scene_steps_taken(self,scene_steps):   Now pass stepc count to result messages
    #     self.scene_steps = scene_steps

    def log_spec_okays(self, component, task):
        if not self.log_spec.has_component(component):
            self.log_onetime_warning(
                f"LOGGER FYI - add '{component}' component to cfg/unified_log_config.txt to support focused logging"
            )
        if not self.log_spec.has_task(task):
            self.log_onetime_warning(
                f"LOGGER FYI - add'{task}' task to cfg/unified_log_config.txt to support focused logging"
            )
        if self.log_spec.has_any_combined_focus():
            if self.log_spec.has_combined_focus(component, task):
                return True
            return False

        elif self.log_spec.has_any_individual_focus():
            if self.log_spec.has_component_focus(
                component
            ) or self.log_spec.has_task_focus(task):
                return True
            return False
        else:
            return True

    def log_one_time_info_message(self, message, message_list):
        if not message in message_list:
            message_list.append(message)
            self.logger.info(message)

    def log_onetime_warning(self, warning):
        self.log_one_time_info_message(warning, one_time_warnings)

    # _1;<time>;<calling_module>;detector;wall discrimination;I;assumption;walls are assumed to be black
    def log_assumption(self, component, task, message):
        if self.log_spec_okays(component, task):
            message = (
                component + delim + task + delim + "ASSUMPTION:" + message
            )
            self.log_one_time_info_message(message, assumptions)

    # _1;<time>;<calling_module>;detector;wall discrimination;I;threshold_set;wall_min = 0.24
    def log_threshold(self, component, task, message):
        if self.log_spec_okays(component, task):
            message = component + delim + task + delim + "THRESHOLD:" + message
            self.log_one_time_info_message(message, thresholds)

    def log_finding(self, component, task, message):
        if self.log_spec_okays(component, task):
            m = component + delim + task + delim + "FINDING:" + message
            self.logger.info(m)

    def warning(self, component, task, message):
        m = component + delim + task + delim + message
        self.logger.warning(m)

    def debug(self, component, task, message):
        if self.log_spec_okays(component, task):
            m = component + delim + task + delim + message
            self.logger.debug(m)

    def error(self, component, task, message):
        m = component + delim + task + delim + message
        self.logger.error(m)

    def critical(self, component, task, message):
        m = component + delim + task + delim + message
        self.logger.critical(m)

    def info(self, component, task, message):
        if self.log_spec_okays(component, task):
            m = component + delim + task + delim + message
            self.logger.info(m)

    # pvoe uses this terminology to pass results: rating, score, report
    # Validation run output we get has this terminology:   <scene_name>  classifiation:1, confidence:0.82, so classification is rating, confidence is score

    def log_pvoe_rating_and_score(self, rating, score):
        score_flag = line_flag["score"]
        message = f"{score_flag}{delim}{self.scene_name}{delim}{pvoe_rating_string}:{rating}{delim}{pvoe_score_string}:{score}"
        self.logger.info(message)

    def log_pvoe_result_plausible(self):
        result = line_flag["result"]
        message = (
            f"{result}{delim}{self.scene_name}{delim}{pvoe_plausible_string}"
        )
        self.logger.info(message)

    def log_pvoe_result_implausible(self):
        result = line_flag["result"]
        message = (
            f"{result}{delim}{self.scene_name}{delim}{pvoe_implausible_string}"
        )
        self.logger.info(message)

    def log_pvoe_result_error(self, error_message):
        result = line_flag["result"]
        message = f"{result}{delim}{self.scene_name}{delim}{exception_string}{delim}{error_message}"
        self.logger.info(message)

    def log_avoe_rating_and_score(self, rating, score):
        score_flag = line_flag["score"]
        message = f"{score_flag}{delim}{self.scene_name}{delim}{avoe_rating_string}:{rating}{delim}{avoe_score_string}:{score}"
        self.logger.info(message)

    def log_avoe_result_expected(self):
        result = line_flag["result"]
        message = (
            f"{result}{delim}{self.scene_name}{delim}{avoe_expected_string}"
        )
        self.logger.info(message)

    def log_avoe_result_unexpected(self):
        result = line_flag["result"]
        message = (
            f"{result}{delim}{self.scene_name}{delim}{avoe_unexpected_string}"
        )
        self.logger.info(message)

    
    def log_avoe_result_noexpectation(self):
        result = line_flag["result"]
        message = (
            f"{result}{delim}{self.scene_name}{delim}{avoe_noexpectation_string}"
        )
        self.logger.info(message)

    def log_avoe_result_error(self, error_message):
        result = line_flag["result"]
        message = f"{result}{delim}{self.scene_name}{delim}{exception_string}{delim}{error_message}"
        self.logger.info(message)

    def log_retrieval_success(self, steps):
        result = line_flag["result"]
        message = f"{result}{delim}{self.scene_name}{delim}{inter_succeeded_string}{delim}steps:{steps}"
        self.logger.info(message)

    def log_retrieval_failure(self, steps):
        result = line_flag["result"]
        message = f"{result}{delim}{self.scene_name}{delim}{inter_failed_string}{delim}steps:{steps}"
        self.logger.info(message)

    def log_retrieval_result_error(self, steps, error_message):
        result = line_flag["result"]
        message = f"{result}{delim}{self.scene_name}{delim}{exception_string}{delim}steps:{steps}{delim}{error_message}"
        self.logger.info(message)


scene_logger = "undefined"
log_spec = None

assumptions = []
thresholds = []
one_time_warnings = []


def get_scene_logger():
    global scene_logger
    return scene_logger


def create_scene_logger(scene_path, log_root_dir, testing=False):
    global scene_logger
    global log_spec
    if "undefined" == scene_logger:
        log_spec = LogSpec(testing)
        print("creating logger at " + log_root_dir)
        scene_logger = SceneLogger(scene_path, log_spec, log_root_dir)
    return scene_logger


logging_value_lookup                = {}
logging_value_lookup["CRITICAL"]    = 50
logging_value_lookup["ERROR"]       = 40
logging_value_lookup["WARNING"]     = 30
logging_value_lookup["INFO"]        = 20
logging_value_lookup["DEBUG"]       = 10
logging_value_lookup["NOTSET"]      = 0
