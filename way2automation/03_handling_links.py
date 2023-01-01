from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.wikipedia.org')

anchor_tags = driver.find_elements(By.TAG_NAME, 'a')

print(len(anchor_tags))

# for anchor_tag in anchor_tags:
#     # print(anchor_tag.text)
#     print(anchor_tag.get_attribute('href'))

# Footer block
footer_block = driver.find_element(By.XPATH, '//*[@id="www-wikipedia-org"]/div[11]')
footer_links = footer_block.find_elements(By.TAG_NAME, 'a')

print(footer_links.__getitem__(-1).text)
# for anchor_tag in footer_links:
#     print(anchor_tag.get_attribute('href')) 