from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class PimPersonalMenu():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)

    def goto_personal_job(self):
        driver = self.driver
        personal_page_menu_job_button = driver.find_element(By.LINK_TEXT, "Job")
        personal_page_menu_job_button.click()

        # wait job page load
        locator = (By.CSS_SELECTOR, "div.orangehrm-horizontal-padding:nth-child(1) > h6:nth-child(1)")
        self.wait.until(expected_conditions.presence_of_element_located(locator))
