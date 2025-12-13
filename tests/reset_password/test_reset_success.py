import allure
import random

@allure.feature("Reset Password")
@allure.story("11: Successful password recovery request")
@allure.title("11: Verify Success toast appears after valid request")
def test_reset_password_success(page):

    with allure.step("Open Reset Password page"):
        page.goto("https://dev.bito.uz/forgot-password")
        page.wait_for_load_state("networkidle")

    with allure.step("Select Uzbekistan country code"):
        page.locator("css=.flag-dropdown").click()

        page.locator("li[data-country-code='uz']").click()

    with allure.step("Enter valid phone number"):
        phone = "942700550"
        phone_input = page.locator("input[name='phone_number']")
        phone_input.wait_for(state="visible", timeout=3000)
        phone_input.fill(phone)

    with allure.step("Wait if page auto-refreshes or validation triggers navigation"):
        try:
            with page.expect_event("framenavigated", timeout=3000):
                pass
        except:
            pass

    with allure.step("Verify success toast appears"):
        toast = page.locator("div[role='status']").filter(has_text="Success")

        try:
            toast.wait_for(state="visible", timeout=8000)
        except:
            allure.attach(
                page.screenshot(full_page=True),
                "toast_not_visible",
                allure.attachment_type.PNG
            )
            raise AssertionError("❌ Success toast chiqmagan!")

        assert toast.is_visible(), "❌ Success toast ko‘rinmadi!"
