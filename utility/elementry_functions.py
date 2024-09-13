import random
import sys

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class Elem_Func:

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,locator_tuple):
        try:
            element = WebDriverWait(self.driver, 10, poll_frequency=1).until(
                EC.presence_of_element_located(locator_tuple))
            return element
        except:
            self.screen_shot()
            raise

    def mouse_hover(self, locator_tuple):
        element = self.find_element(locator_tuple)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def screen_shot(self,  file_name=""):
        """
            This function take screenshot for failed test-case.
        """
        # self.driver.execute_script("document.body.style.zoom='75%'")
        current_dir = os.path.dirname(__file__)
        SCREENSHOT_DIR = os.environ.get("SCREENSHOT_DIR", None)
        if not file_name:
            testcase_dir = os.getcwd()
            testcase_file = os.path.join(testcase_dir, sys.argv[0])
            file_name = os.path.basename(
                testcase_file) + "_" + str(random.randint(1, 1000)) + ".png"
            dir_name = os.path.dirname(testcase_file)
            # screenshot_dir = "../Screenshots/"
            if SCREENSHOT_DIR is None:
                screenshot_dir = os.path.join(current_dir, "Screenshots/")
            else:
                screenshot_dir = os.path.normpath(SCREENSHOT_DIR)
            destination_dir = os.path.join(screenshot_dir,
                                           os.path.basename(dir_name))
            destination_file = os.path.join(destination_dir, file_name)
        else:
            file_name = os.path.basename(file_name)
            file_name = file_name + "_" + str(random.randint(1, 1000)) + ".png"
            if SCREENSHOT_DIR is None:
                destination_dir = os.path.join(current_dir, "Screenshots/")
            else:
                destination_dir = os.path.normpath(SCREENSHOT_DIR)
            destination_file = os.path.join(destination_dir, file_name)

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        self.driver.save_screenshot(destination_file)
        print("Screenshot save to directory: ", destination_file)

