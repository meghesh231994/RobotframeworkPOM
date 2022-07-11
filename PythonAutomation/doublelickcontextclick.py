from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path = "E:\\Workspace\\Selenium webdriver\\chromedriver.exe")
driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')

action = ActionChains(driver)
action.context_click(driver.find_element(By.ID,'double-click')).perform()

action.double_click(driver.find_element(By.ID,'double-click')).perform()

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text

alert.accept()