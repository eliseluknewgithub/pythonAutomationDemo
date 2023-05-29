import time

from appium.webdriver.common.touch_action import TouchAction
from behave import given, when, then
from Utitlities.scrollUtil import swipeLeft


@given(u'I click allow button')
def step_impl(context):
    context.helperfunc.find_by_xpath("//XCUIElementTypeButton[@name='Allow']").click()


@then(u'I click HK button')
def step_impl(context):
    context.helperfunc.find_by_xpath("//XCUIElementTypeButton[@name='splash btn hk en']").click()


@given('I am on the scrollable page in IOS')
def onPage1(context):
    time.sleep(40)
    print("I am on the scrollable page")


@then('I scroll the view from right to left in IOS')
def scroll(context):
    time.sleep(2)
    # for i in range(1, 4):
    #     context.helperfunc.driver.swipe(900, 600, 200, 600, 1000)
    # context.helperfunc.find_by_xpath("//XCUIElementTypeApplication[@name='Pizza Hut']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView").send_keys("0.5").send_keys("0.5").send_keys("0.5")

    element1 = context.helperfunc.find_by_xpath(
        "//XCUIElementTypeApplication[@name='Pizza Hut']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView")

    context.helperfunc.scrollToRight(element1)

    context.helperfunc.scrollToRight(element1)

    context.helperfunc.scrollToRight(element1)


@then('I click Start button in IOS')
def clickStart(context):
    context.helperfunc.find_by_xpath("//XCUIElementTypeButton[@name='walk btn start en']").click()


@given('Open Side Menu in IOS')
def openSideMenu(context):
    print("I am on the Side Menu")


@when('I click the Avatar to open Login page in IOS')
def step_impl(context):
    context.helperfunc.find_by_xpath(
        "//XCUIElementTypeApplication[@name='Pizza Hut']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton").click()
    context.helperfunc.find_by_xpath(
        "//XCUIElementTypeApplication[@name='Pizza Hut']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther").click()


@when('I submit the following credentials to login in IOS')
def step_impl(context):
    for row in context.table:
        context.helperfunc.find_by_xpath(
            "//XCUIElementTypeApplication[@name='Pizza Hut']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeTextField").clear().send_keys(
            row['Username'])
        context.helperfunc.find_by_xpath(
            "//XCUIElementTypeApplication[@name='Pizza Hut']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField").clear().send_keys(
            row['Password'])
        context.helperfunc.find_by_xpath("//XCUIElementTypeButton[@name='general btn alert confirm en']").click()
        try:
            # context.helperfunc.find_by_xpath("//XCUIElementTypeButton[@name='general btn alert confirm en']").click()
            context.helperfunc.tapAction(context.helperfunc.find_by_xpath(
                "//XCUIElementTypeApplication[@name='Pizza Hut']/XCUIElementTypeWindow[1]"), 225, 475)
        except:
            print("element not exist")
