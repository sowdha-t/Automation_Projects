import json
from json import JSONDecodeError

class JsonReader:
    @staticmethod
    def read_json(json_file_path):
        try:
            with open(json_file_path, "r",encoding="utf-8") as json_file:
                data = json.load(json_file)
                return data
        except FileNotFoundError as err:
            raise FileNotFoundError(f"File not found in the path:{json_file_path}") from err
        except JSONDecodeError as err:
            raise ValueError(f"Invalid Json format in file:{json_file_path}") from err



