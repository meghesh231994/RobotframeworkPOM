import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By

selenium_grid_url = "http://localhost:4444"

# Create a desired capabilities object as a starting point.
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['platform'] = "WINDOWS"
capabilities['version'] = "10"

# Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(desired_capabilities=capabilities,
                          command_executor=selenium_grid_url)

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element(By.ID,'autosuggest').send_keys('can')
time.sleep(2)

dropdowns = driver.find_elements(By.XPATH,'//*[contains(@class,"ui-menu-item")]/a')
for dropdown in dropdowns:
    if dropdown.text == 'Canada':
        dropdown.click()

print(driver.find_element(By.ID,'autosuggest').text)