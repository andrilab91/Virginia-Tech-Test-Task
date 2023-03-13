import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


from fixtures.config import url, expected_welcome_message, invalid_login, expected_invalid_credentials_message, \
    expected_required_message
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 25)
        # POM pages
        self.login_page = LoginPage(self.driver)
        self.dashboard = DashboardPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        self.login_page.login()
        self.assertEqual(expected_welcome_message, self.dashboard.dashboard_page_loaded())
        self.tearDown()
    def test_invalid_login(self):
        self.login_page.login(username=invalid_login)
        self.assertEqual(expected_invalid_credentials_message, self.login_page.error_invalid_credentials_actual())
        self.tearDown()
    def test_empty_login(self):
        self.login_page.login(username="", password="")
        self.assertEqual(expected_required_message, self.login_page.required_error_actual())
        self.tearDown()


if __name__ == "__main__":
    unittest.main()
