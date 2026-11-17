import csv

class CSVReader:
    @staticmethod
    def read_csv_data(file_path):
        try:
            with open(file_path,"r",encoding="utf-8-sig") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                if not csv_reader.fieldnames:
                    raise ValueError(f"Invalid CSV format or file is empty:{file_path}")

                data = list(csv_reader)

                if not data:
                    raise ValueError(f"csv file contains headers but no data:{file_path}")

                return data
        except FileNotFoundError as err:
            raise FileNotFoundError(f"File not found in the path: {file_path}") from err


