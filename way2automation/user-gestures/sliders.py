from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://jqueryui.com/resources/demos/slider/default.html")
driver.implicitly_wait(1)

slider = driver.find_element(By.XPATH, '//*[@id="slider"]/span')

action = ActionChains(driver)
action.drag_and_drop_by_offset(slider, 400 ,0).perform()
