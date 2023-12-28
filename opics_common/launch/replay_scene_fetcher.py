import os
import sys
import traceback
import zipfile
from opics_common.launch.utils import get_installed_mcs_version


class ReplaySceneFetcher:
    def __init__(self, scene_type, scene_name):
        
        self.mcs_version = get_installed_mcs_version()
        self.scene_type = scene_type
        self.scene_name = scene_name

        self.ec2b_url = "ubuntu@3.20.113.119"
        self.remote_url = self.ec2b_url

    def set_project_name_and_paths(self, proj):
        self.scene_fname = f"{self.scene_name}.zip"
        if os.path.exists("/home/ubuntu/.optics_this_is_ec2b"):
            self.local_fetch_dest = f"/home/ubuntu/eval6_systest/{proj}/replay_data/{self.mcs_version}/{self.scene_type}"
        else:
            #self.local_fetch_dest = os.path.join(os.environ["REPLAY_HOME"],f"replay_scenes",)
            if "REPLAY_HOME" not in os.environ:
                print("REPLAY_HOME not defined.  Please 'export REPLAY_HOME=<parent_of_opics_dir>'")
                sys.exit()
            self.local_fetch_dest = os.environ["REPLAY_HOME"]
        os.makedirs(self.local_fetch_dest)
        # print(f"local_fetch_dest: {self.local_fetch_dest}")
        self.local_replay_dir = f"{self.local_fetch_dest}/{self.scene_name}"
        # print(f"local_replay_dir: {self.local_replay_dir}")
        self.local_zip_path = f"{self.local_fetch_dest}/{self.scene_fname}"
        # print(f"local_zip_path: {self.local_zip_path}")

        self.remote_path_unzipped = f"/home/ubuntu/eval6_systest/{proj}/replay_data/{self.mcs_version}/{self.scene_type}/{self.scene_name}"
        self.remote_path = f"/home/ubuntu/eval6_systest/{proj}/replay_data/{self.mcs_version}/{self.scene_type}/{self.scene_fname}"

    def get_public_key_path(self):
        if "PEM_PATH" not in os.environ:
            print("PEM_PATH not defined.  Please 'export PEM_PATH=<path_to_pem_file>'")
            sys.exit()
        pem_path = os.environ["PEM_PATH"]
        return pem_path
         
    def fetch_file(self, remote_src, local_dest):
        print(f"...fetching remote file from {remote_src}")
        public_key = self.get_public_key_path()
        print(f"PUBLIC KEY: {public_key}")

        #Zipping up the directory and copying it to the remote server from this file 

        # print(f"Zipping up directory: {self.scene_fname}")

        # os.system(f"ssh -i {public_key} zip -r {self.scene_fname} {self.remote_path_unzipped}")

        print(f"scp -i {public_key} {self.remote_url}:{remote_src} {local_dest}")
        os.system(f"scp -i {public_key} {self.remote_url}:{remote_src} {local_dest}")
        return True

    def unzip_file(self):
        print(f"Unzipping file: {self.local_zip_path}")

        with zipfile.ZipFile(self.local_zip_path, "r") as zip_ref:
            zip_ref.extractall(self.local_fetch_dest)
        
        # os.system(f"chmod a+x {self.local_zip_path}")
        # os.system(f"unzip -o {self.local_zip_path}")
        if os.path.exists(self.local_replay_dir):
            return True
        else:
            print(f"Failed to unzip file: {self.local_zip_path}")
            return False

    def attempt_unzip(self):
        try:
            self.unzip_file()
            return True

        except Exception:
            print(f"Failed to unzip: {self.local_zip_path}")
            traceback.format_exc()
            return False

    def is_replay_data_available_for_scene(self):
        # print(f"Checking for replay data at: {self.scene_name}")
        if os.path.exists(self.local_replay_dir):
            return True
        elif os.path.exists(self.local_zip_path):
            print(f"Found zip file: {self.local_zip_path}")
            return self.attempt_unzip()
        else:
            try:
                print("Attempting fetch replay data from remote server...")
                os.makedirs(self.scene_name, exist_ok=True)
                # print(f'PROJ: {self.proj}')
                self.fetch_file(f"{self.remote_path}", f"{self.local_fetch_dest}")
                return self.attempt_unzip()
            except Exception:
                print(
                    f"Failed to fetch replay data from remote server {self.remote_path}"
                )
                traceback.format_exc()
                sys.exit()
                return False


if __name__== '__main__':
    fetcher = ReplaySceneFetcher('coll', 'coll_val6_0001_01_zz_plaus_6v')
    fetcher.set_project_name_and_paths('pvoe')
    fetcher.is_replay_data_available_for_scene()
