# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
# from page_objects.login import Login
# from page_objects.beneficiary_management import BeneficiaryManagement
#
#
# @pytest.fixture(scope="module")
# def setup():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.get('')
#     driver.maximize_window()
#     login_obj = Login(driver)
#     beneficiary_page = BeneficiaryManagement(driver)
#     login_obj.login('test1234567', 'Test@123456')  # Replace with actual credentials
#     yield driver, beneficiary_page
#     beneficiary_page.logout()
#     driver.quit()
#
#
# def test_beneficiary_management_functionality(setup):
#     driver, beneficiary_page = setup
#     beneficiary_page.click_beneficiary_management()
#     time.sleep(3)
#
#     # Explicit wait for state dropdown to be visible
#     state_dropdown_element = beneficiary_page.wait_for_element(*beneficiary_page.STATE_DROPDOWN)
#
#     # Debugging: Print available options in the state dropdown
#     state_dropdown = Select(state_dropdown_element)
#     options = state_dropdown.options
#     print("Available states:")
#     for option in options:
#         print(option.text)
#
#     # Select state
#     try:
#         beneficiary_page.select_state('Maharashtra')
#     except Exception as e:
#         print(f"Error selecting state: {e}")
#
#     time.sleep(3)
#
#     # Continue with the rest of the test steps
#     try:
#         beneficiary_page.select_district('Parbhani')
#         beneficiary_page.select_taluka('Parbhani')
#         beneficiary_page.select_project('MEDA')
#         beneficiary_page.select_stage('3')
#     except Exception as e:
#         print(f"Error selecting dropdown values: {e}")
#
#     time.sleep(3)
#
#     # File upload
#     try:
#         beneficiary_page.upload_file(
#             r'C:\Users\Innosystech_8_Pc_3\Downloads\allBenf (1)')  # Replace with the actual file path
#     except Exception as e:
#         print(f"Error uploading file: {e}")
#
#     # Optionally, click the download CSV button
#     try:
#         beneficiary_page.click_download_csv_button()
#     except Exception as e:
#         print(f"Error clicking download CSV button: {e}")
#
#     # Click search button
#     try:
#         beneficiary_page.click_search_btn()
#     except Exception as e:
#         print(f"Error clicking search button: {e}")



import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.login import Login
from page_objects.beneficiary_management import BeneficiaryManagement
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('http://erp-gk.gkenergy.in/dashboard/state-management')
    driver.maximize_window()
    login_obj = Login(driver)
    beneficiary_page = BeneficiaryManagement(driver)
    login_obj.login('test1234567', 'Test@123456')  # Replace with actual credentials
    yield driver, beneficiary_page
    beneficiary_page.logout()
    driver.quit()

def test_beneficiary_management_functionality(setup):
    driver, beneficiary_page = setup
    logging.info("Clicking on Beneficiary Management")
    beneficiary_page.click_beneficiary_management()

    # Explicit wait for state dropdown to be visible
    logging.info("Waiting for State dropdown to be visible")
    beneficiary_page.wait_for_element(*beneficiary_page.STATE_DROPDOWN)
    time.sleep(2)  # Pause for visual confirmation

    # Select state
    logging.info("Selecting State: Maharashtra")
    beneficiary_page.select_state('Maharashtra')
    time.sleep(2)  # Pause for visual confirmation

    # Select district
    logging.info("Selecting District: Parbhani")
    beneficiary_page.select_district('Parbhani')
    time.sleep(2)  # Pause for visual confirmation

    # Select taluka
    logging.info("Selecting Taluka: Parbhani")
    beneficiary_page.select_taluka('Parbhani')
    time.sleep(2)  # Pause for visual confirmation

    # Select project
    logging.info("Selecting Project: MEDA")
    beneficiary_page.select_project('MEDA')
    time.sleep(2)  # Pause for visual confirmation

    # Select stage
    logging.info("Selecting Stage: 3")
    beneficiary_page.select_stage('3')
    time.sleep(2)  # Pause for visual confirmation

    # File upload
    logging.info("Uploading file")
    beneficiary_page.upload_file(r'C:\Users\Innosystech_8_Pc_3\Downloads\your_file_name')  # Replace with the actual file path
    time.sleep(2)  # Pause for visual confirmation

    # Optionally, click the download CSV button
    logging.info("Clicking Download CSV button")
    beneficiary_page.click_download_csv_button()
    time.sleep(2)  # Pause for visual confirmation

    # Click search button
    logging.info("Clicking Search button")
    beneficiary_page.click_search_btn()
    time.sleep(2)  # Pause for visual confirmation

    logging.info("Test completed successfully")
