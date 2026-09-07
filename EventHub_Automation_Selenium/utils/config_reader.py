import json
import os

class ConfigReader:

    @staticmethod
    def get_config():
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(project_root, "config", "settings.json")

        with open(config_path, "r") as file:
            return json.load(file)
