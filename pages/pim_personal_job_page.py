from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class PimPersonalJobPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)

    def fill_date_joined(self, date_of_start):
        driver = self.driver
        date_joined_date_picker = driver.find_element(By.CSS_SELECTOR, "input.oxd-input:nth-child(1)")
        date_joined_date_picker.send_keys(date_of_start)

    def save(self):
        driver = self.driver
        job_page_save_button = driver.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(1)")
        job_page_save_button.click()

        # wait for success popup
        locator = (By.CSS_SELECTOR, "#oxd-toaster_1")
        self.wait.until(expected_conditions.presence_of_element_located(locator))
