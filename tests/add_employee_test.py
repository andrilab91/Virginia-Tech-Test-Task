import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.config import empID, expected_first_name, expected_last_name, date_of_start, url, expected_welcome_message
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.main_menu import MainMenu
from pages.pim_add_amployee_page import AddEmployeePage
from pages.pim_employee_list_page import PimEmployeeListPage
from pages.pim_personal_details_page import PimPersonalDetailsPage
from pages.pim_personal_job_page import PimPersonalJobPage
from pages.pim_personal_menu import PimPersonalMenu


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 25)

        # POM pages
        self.login_page = LoginPage(self.driver)
        self.dashboard = DashboardPage(self.driver)
        self.menu = MainMenu(self.driver)
        self.pim_add_employee = AddEmployeePage(self.driver)
        self.pim_employee_list = PimEmployeeListPage(self.driver)
        self.pim_personal_details = PimPersonalDetailsPage(self.driver)
        self.pim_personal_menu = PimPersonalMenu(self.driver)
        self.pim_personal_job = PimPersonalJobPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_employees(self):
        self.login_page.login()
        self.assertEqual(expected_welcome_message, self.dashboard.dashboard_page_loaded())
        self.menu.goto_pim_employee_list()
        self.pim_employee_list.pim_add_employee_button()
        self.pim_add_employee.fill_firstname(expected_first_name)
        self.pim_add_employee.fill_lastname(expected_last_name)
        self.pim_add_employee.fill_and_save_empID(empID)
        self.pim_add_employee.save()
        self.pim_personal_menu.goto_personal_job()
        self.pim_personal_job.fill_date_joined(date_of_start)
        self.pim_personal_job.save()
        self.menu.goto_pim_employee_list()
        self.pim_employee_list.fill_employee_id_field(empID)
        self.pim_employee_list.press_search()
        self.assertEqual(expected_first_name, self.pim_employee_list.actual_first_name())
        self.assertEqual(expected_last_name, self.pim_employee_list.actual_last_name())
        self.pim_employee_list.delete_added_employee()
        self.tearDown()


if __name__ == "__main__":
    unittest.main()
