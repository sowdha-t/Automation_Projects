import configparser
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "config.ini"

class ConfigReader:

    def __init__(self, path=CONFIG_PATH):
        self.config_obj = configparser.ConfigParser()
        if not self.config_obj.read(path):
            raise FileNotFoundError(f"Config file is not found in the path:{path}")

    def get(self,section,key):
        return self.config_obj.get(section,key)

    def get_int(self,section,key):
        return self.config_obj.getint(section,key)