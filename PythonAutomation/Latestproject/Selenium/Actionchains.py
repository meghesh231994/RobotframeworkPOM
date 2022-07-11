from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

ser = Service("E:/Workspace/Selenium webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")

butt = driver.find_element(By.XPATH,'//*[@id="authentication"]/button')
act = ActionChains(driver)
act.double_click(butt).perform()

a = driver.switch_to.alert
print(a.text)
a.accept()