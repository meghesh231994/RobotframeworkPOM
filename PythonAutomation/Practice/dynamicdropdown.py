import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path='E://Workspace//Selenium webdriver//chromedriver.exe')
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element(By.ID,'autosuggest').send_keys('aus')
time.sleep(2)
countries = driver.find_elements(By.XPATH,'//*[@class="ui-menu-item"]')
print(len(countries))
for country in countries:
    if country.text== 'Austria':
        country.click()
        break

