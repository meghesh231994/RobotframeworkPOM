from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='E://Workspace//Selenium webdriver//chromedriver.exe')
driver.get('https://www.makemytrip.com/')

#driver.find_element(By.XPATH,'//*[contains(text(),"DEL, Delhi Airport India")]').click()