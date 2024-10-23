import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.login import Login
from page_objects.warehouse_management import WarehouseManagementPage


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('')
    driver.maximize_window()
    login_obj = Login(driver)
    warehouse_page = WarehouseManagementPage(driver)
    login_obj.login('user', 'pass@2123')  # Replace with actual credentials
    yield driver, warehouse_page
    warehouse_page.logout()
    driver.quit()


def test_stat_management_functionality(setup):
    driver, warehouse_page = setup
    warehouse_page.click_warehouse_management_link()
    warehouse_page.select_state('Maharashtra')
    warehouse_page.select_district('Beed')
    warehouse_page.select_taluka('Dharur')
    warehouse_page.click_search()

    expected_values = ['Dharur']  # Add expected values that should appear in the result row
    assert warehouse_page.verify_results(expected_values), "Expected data not found in the results table"
