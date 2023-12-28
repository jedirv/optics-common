import os

from opics_common.opics_logging.log_loader import LogLoader
from opics_common.scene_type.type_constants import abbrev_types


def get_cube_id_from_filepath(filepath):
    filename = os.path.basename(filepath)
    cube_id = filename.split("_")[4]
    return cube_id


class OpicsLogs:
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
        f = open(filepath, "r")
        lines = f.readlines()
        clean_lines = []
        for line in lines:
            clean_lines.append(line.rstrip())
        f.close()

        log_loader = LogLoader(proj, scene_type, clean_lines, filepath)
        if not scene_type in self.logs[proj]:
            self.logs[proj][scene_type] = []
            self.logs_for_cubes[proj][scene_type] = {}
        self.logs[proj][scene_type].append(log_loader.scene_log)

        cube_id = get_cube_id_from_filepath(filepath)
        if not cube_id in self.logs_for_cubes[proj][scene_type]:
            self.logs_for_cubes[proj][scene_type][cube_id] = []
        self.logs_for_cubes[proj][scene_type][cube_id].append(
            log_loader.scene_log
        )

    def express_exceptions(self, proj):
        exceptions = {}
        for scene_type in abbrev_types[proj]:
            if scene_type in self.logs[proj]:
                for log in self.logs[proj][scene_type]:
                    if not None == log.exception_info:
                        e = log.exception_info
                        if not e in exceptions:
                            exceptions[e] = []
                        exceptions[e].append(log.scene_name)
        print("\n\nException Scenes:\n")
        for e in exceptions:
            scenes = exceptions[e]
            print(f"\n{e}:")
            for scene in scenes:
                print(f"         {scene}")

    def count_results_unknown(self, proj, scene_type):
        count = 0
        for scene_log in self.logs[proj][scene_type]:
            if scene_log.is_unknown_result():
                count += 1
        return count

    def count_results_fail(self, proj, scene_type):
        count = 0
        for scene_log in self.logs[proj][scene_type]:
            if scene_log.is_failure():
                count += 1
        return count

    def count_results_successes(self, proj, scene_type):
        count = 0
        for scene_log in self.logs[proj][scene_type]:
            if scene_log.is_succeed():
                count += 1
        return count

    def count_results_exceptions(self, proj, scene_type):
        count = 0
        for scene_log in self.logs[proj][scene_type]:
            if scene_log.is_exception():
                count += 1
        return count

    def get_count_for_proj_scene(self, proj, scene_type):
        return len(self.logs[proj][scene_type])