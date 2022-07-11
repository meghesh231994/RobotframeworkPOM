
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.service import Service

serv = Service("E:/Workspace/Selenium webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.get("https://www.goibibo.com/")


