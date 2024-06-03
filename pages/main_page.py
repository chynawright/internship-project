from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    OFF_PLAN = (By.CSS_SELECTOR, '[class*="menu-twobutton"]')
    def click_off_plan(self):
        self.find_element(*self.OFF_PLAN).click()