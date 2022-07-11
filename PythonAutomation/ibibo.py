import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='E:\\Workspace\\Selenium webdriver\\chromedriver.exe')
driver.get('https://www.goibibo.com/')

driver.find_element(By.XPATH,'//*[contains(@class,"sc-fotOHu hmnmkS")]/div[1]').click()
driver.find_element(By.XPATH,'//*[contains(@class,"sc-cidDSM dOEpbS")]/input').send_keys('new')
#count = driver.find_elements(By.XPATH,'//*[contains(@class,"autoCompleteTitle ")]')
time.sleep(3)
driver.find_element(By.XPATH,'//*[contains(text(),"New Delhi")]').click()

print(driver.find_element(By.XPATH,'//*[contains(@class,"sc-cidDSM dOEpbS")]/input').text)

