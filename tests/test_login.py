from pages.login_page import LoginPage
from playwright.sync_api import expect
from ultis.messages import ERROR_LOGIN_FAILED
import allure

@allure.feature("Login Feature")
@allure.story("Login with invalid credentials")
@allure.link("https://bsv-test-phi2.eventos.work/console/login", name="Login Page")

class TestLogin:
    @allure.title("TC_001: Test login with invalid credentials")
    def test_login_with_invalid_credentials(self, open_login_page):
        open_login_page.login("invalid_user@gmail.com", "invalid_pass")
        expect(open_login_page.page.locator(f"text={ERROR_LOGIN_FAILED}")).to_be_visible()
