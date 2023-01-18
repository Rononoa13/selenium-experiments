"""
#
#
"""
# from typing import 
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    
    def __init__(self, driver:WebDriver, teardown=False) -> None:
        self.driver = driver
        self.teardown = teardown

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tracebacklf):
        if self.teardown:
            self.driver.quit()

    def apply_star_rating(self, star_value):
        star_filtration_box_element = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        star_filtration_box_element = star_filtration_box_element[0]
        # print(star_filtration_box_element)

        # star_child_elements = star_filtration_box_element.find_elements(By.CSS_SELECTOR,"*")
        # print(len(star_child_elements)) 
        star_filtration_box = star_filtration_box_element.find_elements(By.CSS_SELECTOR, f"input[name='class={star_value}']")
        # print(len(star_filtration_box))
        
        
        for star_element in star_filtration_box:
            # star_filtration_box_element.find_elements(By.CSS_SELECTOR, f"input[name='class={star_value}']")
            star_element.click()



