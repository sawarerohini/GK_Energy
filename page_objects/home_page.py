# home_page.py
from selenium.webdriver.common.by import By
from page_objects.base import Base

class HomePage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.desktops_menu = (By.XPATH, "//a[normalize-space()='Desktops']")
        self.pc_option = (By.XPATH, "//a[normalize-space()='PC (0)']")

    def hover_and_click_pc_option(self):
        self.hover_over_element(self.desktops_menu)
        self.click_element(self.pc_option)
