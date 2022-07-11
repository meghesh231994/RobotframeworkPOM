
from selenium import webdriver
from selenium.webdriver.common.by import By
validate = 'Option3'

driver = webdriver.Chrome(executable_path='E:\\Workspace\\Selenium webdriver\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.ID,'name').send_keys(validate)
driver.find_element(By.ID,'alertbtn').click()
alert = driver.switch_to.alert
alertText = alert.text
assert validate in alertText
alert.accept()