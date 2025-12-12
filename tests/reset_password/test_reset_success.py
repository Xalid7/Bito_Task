import allure

@allure.feature("Reset Password")
@allure.story("11: Successful password recovery request")
@allure.title("11: Verify Success toast appears after valid request")
def test_reset_password_success(page):
    with allure.step("Open Reset Password page"):
        page.goto("https://dev.bito.uz/forgot-password")
    with allure.step("Enter valid phone number"):
        page.locator("input[name='phone_number']").fill("942700550")
    # with allure.step("Click submit button"):
    #     page.locator("button[type='submit']").click()
    with allure.step("Verify success toast is visible"):
        # 1) Success toast paydo bo‘lishini kutamiz
        page.wait_for_selector(
            "div[role='status']:has-text('Success')",
            timeout=5000
        )
        success_toast = page.locator("div[role='status']:has-text('Success')").first
        assert success_toast.is_visible(), "Success toast ko‘rinmadi"
