from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddEmployeePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)

    def fill_firstname(self, expected_first_name):
        driver = self.driver
        first_name_input_field = driver.find_element(By.NAME, "firstName")
        first_name_input_field.send_keys(expected_first_name)

    def fill_lastname(self, expected_last_name):
        driver = self.driver
        last_name_input_field = driver.find_element(By.NAME, "lastName")
        last_name_input_field.send_keys(expected_last_name)


    def fill_and_save_empID(self, empID):
        driver = self.driver
        employee_ID_field = driver.find_element(By.CSS_SELECTOR,
                                                ".oxd-grid-2 > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
        employee_ID_field.click()
        employee_ID_field.send_keys(Keys.COMMAND + "a")
        employee_ID_field.send_keys(Keys.DELETE)
        employee_ID_field.send_keys(empID)


    def save(self):
        driver = self.driver
        save_button = driver.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(3)")
        save_button.click()
        locator = (By.CSS_SELECTOR, "div.orangehrm-horizontal-padding:nth-child(1) > h6:nth-child(1)")
        self.wait.until(expected_conditions.presence_of_element_located(locator))
