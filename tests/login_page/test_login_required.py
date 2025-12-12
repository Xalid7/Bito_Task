import pytest
import allure

@allure.title("02: Login with empty phone number")
def test_empty_phone_number(page, login_page):

    page.goto("https://dev.bito.uz/login")

    login_page.enter_password("12345")
    login_page.click_login_button()

    error_text = login_page.get_error_text()

    expected_errors = [
        "Номер телефона обязателен",
        "Invalid value",
        "Неверное значение"
    ]


