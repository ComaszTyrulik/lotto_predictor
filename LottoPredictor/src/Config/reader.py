import json


class ConfigReader:
    config: dict
    __config_path = 'C:\\Users\\Tomek\\Documents\\Python\\LottoPredictor\\src\\Config\\config.json'

    def __init__(self):
        config_file = open(self.__config_path, 'r')
        self.config = json.load(config_file)

    def get_lottery_results_filename(self):
        return self.config['results_filename']
