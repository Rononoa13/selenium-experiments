from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

def is_element_present(how, what):
    try:
        driver.find_element(how, what)
        return True
    except NoSuchElementException:
        return False

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(1)

driver.get('http://www.tizag.com/htmlT/htmlcheckboxes.php')
# sport_checkbox = driver.find_element(By.XPATH, '//div[4]/input[1]')
# sport_checkbox.click()
# i = 1

# while is_element_present(By.XPATH, f"//div[4]/input[{str(i)}]"):
#     driver.find_element(By.XPATH, f"//div[4]/input[{str(i)}]").click()
#     i += 1
# driver.find_element(By.XPATH, '//div[4]/input[2]').click()
# driver.find_element(By.XPATH, '//div[4]/input[3]').click()
# driver.find_element(By.XPATH, '//div[4]/input[4]').click()

# checkboxes = driver.find_elements(By.NAME, 'sports')
# for checkbox in checkboxes:
#     checkbox.click()

checkbox_block = driver.find_element(By.XPATH, '//td/div[4]')

checkboxes = checkbox_block.find_elements(By.NAME, 'sports')
for checkbox in checkboxes:
    checkbox.click()