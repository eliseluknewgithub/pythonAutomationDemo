from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HelperFunc(object):
    __TIMEOUT = 50

    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self.driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def maximize(self):
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def find_by_xpath(self, xpath):
        return self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    # def find_by_name(self, name):
    #     return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self.driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    # def scrollToLeft(self, element1, element2):
    #     self.driver.execute_script("mobile: scroll",
    #                                {"direction": "left", 'element': element1,
    #                                 'toVisible': element2})

    def scrollToRight(self, element1):
        self.driver.execute_script("mobile: scroll",
                                   {"direction": "right", 'element': element1})



    def tapAction(self,element,x,y):
        action = TouchAction(self.driver)
        action.tap(element, x, y).perform()