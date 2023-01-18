from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
from booking.booking_filtration import BookingFiltration
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

class Booking:

    def __init__(self, driver, teardown=False):
        self.driver = driver
        self.teardown = teardown
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # super().__init__()

    def __enter__(self):
        # print('enter method called')
        # self.driver.get(const.BASE_URL)
        return self

    def __exit__(self, exc_type, exc_value, exc_tracebacklf):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)
        
    def change_currency(self, currency=None):
        # Css selector for currency in nav bar.
        # currency_element = self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
        
        # XPATH for currency in nav bar.
        currency_element = self.driver.find_element(By.XPATH, '//*[@id="b2indexPage"]/header/nav[1]/div[2]/div[1]/button')
        currency_element.click()

        # changee currency from function arguement 
        select_currency_element = self.driver.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param="changed_currency=1&selected_currency={currency}&top_currency=1"]')
        select_currency_element.click()

    def select_place_to_go(self, place_to_go):
        # 
        search_field_element = self.driver.find_element(By.NAME, "ss")
        search_field_element.clear()
        search_field_element.send_keys(place_to_go)
        first_result = self.driver.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()
    
    def select_date(self, check_in, check_out):
        check_in_element = self.driver.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in}"]')
        check_in_element.click()

        check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        select_element = self.driver.find_element(By.ID, 'xp__guests__toggle')
        select_element.click()

        while True:
            decrease_adult_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
            decrease_adult_element.click()

            # If value of adult count reaches 1
            # Get out of while loop
            count_adult_element = self.driver.find_element(By.ID, 'group_adults')
            count_adult_element = count_adult_element.get_attribute('value') #Should return 1
            # print(count_adult_element.get_attribute('value'))

            if int(count_adult_element) == 1:
                break

        increase_adult_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')

        for _ in range(count-1):
            increase_adult_element.click()

    def click_search(self):
        search_button_element = self.driver.find_element(By.CSS_SELECTOR, "button[type='Submit']")
        search_button_element.click()

    
    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(star_value=3)





