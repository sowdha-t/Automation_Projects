import configparser
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "config.ini"

class ConfigReader:

    def __init__(self, path=CONFIG_PATH):
        self.parser = configparser.ConfigParser()
        if not self.parser.read(path):
            raise FileNotFoundError(f"Config file is not found in the path:{path}")

    def get(self,section,key):
        return self.parser.get(section,key)

    def get_int(self,section,key):
        return self.parser.getint(section,key)