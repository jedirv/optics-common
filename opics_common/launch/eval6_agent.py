import os
import random
import sys
import traceback

import machine_common_sense as mcs

from opics_common.launch.constants import MCS_CONTROLLER, OPICS_SCENE_TYPE_HANDLING, SCENE_TYPE_IS_PROVIDED, SCENE_TYPE_IS_DEDUCED
from opics_common.launch.replay_controller import ReplayController
from opics_common.launch.replay_scene_fetcher import ReplaySceneFetcher
from opics_common.opics_logging.scene_logger import create_scene_logger
from opics_common.scene_type.inter_scene_type_to_solver_map import inter_scene_type_to_solver_map


class Evaluation6_Agent:
    def __init__(
        self,
        config_ini_path,
        level,
        controller_type,
        json_scene_category,
        run_state,
        additional_logs,
        seed=-1,
    ):
        self.run_state = run_state
        self.level = level
        self.controller_type = controller_type
        self.config_ini_path = config_ini_path
        self.additional_logs = additional_logs
        self.json_scene_category = json_scene_category

        if seed != -1:
            random.seed(seed)

    def init_mcs_controller(self):
        try:
            print("------ creating mcs controller ------")
            self.controller = mcs.create_controller(
                config_file_or_dict=self.config_ini_path
            )
            self.run_state.controller_up()
        except Exception as err:
            traceback.print_exc()
            self.run_state.convert_exception_to_run_state(
                err, "during instantiation of live controller"
            )

    def init_replay_controller(self, proj, abbrev_scene_type):
        print(
            f"------- creating replay controller for {proj} {abbrev_scene_type}-------"
        )
        self.controller = ReplayController(proj, abbrev_scene_type)
        self.run_state.controller_up()

    def get_proj_for_json_scene_category(self, json_scene_category):
        if json_scene_category == "intuitive physics":
            return 'pvoe'
        elif json_scene_category == 'agents':
            return 'avoe'
        elif json_scene_category in ['retrieval', 'imitation','multi retrieval', 'passive']:
            return 'inter'
        else:
            raise Exception(f'unkown json_scene_category: {json_scene_category}')


    def init_controller(self,abbrev_scene_type, scene_name, proj):
        if self.controller_type == MCS_CONTROLLER:
            self.init_mcs_controller()
        else:
            # attempting to run a replay scene
            print('...instantiating ReplaySceneFetcher...')
            replay_fetcher = ReplaySceneFetcher(abbrev_scene_type, scene_name)
            replay_fetcher.set_project_name_and_paths(proj)
            if replay_fetcher.is_replay_data_available_for_scene():
                print(
                    f"...replay data available for scene - initializing replay controller"
                )
                self.init_replay_controller(proj, abbrev_scene_type)
            else:
                print(
                    f"...replay data NOT available for scene - initializing mcs controller"
                )
                self.init_mcs_controller()
        if self.controller is None:
            if self.run_state.is_optics_run():
                self.run_state.controller_timed_out()
                return
            else:
                # not a systest run, just exit
                print("Could not instantiate controller! - exiting")
                sys.exit()


    def get_scene_type_solver_for_inter(self, scene_name):
        solver_name = None
        if OPICS_SCENE_TYPE_HANDLING in os.environ:
            scene_type_handling_setting = os.environ[OPICS_SCENE_TYPE_HANDLING]
            if not scene_type_handling_setting in [SCENE_TYPE_IS_PROVIDED, SCENE_TYPE_IS_DEDUCED]:
                print(f'\n\nERROR - {OPICS_SCENE_TYPE_HANDLING} must be set to one of these: {SCENE_TYPE_IS_PROVIDED}, {SCENE_TYPE_IS_DEDUCED} \n\n')
                print(f'{OPICS_SCENE_TYPE_HANDLING} currently set to {scene_type_handling_setting} \n\n')
                sys.exit()

            print(f'\n\n\n OPICS_SCENE_TYPE_HANDLING setting detected as: {scene_type_handling_setting}')
            if SCENE_TYPE_IS_PROVIDED == scene_type_handling_setting:
                scene_type_abbrev = scene_name.split('_')[0]
                solver_name = inter_scene_type_to_solver_map[scene_type_abbrev]
                print(f'....SOLVER NAME MAPPED FROM SCENE TYPE WAS {solver_name}')
            else:
                print(f'....SOLVER_NAME passed is None')
        print('\n\n')
        return solver_name

    def run_scene(self, scene_path, scene_json, log_dir):
        proj = self.get_proj_for_json_scene_category(self.json_scene_category)

        # can't put the imports inside a function as they will go out of scope
        print(f'importing {proj} dependencies...')
        try:
            if proj == "pvoe":
                # NOTE(Mazen): preventing the issue of TF not being able to load
                # which causes a crash
                import tensorflow as tf  # isort:skip
                import torch  # isort:skip
                print("TensorFlow version:", tf.__version__)
                print("PyTorch version:", torch.__version__)
                import opics_pvoe.pvoe.pvoe_agent as physics_voe_agent
            elif proj == "avoe":
                from opics.avoe.agency_voe_agent import AgencyVoeAgent
            else: # proj == 'inter'
                print('trying to import InterAgent')
                from opics_inter.inter.inter_agent import InterAgent

                print('apparently succeeded importing InterAgent')
            
        except ImportError as err:
            self.run_state.bad_environment()
            traceback.print_exc()
            print(f"Did you remember to activate the conda environment? {err}")
            sys.exit()

        self.run_state.starting_controller()
        scene_name = os.path.basename(scene_path).split(".")[0]
        abbrev_scene_type = scene_name.split("_")[0]
        self.init_controller(abbrev_scene_type, scene_name, proj)

        # for some reason, can't put consumption of imported classes inside a function as they will go out of scope !?
        agent = None
        try:
            if proj == "pvoe":
                agent = physics_voe_agent.PhysicsVoeAgent(self.controller, self.level, scene_name, enable_logger=self.additional_logs)
            elif proj == "avoe":
                agent = AgencyVoeAgent(self.controller, self.level)
            else: # proj == 'inter'
                agent = InterAgent(self.controller, self.level, scene_name, enable_logger=self.additional_logs)
        except Exception as err:
            self.run_state.initialization_error()
            traceback.print_exc()
            print(f"Error during initialization: {err}")
            sys.exit()
        #return agent

        self.scene_logger = create_scene_logger(scene_path, log_dir)
        if isinstance(self.controller, ReplayController):
            self.controller.set_scene_name(scene_path)

        if proj == 'inter':
            solver_name = self.get_scene_type_solver_for_inter(scene_name)
            agent.try_run_scene(scene_json, scene_path, self.run_state, scene_name, scene_type=solver_name)
        else:
            agent.try_run_scene(scene_json, scene_path, self.run_state)
