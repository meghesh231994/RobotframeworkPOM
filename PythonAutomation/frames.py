import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path = "E:\\Workspace\\Selenium webdriver\\chromedriver.exe")
driver.get('https://the-internet.herokuapp.com/iframe')

driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.XPATH,'//*[contains(@class,"mce-content-body")]').clear()
driver.find_element(By.CSS_SELECTOR,'#tinymce').send_keys('hello')
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,'h3').text)
