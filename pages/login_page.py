from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.config import username, password


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)

    def login(self, username=username, password=password):
        driver = self.driver

        # preload wait
        locator = (By.NAME, "username")
        self.wait.until(expected_conditions.presence_of_element_located(locator))
        password_field = driver.find_element(By.NAME, "password")
        login_field = driver.find_element(By.NAME, "username")
        submit_login_button = driver.find_element(By.CSS_SELECTOR, ".oxd-button")
        login_field.send_keys(username)
        password_field.send_keys(password)
        submit_login_button.click()


    def error_invalid_credentials_actual(self):

        locator_error = (By.CSS_SELECTOR, ".oxd-alert-content-text")
        self.wait.until(expected_conditions.presence_of_element_located(locator_error))
        error_text = self.driver.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text").text
        return error_text


    def required_error_actual(self):
        driver = self.driver
        required_error_text = driver.find_element(By.CSS_SELECTOR,
                                              "div.oxd-form-row:nth-child(2) > div:nth-child(1) > span:nth-child(3)").text
        return required_error_text