from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PimEmployeeListPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)

    def pim_add_employee_button(self):
        driver = self.driver
        add_employee_button = driver.find_element(By.CSS_SELECTOR, "button.oxd-button--secondary:nth-child(1)")
        add_employee_button.click()

        #wait for page load
        locator = (By.CSS_SELECTOR, ".orangehrm-main-title")
        self.wait.until(expected_conditions.presence_of_element_located(locator))


    def fill_employee_id_field(self, empID):
        driver = self.driver

        PIM_search_field_by_empID = driver.find_element(By.CSS_SELECTOR, "input.oxd-input:nth-child(1)")
        PIM_search_field_by_empID.send_keys(empID)

    def press_search(self):
        driver = self.driver
        PIM_search_button = driver.find_element(By.CSS_SELECTOR, "button.oxd-button:nth-child(2)")
        PIM_search_button.click()

        # wait for results
        sleep(3)
    def actual_first_name(self):
        driver = self.driver
        return driver.find_element(By.CSS_SELECTOR, "div.oxd-table-card:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)").text

    def actual_last_name(self):
        driver = self.driver
        return driver.find_element(By.CSS_SELECTOR, "div.oxd-table-card:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1)").text


    def delete_added_employee(self):
        driver = self.driver
        employee_delete_button = driver.find_element(By.CSS_SELECTOR, "button.oxd-table-cell-action-space:nth-child(1)")
        employee_delete_button.click()

        #wait for warning popup
        locator_warning = (By.CSS_SELECTOR, ".oxd-text--card-title")
        self.wait.until(expected_conditions.visibility_of_element_located(locator_warning))

        warning_popup_yes = driver.find_element(By.CSS_SELECTOR, ".oxd-button--label-danger")
        warning_popup_yes.click()

        # wait for success popup
        locator_success = (By.CSS_SELECTOR, "#oxd-toaster_1")
        self.wait.until(expected_conditions.presence_of_element_located(locator_success))







