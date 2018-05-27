from configparser import ConfigParser
from selenium import webdriver
import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def config():
    os.chdir("..")
    config_file_path = os.path.abspath('config.ini')
    parser = ConfigParser()
    parser.read(config_file_path)
    return parser


@pytest.fixture(scope='function')
def driver(request, config):
    if config['SELENIUM']['webdriver'] == 'chrome':
        driver = webdriver.Chrome(config['SELENIUM']['location'])

    def fin():
        print("\nClosing webdriver")
        driver.close()
    request.addfinalizer(fin)
    return driver