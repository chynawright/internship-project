from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.sign_in_page import SignInPage
from pages.base_page import Page
from pages.total_projects_page import TotalProjectsPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.sign_in_page = SignInPage(driver)
        self.main_page = MainPage(driver)
        self.total_projects_page = TotalProjectsPage(driver)
        self.product_page =ProductPage(driver)

