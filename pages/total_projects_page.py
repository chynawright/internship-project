from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class TotalProjectsPage(Page):

    PROJECT = (By.CSS_SELECTOR, "[wized*='cardOfProperty']")
    PROJECT_TWO = (By.CSS_SELECTOR, "[w-el-class*='project-card w-inline-block']")
    MENU = (By.CSS_SELECTOR, "[class='menu-mobile hero-menu']")
    OFF_PLAN_BOTTOM = (By.CSS_SELECTOR, '[class*="menu-link w-inline-block w--current"]')


    def click_first_product(self):
        self.wait_until_clickable_click(*self.PROJECT)








