
import os
if __name__ == '__main__':
    src_dir = '/home/jedirv/mcs/eval_7_validation_renamed/inter'
    files = os.listdir(src_dir)
    for file in files:
        stype = file.split('_')[0]
        dst_dir = os.path.join(src_dir,stype)
        os.makedirs(dst_dir,exist_ok=True)
        cmd = f'mv {os.path.join(src_dir,file)} {os.path.join(dst_dir,file)}'
        print(cmd)
        os.system(cmd)
    