import os
import sys


class LogSpec:
    def __init__(self, testing=False):
        self.log_level = "INFO"
        self.components = []
        self.tasks = []
        self.focus_components = []
        self.focus_tasks = []
        self.focus_component_tasks = []
        if testing == True:
            print("loading hardcoded log spec entries for testing")
            self.load_lines(get_test_spec_lines())
        else:
            print("...loading log spec from cfg/unified_log_config.txt")
            self.load_lines(get_log_spec_lines())
        self.express_log_config()

    def express_log_config(self):
        print()
        print(
            f"LOG CONFIG - registered components: {list_on_one_line(self.components)}"
        )
        print(
            f"LOG CONFIG - registered tasks:      {list_on_one_line(self.tasks)}"
        )
        if self.has_any_combined_focus():
            print(
                "LOG CONFIG - logging statements with these combinations of component and task will be logged:"
            )
            for ct in self.focus_component_tasks:
                print(f"LOG CONFIG        {ct}")
        elif self.has_any_individual_focus():
            if len(self.focus_components) != 0:
                print(
                    "LOG CONFIG - logging statements with these components will be logged:"
                )
                for fc in self.focus_components:
                    print(f"LOG CONFIG        {fc}")
            if len(self.focus_tasks) != 0:
                print(
                    "LOG CONFIG - logging statements with these tasks will be logged:"
                )
                for ft in self.focus_tasks:
                    print(f"LOG CONFIG        {ft}")
        else:
            print("LOG CONFIG       all components+tasks will be logged")
        print()

    def load_lines(self, lines):
        for line in lines:
            line = clean_string(line)
            if not line.startswith("#") and not line == "":
                parts = line.split("=")
                key = parts[0]
                val = parts[1]
                if key == "component":
                    self.components.append(val)
                elif key == "task":
                    self.tasks.append(val)
                elif key == "log_level":
                    self.log_level = self.validate_log_level(val)
                elif key == "focus_component":
                    self.focus_components.append(val)
                elif key == "focus_task":
                    self.focus_tasks.append(val)
                elif key == "focus_component_task":
                    self.focus_component_tasks.append(clean_string(val))
                else:
                    print(
                        f"ERROR: invalid key in log_config: {key} - must be log_level|component|task|focus_component|focus_task|focus_component_task"
                    )
                    log_usage()
                    sys.exit()
        self.validate_focus_tasks()
        self.validate_focus_components()
        self.validate_focus_component_tasks()

    def is_component_declared(self, component):
        return component in self.components

    def is_task_declared(self, task):
        return task in self.tasks

    def validate_focus_component_tasks(self):
        for item in self.focus_component_tasks:
            parts = item.split("+")
            if not len(parts) == 2:
                print(
                    f"ERROR: invalid value for focus_component_task declaration: {item}"
                )
                log_usage()
                sys.exit()
            if not self.is_component_declared(parts[0]):
                print(
                    f"ERROR: undeclared component used in focus_component_task declaration: {item} -check for typo"
                )
                log_usage()
                sys.exit()
            if not self.is_task_declared(parts[1]):
                print(
                    f"ERROR: undeclared task used in focus_component_task declaration: {item} -check for typo"
                )
                log_usage()
                sys.exit()

    def validate_focus_tasks(self):
        for task in self.focus_tasks:
            if not self.is_task_declared(task):
                print(
                    f"ERROR: undeclared task used in focus_task declaration: {task} -check for typo"
                )
                log_usage()
                sys.exit()

    def validate_focus_components(self):
        for c in self.focus_components:
            if not self.is_component_declared(c):
                print(
                    f"ERROR: undeclared component used in focus_component declaration: {c} -check for typo"
                )
                log_usage()
                sys.exit()

    def validate_log_level(self, level):
        valid_list = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
        if not level.upper() in valid_list:
            print(
                f"ERROR: invalid log level specified in log_config.txt: {level}"
            )
            sys.exit()
        return level.upper()

    def get_level(self):
        return self.log_level

    def has_any_combined_focus(self):
        return len(self.focus_component_tasks) > 0

    def has_combined_focus(self, component, task):
        combined = component + "+" + task
        if combined in self.focus_component_tasks:
            return True
        return False

    def has_any_individual_focus(self):
        return len(self.focus_components) + len(self.focus_tasks) > 0

    def has_component_focus(self, component):
        if component in self.focus_components:
            return True
        return False

    def has_task_focus(self, task):
        if task in self.focus_tasks:
            return True
        return False

    def has_component(self, component):
        if component in self.components:
            return True
        return

    def has_task(self, task):
        if task in self.tasks:
            return True
        return False


def clean_string(s):
    s = s.replace(" ", "")
    s = s.replace("\t", "")
    s = s.rstrip()
    return s


def log_usage():
    print(
        "# logging level is defaulted to INFO unless a log_level declaration is present"
    )
    print("log_level=DEBUG")
    print("")
    print("")
    print(
        "# components declared like this will be logged unless focus declarations are present"
    )
    print("component = tracker")
    print("component=open_container_skill")
    print("")
    print(
        "# tasks declared like this will be logged unless focus declarations are present"
    )
    print("task = destination prediction")
    print("task =  soccer ball recog")
    print("")
    print(
        "# if a focus_task or focus_component declarations is present, only components and tasks mentioned in those will be logged"
    )
    print(
        "# (component and task entries not mentioned will be ignored for logging"
    )
    print("focus_task=soccer ball recog")
    print("focus_component=wall remover")
    print("")
    print(
        "# if any focus_component_task declarations are present, only logging statements involving both that component and that task will be logged"
    )
    print(
        "# (component and task declarations will be ignored as well as  focus_component and focus_task declarations"
    )
    print("focus_component_task=tracker+destination prediction")
    print("")


def get_log_spec_lines():
    dir = os.getenv("OPTICS_HOME")
    cfg_dir = os.path.join(dir, "cfg")
    log_spec = os.path.join(cfg_dir, "unified_log_config.txt")
    if not os.path.exists(log_spec):
        print(
            "WARNING - cfg/unified_log_config.txt not found - unified logging system not configured - loging statements will be ignored"
        )
        return []
    else:
        with open(log_spec) as f:
            lines = f.readlines()
            return lines


def get_test_spec_lines():
    lines = []
    lines.append("log_level=INFO")
    lines.append("")
    lines.append("component=comp_a")
    lines.append("component = comp_b")
    lines.append("task = task_1")
    lines.append("task = task_2")
    lines.append("task = task_3")
    lines.append("#focus_task = task_1")
    lines.append("#focus_component_task = comp_a+task_1")
    lines.append("#focus_component_task = comp_b+task_3")
    return lines


def list_on_one_line(items):
    result = ""
    delim = ", "
    for item in items:
        result += item
        result += delim
    result = result[: -len(delim)]
    return result
