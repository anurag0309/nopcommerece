import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
global actions
# @pytest.fixture()
# def setup():
#     options = Options()
#     options.add_experimental_option("detach", True)
#     options.add_argument("--disable-notifications")
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/117 Safari/537.36")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("useAutomationExtension", False)
#     options = webdriver.EdgeOptions()
#     driver = webdriver.Edge(options=options)
#     WebDriverWait(driver, 50)
#     driver.maximize_window()
#     return driver

# If we want to run test cases in specific browser how we can do it.

def pytest_addoption(parser):
    parser.addoption('--browser',action='store', default='chrome',
                     help='Specify the browser: chrome or firefox or edge')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError('Unsupported Browser')
    return driver









#
# @pytest.fixture()
# def dict1(request1):
#     request1 = {
#         "chrome": webdriver.ChromeOptions(),
#         "edge": webdriver.EdgeOptions(),
#         "firefox": webdriver.FirefoxOptions(),}
#
# @pytest.fixture()
# def dict2(request2):
#     request2 = {
#         "chrome": webdriver.Chrome(options=options),
#         "edge": webdriver.Edge(options=options),
#         "firefox": webdriver.Firefox(options=options),
#     }
#
#
# @pytest.fixture()
# def setup(browser,dict1,dict2):
#     global option_1, driver_1
#
#     options = Options()
#     options.add_experimental_option("detach", True)
#     options.add_argument("--disable-notifications")
#     # driver = actions.get(browser)
#     print('11111111111111111111111111111111')
#     print('browser>>>>>>>>',browser)
#
#
#     #     options = webdriver.EdgeOptions()
#     #     driver = webdriver.Edge(options=options)
#
#     print('222222222222222222222222222222222222222222222')
#     option_1 = option_1.get(browser)
#     driver_1 = driver_1.get(browser)
#     option_1
#     driver_1
#     print('3333333333333333333333333333333333333333')
#     driver = driver_1
#     WebDriverWait(driver, 50)
#     driver.maximize_window()
#     return driver