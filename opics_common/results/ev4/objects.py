import argparse
import json
import os
import sys

from header_val_indices import val_index

foci = []
# foci.append('centerOfMass.x')
# foci.append('centerOfMass.y')
# foci.append('centerOfMass.z')
# foci.append('changeMaterials.materials')
# foci.append('changeMaterials.stepBegin')
# foci.append('mass')
# foci.append('materials')
# foci.append('moves.stepBegin')
# foci.append('moves.stepEnd')
# foci.append('moves.vector.x')
# foci.append('moves.vector.y')
# foci.append('moves.vector.z')
# foci.append('resetCenterOfMass')
# foci.append('salientMaterials')
# foci.append('shows.position.x')
# foci.append('shows.position.y')
# foci.append('shows.position.z')
# foci.append('shows.rotation.x')
# foci.append('shows.rotation.y')
# foci.append('shows.rotation.z')
# foci.append('shows.scale.x')
# foci.append('shows.scale.y')
# foci.append('shows.scale.z')
# foci.append('shows.stepBegin')
# foci.append('shrouds.stepBegin')  shrouds used to hide the invisible support for
foci.append("shrouds.stepEnd")
# foci.append('togglePhysics.stepBegin')


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene_dir", default="junk1")
    parser.add_argument("--answer_key", default="junk2")
    return parser


value_map = {}
vals_seen = []


def note_value_of(data, key, success):
    if key in data:
        val = data[key]
        if not val in value_map:
            value_map[val] = {}
            value_map[val]["Correct"] = 0
            value_map[val]["Incorrect"] = 0
        value_map[val][success] += 1


def note_value(val, success):
    if type(val) == float:
        val = round(val, 3)
    if not val in value_map:
        value_map[val] = {}
        value_map[val]["Correct"] = 0
        value_map[val]["Incorrect"] = 0
    value_map[val][success] += 1
    if not val in vals_seen:
        vals_seen.append(val)


def get_physics_object(data):
    objs = data["objects"]
    for o in objs:
        if "physics" in o:
            return o


def has_invisible_support(data):
    objs = data["objects"]
    for o in objs:
        if o["id"].startswith("invisible"):
            return True
    return False


def remove_invisible_cube(data):
    objs = data["objects"]
    new_objs = []
    for o in objs:
        if o["id"].startswith("invisible"):
            pass
        else:
            new_objs.append(o)
    data["objects"] = new_objs


def get_percent_string(val, boldness):
    remainder = 100 - val
    marker = "="
    if boldness == "bold":
        marker = "#"
    result = ""
    for i in range(0, val):
        result = result + marker
    for i in range(0, remainder):
        result = result + "."
    return result


def get_value_for_focus(obj, focus):
    parts = focus.split(".")
    result = None
    if len(parts) == 3:
        if parts[0] in obj:
            if parts[1] in obj[parts[0]]:
                if parts[2] in obj[parts[0]][parts[1]]:
                    result = obj[parts[0]][parts[1]][parts[2]]
    elif len(parts) == 2:
        if parts[0] in obj:
            if parts[1] in obj[parts[0]]:
                result = obj[parts[0]][parts[1]]
    elif len(parts) == 1:
        if parts[0] in obj:
            result = obj[parts[0]]
    else:
        print("focus {} has more than three levels".format(focus))
    return result


if __name__ == "__main__":
    args = make_parser().parse_args()
    scene_dir = args.scene_dir
    answer_key = args.answer_key

    if not os.path.isdir(scene_dir):
        print("scene_dir dir {} doesn't exist.".format(scene_dir))
        print(
            "usage:  python results_by_shape.py --scene_dir <scene_dir> --answer_key <answer_key_path>"
        )
        sys.exit()
    if not os.path.isfile(answer_key):
        print("answer_key {} not valid.".format(answer_key))
        print(
            "usage:  python results_by_shape.py --scene_dir <scene_dir> --answer_key <answer_key_path>"
        )
        sys.exit()
    # limit = 100
    limit = 45
    print("scene_dir {}".format(scene_dir))
    print("answer_key {}".format(answer_key))
    for focus in foci:
        print("--------------------------------------------")
        print(
            "object item {} that gets {} or less percent correct".format(
                focus, limit
            )
        )
        value_map = {}
        vals_seen = []

        f = open(answer_key)
        lines = f.readlines()
        f.close()
        count = 0
        success_count = 0
        fail_count = 0
        mystery_count = 0
        for i in range(2, len(lines)):
            line = lines[i]
            parts = line.split(",")
            scene_name = parts[val_index["TEST NAME"]]
            success = parts[val_index["EVALUATION SCORE ACCURACY"]]
            scene_filename = scene_name + ".json"
            scene_path = os.path.join(scene_dir, scene_filename)
            if not os.path.isfile(scene_path):
                print("error - cannot find file {}".format(scene_path))
                sys.exit()
            f = open(scene_path)
            data = json.load(f)
            f.close()
            obj = get_physics_object(data)
            val = None
            if focus == "shows.position.x":
                val = obj["shows"][0]["position"]["x"]
            elif focus == "shows.position.y":
                val = obj["shows"][0]["position"]["y"]
            elif focus == "shows.position.z":
                val = obj["shows"][0]["position"]["z"]
            elif focus == "shows.rotation.x":
                val = obj["shows"][0]["rotation"]["x"]
            elif focus == "shows.rotation.y":
                val = obj["shows"][0]["rotation"]["y"]
            elif focus == "shows.rotation.z":
                val = obj["shows"][0]["rotation"]["z"]
            elif focus == "shows.scale.x":
                val = obj["shows"][0]["scale"]["x"]
            elif focus == "shows.scale.y":
                val = obj["shows"][0]["scale"]["y"]
            elif focus == "shows.scale.z":
                val = obj["shows"][0]["scale"]["z"]
            elif focus == "shows.stepBegin":
                val = obj["shows"][0]["stepBegin"]
            elif focus == "moves.stepEnd":
                val = obj["moves"][0]["stepEnd"]
            elif focus == "moves.vector.x":
                val = obj["moves"][0]["vector"]["x"]
            elif focus == "moves.vector.y":
                val = obj["moves"][0]["vector"]["y"]
            elif focus == "moves.vector.z":
                val = obj["moves"][0]["vector"]["z"]
            elif focus == "shrouds.stepEnd":
                if has_invisible_support(data):
                    val = "invisible_support"
            else:
                val = get_value_for_focus(obj, focus)
            if val != None:
                note_value(val, success)

            count += 1
            if success == "Correct":
                success_count += 1
            elif success == "Incorrect":
                fail_count += 1
            else:
                mystery_count += 1

        for v in sorted(vals_seen):
            correct_count = value_map[v]["Correct"]
            incorrect_count = value_map[v]["Incorrect"]
            total = correct_count + incorrect_count
            percent_correct = int((float(correct_count) / float(total)) * 100)
            percent_string = ""
            if percent_correct < limit:
                percent_string = get_percent_string(percent_correct, "bold")
            else:
                percent_string = get_percent_string(percent_correct, "faint")
            #'hi'.ljust(10)
            pc = "{} %".format(percent_correct).ljust(6)
            pretty_val = "{}".format(v).ljust(7)
            ratio = " {}/{}".format(correct_count, total).ljust(8)
            print(
                "{}- grav {} val {} {} {}".format(
                    pc, focus, pretty_val, ratio, percent_string
                )
            )
        print(
            "total lines processed {} succeed {}  fail {}  ??? {}".format(
                count, success_count, fail_count, mystery_count
            )
        )
