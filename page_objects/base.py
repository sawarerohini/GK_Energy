from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from utility.elementry_functions import Elem_Func
from selenium.webdriver.support import expected_conditions as EC



class Base:

    def __init__(self, driver):
        self.driver = driver
        self.EF = Elem_Func(self.driver)
        self.wait = WebDriverWait(driver, 10)


        # Locators

        # Admin (user-management)
        self.state_management_tab = (By.XPATH, "//a[@href='/dashboard/state-management']")

        # PIM (configuration)
        # self.pim_tab = (By.XPATH, "//a[contains(@href,'viewPimModule')]")
        self.pim_tab = (By.LINK_TEXT, "PIM")
        # leave
        self.leave_tab = (By.LINK_TEXT, "Leave")
        # Time
        self.time_tab = (By.XPATH, "//a[@href='/web/index.php/time/viewTimeModule']")

        self.wairehouse_managment_tab = (By.XPATH,"//span[normalize-space()='Warehouse Management']")
        # Logout Locators
        # self.user_profile = (By.XPATH, "//div[@class='header-part-right']//span[1]")


        # self.logout_link = (By.LINK_TEXT, "//a[normalize-space()='Logout']")

    # def click_user_profile(self):
    #     self.EF.find_element(self.user_profile).click()
    #
    # def click_logout_link(self):
    #     self.EF.find_element(self.logout_link).click()

    # def logout(self):
    #     self.click_user_profile()
    #     self.click_logout_link()

    def logout(self):
        user_menu_button = (By.XPATH, "//div[@class='header-part-right']//span[1]")  # Adjust the locator as needed
        logout_button = (By.XPATH, "//a[normalize-space()='Logout']")  # Adjust the locator as needed
        self.click_element(*user_menu_button)
        self.click_element(*logout_button)

    def navigate_to_tab(self, tab_link):
        self.EF.find_element(tab_link).click()

    # def navigate_to_page(self, menu_order):
    #     for menu in menu_order:
    #         if menu == menu_order[-1]:
    #             self.EF.find_element(menu).click()
    #
    #         else:
    #             self.EF.mouse_hover(menu)

    # def click_element(self, locator):
    #     element = self.wait.until(EC.element_to_be_clickable(locator))
    #     element.click()

    # def find_element(self, locator):
    #     return self.wait.until(EC.visibility_of_element_located(locator))

    def take_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)

    # def hover_over_element(self, locator):
    #     element = self.wait.until(EC.visibility_of_element_located(locator))
    #     ActionChains(self.driver).move_to_element(element).perform()
    def select_dropdown_by_visible_text(self, locator, text):
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def find_element(self, locator):
        print(f"Finding element with locator: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    # def click_element(self, locator):
    #     print(f"Waiting to click element with locator: {locator}")
    #     element = self.wait.until(EC.element_to_be_clickable(locator))
    #     element.click()
    #     print(f"Clicked element with locator: {locator}")

    def hover_over_element(self, locator):
        print(f"Waiting to hover over element with locator: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
        print(f"Hovered over element with locator: {locator}")

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click_element(self, by, value):
        element = self.wait_for_element(by, value)
        element.click()

    def scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)







