import pytest
from pages.login_page import LoginPage
from utils.excel_utils import ExcelUtils

#Parse Excel matrix rows before run time starts
test_records = ExcelUtils.get_sheet_data("data/login_data.xlsx","Sheet1")
case_ids = [row["test_case"] for row in test_records]

@pytest.mark.parametrize("data",test_records,ids=case_ids)
def test_eventhub_login_matrix(driver,data):
    #Initialize the specific page object with the driver state
    login_page = LoginPage(driver)

    #Execute the step sequence
    login_page.login_to_eventhub(data["email"],data["password"])

    #Assert conditions based on test objective matrix
    if "invalid" in data["test_case"]:
        assert "Invalid Credentials" in login_page.get_error_message()
    else:
        assert "dashboard" in driver.current_url.lower()



