from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import alert

ser = Service("E:/Workspace/Selenium webdriver/lat/chromedriver.exe")

driver = webdriver.Chrome(service=ser)

driver.get('https://demo.guru99.com/test/simple_context_menu.html')

cli = driver.find_element(By.XPATH,'//*[text()="Double-Click Me To See Alert"]')
act = ActionChains(driver)
act.double_click(cli).perform()

al = alert.driver.switch_to.alert
al.text()
al.accept()