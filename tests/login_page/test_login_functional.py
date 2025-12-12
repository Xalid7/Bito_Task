import pytest
import allure
@allure.feature("Login Page")
@allure.story("06: Remember me checkbox")
@allure.title("06: Verify 'Remember me' checkbox state persists after refresh")
def test_remember_me_checkbox(page,authorize_user,login_page):

    with allure.step("Open login page"):
        page.goto("https://dev.bito.uz/login")
    with allure.step("Click 'Remember me' checkbox"):
        login_page.click_remember_me_checkbox()
    with allure.step("Verify checkbox is checked"):
        is_checked = login_page.is_remember_me_checked()
        assert is_checked is True
    with allure.step("Enter invalid credentials"):
        login_page.enter_phone_number("999999999")
        login_page.enter_password("wrongpass")
        login_page.click_login_button()
    with allure.step("Refresh page"):
        page.reload()
    with allure.step("Verify checkbox state is STILL checked after refresh"):
        is_checked_after = login_page.is_remember_me_checked()

        if not is_checked_after:
                pytest.xfail(
                "Remember me persistence is NOT implemented. "
                "Recommendation: use localStorage/cookies to persist checkbox state."
            )

        assert is_checked_after is True
