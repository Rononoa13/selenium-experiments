from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
driver.implicitly_wait(2)
#
driver.switch_to.frame("iframeResult")
try_button = driver.find_element(By.XPATH, "//button[text()='Try it']").click()
 