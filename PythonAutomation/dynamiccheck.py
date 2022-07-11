
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='E:\\Workspace\\Selenium webdriver\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

checkboxes = driver.find_elements(By.XPATH,'//*[contains(@type,"checkbox")]')
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option1':
        checkbox.click()
        assert checkbox.is_selected()


radio = driver.find_elements(By.NAME,'radioButton')
radio[0].click()
assert radio[0].is_selected()