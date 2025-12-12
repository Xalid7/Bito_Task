from typing import List
from playwright.sync_api import Page, expect
import random, string


class BaseScreen:
    def __init__(self, page: Page):
        self.contex = page.context
        self.page = page
        self.timeout = 20000

    # =========================
    def get_element(self, locator):
        method = locator[0]
        values = locator[1]
        return self.get_element_by_type(method, values)

    def get_element_by_type(self, method, value):
        if method == "role":
            return self.page.get_by_role(value[0], name=value[0], exact=True)
        elif method == "id":
            return self.page.get_by_test_id(value)
        elif method == "xpath":
            return self.page.locator(value)
        elif method == "pla":
            return self.page.get_by_placeholder(value)
        elif method == "txt":
            return self.page.get_by_text(value)
        elif method == "label":
            return self.page.get_by_label(value)
        elif method == "tit":
            return self.page.get_by_title(value)
        else:
            raise Exception("Invalid locator method.")

    # =========================
    def navigate_to(self, url):
        self.page.goto(url)

    def get_current_url(self):
        return self.page.url

    # =========================
    def click(self, locator):
        self.get_element(locator).wait_for(timeout=self.timeout)
        self.get_element(locator).click(timeout=self.timeout)

    def fill(self, locator, text):
        self.get_element(locator).wait_for(timeout=self.timeout)
        self.get_element(locator).fill(text, timeout=self.timeout)

    def type(self, locator, text):
        self.get_element(locator).wait_for(timeout=self.timeout)
        self.get_element(locator).type(text, timeout=self.timeout)

    def check(self, locator):
        self.get_element(locator).wait_for(timeout=self.timeout)
        self.get_element(locator).check(timeout=self.timeout)

    def is_element_checked(self, locator):
        self.get_element(locator).wait_for(timeout=self.timeout)
        return self.get_element(locator).is_checked(timeout=self.timeout)

    # =========================
    def wait_element(self, locator):
        self.get_element(locator).wait_for(timeout=self.timeout)

    def is_element_visible(self, locator):
        try:
            self.get_element(locator).wait_for(timeout=self.timeout)
            return self.get_element(locator).is_visible(timeout=self.timeout)
        except:
            return False

    def get_element_text(self, locator):
        self.get_element(locator).wait_for(timeout=self.timeout)
        return self.get_element(locator).text_content(timeout=self.timeout)

    def get_screenshot(self, screenshot_name):
        self.page.screenshot(path=f"screenshots/{screenshot_name}", full_page=True)
