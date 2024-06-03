from selenium.webdriver.common.by import By

from pages.base_page import Page

class ProductPage(Page):
    ARCH = (By.CSS_SELECTOR, '[data-w-tab*="Tab 1"]')
    INT = (By.CSS_SELECTOR, '[data-w-tab*="Tab 2"]')
    LOB = (By.CSS_SELECTOR, '[data-w-tab*="Tab 3"]')
    def verify_architecture(self):
        self.wait_until_visible(*self.ARCH)
        self.wait_until_visible(*self.INT)
        self.wait_until_visible(*self.LOB)

    def verify_interior(self):
        self.wait_until_clickable_click(*self.ARCH)
        self.wait_until_clickable_click(*self.INT)
        self.wait_until_clickable_click(*self.LOB)