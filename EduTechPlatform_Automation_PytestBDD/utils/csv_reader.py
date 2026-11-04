import csv
from pathlib import Path

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"
print(DATA_FOLDER)

def read_csv(file_name):
    file_path = DATA_FOLDER / file_name
    with open(file_path,newline="",encoding="utf-8")  as file:
        return list(csv.DictReader(file))

def get_row(file_name,case_id):

    for row in read_csv(file_name):
        if row["case_id"] == case_id:
            return row
    raise ValueError(f"Case id {case_id} was not found in {file_name}")