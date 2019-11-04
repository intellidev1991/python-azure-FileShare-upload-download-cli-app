
import json


class Configuration:
    def __init__(self):
        config = self.read_config('config.json')
        self.account_name = config["configs"]["account_name"]
        self.account_key = config["configs"]["account_key"]
        self.file_share = config["configs"]["file_share"]

    def read_config(self, config_file):
        """ Read config.json and pass it as dictionary """
        data = {}
        with open(config_file, encoding='utf-8') as f:
            data = json.load(f)
        return data
