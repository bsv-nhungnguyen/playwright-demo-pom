import pytest
import dotenv
import os
from pathlib import Path
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import allure
_PROJECT_ROOT = Path(__file__).parent
dotenv.load_dotenv(_PROJECT_ROOT / '.env')

@pytest.fixture(scope="function")
def page():
    browser = "chromium"
    headless = False 
    with sync_playwright() as p:
        if browser == "chromium":
            browser = p.chromium.launch(headless=headless)
        elif browser == "firefox":
            browser = p.firefox.launch(headless=headless)
        elif browser == "webkit":
            browser = p.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        context = browser.new_context()
        page = context.new_page()
        yield page

        context.close()
        browser.close()

# @pytest.fixture(scope="function", params=["chromium", "firefox", "webkit"])
# def browser(request):
#     browser_type = request.param
#     headless = False 
#     with sync_playwright() as p:
#         if browser_type == "chromium":
#             browser = p.chromium.launch(headless=headless)
#         elif browser_type == "firefox":
#             browser = p.firefox.launch(headless=headless)
#         elif browser_type == "webkit":
#             browser = p.webkit.launch(headless=headless)
#         else:
#             raise ValueError(f"Unsupported browser: {browser_type}")
#         context = browser.new_context()
#         page = context.new_page()
#         yield page

#         context.close()
#         browser.close()

@pytest.fixture(scope="function")
def open_login_page(page):
    login_page = LoginPage(page)
    login_page.page.goto(os.getenv('BASE_URL'))
    yield login_page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        page = item.funcargs.get("page") or (
            item.funcargs.get("login").page if item.funcargs.get("login") else None
        )

        if page:
            status = "PASSED" if rep.passed else "FAILED"
            try:
                allure.attach(
                    page.screenshot(full_page=True),
                    name=f"{item.name}_{status}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                allure.attach(
                    body=f"Could not capture screenshot: {e}",
                    name=f"{item.name}_SCREENSHOT_ERROR",
                    attachment_type=allure.attachment_type.TEXT
                )
