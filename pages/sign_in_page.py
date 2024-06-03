from selenium.webdriver.common.by import By

from pages.base_page import Page




class SignInPage(Page):

    USERNAME = (By.ID, 'email-2')
    PASSWORD = (By.ID, 'field')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[class*=login-button w-button']")
    REELLY = 'https://soft.reelly.io/sign-in'

    def open_reelly(self):
        self.open('https://soft.reelly.io/sign-in')
    def login(self):
        self.find_element(*self.USERNAME).send_keys('chynawright06@gmail.com')
        self.find_element(*self.PASSWORD).send_keys('Freedom$99')
        self.wait_until_clickable_click(*self.LOGIN_BUTTON)
