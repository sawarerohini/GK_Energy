import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
from page_objects.login import Login
from page_objects.inventory_management import Inventary_Management

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('http://erp-gk.gkenergy.in/dashboard/state-management')
    driver.maximize_window()
    login_obj = Login(driver)
    stat_page = Inventary_Management(driver)
    login_obj.login('test1234567', 'Test@123456')  # Replace with actual credentials
    yield driver, stat_page
    stat_page.logout()
    driver.quit()

def test_inventory_management_functionality(setup):
    driver, inventory_obj = setup
    inventory_obj.click_inventory_management_link()
    inventory_obj.select_state('Maharashtra')
    inventory_obj.select_district_drp('Jalna')
    inventory_obj.select_taluka_drp('Jafferabad')
    inventory_obj.click_search_btn()

    expected_values = ['Jalna']  # Add expected values that should appear in the result row

    retries = 3
    for attempt in range(retries):
        try:
            assert inventory_obj.verify_results(expected_values), "Expected data not found in the results table"
            break
        except StaleElementReferenceException:
            if attempt < retries - 1:
                print(f"StaleElementReferenceException caught. Retrying... (attempt {attempt + 1})")
                continue
            else:
                raise
