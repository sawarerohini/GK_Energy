from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base import Base


class BeneficiaryManagement(Base):

    BENEFICIARY_MANAGEMENT = (By.XPATH, "//span[normalize-space()='Beneficiary Management']")
    STATE_DROPDOWN = (By.XPATH, "//select[@id='state']")
    DISTRICT_DROPDOWN = (By.XPATH, "//select[@id='district']")
    TALUKA_DROPDOWN = (By.XPATH, "//select[@id='taluka']")
    PROJECT_DROPDOWN = (By.XPATH, "//select[@id='agent']")
    STAGE_DROPDOWN = (By.XPATH, "//select[@id='stage']")
    CHOOSE_FILE = (By.XPATH, "//input[@type='file']")
    SEARCH_BTN = (By.XPATH, "//button[@class='btn btn-primary btn-outline-primary mtt-44 mx-2']")
    DOWNLOAD_CSV = (By.XPATH, "//button[@class='btn btn-secondary btn-outline-secondary mtt-44']")

    def click_beneficiary_management(self):
        self.click_element(*self.BENEFICIARY_MANAGEMENT)

    def select_state(self, state_name):
        state_dropdown = Select(self.wait_for_element(*self.STATE_DROPDOWN))
        state_dropdown.select_by_visible_text(state_name)

    def select_district(self, district_name):
        district_dropdown = Select(self.wait_for_element(*self.DISTRICT_DROPDOWN))
        district_dropdown.select_by_visible_text(district_name)

    def select_taluka(self, taluka_name):
        taluka_dropdown = Select(self.wait_for_element(*self.TALUKA_DROPDOWN))
        taluka_dropdown.select_by_visible_text(taluka_name)

    def select_project(self, project_name):
        project_dropdown = Select(self.wait_for_element(*self.PROJECT_DROPDOWN))
        project_dropdown.select_by_visible_text(project_name)

    def select_stage(self, stage_name):
        stage_dropdown = Select(self.wait_for_element(*self.STAGE_DROPDOWN))
        stage_dropdown.select_by_visible_text(stage_name)

    def upload_file(self, file_path):
        self.driver.find_element(*self.CHOOSE_FILE).send_keys(file_path)

    def click_download_csv_button(self):
        self.driver.find_element(*self.DOWNLOAD_CSV).click()

    def click_search_btn(self):
        self.driver.find_element(*self.SEARCH_BTN).click()

    def wait_for_element(self, by, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
