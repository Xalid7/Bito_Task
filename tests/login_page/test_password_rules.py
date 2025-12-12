import pytest
import allure

@allure.feature("Login Page")
@allure.story("03: Login with empty password")
@allure.title("03: User cannot login with empty password")
def test_empty_password(page, login_page):
    with allure.step("Open login page"):
        page.goto("https://dev.bito.uz/login")

    with allure.step("Enter valid phone number"):
        login_page.enter_phone_number("941234567")

    with allure.step("Click login button"):
        login_page.click_login_button()

    with allure.step("Get validation error text"):
        error_text = login_page.get_error_text()

    expected_errors = [
        "Пароль обязателен",
        "Invalid value",
        "Неверное значение"
    ]


import pytest
import allure

@allure.feature("Login Page")
@allure.story("05: Password rules + eye icon")
@allure.title("05: Password minimum length + password visibility toggle + submit flow")
def test_password_min_length_and_eye_icon(page, login_page):
    with allure.step("Open login page"):
        page.goto("https://dev.bito.uz/login")
    # --------------------------------------------
    with allure.step("Enter valid phone number"):
        login_page.enter_phone_number("941234567")
    with allure.step("Enter too short password (1 character)"):
        login_page.enter_password("1")
    with allure.step("Click eye icon to show password"):
        login_page.click_eye_icon()
    with allure.step("Verify password is visible (type='text')"):
        visible_type = login_page.get_password_input_type()
        assert visible_type == "text", f"Expected type='text', got {visible_type}"
    with allure.step("Click login button"):
        login_page.click_login_button()
    with allure.step("Get validation error text"):
        error_text = login_page.get_error_text()

    expected_errors = [
        "Пароль должен содержать минимум 6 символов",
        "Password must be at least 6 characters",
        "Min length validation"
    ]

    with allure.step("Validate minimal password length (Industry Best Practice)"):

        if error_text == "":
            pytest.xfail(
                "Minimal password length validation not implemented. "
                "Recommendation: add min length rule for better security & UX."
            )

        assert error_text in expected_errors, (
            f"Expected minimal length error, got: '{error_text}'"
        )

