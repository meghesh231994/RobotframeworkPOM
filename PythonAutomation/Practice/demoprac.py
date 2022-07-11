from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='E://Workspace//Selenium webdriver//chromedriver.exe')

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

#Dropdown select
dropdown = Select(driver.find_element(By.ID,'dropdown-class-example'))
dropdown.select_by_index(1)
dropdown.select_by_value('option2')

#checkbox
driver.find_element(By.XPATH,'//input[@id="checkBoxOption2"]').click()

#radiobutton
driver.find_element(By.XPATH,'//*[contains(@value,"radio1")]').click()