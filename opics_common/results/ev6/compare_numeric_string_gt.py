from opics_common.results.ev5.header_val_indices_ev5 import val_index


if __name__ == "__main__":
    f = open('/home/jedirv/Downloads/eval6_results_avoe.csv', 'r')
    lines = f.readlines()
    f.close()
    for answer_key_line in lines:
        if answer_key_line.startswith("Total"):
            continue
        if answer_key_line.startswith("CATEGORY"):
            continue
        parts = answer_key_line.split(",")
        scene_id = parts[val_index["TEST NAME"]]

        expectedness = parts[val_index["GOAL ANSWER CHOICE"]]
        ngt = parts[val_index["EVALUATION SCORE NUMERICAL GROUND TRUTH"]]

        if expectedness == 'expected' and ngt == '0':
            print(f'{scene_id} is expected but ngt is 0')
            continue
        if expectedness == 'unexpected' and ngt == '1':
            print(f'{scene_id} is unexpected but ngt is 1')
            continue