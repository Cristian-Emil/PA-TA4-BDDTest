import time

from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate_to_page()
    time.sleep(1)

@when('I click the cookie button')
def step_impl(context):
    context.login_page.click_accept_cookie()
    time.sleep(1)

@when('I insert the email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)
    time.sleep(1)

@when('I insert the password "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)
    time.sleep(1)

@when('I click the loggin button')
def step_impl(context):
    context.login_page.click_loggin()
    time.sleep(1)
git
@then('I see no account error displayed')
def step_impl(context):
    assert context.login_page.no_account_error_is_displayed(), "nu e afisat mesajul de eroare"
    # assert context.login_page.no_account_error_is_displayed()
