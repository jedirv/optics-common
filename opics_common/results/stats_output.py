from opics_common.scene_type.type_constants import cubes_for_type

log_file_flag           = "log_file:"
flag_stats_all_scenes   = "all:"
flag_for_class          = {}
flag_for_class["avoe"]  = "avoe:"
flag_for_class["pvoe"]  = "pvoe:"
flag_for_class["inter"] = "inter:"

# flag_for_type                                 = {}
# flag_for_type['collision']                    = 'coll:'
# flag_for_type['gravity']                      = 'grav:'
# flag_for_type['object_permanence']            = 'op:'
# flag_for_type['shape_constancy']              = 'sc:'
# flag_for_type['spatio_temporal_continuity']   = 'stc:'


def stats_title(log_name):
    print("")
    print("")
    print(f"{log_file_flag} {log_name}")


def get_graph_line(percent_correct):
    hit_int = int(percent_correct * 100)
    scale = 0.5
    hit_scaled = int(float(hit_int) * scale)
    g = ""
    for i in range(1, hit_scaled + 1):
        g += "#"
    for i in range(hit_scaled, 51):
        g += "."
    return g


def get_graph_line_articulate(
    portion_correct, portion_exceptions, portion_missing
):
    hit_int = int(portion_correct * 100)
    missing_int = int(portion_missing * 100)
    exception_int = int(portion_exceptions * 100)
    scale = 0.5
    upper_lim = int(scale * 100) + 1
    hit_scaled = int(scale * float(hit_int))
    missing_scaled = int(scale * float(missing_int))
    exception_scaled = int(scale * float(exception_int))
    hit_and_exception_scaled = hit_scaled + exception_scaled
    hit_and_exception_and_missing_scaled = (
        hit_and_exception_scaled + missing_scaled
    )

    g = ""
    for i in range(1, hit_scaled + 1):
        g += "#"
    for i in range(hit_scaled + 1, hit_and_exception_scaled + 1):
        g += "!"
    for i in range(
        hit_and_exception_scaled + 1, hit_and_exception_and_missing_scaled + 1
    ):
        g += "!"
    for i in range(hit_and_exception_and_missing_scaled + 1, upper_lim):
        g += "."
    return g


def get_graph_line_with_missing(percent_correct, percent_missing):
    hit_int = int(percent_correct * 100)
    missing_int = int(percent_missing * 100)
    scale = 0.5
    upper_lim = int(scale * 100) + 1
    hit_scaled = int(float(hit_int) * scale)
    missing_scaled = int(float(missing_int) * scale)
    hit_or_missing_scaled = hit_scaled + missing_scaled

    g = ""
    for i in range(1, hit_scaled + 1):
        g += "#"
    for i in range(hit_scaled + 1, hit_or_missing_scaled + 1):
        g += "?"
    for i in range(hit_or_missing_scaled + 1, upper_lim):
        g += "."
    return g


def stat_line(flag, success_count, scene_count, percent_correct, caveat):
    if percent_correct == "no scenes":
        print("")
    else:
        graph = get_graph_line(percent_correct)
        ratio_string = f"{success_count}/{scene_count}"
        # percent_string = '{:.2f}'.format(percent_correct)
        percent_string = "{}% ".format(int(percent_correct * 100))
        print(
            "{}{}{}{}{}".format(
                flag.ljust(10),
                ratio_string.ljust(8),
                caveat.ljust(5),
                percent_string.ljust(5),
                graph,
            )
        )


def get_pathology_addendum(exception_count, missing_count, broken_scene_count):
    exception_string = ""
    if exception_count > 0:
        exception_string = f"!except {exception_count} ".ljust(14)
    missing_string = ""
    if missing_count > 0:
        missing_string = f"?missing {missing_count} ".ljust(15)
    broken_string = ""
    if broken_scene_count > 0:
        broken_string = f"({broken_scene_count} broken logs ignored)"
    addendum = f"{exception_string}{missing_string}{broken_string}"
    return addendum


def stat_line_articulate(
    flag,
    cube_id,
    success_count,
    scene_count,
    missing_count,
    exception_count,
    broken_scene_count,
):
    if scene_count == 0:
        print("")
    else:
        portion_correct = float(success_count) / float(scene_count)
        portion_exceptions = float(exception_count) / float(scene_count)
        portion_missing = float(missing_count) / float(scene_count)
        graph = get_graph_line_articulate(
            portion_correct, portion_exceptions, portion_missing
        )
        ratio_string = f"{success_count}/{scene_count}"
        if cube_id == "":
            flag = flag.ljust(len(flag) + 4)
        else:
            cube_id_ljust = f"{cube_id}".ljust(4)
            flag = f"{flag} {cube_id_ljust}".ljust(len(flag) + len(cube_id_ljust) + 4)

        ratio_string = ratio_string.ljust(10)
        percent_correct_string = "{}% ".format(
            int(portion_correct * 100)
        ).ljust(5)
        pathology_addendum = get_pathology_addendum(
            exception_count, missing_count, broken_scene_count
        )
        print(
            f"{flag}{ratio_string}{percent_correct_string}{graph}  {pathology_addendum}"
        )


def stat_line_with_specified_name_length(
    flag, success_count, scene_count, percent_correct, caveat, name_length
):
    if percent_correct == "no scenes":
        print("")
    else:
        graph = get_graph_line(percent_correct)
        ratio_string = f"{success_count}/{scene_count}"
        percent_string = "{}% ".format(int(percent_correct * 100))
        print(
            "{}{}{}{}{}".format(
                flag.ljust(name_length),
                ratio_string.ljust(8),
                caveat.ljust(5),
                percent_string.rjust(6),
                graph,
            )
        )


def stat_line_with_missing_info(
    flag,
    success_count,
    scene_count,
    percent_correct,
    percent_missing,
    name_length,
    counts_summary,
):
    if percent_correct == "no scenes":
        print("")
    else:
        graph = get_graph_line_with_missing(percent_correct, percent_missing)
        ratio_string = f"{success_count}/{scene_count}"
        percent_string = "{}% ".format(int(percent_correct * 100))
        print(
            "{}{}{}{}{}".format(
                flag.ljust(name_length),
                ratio_string.ljust(8),
                percent_string.rjust(5),
                graph,
                counts_summary,
            )
        )


def no_stats_line(flag):
    print(f"{flag}")


def warning(s):
    print()
    print(f"      WARNING : {s}")
    print()


def get_caveat(missing_results_count):
    caveat = "  "
    if missing_results_count > 0:
        caveat = f"{missing_results_count}?"
    return caveat


def express_results_summary(
    success_count,
    scene_count,
    missing_results_count,
    exception_count,
    broken_scene_count,
):
    stat_line_articulate(
        flag_stats_all_scenes,
        "",
        success_count,
        scene_count,
        missing_results_count,
        exception_count,
        broken_scene_count,
    )


def express_category_results_summary(
    success_count, scene_count, category, missing_results_count
):
    if scene_count == 0:
        no_stats_line(category)
    else:
        caveat = get_caveat(missing_results_count)
        percent_correct = float(success_count) / float(scene_count)
        stat_line(
            category, success_count, scene_count, percent_correct, caveat
        )


def get_counts_summary(counts):
    missing_count = counts["missing_results_count"]
    correct_count = counts["success_count"]
    scene_count = counts["scene_count"]
    incorrect_count = scene_count - correct_count - missing_count
    missing_string = ""
    if missing_count > 0:
        missing_string = f"missing: {missing_count}"
    correct_string = f"{correct_count}".rjust(4)
    incorrect_string = f"{incorrect_count}".rjust(4)
    return f"   y:{correct_string}  n:{incorrect_string}   {missing_string}"


def print_results_for_outcome_counts(scene_type, name_length, counts):
    
    missing_count = counts["missing_results_count"]
    exception_count = counts["exception_count"]
    success_count = counts["success_count"]
    scene_count = counts["scene_count"]
    scene_type = scene_type.ljust(name_length + 1)
    stat_line_articulate(
        scene_type,
        "",
        success_count,
        scene_count,
        missing_count,
        exception_count,
        0,
    )


def print_results_for_scene_classifier(
    scene_type, name_length, counts
):
    scene_count = counts["scene_count"]
    success_count = counts["success_scene_classifier_count"]
    scene_type = scene_type.ljust(name_length + 1)
    stat_line_articulate(
        scene_type,
        "",
        success_count,
        scene_count,
        0,
        0,
        0,
    )

def print_results_for_outcome_counts_with_cube_ids(
    scene_type, cube_id, name_length, counts
):
    missing_count = counts["missing_results_count"]
    exception_count = counts["exception_count"]
    success_count = counts["success_count"]
    scene_count = counts["scene_count"]
    scene_type = scene_type.ljust(name_length + 1)
    stat_line_articulate(
        scene_type,
        cube_id,
        success_count,
        scene_count,
        missing_count,
        exception_count,
        0,
    )

def express_scene_classifier_results(counts, abbrev_types):
    normalized_name_length = get_max_name_length_plus_buffer(abbrev_types)
    for scene_type in abbrev_types:
        type_counts = counts[scene_type]
        scene_count = type_counts["scene_count"]
        if scene_count == 0:
            no_stats_line(scene_type)
        else:
            print_results_for_scene_classifier(scene_type, normalized_name_length, type_counts)
    print("\n\n---incorrect scene classifier scenes---")
    for scene_type in abbrev_types:
        type_counts = counts[scene_type]
        if len(type_counts["incorrect_classifier_scenes"]) != 0:
            for scene_name in type_counts["incorrect_classifier_scenes"]:
                print(scene_name)


def express_results_by_scene_type(counts, abbrev_types):
    normalized_name_length = get_max_name_length_plus_buffer(abbrev_types)
    for scene_type in abbrev_types:
        #print(f'scene_type_being_processed {scene_type}')
        type_counts = counts[scene_type]
        scene_count = type_counts["scene_count"]
        #print(f'scene_count : {scene_count}')
        if scene_count == 0:
            no_stats_line(scene_type)
        else:
            print_results_for_outcome_counts(
                scene_type, normalized_name_length, type_counts
            )


def express_results_by_cube_ids(counts, proj, abbrev_types):
    normalized_name_length = get_max_name_length_plus_buffer(abbrev_types)
    for scene_type in abbrev_types:
        for cube_id in cubes_for_type[proj][scene_type]:
            cube_counts = counts[scene_type + "_" + cube_id]
            scene_count = cube_counts["scene_count"]
            if scene_count == 0:
                # don't emit an empty line for cubeids not in this run
                #no_stats_line(scene_type)
                pass
            else:
                print_results_for_outcome_counts_with_cube_ids(
                    scene_type, cube_id, normalized_name_length, cube_counts
                )


def get_max_name_length_plus_buffer(l):
    max = 0
    for name in l:
        if len(name) > max:
            max = len(name)
    return max + 1


def dotted_line():
    print(
        "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
    )


def header(s):
    print("")
    dotted_line()
    print(f"\t{s}")
    dotted_line()


def warn_missing_result(scene_name):
    print(
        f"       WARNING - scene {scene_name} result missing - omitted from stats"
    )
