

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='E:\\Workspace\\Selenium webdriver\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

checkboxes = driver.find_elements(By.XPATH,'//*[contains(@type,"checkbox")]')

for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()

