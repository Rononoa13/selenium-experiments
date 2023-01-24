from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
# driver.implicitly_wait(4)
#  
driver.find_element(By.XPATH, "//input[@value='Sign in']").click()

alert = Alert(driver)
time.sleep(2)
print(alert.text)
alert.accept()