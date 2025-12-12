import pytest
import allure

@allure.feature("Login Page")
@allure.story("04: Invalid phone number format")
@allure.title("04: User cannot login with invalid phone number format")
def test_invalid_phone_number_format(page,login_page):
    with allure.step("Open login page"):
        page.goto("https://dev.bito.uz/login")
    with allure.step("Enter invalid phone number format"):
        login_page.enter_phone_number("+998941623")
    with allure.step("Enter password"):
        login_page.enter_password("1234567789")
    with allure.step("Click login button"):
        login_page.click_login_button()
    with allure.step("Get validation error text"):
        error_text = login_page.get_error_text()

    expected_errors = [
        "Неверное значение",
        "Invalid value",
        "Please pay attention to the filled information"
    ]
