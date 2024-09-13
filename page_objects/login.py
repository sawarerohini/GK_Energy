# import time
# from telnetlib import EC
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# from utility.elementry_functions import Elem_Func
# from constants import USERNAME, PASSWORD
#
#
# class Login:
#     def __init__(self, driver):
#         self.driver=driver
#         self.EF=Elem_Func(self.driver)
#
#         # Locators
#         self.username_txt=(By.ID, "email")
#         self.password_txt=(By.ID, "password")
#         self.login_btn=(By.XPATH, "//button[@name='submit']")
#         self.dashboard_element=(By.XPATH,"//button[@class='btn btn-primary btn-outline-primary mx-2']")
#
#     def enter_username(self, username):
#         self.driver.find_element(*self.username_txt).send_keys(username)
#
#     def enter_password(self, password):
#         self.driver.find_element(*self.password_txt).send_keys(password)
#
#     def click_login_btn(self):
#         self.driver.find_element(*self.login_btn).click()
#
#     # def wait_for_dashboard(self):
#     #     print("Waiting for dashboard to load...")
#     #     WebDriverWait(self.driver, 30).until(
#     #         EC.visibility_of_element_located(self.dashboard_element)
#     #     )
#     #     print("Dashboard loaded.")
#     #
#
#
#

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID,"email")))
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID,"password")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@name='submit']")))

        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()

        # Debugging information
        print("Username and password fields populated and login button clicked")
