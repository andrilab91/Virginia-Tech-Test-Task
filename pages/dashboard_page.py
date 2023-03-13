from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DashboardPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)
    def dashboard_page_loaded(self):
        driver = self.driver
        locator_dashboard = (By.CSS_SELECTOR, "h6.oxd-text")
        self.wait.until(expected_conditions.presence_of_element_located(locator_dashboard))
        return driver.find_element(By.CSS_SELECTOR, "h6.oxd-text").text
