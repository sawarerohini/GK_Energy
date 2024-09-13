from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base import Base

class ReportsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.report_menu = (By.XPATH, "//li[@class='nav-item active']//span[@class='nav-text']")
        self.beneficiary_registration_link = (By.XPATH, "//span[normalize-space()='Beneficiary Registration']")

    def hover_and_click_beneficiary_registration_link(self):
        print("Attempting to hover over the report menu...")
        self.hover_over_element(self.report_menu)
        print("Clicking on the beneficiary registration link...")
        self.click_element(self.beneficiary_registration_link)
        print("Clicked on the beneficiary registration link.")
