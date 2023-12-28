

if __name__ == '__main__':
    answer_path = '/home/jedirv/Downloads/eval6_results.csv'
    f = open(answer_path, 'r')
    lines = f.readlines()
    f.close()
    header = lines[0]
    colnames = header.rstrip().split(',')
    for colname in colnames:
        print(colname)