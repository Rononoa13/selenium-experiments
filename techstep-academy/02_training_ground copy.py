from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

baseURL = 'https://techstepacademy.com'
driver = webdriver.Chrome(options=options)
driver.get(f"{baseURL}/training-ground")

print(f"I have arrived")
WebDriverWait(driver, 10).until(alert_is_present())
print(f"An alert appeared.")