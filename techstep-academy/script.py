from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get('https://techstepacademy.com/training-ground')

input_element = browser.find_element(By.CSS_SELECTOR, 'input#ipt1')
input_element.send_keys('Test')

button_element = browser.find_element(By.NAME, "butn1")
button_element.click()



#Switch the control to the Alert window
obj = browser.switch_to.alert
#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )
#use the accept() method to accept the alert
obj.accept()
print(" Clicked on the OK Button in the Alert Window")

# 
second_button = browser.find_element(By.CSS_SELECTOR, 'button#b2')
second_button.click()
obj = browser.switch_to.alert
obj.accept()

# 
input_element = browser.find_element(By.CSS_SELECTOR, 'input#ipt2')
input_element.send_keys('Second Automation')

