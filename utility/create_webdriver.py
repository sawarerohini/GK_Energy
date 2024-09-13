from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from constants import BROWSER


class WebDriver:
    def __new__(cls):
        if BROWSER.lower() == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        else:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        return driver
