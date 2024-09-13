# test_home_page.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.home_page import HomePage

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://demo.opencart.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_hover_and_click_pc_option(setup):
    driver = setup
    home_page = HomePage(driver)
    home_page.hover_and_click_pc_option()
    # Add assertions or further steps if needed
