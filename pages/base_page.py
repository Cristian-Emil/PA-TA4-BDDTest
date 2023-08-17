
from driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

class BasePage(Driver):

    def click(self, locator):
        self.driver.find_element(*locator).click()

        # self.driver.find_element("container_selector").find_element("details_locator").find_element("find_title_locator)

    def type(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)


    def is_displayed(self,locator) -> bool:
        return self.wait_for_element(locator,3).is_displayed()
        # self.wait_for_element(locator,3).is_enabled()
        # self.driver.find_element(*locator, self.is_displayed)


    def wait_for_element(self, locator, wait_time) -> WebElement:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.visibility_of_element_located(locator))
        # return wait.until(EC.presence_of_element_located(locator))
