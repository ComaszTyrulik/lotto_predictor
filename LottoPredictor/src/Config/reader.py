import json

import os;
from os import path

class ConfigReader:
    config: dict
    __config_path = path.join(path.dirname(__file__), 'config.json')


    def __init__(self):
        config_file = open(self.__config_path, 'r')
        self.config = json.load(config_file)

    def get_lottery_results_filename(self):
        return self.config['results_filename_' + os.name]
