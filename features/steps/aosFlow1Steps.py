import time

from behave import given, when, then
from Utitlities.scrollUtil import swipeLeft


@given('I click HK button')
def clickHKButton(context):
    context.helperfunc.find_by_id("com.pizzahut.app:id/hk_btn").click()



@given('I am on the scrollable page')
def onPage1(context):
    time.sleep(100)
    print("I am on the scrollable page")


@then('I scroll the view from right to left')
def scroll(context):
    # swipeLeft(3, context.helperfunc.driver)
    for i in range(1, 4):
        context.helperfunc.driver.swipe(900, 600, 200, 600, 1000)


@then('I click Start button')
def clickStart(context):
    context.helperfunc.find_by_id("com.pizzahut.app:id/btnStart").click()


@given('Open Side Menu')
def openSideMenu(context):
    print("I am on the Side Menu")


@when('I click the Avatar to open Login page')
def step_impl(context):
    context.helperfunc.find_by_id("com.pizzahut.app:id/imgMenu").click()
    context.helperfunc.find_by_id("com.pizzahut.app:id/imgProfile").click()


@when('I submit the following credentials to login')
def step_impl(context):
    for row in context.table:
        context.helperfunc.find_by_id("com.pizzahut.app:id/txtAccountName").send_keys(row['Username'])
        context.helperfunc.find_by_id("com.pizzahut.app:id/txtPw").send_keys(row['Password'])
        context.helperfunc.find_by_id("com.pizzahut.app:id/btnLogin").click()
        try:
            context.helperfunc.find_by_id("com.pizzahut.app:id/btnAlertPositive").click()
        except:
            print("element not exist")


