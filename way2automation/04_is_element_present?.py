from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.remote.errorhandler import ErrorCode

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# def is_element_present(id):
#     try:
#         driver.find_element(By.ID, id)
#         return True
#     except NoSuchElementException:
#         return False

# def is_element_present(how, what):
#     try:
#         driver.find_element(how, what)
#         return True
#     except NoSuchElementException:
#         return False

def is_element_present(how, what):
	if len(driver.find_elements(how, what)) == 0:
		return False
	else:
		return True

driver = webdriver.Chrome(options=options)
driver.get('https://www.gmail.com')
driver.implicitly_wait(2)

# print(driver.find_element(By.ID, 'identifierId').is_displayed())
# print(is_element_present('identifierId'))
print(is_element_present(By.ID, 'identifierId'))