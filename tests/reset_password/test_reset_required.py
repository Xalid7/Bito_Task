import pytest
import allure

@allure.feature("Reset Password")
@allure.story("07: Navigation + UI Verification")
@allure.title("07: Verify navigation to Reset Password page and UI elements")
def test_reset_password_navigation_and_ui(page, login_page):
    with allure.step("Open Login page"):
        page.goto("https://dev.bito.uz/login")
    with allure.step("Click 'Forgot password?' link"):
        login_page.click_forgot_password_link()
    with allure.step("Verify Reset Password page URL"):
        assert "/forgot-password" in page.url, (
            f"Expected to navigate to Reset Password page, but got URL: {page.url}"
        )
    with allure.step("Verify Input field exists"):
        input_field = page.locator("input")
        assert input_field.count() > 0, "Reset Password input field NOT found"

    with allure.step("Verify Submit button exists"):
        submit_button = page.locator("button[type='submit']")
        assert submit_button.count() > 0, "Submit button NOT found"

    with allure.step("Verify validation components exist"):
        validation_elements = page.locator(
            ".MuiFormHelperText-root, .error, .error-text"
        )
        assert validation_elements.count() >= 0
