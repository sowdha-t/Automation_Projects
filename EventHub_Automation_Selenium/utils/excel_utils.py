import openpyxl

class ExcelUtils:
    @staticmethod
    def get_sheet_data(file_path,sheet_name):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]

        headers = [cell.value for cell in sheet[1]]
        data_rows = []

        for row in sheet.iter_rows(min_row=2,values_only=True):
            if not any(row):
                continue
            data_rows.append(dict(zip(headers,row)))

        workbook.close()
        return data_rows
