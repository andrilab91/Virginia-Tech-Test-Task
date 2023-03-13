from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainMenu():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)

    def goto_pim_employee_list(self):
        driver = self.driver
        PIM_menu_button = driver.find_element(By.LINK_TEXT, "PIM")
        PIM_menu_button.click()
        locator_PIM_page = (By.CSS_SELECTOR, "h5.oxd-text")
        self.wait.until(expected_conditions.presence_of_element_located(locator_PIM_page))