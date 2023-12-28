import os

from opics_common.opics_logging.stdout_log import AvoeStdoutLog
from opics_common.scene_type.type_constants import abbrev_types


def get_cube_id_from_filepath(filepath):
    filename = os.path.basename(filepath)
    cube_id = filename.split("_")[4]
    return cube_id


class StdoutLogs:
    def __init__(self):
        self.logs                     = {}
        self.logs["pvoe"]             = {}
        self.logs["avoe"]             = {}
        self.logs["inter"]            = {}

        self.logs_for_cubes           = {}
        self.logs_for_cubes["pvoe"]   = {}
        self.logs_for_cubes["avoe"]   = {}
        self.logs_for_cubes["inter"]  = {}

    def load_file(self, filepath, proj, scene_type):
        if proj == 'pvoe':
             raise Exception('PvoeStdoutLog not yet implemented')
        if proj == 'inter':
            raise Exception('InterStdoutLog not yet implemented')
        f = open(filepath, "r")
        lines = f.readlines()
        clean_lines = []
        for line in lines:
            clean_lines.append(line.rstrip())
        f.close()

        stdout_log = AvoeStdoutLog(filepath, scene_type, clean_lines)
        if not scene_type in self.logs[proj]:
            self.logs[proj][scene_type] = []
            self.logs_for_cubes[proj][scene_type] = {}
        self.logs[proj][scene_type].append(stdout_log)

        cube_id = get_cube_id_from_filepath(filepath)
        if not cube_id in self.logs_for_cubes[proj][scene_type]:
            self.logs_for_cubes[proj][scene_type][cube_id] = []
        self.logs_for_cubes[proj][scene_type][cube_id].append(stdout_log)
