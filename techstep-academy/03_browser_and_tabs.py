from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options)
# driver2 = webdriver.Chrome(options=options)

driver.get(f"https://techstepacademy.com")
# driver2.get(f"https://www.google.com")
driver.execute_script('window.open("https://techstepacademy.com/training-ground", "_blank");')
driver.execute_script('window.open("https://www.google.com", "_blank");')
driver.execute_script('window.open("https://amazon.com","_blank")')

