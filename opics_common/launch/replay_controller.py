import os
import pickle
import sys

import numpy as np
from PIL import Image

from opics_common.launch.utils import get_installed_mcs_version
#REPLAY_HOME instead OPICS_HOME as an env variable

class ReplayController:
    def __init__(self, project, scene_type):
        self.step_num = 1
        self.project = project
        self.scene_type = scene_type
        self.mcs_version = get_installed_mcs_version()
        # FOR EC2B
        if os.path.exists("/home/ubuntu/.optics_this_is_ec2b"):
            self.replay_root_dir = f"/home/ubuntu/eval6_systest/{self.project}/replay_data/{self.mcs_version}/{self.scene_type}"
        else:
            if "REPLAY_HOME" not in os.environ:
                print("ERROR - REPLAY_HOME not defined. please export REPLAY_HOME=<parent_dir_of_replay_scenes>")
                sys.exit()

            if os.path.exists(os.environ["REPLAY_HOME"]) == False:
                print(f"ERROR - REPLAY_HOME directory does not exist: {os.environ['REPLAY_HOME']}")
                os.makedirs(os.environ["REPLAY_HOME"], exist_ok=True)
                
                
            self.replay_root_dir = os.path.join(os.environ["REPLAY_HOME"])
            
            
        print("replay_root_dir", self.replay_root_dir)

        
            
    def set_scene_name(self, scene_path):
        self.scene_name = os.path.basename(scene_path)
        self.scene_name = self.scene_name.replace(".json", "")
        self.replay_scene_dir = os.path.join(
            self.replay_root_dir, self.scene_name
        )
        self.step_output_dir = os.path.join(
            self.replay_scene_dir, "Step_Output"
        )

    def end_scene(self, rating, score, report):
        pass

    def start_scene(self, scene_json):
        step_output = self.load_step_output_for_frame(self.step_num)
        step_output.image_list = []

        step_output.object_mask_list = []
        step_output.image_list.append(
            self.load_image_data(self.step_num, "RGB")
        )
        step_output.object_mask_list.append(
            self.load_image_data(self.step_num, "Mask")
        )
        self.step_num += 1
        return step_output

    def step(self, action):
        step_output = self.load_step_output_for_frame(self.step_num)
        step_output.image_list = []
        step_output.object_mask_list = []
        step_output.image_list.append(
            self.load_image_data(self.step_num, "RGB")
        )
        step_output.object_mask_list.append(
            self.load_image_data(self.step_num, "Mask")
        )
        self.step_num += 1
        return step_output

    def load_step_output_for_frame(self, frame_num):
        frame_number_string = str(frame_num).zfill(6)
        step_output_file = os.path.join(
            self.step_output_dir, f"{frame_number_string}.pickle"
        )
        with open(step_output_file, "rb") as f:
            step_output = pickle.load(f)
        return step_output

    def load_image_data(self, frame_num, dirname):
        frame_number_string = str(frame_num).zfill(6)
        image_file = os.path.join(
            self.replay_scene_dir, f"{dirname}/{frame_number_string}.png"
        )
        with Image.open(image_file) as f:
            image_array = np.asarray(f)
            image = Image.fromarray(image_array)
        return image

    def load_depth_map_data(self, frame_num, dirname):
        frame_number_string = str(frame_num).zfill(6)
        depth_map_file = os.path.join(
            self.replay_scene_dir, f"{dirname}/{frame_number_string}.pickle"
        )
        # pdb.set_trace()
        with open(depth_map_file, "rb") as f:
            depth_map = pickle.load(f)
            # depth_map_list = Image.fromarray(depth_map_array)

        return depth_map
