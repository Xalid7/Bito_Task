import pytest
import allure
from screens.login_screen.login_screens import LoginScreen


# =====================================
# PAGE FIXTURE (Browser + Context + Page)
# =====================================

@pytest.fixture(scope="function")
def page(playwright):

    # Launch browser fully maximized
    browser = playwright.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )

    # Create context with full HD viewport
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )

    # Open page
    page = context.new_page()
    try:
        yield page
    finally:
        if not page.is_closed():
            page.close()
        context.close()
        browser.close()


# =====================================
# ALLURE FAILURE SCREENSHOT
# =====================================

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page and not page.is_closed():
            try:
                allure.attach(
                    page.screenshot(full_page=True),
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except:
                pass


# =====================================
# PAGE OBJECT FIXTURES
# =====================================

@pytest.fixture
def login_page(page):
    return LoginScreen(page)


@pytest.fixture(scope="function")
def authorize_user(page, login_page):
    page.goto("https://dev.bito.uz/login")
    assert login_page.is_authorization_page_open()
    login_page.enter_phone_number("+998941623303")
    login_page.enter_password("12345")
    login_page.click_remember_me_checkbox()
    login_page.click_login_button()
    yield



# # ================================
#
# from screens.login_screen import LoginScreen
# from screens.reset_password_page_screen import ResetPasswordPage
#
# @pytest.fixture
# def login_page(page):
#     return LoginScreen(page)
#
# @pytest.fixture
# def reset_page(page):
#     return ResetPasswordPage(page)
