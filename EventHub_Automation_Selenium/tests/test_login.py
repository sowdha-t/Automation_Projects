import pytest
from pages.login_page import LoginPage
from utils.json_reader import JsonReader

test_records = JsonReader.read_json("data/local/login_data.json")

case_ids = [data["test_case"] for data in test_records]


@pytest.mark.parametrize("data",test_records,ids=case_ids)
def test_eventhub_login_matrix(driver,data):
    login_page = LoginPage(driver)
    print(test_records)
    #Execute the step sequence
    login_page.login_to_eventhub(
        data["email"],
        data["password"]
    )

    if data["test_case"] == "valid_login":
        assert "EventHub — Discover & Book Events" in driver.title
    else:
        assert "Invalid" in login_page.get_error_message()




