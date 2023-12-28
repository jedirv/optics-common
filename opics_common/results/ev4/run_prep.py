import argparse
import os
import sys

issues = []


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", default="junk2")
    parser.add_argument("--action", default="junk2")
    return parser


def prep_spec(spec, lines):
    # filename will have level, system (ex pvoe), tag that will be used to create dir :  pvoe_L1_xyz
    spec_parts = spec.split("_")
    if len(spec_parts) != 3:
        print("specname must be of the form  pvoe_L1_<tag> {}".format(spec))
        sys.exit()
    system = spec_parts[0]
    if not (system == "pvoe" or system == "avoe" or system == "interactive"):
        print(
            "system must be either pvoe, avoe, or interactive:  {}".format(
                system
            )
        )
        sys.exit()
    level = spec_parts[1]
    if not (level == "L1" or level == "L2" or level == "Oracle"):
        print("level must be either L1, L2 or Oracle")
        sys.exit()
    os.chdir("..")
    if not os.path.exists(spec):
        os.system("mkdir  {}".format(spec))
    os.chdir(spec)
    for line in lines:
        if not line.startswith("#"):
            fetch_scene_file(line, spec)


def fetch_scene_file(line, spec):
    # target_file looks like oscar_0001_01_SS1
    # line will look like grav_L2_SS1_plaus_incorrect_oscar_0006_01
    print("line: {}".format(line))
    parts = line.split("_")
    code_name = parts[5]
    test_num = parts[6]
    test_scene_num = parts[7]
    cube_id = parts[2]
    scene_fname = (
        code_name
        + "_"
        + test_num
        + "_"
        + test_scene_num
        + "_"
        + cube_id
        + "_debug.json"
    )
    target_url = (
        "https://resources.machinecommonsense.com/eval-scenes-4/" + scene_fname
    )
    print("fetching target url {}".format(target_url))
    # we are positioned in the dir named for the spec
    os.system("wget " + target_url)
    dest_path = "{}.json".format(line)
    os.system("mv {} {}".format(scene_fname, dest_path))
    if not os.path.isfile(dest_path):
        issues.append(
            "ERROR - file {} did not arrive after mv".format(dest_path)
        )


def package_spec(spec, lines, spec_fname):
    os.chdir("..")
    basedir = os.getcwd()
    print("*basedir is now " + basedir)
    package_dir = "package_" + spec
    dest_root_dir = os.path.join(basedir, package_dir)
    print("....creating package_dir {}".format(package_dir))
    if not os.path.exists(dest_root_dir):
        os.mkdir(dest_root_dir)
    os.system("cp analysis/{} {}".format(spec_fname, dest_root_dir))
    tracking_dir = os.path.join(basedir, "tracking_logs")
    # /tracking_logs/grav_L1_DD1_plaus_correct_oscar_0001_19/tracker_imgs
    mp4_log_file = "error_log.txt"
    for line in lines:
        mp4_dest_dir = os.path.join(dest_root_dir, line)
        print("....creating mp4_dest_dir {}".format(mp4_dest_dir))
        if not os.path.exists(mp4_dest_dir):
            os.system("mkdir " + mp4_dest_dir)
        line_dir = os.path.join(tracking_dir, line)
        tracker_imgs_dir = os.path.join(line_dir, "tracker_imgs")
        gen_video(
            line, tracker_imgs_dir, mp4_dest_dir, mp4_log_file, "tracker"
        )

    logs_dir = os.path.join(basedir, "logs")
    for line in lines:
        mp4_dest_dir = os.path.join(dest_root_dir, line)
        pybullet_imgs_dir = os.path.join(logs_dir, line)
        print(
            "about to create pybullet video in logs dir {}".format(
                pybullet_imgs_dir
            )
        )
        gen_video(
            line, pybullet_imgs_dir, mp4_dest_dir, mp4_log_file, "pybullet"
        )

    os.chdir(basedir)
    scene_dir = os.path.join(basedir, spec)
    for line in lines:
        scene_file = os.path.join(scene_dir, line + ".json")
        mp4_dest_dir = os.path.join(dest_root_dir, line)
        print(
            "...copying scene file {} to {}".format(scene_file, mp4_dest_dir)
        )
        os.system("cp {} {}".format(scene_file, mp4_dest_dir))

    print("ZIPPING mp4 files")
    os.chdir(basedir)
    os.system("zip -r {}.zip {}".format(package_dir, package_dir))


def gen_video(line, imgs_dir, mp4_dest_dir, mp4_log_file, video_type):
    print("creating video in {}".format(imgs_dir))
    os.chdir(imgs_dir)
    mp4_fname = "{}_12fps_{}.mp4".format(line, video_type)
    print("creating video  {}".format(mp4_fname))
    os.system(
        "ffmpeg -framerate 12 -i %d.png -pix_fmt yuv420p {}".format(mp4_fname)
    )
    if not os.path.isfile(mp4_fname):
        issues.append("WARNING mp4 {} not valid.".format(mp4_fname))
        os.system(
            'echo "mp4 {} was not generated" >> {}'.format(
                mp4_fname, mp4_log_file
            )
        )
    else:
        os.system("mv {} {}".format(mp4_fname, mp4_dest_dir))


def remove_comments(lines):
    result = []
    for line in lines:
        if not line.startswith("#"):
            result.append(line.rstrip())
    return result


if __name__ == "__main__":
    args = make_parser().parse_args()
    spec_fname = args.spec
    action = args.action
    if not (action == "prep" or action == "package"):
        print("action {} not valid.".format(action))
        print(
            "usage:  python run_prep.py --spec <spec_fname> --action <prep|package>"
        )
        sys.exit()
    if not os.path.isfile(spec_fname):
        print("spec_path {} not valid.".format(spec_fname))
        print(
            "usage:  python run_prep.py --spec <spec_fname> --action <prep|package>"
        )
        sys.exit()

    print("spec_path {}".format(spec_fname))

    spec = spec_fname.split(".")[0]

    if action == "prep":
        f = open(spec_fname)
        lines = f.readlines()
        f.close()
        lines_no_comments = remove_comments(lines)
        prep_spec(spec, lines_no_comments)

    elif action == "package":
        f = open(spec_fname)
        lines = f.readlines()
        f.close()
        lines_no_comments = remove_comments(lines)
        package_spec(spec, lines_no_comments, spec_fname)
    else:
        pass

    if len(issues) != 0:
        print("ISSUES...")
        for issue in issues:
            print(issue)
