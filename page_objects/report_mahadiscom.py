from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://kusumoffice.mahadiscom.in/solar/dashboard")
driver.maximize_window()
desktops = driver.find_element(By.XPATH,"//li[@class='nav-item active']//span[@class='nav-text']")
action = ActionChains(driver)
action.move_to_element(desktops).pause(3).click(driver.find_element(By.XPATH,"//span[normalize-space()='Beneficiary Registration']")).perform()




