from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.opencart.com/")
driver.maximize_window()
desktops = driver.find_element(By.XPATH,"//a[normalize-space()='Desktops']")
action = ActionChains(driver)
action.move_to_element(desktops).pause(3).click(driver.find_element(By.XPATH,"//a[normalize-space()='PC (0)']")).perform()

