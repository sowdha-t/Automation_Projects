import configparser
from pathlib import Path
config_file_path = Path(__file__).resolve().parent.parent / "config" / "config.ini"
class ConfigReader:
    def __init__(self,file_path=config_file_path):
        self.config = configparser.ConfigParser()
        self.config.read(file_path)
        if not self.config.read(file_path):
            raise FileNotFoundError(f"Config file is not found in the path:{file_path}")


    def get(self,section,key):
        return self.config.get(section,key)

    def get_int(self,section,key):
        return self.config.getint(section,key)

    def get_bool(self,section,key):
        return self.config.getboolean(section,key)