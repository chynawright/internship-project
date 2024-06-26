import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from support.logger import logger
# from allure_behave.hooks import allure_report

from app.application import Application

# Run Behave tests with Allure results
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_app_ui_tests.feature


def browser_init(context, scenario_name):
    # """
    # :param context: Behave context
    # """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # MOBILE EMULATION #
    mobile_emulation = {"deviceName": "iPhone XR"}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    # options=options,
    # service=service
    # )

    # bs_user = 'chyna_1iNWTw'
    # bs_key = 'foTxpt4R8yYQnqzeczmT'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    # options = Options()
    # bstack_options = {
      #  'os': 'Windows',
       # 'osVersion': '10',
        #  'browserName': 'Chrome',
       # 'sessionName': scenario_name

   # }
  #  options.set_capability('bstack:options', bstack_options)
   # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario_name='AQA-215')


def before_step(context, step):
    logger.info(f'Step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()


# allure_report("path/to/result/dir")