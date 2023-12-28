import os

from opics_common.opics_logging.log_constants import (
    delim,
    index_map,
    line_flag,
)
from opics_common.opics_logging.scene_log import (
    AvoeSceneLog,
    InterSceneLog,
    PvoeSceneLog,
)
from opics_common.results.stats_output import warning


class LogLoader:
    def __init__(self, category, abbrev_type, lines, path):
        self.lines = lines
        self.path = path
        name = os.path.basename(path).split(".")[0].split("__")[0]
        self.scene_log = self.load_scene_log(category, abbrev_type, name)

    def get_line_with_cue(self, lines, cue):
        for line in lines:
            if cue in line:
                return line
        return "missing"

    def load_scene_log(self, category, abbrev_type, name):
        scene_log = "?"
        # start_line = self.get_line_with_cue(
        #     self.lines, line_flag["scene_start"]
        # )
        # start_time = "?"
        # module = "?"
        # if start_line != "missing":
        #     (
        #         start_time,
        #         module,
        #         scene_name,
        #         scene_type,
        #     ) = get_scene_info_from_start_line(start_line)
        if category == "pvoe":
            scene_log = PvoeSceneLog(name, abbrev_type)
        elif category == "avoe":
            scene_log = AvoeSceneLog(name, abbrev_type)
        elif category == "inter":
            scene_log = InterSceneLog(name, abbrev_type)
        # if start_line == "missing":
        #     scene_log.is_broken = True
        #     warning(f"missing start line in {name}")
        scene_log.add_lines(self.lines)
        result_line = self.get_line_with_cue(self.lines, line_flag["result"])
        if result_line == "missing":
            scene_log.is_broken = True
            warning(f"missing result line in {name}")
        else:
            scene_log.add_result(result_line, category)
            scene_log.extract_any_error_info(result_line)
            if category == "inter":
                scene_log.extract_step_count(result_line)
        return scene_log


def get_scene_info_from_start_line(line):
    start_scene_cue = line_flag["scene_start"]
    parts = line.split(delim)
    scene_name_index = index_map[start_scene_cue]["scene_name"]
    scene_type_index = index_map[start_scene_cue]["scene_type"]
    scene_start_index = index_map[start_scene_cue]["time"]
    module_index = index_map[start_scene_cue]["module"]
    scene_name = parts[scene_name_index]
    scene_type = parts[scene_type_index]
    start_time = parts[scene_start_index]
    module = parts[module_index]
    return (start_time, module, scene_name, scene_type)
