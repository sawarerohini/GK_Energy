import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_objects.base import Base
from selenium.common.exceptions import TimeoutException

warehouse_management_link = (By.XPATH, "//span[normalize-space()='Warehouse Management']")

class WarehouseManagementPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.warehouse_management_link = (By.XPATH, "//span[normalize-space()='Warehouse Management']")

        self.state_ddl = (By.XPATH, "//select[@id='state']")
        self.district_ddl = (By.XPATH, "//select[@id='district']")
        self.taluka_ddl = (By.XPATH, "//select[@id='taluka']")
        self.search_btn = (By.XPATH, "//button[@class='btn btn-primary btn-outline-primary mtt-44 mx-2']")
        self.RESULTS_TABLE_ROWS = (By.XPATH, "//td[8]")


    def click_warehouse_management_link(self):
        self.click_element(*self.warehouse_management_link)
        time.sleep(3)

    def select_state(self, state_name):
        state_dropdown = Select(self.wait_for_element(*self.state_ddl))
        options = [option.text for option in state_dropdown.options]
        print("Available state options:", options)
        state_dropdown.select_by_visible_text(state_name)
        time.sleep(3)

    def select_district(self, district_name):
        district_dropdown = Select(self.wait_for_element(*self.district_ddl))
        district_dropdown.select_by_visible_text(district_name)
        time.sleep(3)

    def select_taluka(self, taluka_name):
        taluka_dropdown = Select(self.wait_for_element(*self.taluka_ddl))
        taluka_dropdown.select_by_visible_text(taluka_name)
        time.sleep(3)

    def click_search(self):
        self.click_element(*self.search_btn)
        time.sleep(3)

    def verify_results(self, expected_values):
        # Wait for results to be visible
        self.wait_for_element_to_be_visible(*self.RESULTS_TABLE_ROWS)
        rows = self.driver.find_elements(*self.RESULTS_TABLE_ROWS)

        if not rows:
            print("No rows found in the results table.")
            return False

        for row in rows:
            print(row.text)  # Print row text for debugging purposes
            if all(value in row.text for value in expected_values):
                return True

        return False

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

    def wait_for_element(self, by, value, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_element_to_be_visible(self, by, value, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))
