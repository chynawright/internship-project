from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class MainPage(Page):
    OFF_PLAN = (By.CSS_SELECTOR, '[class*="menu-twobutton"]')
    OFF_PLAN_BOTTOM = By.CSS_SELECTOR, '[class*="menu-link w-inline-block w--current"]'
    def click_off_plan(self):
        # self.wait_until_clickable_click(*self.OFF_PLAN_BOTTOM)
        self.find_element(*self.OFF_PLAN).click()