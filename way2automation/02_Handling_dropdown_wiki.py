# selenium.webdriver.support.select API

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.wikipedia.org')

# Wiki dropdown example 
# elements because <select> has many option elements.
options = driver.find_elements(By.TAG_NAME, 'option')

for option in options:
    print(option.text)
    print(option.get_attribute("lang"))

print(f"Total value is ", {len(options)})