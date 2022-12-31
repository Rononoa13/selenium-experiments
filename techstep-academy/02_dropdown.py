from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

baseURL = 'https://techstepacademy.com'
driver = webdriver.Chrome(options=options)
driver.get(f"{baseURL}/training-ground")
driver.implicitly_wait(5)

sel1 = driver.find_element(By.NAME, 'mySelect')
my_selection = Select(sel1)
