import allure
from screens.base_screen import BaseScreen


class LoginScreen(BaseScreen):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.title = ("xpath", "//h3[text()='Login']")
        self.phone_number_field = ("xpath", "//*[@name='phone_number']")
        self.password_field = ("xpath", "//*[@name='password']")
        self.eye_icon = ("xpath", "//*[contains(@class, 'MuiSvgIcon-root MuiSvgIcon-colorInfo MuiSvgIcon-fontSizeMedium visibilityIcon css-149l1eo')]")
        self.checkbox = ("xpath", "//*[@type='checkbox']")
        self.login_button = ("xpath", "//*[@type='submit']")
        self.forgot_password = ("xpath", "//button[@type='button' and text()='Forgot password?']")

    def get_error_text(self):
        locators = [
            ("xpath", "//span[text()='Неверное значение']"),
            ("xpath", "//*[text()='Invalid value']"),
            ("xpath", "//p[@class='css-1fz6f5n']"),
            ("xpath", "//div[contains(@class,'Mui-error')]/p"),
            ("xpath", "//div[@role='status' and text()='Please pay attention to the filled information']")
        ]

        for locator in locators:
            try:
                element = self.get_element(locator)

                # WARNING: locator.is_visible() is SLOW (default timeout = 30 sec)
                # FIX: we call is_visible(timeout=700) to avoid blocking
                if element.is_visible(timeout=700):
                    text = element.text_content(timeout=700)
                    if text:
                        return text.strip()
            except Exception:
                # ignore locator errors & continue loop
                continue

        return ""

    @allure.step("Check if Login page is open")
    def is_authorization_page_open(self):
        self.wait_element(self.title)
        return self.is_element_visible(self.title)

    @allure.step("Enter phone number: {phone_number}")
    def enter_phone_number(self, phone_number: str):
        self.fill(self.phone_number_field, phone_number)

    @allure.step("Enter password: {password}")
    def enter_password(self, password: str):
        self.fill(self.password_field, password)

    @allure.step("Click eye icon")
    def click_eye_icon(self):
        self.page.locator("div.css-c99983 svg.visibilityOffIcon").first.click(force=True)

    @allure.step("Click ")
    def click_remember_me_checkbox(self):
        self.page.locator("label[for='_remember_me']").click()

    @allure.step("Click ")
    def is_remember_me_checked(self):
        return self.page.locator("input#_remember_me").is_checked()

    @allure.step("Click ")
    def get_password_input_type(self):
        return self.page.locator("input[name='password']").get_attribute("type")

    @allure.step("Click Login button")
    def click_login_button(self):
        self.click(self.login_button)

    @allure.step("Click Forgot Password link")
    def click_forgot_password(self):
        self.click(self.forgot_password)

    @allure.step("Click Forgot Password link")
    def click_forgot_password_link(self):
        self.page.locator("text=Forgot password?").click()

    @allure.step("Reset Password page")
    def open_reset_password_page(self):
        self.page.goto("https://dev.bito.uz/forgot-password")

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.page.locator("button[type='submit']").click()

    @allure.step("Get error message")
    def get_reset_error_text(self):
        return self.page.locator("text=Invalid value")

    @allure.step("Enter reset input")
    def enter_reset_input(self, value):
        self.page.locator("input").fill("+998941623303")

    @allure.step("Click reset submit button")
    def click_reset_submit(self):
        self.page.locator("button[type='submit']").click()

    @allure.step("Get reset error message")
    def get_reset_invalid_error(self):
        return self.page.locator("text=User with this details not found")
