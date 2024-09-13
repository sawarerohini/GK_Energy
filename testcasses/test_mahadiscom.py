import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.login_page import LoginPage
from page_objects.mahadiscom_page import ReportsPage

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://kusumoffice.mahadiscom.in/solar/dashboard")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_hover_and_click_beneficiary_registration_link(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Perform login
    print("Logging in...")
    login_page.login("ho@mahadiscom.in", "Discom@123")

    # Check if login was successful
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='menu-toggle']")))
    print("Login successful.")

    # Create Reports page object
    reports_page = ReportsPage(driver)
    reports_page.hover_and_click_beneficiary_registration_link()
    # Add assertions or further steps if needed
