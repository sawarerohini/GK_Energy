import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base import Base

class StaffManagement(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.STAFF_MANAGEMENT = (By.XPATH, "//span[normalize-space()='Staff Management']")
        self.ADD_STAFF_BTN = (By.XPATH, "//button[@class='btn btn-primary btn-outline-primary my-2']")
        self.FIRST_NAME_TXT = (By.XPATH, "//input[@id='first-name']")
        self.LAST_NAME_TXT = (By.XPATH, "//input[@placeholder='Enter last name']")
        self.EMAIL_TXT = (By.XPATH, "//input[@placeholder=' Enter email id']")
        self.CONTACT_NO = (By.XPATH, "//input[@placeholder=' Enter contact number']")
        self.GENDER_RADIOBTN = (By.XPATH, "//input[@value='female']")
        self.DATE_OF_JOINING = (By.XPATH, "//div[6]//div[1]//div[1]//input[1]")
        self.DATE_OF_BIRTH = (By.XPATH, "2024-06")
        self.SELECT_PROFILE_DRP = (By.XPATH, "//select[@formcontrolname='groupId']")
        self.USER_NAME_TXT = (By.XPATH, "//input[@id='username']")
        self.PASSWORD_TXT = (By.XPATH, "//input[@id='password']")
        self.CONFIRM_PASSWORD_TXT = (By.XPATH, "//input[@id='confirmPassword']")
        self.ADDRESS_TXT = (By.XPATH, "//textarea[@id='address']")
        self.PIN_CODE_TXT = (By.XPATH, "//input[@id='pincode']")
        self.STATE_DRP = (By.XPATH, "//select[@id='state']")
        self.DISTRICT_DRP = (By.XPATH, "//select[@id='district']")
        self.TALUKA_DRP = (By.XPATH, "//span[@class='dropdown-multiselect--active']//span[@class='dropdown-multiselect__caret']")
        self.SELECT_TALUKA = (By.XPATH, "//div[@class='multiselect-item-checkbox']//label")
        self.VILLAGE_DRP = (By.XPATH, "//span[contains(text(),'Select Village')]")
        self.SELECT_VILLAGE = (By.XPATH, "//div[@class='multiselect-item-checkbox']//label")
        self.WAREHOUSE_DRP = (By.XPATH, "//select[@class='form-control ng-untouched ng-pristine ng-valid']")
        self.STATUS_DRP = (By.XPATH, "//select[@class='form-control ng-untouched ng-pristine ng-invalid']")

    def click_staff_management(self):
        self.click_element(*self.STAFF_MANAGEMENT)
        time.sleep(3)

    def click_add_staff(self):
        self.click_element(*self.ADD_STAFF_BTN)
        time.sleep(3)

    def enter_first_name(self, add_first_name_txt):
        self.find_element(self.FIRST_NAME_TXT).clear()
        self.find_element(self.FIRST_NAME_TXT).send_keys(add_first_name_txt)
        time.sleep(2)

    def enter_last_name(self, add_last_name_txt):
        self.find_element(self.LAST_NAME_TXT).clear()
        self.find_element(self.LAST_NAME_TXT).send_keys(add_last_name_txt)
        time.sleep(2)

    def enter_email(self, add_email_txt):
        self.find_element(self.EMAIL_TXT).clear()
        self.find_element(self.EMAIL_TXT).send_keys(add_email_txt)
        time.sleep(2)

    def enter_contact_no(self, add_contact_no_txt):
        self.find_element(self.CONTACT_NO).clear()
        self.find_element(self.CONTACT_NO).send_keys(add_contact_no_txt)
        time.sleep(2)

    def click_gender_radio_btn(self):
        self.find_element(self.GENDER_RADIOBTN).click()
        time.sleep(2)

    def enter_date_of_joining(self, add_date_of_joining_txt):
        self.find_element(self.DATE_OF_JOINING).clear()
        self.find_element(self.DATE_OF_JOINING).send_keys(add_date_of_joining_txt)
        time.sleep(2)

    def click_date_of_birth(self):
        self.find_element(self.DATE_OF_BIRTH).click()
        time.sleep(2)

    def select_profile(self, profile):
        profile_dropdown = Select(self.wait_for_element(*self.SELECT_PROFILE_DRP))
        profile_dropdown.select_by_visible_text(profile)

    def enter_username_txt(self, username):
        self.find_element(self.USER_NAME_TXT).clear()
        self.find_element(self.USER_NAME_TXT).send_keys(username)

    def enter_password_txt(self, password):
        self.find_element(self.PASSWORD_TXT).clear()
        self.find_element(self.PASSWORD_TXT).send_keys(password)

    def select_state_drp(self, state):
        state_dropdown = Select(self.wait_for_element(*self.STATE_DRP))
        state_dropdown.select_by_visible_text(state)
        time.sleep(2)

    def select_district_drp(self, district):
        district_dropdown = Select(self.wait_for_element(*self.DISTRICT_DRP))
        district_dropdown.select_by_visible_text(district)
        time.sleep(2)

    # def select_multiple_options(self, dropdown_locator, options_locator, options):
    #     # Wait until the dropdown is clickable and then click it
    #     dropdown_element = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(dropdown_locator)
    #     )
    #     dropdown_element.click()
    #     time.sleep(2)  # Wait for the options to be displayed
    #
    #     # Debugging: Check if the dropdown is actually opened
    #     print("Dropdown clicked, now finding options")
    #
    #     # Find the options and select the specific ones
    #     options_elements = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_all_elements_located(options_locator)
    #     )
    #
    #     for option in options_elements:
    #         if option.text in options:
    #             option.click()
    #
    # def select_taluka_drp(self, talukas):
    #     self.select_multiple_options(self.TALUKA_DRP, self.SELECT_TALUKA, talukas)
    #
    # def select_village_drp(self, villages):
    #     self.select_multiple_options(self.VILLAGE_DRP, self.SELECT_VILLAGE, villages)
    #
    # def scroll_and_select_village(self, village):
    #     village_element = self.find_element(self.VILLAGE_DRP)
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", village_element)
    #     time.sleep(1)  # Wait for scrolling to complete
    #     village_dropdown = Select(self.wait_for_element(*self.VILLAGE_DRP))
    #     village_dropdown.select_by_visible_text(village)
    #
    # def find_elements(self, locator):
    #     return self.driver.find_elements(*locator)