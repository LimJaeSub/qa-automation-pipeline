from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://automationexercise.com/login"

    EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    def open(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)