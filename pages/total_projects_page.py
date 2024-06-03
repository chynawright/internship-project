from selenium.webdriver.common.by import By

from pages.base_page import Page


class TotalProjectsPage(Page):

    PROJECT = (By.CSS_SELECTOR, "[wized*='cardOfProperty']")
    ARCH = (By.CSS_SELECTOR, '[data-w-tab*="Tab 1"]')

    def click_first_product(self):
        self.wait_until_clickable_click(*self.PROJECT)







