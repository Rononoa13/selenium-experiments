# selenium.webdriver.support.select API

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://echoecho.com/htmlforms11.htm')

# dropdown = driver.find_element(By.NAME, 'dropdownmenu').send_keys('Cheese')
dropdown = driver.find_element(By.NAME, 'dropdownmenu')
dropdown = Select(dropdown)

dropdown.select_by_index(1)
dropdown.select_by_visible_text('Milk')
