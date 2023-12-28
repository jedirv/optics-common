import configparser
import os
import subprocess

import yaml


def get_unity_path(cfg_dir):
    yaml_path = os.path.join(cfg_dir, "unity_path.yaml")
    if not os.path.exists(yaml_path):
        raise FileNotFoundError("unity_path.yaml missing from cfg dir")
    with open(yaml_path, "r") as config_file:
        config = yaml.safe_load(config_file)
    return os.path.join(config["unity_path"])


def get_config_ini_path(cfg_dir):
    print(f"cwd: {os.getcwd()}")
    print("cfg_dir: ", cfg_dir)
    ini_path = os.path.join(cfg_dir, "mcs_config.ini")
    print("ini_path: ", ini_path)
    if not os.path.exists(ini_path):
        raise FileNotFoundError("mcs_config.ini missing from cfg dir")
    return ini_path


def get_level_from_config_ini(config_ini_path):
    config_ini = configparser.ConfigParser()
    config_ini.read(config_ini_path)
    return config_ini["MCS"]["metadata"]


def get_installed_mcs_version():
    result = subprocess.check_output(
        "pip list | grep machine-common-sense", shell=True
    )
    result = result.decode("utf-8").rstrip()
    lines = result.split("\n")
    answer_line = lines[0]
    answer = answer_line.replace("machine-common-sense", "").strip()
    return answer
