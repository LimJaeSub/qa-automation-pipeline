from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    URL = "https://automationexercise.com/products"
    
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='search_product']")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[id='submit_search']")
    RESULTS = (By.CSS_SELECTOR, ".productinfo")
    
    def open(self):
        self.driver.get(self.URL)
    
    def search(self, keyword):
        self.type(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BTN)

    def get_results(self):
        try:
            self.find(self.RESULTS)
            return self.driver.find_elements(*self.RESULTS)
        except:
            return []