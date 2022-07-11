import time

from multipledispatch.dispatcher import source
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
    command_executor='http://localhost:4444',
    options=options)

driver.get('https://www.makemytrip.com/')

driver.find_element(By.ID,'fromCity').click()
