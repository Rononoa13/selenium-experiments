from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
driver.implicitly_wait(1)

# 
def capture_screenshot(d, path):
    filename = f"{path}screenshot_{time.asctime().replace(':', '_')}.png"
    d.save_screenshot(filename)
# 
driver.switch_to.frame("iframeResult")
ele = driver.find_element(By.XPATH, "//button[text()='Try it']")
driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');", ele)

# driver.save_screenshot("/home/roronoa/Documents/Selenium-Practices/w/ay2automation/JavascriptandScreenshots/screenshots/test.png")
# driver.save_screenshot("./screenshots/test2.png")
capture_screenshot(driver, "./screenshots/")
driver.close()