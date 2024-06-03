from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ARCH = (By.CSS_SELECTOR, '[data-w-tab*="Tab 1"]')
INT = (By.CSS_SELECTOR, '[data-w-tab*="Tab 2"]')
LOB = (By.CSS_SELECTOR, '[data-w-tab*="Tab 3"]')


@given('Open the main page')
def open_reelly(context):
    context.app.sign_in_page.open_reelly()


@when('Log in to the page')
def login(context):
    #context.app.sign_in_page.login()
    context.driver.find_element(By.ID, 'email-2').send_keys('chynawright06@gmail.com')
    context.driver.find_element(By.ID, 'field').send_keys('Freedom$99')
    context.driver.find_element(By.CSS_SELECTOR, "[class*='login-button w-button']").click()


@when('Click “off plan” on the left side of the menu')
def click_off_plan(context):
    #context.driver.find_element(By.CSS_SELECTOR, '[class*="menu-twobutton"]').click()
    context.app.main_page.click_off_plan()


@when('Click on the first product')
def click_first_product(context):
    # context.driver.find_element(By.CSS_SELECTOR, "[wized*='cardOfProperty']").click()
    context.app.total_projects_page.click_first_product()


@then('Verify the three options of visualization are “architecture”, “interior”, “lobby”')
def verify_architecture(context):
    context.app.product_page.verify_architecture()
    # context.wait.until(EC.presence_of_element_located(ARCH))
    # context.wait.until(EC.presence_of_element_located(INT))
    # context.wait.until(EC.presence_of_element_located(LOB))


@then('Verify the visualization options are clickable')
def verify_interior(context):
    context.app.product_page.verify_interior()
    # context.wait.until(EC.element_to_be_clickable(ARCH)).click()