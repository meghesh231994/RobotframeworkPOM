'''
from selenium import webdriver


driver = webdriver.Chrome(executable_path='E://Workspace//Selenium webdriver//chromedriver.exe')

driver.get('https://www.google.com')
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.minimize_window()
driver.back()
driver.close()
'''