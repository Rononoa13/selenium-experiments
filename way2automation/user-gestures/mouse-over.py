from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("http://way2automation.com")
driver.implicitly_wait(1)

# //*[@id="menu-item-27617"]/a
# '//*[@id="menu-item-27617"]/a/span[2]
resource_tab = driver.find_element(By.XPATH, '//*[@id="menu-item-27617"]/a')

action = ActionChains(driver)
action.move_to_element(resource_tab).perform()

practice_site_link = driver.find_element(By.XPATH, '//*[@id="menu-item-27619"]/a/span[2]').click()