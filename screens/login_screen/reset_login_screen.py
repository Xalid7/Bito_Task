import allure
from screens.base_screen import BaseScreen


class ResetLoginScreen(BaseScreen):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        self.title = ("xpath", "//*[text()='Forgot password']")
        self.phone_number_field = ("xpath", "//*[@name='phone_number']")
        self.submit_button = ("xpath", "//*[text()='Get SMS']")
        self.back_button = ("xpath", "//*[text()='Back']")

    def get_error_text_reset(self):
        locators = [
            ("xpath", "//span[text()='Неверное значение']"),
            ("xpath", "//*[text()='Invalid value']"),
            ("xpath", "//*[@class='css-1f26fsn']"),
            ("xpath", "//div[contains(@class,'Mui-error')]/p"),
            ("xpath", "//div[@role='status' and text()='Please pay attention to the filled information']"),
            ("xpath", "//div[@role='status' and text()='User with this details not found']"),
            ("xpath", "//div[@role='status' and text()='Too many attempts']"),
            ("xpath", "//p[text()='Поле обязательно']"),
            # ("xpath", "//div[@role='status' and text()='Success']"),
        ]

        for locator in locators:
            try:
                if self.is_element_visible(locator):
                    return self.get_element(locator).text_content().strip()
            except:
                pass

        return ""

    @allure.step("Enter reset input value")
    def enter_reset_value(self, value):
        self.set_value(self.phone_number_field, value)

    @allure.step("Click Submit button")
    def click_submit(self):
        self.click(self.submit_button)
