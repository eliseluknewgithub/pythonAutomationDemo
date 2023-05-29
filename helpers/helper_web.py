from selenium import webdriver
from helpers.helper_base import HelperFunc


def get_browser(browser):
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome())
    elif browser == "firefox":
        return HelperFunc(webdriver.Firefox())
    elif browser == "edge":
        return HelperFunc(webdriver.Edge())
    elif browser == "ie":
        return HelperFunc(webdriver.Ie())