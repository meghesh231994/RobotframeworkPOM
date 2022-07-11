
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path = "E:\\Workspace\\Selenium webdriver\\chromedriver.exe")
driver.get('https://rahulshettyacademy.com/AutomationPractice/')


action = ActionChains(driver)
menu = driver.find_element(By.ID,'mousehover')
action.move_to_element(menu).perform()
childmenu = driver.find_element(By.LINK_TEXT,'Reload')
action.move_to_element(childmenu).click().perform()