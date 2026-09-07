import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.json_reader import JsonReader

test_records = JsonReader.read_json("data/local/login_data.json")

case_ids = [data["test_case"] for data in test_records]


@pytest.mark.parametrize("data",test_records,ids=case_ids)
def test_eventhub_login_matrix(driver,data):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    #Execute the step sequence
    login_page.login_to_eventhub(
        data["email"],
        data["password"]
    )

    if data["expected_result"] == "success":
        actual_email = dashboard_page.get_user_email()
        print("Email from Dashboard:",actual_email)
        assert data["email"] == actual_email
    #For Authentication errors
    elif data["expected_result"] == "authentication_error":
        actual_message = login_page.get_authentication_error_msg()
        assert  data["expected_message"] in actual_message
    #For Field -level Validation errors
    elif data["expected_result"] == "validation_error":
        if data["validation_field"] == "email":
            actual_message = login_page.get_email_validation_msg()

        elif data["validation_field"] == "password":
            actual_message = login_page.get_password_validation_msg()

        else:
            raise ValueError(
                f"Unsupported validation field: "
                f"{data['validation_field']}"
            )
        assert actual_message == data["expected_message"]

    else:
        raise ValueError(
            f"Unsupported expected result: "
            f"{data['expected_result']}"
        )




