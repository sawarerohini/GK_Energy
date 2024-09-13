import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from page_objects.login import Login
from page_objects.survey_report import Survey_Report
import time
import os

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('http://erp-gk.gkenergy.in/dashboard/state-management')
    driver.maximize_window()
    login_obj = Login(driver)
    survey_obj = Survey_Report(driver)
    login_obj.login('test1234567', 'Test@123456')  # Replace with actual credentials
    yield driver, survey_obj
    survey_obj.logout()
    driver.quit()

def test_survey_report_functionality(setup):
    driver, survey_obj = setup
    survey_obj.click_survey_report_link()
    survey_obj.select_state('Maharashtra')
    survey_obj.select_district_drp('Nagpur')
    survey_obj.select_taluka_drp('Mauda')
    survey_obj.click_search_btn()

    time.sleep(10)  # Increase wait time to ensure data is loaded

    # expected_values = ['Mauda']  # Add expected values that should appear in the result row
    #
    # retries = 3
    # for attempt in range(retries):
    #     try:
    #         assert survey_obj.verify_results(expected_values), "Expected data not found in the results table"
    #         break
    #     except (StaleElementReferenceException, TimeoutException) as e:
    #         if attempt < retries - 1:
    #             print(f"Exception {e} caught. Retrying... (attempt {attempt + 1})")
    #             time.sleep(2)  # Add a small delay before retrying
    #             continue
    #         else:
    #             driver.save_screenshot(f"test_failure_attempt_{attempt + 1}.png")
    #             # Adding more debug information
    #             with open(f"page_source_{attempt + 1}.html", "w", encoding="utf-8") as f:
    #                 f.write(driver.page_source)
    #             raise