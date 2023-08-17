import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    # _URL="https://www.zooplus.ro/account"
    _URL = "https://www.zooplus.ro/checkout/login?notLoggedIn=true"
    EMAIL_INPUT= (By.ID, "customerEmail")
    PASSWORD_INPUT = (By.ID, "customerPassword")
    LOGGIN_BUTTON = (By.XPATH, "//span[text()='Intră în cont']")
    # LOGIN_BUTTON= (By.CLASS_NAME, "button_group")                             # varianta 2, cea cu XPATH
    COOKIE_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    NO_ACCOUNT_ERROR = (By.XPATH, "//div[@data-zta='SSOLoginErrorMessage'][@aria-hidden='false']")
    # NO_ACCOUNT_ERROR = (By.XPATH,"//p[text()='Datele de logare introduse nu sunt corecte. Vă rugăm verificați și încercați din nou.']")
    # NO_ACCOUNT_ERROR= (By.XPATH, "//div.v3-notification__text[text()='Datele de logare introduse nu sunt corecte.Va rugam verificati si introduceti din nou ']")

    print("f1")
    def navigate_to_page(self):
        self.driver.get(self._URL)
        time.sleep(1)

    print("f2")
    def click_accept_cookie(self):
        self.click(locator=self.COOKIE_BUTTON)
        time.sleep(4)

    print("f3")
    def set_email(self, email):
        self.type(locator=self.EMAIL_INPUT, text=email)
        time.sleep(2)

    print("f4")
    def set_password(self,password):
        # self.type(text=password, locator=self.PASSWORD_INPUT)          # schimbam elementele intre ele si nu avem efect
        self.type(locator= self.PASSWORD_INPUT, text= password)
        time.sleep(1)

    print("f5")
    def click_loggin(self):
        self.click(locator=self.LOGGIN_BUTTON)
        time.sleep(1)

    print("f6")
    def no_account_error_is_displayed(self):
        return self.is_displayed(self.NO_ACCOUNT_ERROR)
