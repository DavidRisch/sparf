import os

class EnvironmentSettings:
    def __init__(self, data_root='', debug=False):
        self.workspace_dir = '/mnt/workfiles/sparf_output/workspace'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/mnt/workfiles/sparf_output/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = self.workspace_dir    # Directory for saving other models pre-trained networks
        self.eval_dir = '/mnt/workfiles/sparf_output/eval'    # Base directory for saving the evaluations.
        self.log_dir = '/mnt/workfiles/sparf_output/log'

        self.llff = ''
        self.dtu = '/mnt/workfiles/sparf_data/dtu_dataset/rs_dtu_4/DTU'
        self.dtu_depth = ''
        self.dtu_mask = ''
        self.replica = ''
