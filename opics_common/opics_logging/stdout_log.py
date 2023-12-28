import os

class StdoutLog:
    def __init__(self, scene_name, scene_type, lines):
        self.scene_name = scene_name
        self.scene_type = scene_type
        self.lines = lines
        self.score = None
        self.exception_occurred = False

class AvoeStdoutLog(StdoutLog):
    def __init__(self, path, scene_type, lines):
        scene_name = os.path.basename(path).split(".")[0].replace('_stdout','')
        super(AvoeStdoutLog, self).__init__(scene_name, scene_type, lines)
        for line in lines:
            if ';classification:' in line:
                self.score = float(line.split(';')[1].split(':')[1])
            if 'Exception' in line:
                self.exception_occurred = True

   
  