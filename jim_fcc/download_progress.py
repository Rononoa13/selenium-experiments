from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.globalsqa.com/demoSite/practice/progressbar/download.html')

driver.implicitly_wait(3)
download_button = driver.find_element(By.ID, 'downloadButton')
download_button.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), # Element Filteration
        'Complete!' # The expected text
    )
)