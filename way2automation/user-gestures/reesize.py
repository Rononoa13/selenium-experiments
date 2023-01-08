from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://jqueryui.com/resources/demos/resizable/default.html")
driver.implicitly_wait(1)

resizable = driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
action = ActionChains(driver)
action.drag_and_drop_by_offset(resizable, 100, 100).perform()