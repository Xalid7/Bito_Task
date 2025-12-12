import pytest
import allure
@allure.feature("Reset Password")
@allure.story("09: Empty input validation")
@allure.title("09: Verify validation error when submitting empty input")
def test_reset_password_empty_input(page, login_page):
    with allure.step("Open Reset Password page"):
        page.goto("https://dev.bito.uz/forgot-password")
    with allure.step("Open Reset Password page"):
        login_page.open_reset_password_page()
    with allure.step("Click submit with empty input"):
        login_page.click_submit_button()
    with allure.step("Check error"):
        assert login_page.get_reset_error_text().is_visible()
@allure.feature("Reset Password")
@allure.story("10: Invalid email/phone format")
@allure.title("10: Verify error for invalid email or phone number")
def test_reset_password_invalid_format(page):
    page.goto("https://dev.bito.uz/forgot-password")
    page.locator("input[name='phone_number']").fill("+998941623303")
    page.locator("button[type='submit']").click()
    page.wait_for_timeout(500)
    possible_errors = [
        "text=User with this details not found",
        ".v-snack__content",
        ".v-snack__wrapper",
        ".error--text",
        ".v-alert__content",
        ".v-messages__message",
        "text=not found",
        "text=Invalid",
        "text=Неверное значение",
    ]

    found = None
    for loc in possible_errors:
        locator = page.locator(loc)
        if locator.count() > 0 and locator.first.is_visible():
            found = locator.first.inner_text().strip()
            print("FOUND LOCATOR:", loc)
            print("TEXT:", found)
            break

    assert found is not None, "Expected validation message was NOT displayed."
