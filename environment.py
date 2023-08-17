import time

from driver import Driver
from pages.login_page import LoginPage


def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
time.sleep(1)


def after_all(context):
    context.browser.close_pyta()
time.sleep(1)