from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

baseURL = 'https://techstepacademy.com'
driver = webdriver.Chrome(options=options)
driver.get(f"{baseURL}/trial-of-the-stones")

# Riddle of Stones
stone_input = "//input[@id='r1Input']"
answer_button = "//button[@id='r1Btn']"
stone_input_box = driver.find_element(By.XPATH, stone_input)
stone_input_box.send_keys("rock")
stone_answer_button = driver.find_element(By.XPATH, answer_button)
stone_answer_button.click()

# Riddle of Secrets
secret_input = "//input[@id='r2Input']" #Input box for riddle of secrets
answer_button = "//button[@id='r2Butn']" #Answer button for riddle of secrets
secret_input_box = driver.find_element(By.XPATH, secret_input)
# answer = "//div[@id='passwordBanner']/h4"
# answer_riddle_stone = driver.find_element(By.XPATH, answer)
# password = answer_riddle_stone.text

answer = "div#passwordBanner > h4"
answer_riddle_stone = driver.find_element(By.CSS_SELECTOR, answer)
password = answer_riddle_stone.text

secret_input_box.send_keys(password)

secrets_answer_button = driver.find_element(By.XPATH, answer_button)
secrets_answer_button.click()

#  The two merchants
first_merchant_xPath = '//p[contains(text(),"3000")] /../span'
merchant_input_box = driver.find_element(By.ID, 'r3Input')
first_merchant = driver.find_element(By.XPATH, first_merchant_xPath)
first_merchant_name = first_merchant.text

# print(first_merchant_name)
merchant_input_box.send_keys(first_merchant_name)

merchant_answer_element = "r3Butn"
merchant_answer_button = driver.find_element(By.ID, merchant_answer_element)
merchant_answer_button.click()

# Check answer
check_answer = 'checkButn'
check_answer_button = driver.find_element(By.ID, check_answer)
check_answer_button.click()

# ?Final  trial
trial_message = 'trialCompleteBanner'
trial_message_ = driver.find_element(By.ID, trial_message)
trial_message_.text

assert trial_message_.text == 'Trial Complete'