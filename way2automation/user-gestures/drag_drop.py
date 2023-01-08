from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.implicitly_wait(1)

dragable = driver.find_element(By.ID, 'draggable')
droppable = driver.find_element(By.ID, 'droppable')

action = ActionChains(driver)
action.drag_and_drop(dragable, droppable).perform()
# action.drag_and_drop_by_offset(dragable, 300, 300).perform()