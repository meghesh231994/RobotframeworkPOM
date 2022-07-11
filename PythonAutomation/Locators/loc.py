
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='E:\\Workspace\\Selenium webdriver\\chromedriver.exe')

driver.get('https://www.rahulshettyacademy.com/angularpractice/')
driver.maximize_window()

driver.find_element(By.NAME, "name").send_keys('meghesh')

driver.find_element(By.NAME, 'email').send_keys('meghesh')

driver.find_element(By.ID, 'exampleInputPassword1').send_keys('gee')

s = Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
s.select_by_index(1)


driver.find_element(By.XPATH,"//*[contains(@class,'btn-success')]").click()

message = driver.find_element(By.XPATH,"//*[contains(@class,'alert-success')]").text

assert "success" in message

