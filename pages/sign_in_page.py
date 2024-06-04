from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page
from time import sleep




class SignInPage(Page):

    USERNAME = (By.ID, 'email-2')
    PASSWORD = (By.ID, 'field')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[wized*='loginButton']")

    def open_reelly(self):
        self.open('https://soft.reelly.io/sign-in')

    def email(self, email):
        self.input_text(email,*self.USERNAME)

    def password(self, password):
        self.input_text(password, *self.PASSWORD)


    def login(self):
        self.wait_until_clickable_click(*self.LOGIN_BUTTON)
