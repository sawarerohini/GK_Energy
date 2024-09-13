import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from page_objects.login import Login
from page_objects.staff_management import StaffManagement

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('http://erp-gk.gkenergy.in/dashboard/state-management')
    driver.maximize_window()
    login_obj = Login(driver)
    staff_obj = StaffManagement(driver)
    login_obj.login('test1234567', 'Test@123456')  # Replace with actual credentials
    yield driver, staff_obj
    staff_obj.logout()
    driver.quit()

def test_stat_management_functionality(setup):
    driver, staff_obj = setup
    staff_obj.click_staff_management()
    staff_obj.click_add_staff()
    staff_obj.enter_first_name('rohi')
    staff_obj.enter_last_name('savare')
    staff_obj.enter_email('abc45@gmail.com')
    staff_obj.enter_contact_no('3434235893')
    staff_obj.click_gender_radio_btn()
    staff_obj.enter_date_of_joining('09/04/2024')
    staff_obj.select_profile('SuperAdmin')
    staff_obj.enter_username_txt('abc')
    staff_obj.enter_password_txt('abc@321')
    staff_obj.select_state_drp('Maharashtra')
    staff_obj.select_district_drp('Latur')
    # staff_obj.select_taluka_drp(['Achalpur', 'Ausa'])  # List of talukas to be selected
    # staff_obj.select_village_drp(['Ambuj', 'Algarwadi'])  # List of villages to be selected
