
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        username_field = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='validate-input wrap-input100 mb-4']//input[@id='useremail']")))
        password_field = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Login']")))

        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()

        # Debugging information
        print("Username and password fields populated and login button clicked")
