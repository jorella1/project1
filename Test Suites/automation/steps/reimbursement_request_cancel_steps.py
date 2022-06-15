from behave import when, then, given
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

@given(u'An employee is on the profile page with a request pending {amount} {description}')
def step_home_page(context, amount, description):
    context.driver.get("http://127.0.0.1:5000/login")
    context.Project_login.username_bar().send_keys("jorell")
    context.Project_login.password_bar().send_keys("password")
    context.Project_login.login_button().click()
    context.Project_profile.requested_amount().send_keys(amount)
    context.Project_profile.request_description().send_keys(description)
    context.Project_profile.submit_request().click()

@then(u'They are able to cancel their request and not see {amount} and {description}')
def step_impl(context, amount, description):
    context.Project_profile.cancel_request_button().click()
    assert not amount or description in context.driver.find_element(By.ID, "curr_table").text

@then(u'They will then log out')
def step_impl(context):
    context.Project_login.logout_button().click()
