from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave.fixture import use_fixture_by_tag
from helpers.helper_appium import get_appium
from helpers.helper_base import HelperFunc


def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)

    # Reading the browser type from the configuration file for Selenium Python Tutorial
    helper_func = get_appium(config.get('Environment', 'Appium'))
    context.helperfunc = helper_func


def after_all(context):
    context.helperfunc.close()
