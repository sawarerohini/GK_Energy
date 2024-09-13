import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.login import Login
from page_objects.state_management import StatManagementPage


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('http://erp-gk.gkenergy.in/dashboard/state-management')
    driver.maximize_window()
    login_obj = Login(driver)
    stat_page = StatManagementPage(driver)
    login_obj.login('test1234567', 'Test@123456')  # Replace with actual credentials
    yield driver, stat_page
    stat_page.logout()
    driver.quit()


def test_stat_management_functionality(setup):
    driver, stat_page = setup
    stat_page.click_stat_management()
    stat_page.select_state('Maharashtra')
    stat_page.select_district('Parbhani')
    stat_page.select_taluka('Purna')
    stat_page.click_search()

    expected_values = ['Purna']  # Add expected values that should appear in the result row
    assert stat_page.verify_results(expected_values), "Expected data not found in the results table"
