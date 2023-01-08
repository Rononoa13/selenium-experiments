from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://deluxe-menu.com/popup-mode-sample.html")
driver.implicitly_wait(1)

img = driver.find_element(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/p[2]/img')

action = ActionChains(driver)
action.context_click(img).perform()


product_info = driver.find_element(By.ID, 'dm2m1i1tdT')
action.move_to_element(product_info).perform()

installation = driver.find_element(By.ID, 'dm2m2i1tdT')
action.move_to_element(installation).perform()

setup = driver.find_element(By.ID, 'dm2m3i1tdT')
# action.move_to_element(setup).perform()
setup.click()
