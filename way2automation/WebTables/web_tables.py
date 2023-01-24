from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
# from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.nba.com/standings")
driver.implicitly_wait(3)


WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.ID, "onetrust-accept-btn-handler")
    )
).click()

eastern_conf_block = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/section[2]/div/div[2]/div[2]/table')
rows = eastern_conf_block.find_elements(By.XPATH, '//tbody/tr')
total_rows = len(rows)
# total_rows = total_rows / 


cols = eastern_conf_block.find_elements(By.XPATH, "//tbody/tr[1]/td")
total_cols = len(cols)
# total_cols = total_cols / 2

print(f"Total rows are: {total_rows} and total columns are: {total_cols}")

# while True:
#     try:
#         for row in rows:
#             print(row.text)
#     except StaleElementReferenceException:
#         print(f"stale element reference: element is not attached to the page document")
        
# print(f"----------------- Second Way -------------------")

# start_xpath = "//tbody/tr["
# mid_xpath = "]/td["
# end_xpath = "]"

# for row in range(1, total_rows+1):
#     for col in range(1, total_cols + 1):
#         # print(f"{start_xpath}{str(row)}{mid_xpath}{str(col)}{end_xpath}")
#         print(driver.find_elements(By.XPATH, f"{start_xpath}{str(row)}{mid_xpath}{str(col)}{end_xpath}"))
