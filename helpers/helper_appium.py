from appium import webdriver
# from selenium import webdriver
from helpers.helper_base import HelperFunc


def get_appium(appiumDriver):
    if appiumDriver == "aos":
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android'
        desired_caps['appPackage'] = 'com.pizzahut.app'
        desired_caps['appActivity'] = 'com.gt.android.app.controller.core.SplashActivity'
        desired_caps['newCommandTimeout'] = 200
        desired_caps['noReset'] = True
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return HelperFunc(driver)

    elif appiumDriver == "ios":
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '13.3'
        desired_caps['deviceName'] = 'iPhone 11 Pro Max'
        # desired_caps['udid'] = '40545022-FD58-4311-B28A-B4EADB417E17'
        # desired_caps['bundleId'] = 'com.rahul.IntegrationApp'
        desired_caps['newCommandTimeout'] = 100
        desired_caps['app'] = '/Users/eliseluk/Desktop/PizzaHut_iOS_Sim_CRM_UAT.zip'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return HelperFunc(driver)
