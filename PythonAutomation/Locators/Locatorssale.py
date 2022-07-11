
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='E:\\Workspace\\Selenium webdriver\\chromedriver.exe')

driver.get('https://login.salesforce.com/?locale=in')

driver.find_element(By.NAME,'username').send_keys('meghesh')
driver.find_element(By.ID,'password').send_keys('he')

driver.find_element(By.LINK_TEXT,'Forgot Your Password?').click()

#//*[contains(@name,"login")]/div[1]/label
driver.find_element(By.XPATH,'//*[contains(@name,"forgotPassword")]/div[1]/input[3]').click()

print(driver.find_element(By.XPATH,'//*[contains(@name,"login")]/div[1]/label').text)