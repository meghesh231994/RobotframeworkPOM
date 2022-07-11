import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='E:\\Workspace\\Selenium webdriver\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.find_element(By.ID,'autosuggest').send_keys('ind')
time.sleep(2)
countries = driver.find_elements(By.XPATH,'//*[contains(@class,"ui-menu-item")] /a')
#print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break
print(driver.find_element(By.ID,'autosuggest').text)