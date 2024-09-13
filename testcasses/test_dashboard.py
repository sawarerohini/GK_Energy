import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from page_objects.login import Login
from page_objects.dashboard_page import DashboardPage
from constants import PASSWORD, USERNAME

class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(30)
        self.driver.get('http://erp-gk.gkenergy.in/dashboard/home')
        self.login = Login(self.driver)
        self.dashboard_page = DashboardPage(self.driver)

    def test_dashboard_graphs(self):
        # Perform login
        self.login.enter_username(USERNAME)
        self.login.enter_password(PASSWORD)
        time.sleep(3)
        self.login.click_login_btn()
        time.sleep(3)

        # Wait for dashboard page to load
        self.login.wait_for_dashboard()
        time.sleep(3)

        # Select values from dropdowns
        self.dashboard_page.select_stat_name('Maharashtra')
        time.sleep(2)
        self.dashboard_page.select_project('MEDA')
        self.dashboard_page.select_stage('2')

        # Click the search button
        self.dashboard_page.click_search_button()

        # Wait for the graph and pie chart to load
        self.dashboard_page.wait_for_stat_graph()
        self.dashboard_page.wait_for_pie_chart()

        # Validate the presence of the graph and pie chart
        stat_graph = self.driver.find_element(*self.dashboard_page.stat_graph)
        pie_chart = self.driver.find_element(*self.dashboard_page.pie_chart)

        self.assertTrue(stat_graph.is_displayed())
        self.assertTrue(pie_chart.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
