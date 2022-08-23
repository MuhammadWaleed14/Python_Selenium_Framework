import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils.utilities import Utilities

obj_utils = Utilities()


def pytest_bdd_before_scenario():
    str_browser = obj_utils.read_config("browser")
    if str_browser == "chrome":
        browseroptions = webdriver.ChromeOptions()
        browseroptions.add_argument("start-maximized")
        pytest.driver = webdriver.Chrome(pytest.project_root + "/browsers/chromedriver.exe", options=browseroptions)
    elif str_browser == "firefox":
        str_firefox_binary = str(obj_utils.read_config("firefox_binary"))
        ffoptions = Options()
        ffoptions.binary_location = str_firefox_binary
        ffoptions.add_argument("start-maximized")
        pytest.driver = webdriver.Firefox(executable_path=pytest.project_root + r"/browsers/geckodriver.exe", options=ffoptions)


def pytest_bdd_after_scenario():
    pytest.driver.quit()


@pytest.fixture(scope='session', autouse=True)
def project_root():
    pytest.project_root = os.path.dirname(os.path.abspath(__file__))