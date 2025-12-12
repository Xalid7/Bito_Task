import allure
import pytest


@allure.feature("Login Page")
@allure.story("01: Verify Login page UI elements")
@allure.severity(allure.severity_level.CRITICAL)
class TestLoginPage:
    @allure.title("TC-01: Login page UI elements are displayed correctly")
    def test_login_page_ui(self,authorize_user, page, login_page):
        with allure.step("Open login page"):
            page.goto("https://dev.bito.uz/login")

        with allure.step("Verify Login page is opened"):
            assert login_page.is_authorization_page_open(), "Login page title not visible!"

        with allure.step("Verify phone number input exists"):
            assert login_page.is_element_visible(login_page.phone_number_field)

        with allure.step("Verify password input exists"):
            assert login_page.is_element_visible(login_page.password_field)


        with allure.step("Verify checkbox exists"):
            assert login_page.is_element_visible(login_page.checkbox)

        with allure.step("Verify Login button exists"):
            assert login_page.is_element_visible(login_page.login_button)

        with allure.step("Verify 'Forgot password' link exists"):
            assert login_page.is_element_visible(login_page.forgot_password)
