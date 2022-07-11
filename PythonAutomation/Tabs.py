from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path = "E:\\Workspace\\Selenium webdriver\\chromedriver.exe")
driver.get('https://the-internet.herokuapp.com/windows')
print(driver.find_element(By.TAG_NAME,'h3').text)
driver.find_element(By.XPATH,'//*[contains(@href,"/windows/new")]').click()
childwindow = driver.window_handles[1]

driver.switch_to.window(childwindow)
print(driver.find_element(By.TAG_NAME, 'h3').text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
assert 'opening a new window'== driver.find_element(By.TAG_NAME, 'h3').text
