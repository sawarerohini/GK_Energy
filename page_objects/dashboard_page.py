from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base import Base


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.stat_name_dropdown = (By.XPATH, "//select[@id='state']")
        self.project_dropdown = (By.XPATH, "//select[@id='project']")
        self.stage_dropdown = (By.XPATH, "//select[@id='stage']")
        self.search_button = (By.ID, "//button[@class='btn btn-primary btn-outline-primary mx-2']")
        self.stat_graph = (By.ID, "//button[@class='btn btn-primary btn-outline-primary mx-2']")
        self.pie_chart = (By.ID, "//button[@class='btn btn-primary btn-outline-primary mx-2']")

    def select_stat_name(self, stat_name):
        Select(self.driver.find_element(*self.stat_name_dropdown)).select_by_visible_text(stat_name)

    def select_project(self, project):
        Select(self.driver.find_element(*self.project_dropdown)).select_by_visible_text(project)

    def select_stage(self, stage):
        Select(self.driver.find_element(*self.stage_dropdown)).select_by_visible_text(stage)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def wait_for_stat_graph(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.stat_graph))

    def wait_for_pie_chart(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.pie_chart))
