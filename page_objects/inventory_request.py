from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base import Base
import time


class Inventory_Request(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.inventory_request_link = (By.XPATH, "//span[normalize-space()='Inventory Request']")
        self.state_drp = (By.XPATH, "//select[@id='state']")
        self.district_drp = (By.XPATH, "//select[@id='district']")
        self.taluka_drp = (By.XPATH, "//div[3]//div[1]//select[1]")
        self.status_drp = (By.XPATH,"//div[4]//div[1]//select[1]")
        self.search_btn = (By.XPATH, "//button[@class='btn btn-primary btn-outline-primary mtt-44 mx-2']")
        self.result_table_row = (By.XPATH,"/html[1]/body[1]/app-root[1]/app-dashboard[1]/app-inventory-requestes[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]")

    def click_inventory_request_link(self):
        self.click_element(*self.inventory_request_link)
        time.sleep(3)

    def select_state(self, state_name):
        # Wait for the state dropdown to be present and visible
        state_dropdown = Select(self.wait_for_element_to_be_visible(*self.state_drp))
        time.sleep(2)  # Additional sleep to ensure options are populated

        # Capture the options for debugging purposes
        options = [option.text for option in state_dropdown.options]
        print("Available state options:", options)

        if state_name not in options:
            print(f"State {state_name} not found in the dropdown options.")
            self.driver.save_screenshot("state_dropdown_error.png")
            raise Exception(f"State {state_name} not found in the dropdown options.")

        state_dropdown.select_by_visible_text(state_name)
        time.sleep(3)

    def select_district_drp(self, district_name):
        district_dropdown = Select(self.wait_for_element_to_be_visible(*self.district_drp))
        district_dropdown.select_by_visible_text(district_name)
        time.sleep(2)

    def select_taluka_drp(self, taluka_name):
        taluka_dropdown = Select(self.wait_for_element_to_be_visible(*self.taluka_drp))
        time.sleep(2)  # Additional sleep to ensure options are populated

        options = [option.text for option in taluka_dropdown.options]
        print("Available taluka options:", options)

        if taluka_name not in options:
            print(f"Taluka {taluka_name} not found in the dropdown options.")
            self.driver.save_screenshot("taluka_dropdown_error.png")
            raise Exception(f"Taluka {taluka_name} not found in the dropdown options.")

        taluka_dropdown.select_by_visible_text(taluka_name)
        time.sleep(2)

    def select_status_drp(self, status_name):
        status_dropdown = Select(self.wait_for_element_to_be_visible(*self.status_drp))
        time.sleep(2)  # Additional sleep to ensure options are populated

        options = [option.text for option in status_dropdown.options]
        print("Available status options:", options)

        if status_name not in options:
            print(f"Status {status_name} not found in the dropdown options.")
            self.driver.save_screenshot("status_dropdown_error.png")
            raise Exception(f"Status {status_name} not found in the dropdown options.")

        status_dropdown.select_by_visible_text(status_name)
        time.sleep(2)
    def click_search_btn(self):
        self.click_element(*self.search_btn)

    def verify_results(self, expected_values):
        self.wait_for_element_to_be_visible(*self.result_table_row)
        rows = self.driver.find_elements(*self.result_table_row)

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
