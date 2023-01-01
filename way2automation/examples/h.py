from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.gmail.com')
driver.implicitly_wait(20)

username_input_box = driver.find_element(By.ID, 'identifierId')
username_input_box.send_keys('trainer@way2automation.com')

# 

driver.find_element(By.XPATH ,'//*[@id="identifierNext"]/div/button').click()


driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('sdfsdf')
# driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()

WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable
    ((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))
).click()
# driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[3]').click()

error_message = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[2]/div[2]').text
# error_message = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[3]').click()
print(f"{error_message}")