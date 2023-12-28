line_flag                   = {}
line_flag["scene_start"]    = "SCENE_START"
line_flag["score"]          = "SCORE"
line_flag["result"]         = "RESULT"
line_flag["scene_classifier_answer"] = "SCENE_CLASSIFIER_ANSWER"

index_map = {
    line_flag["scene_start"]: {
        "time"                    : 0,
        "log_level"               : 1,
        "module"                  : 2,
        "scene_name"              : 4,
        "scene_type"              : 5,
    },
    line_flag["result"]: {
        "pvoe": {
            "time"                : 0,
            "log_level"           : 1,
            "result_value"        : 2,
            "module"              : 3,
            "scene_name"          : 4,
            "exception_detail"    : 5,
        },
        #    2023-03-06 16:27:43 ; RESULT ; error ; InterAgent:try_run_scene ; SCENE_NAME NOT SET ; LookDown-{} not in [('Pass', {})]
        "inter": {
            "time"                : 0,
            "log_level"           : 1,
            "result_value"        : 2,
            "module"              : 3,
            "scene_name"          : 4,
            "exception_detail"    : 5,
            "step_count"          : 6,
        },
        "avoe": {
            "time"                : 0,
            "log_level"           : 1,
            "module"              : 2,
            "scene_name"          : 4,
            "result_value"        : 5,
            "exception_detail"    : 6,
        },
    },
    line_flag["scene_classifier_answer"]: { ## 2023-03-04 15:14:24 ; CLASSIFIER ; seeing_leads_to_knowing ; InterAgent:try_run_scene ; SCENE_NAME NOT SET ;
        "inter": {
            "time"                : 0,
            "log_level"           : 1,
            "answer_value"        : 2,
            "module"              : 3,
            "scene_name"          : 4,
        },
    },
}
# index_map = {}
# index_map[line_flag["scene_start"]] = {}
# index_map[line_flag["scene_start"]]["time"] = 0
# index_map[line_flag["scene_start"]]["log_level"] = 1
# index_map[line_flag["scene_start"]]["module"] = 2
# index_map[line_flag["scene_start"]]["scene_name"] = 4
# index_map[line_flag["scene_start"]]["scene_type"] = 5

# index_map[line_flag["result"]] = {}
# index_map[line_flag["result"]]["time"] = 0
# index_map[line_flag["result"]]["log_level"] = 1
# index_map[line_flag["result"]]["module"] = 2
# index_map[line_flag["result"]]["scene_name"] = 4
# index_map[line_flag["result"]]["result_value"] = 5
# index_map[line_flag["result"]]["inter_step_count"] = 6
# index_map[line_flag["result"]]["inter_exception_detail"] = 7
# index_map[line_flag["result"]]["pvoe_exception_detail"] = 6


pvoe_plausible_string   = "plausible"
pvoe_implausible_string = "implausible"
pvoe_rating_string      = "rating"
pvoe_score_string       = "score"
pvoe_error_string       = "error"
inter_succeeded_string  = "succeeded"
inter_failed_string     = "failed"
inter_error_string      = "error"
avoe_expected_string    = "expected"
avoe_unexpected_string  = "unexpected"
avoe_noexpectation_string  = "noexpectation"
avoe_rating_string      = "rating"
avoe_score_string       = "score"
avoe_error_string       = "error"
exception_string        = "Exception"
error_string            = "error"

delim                   = " ; "
