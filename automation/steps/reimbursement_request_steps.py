from behave import when, then, given
from selenium.webdriver.support.select import Select

@given(u'An employee is on the login page')
def step_home_page(context):
    context.driver.get("http://127.0.0.1:5000/")
    context.Project_landing.index_login_button().click()


@when(u'They log in with {username} and {password} and are taken to the profile page')
def step_impl(context,username,password):
    context.Project_login.username_bar().send_keys(username)
    context.Project_login.password_bar().send_keys(password)
    context.Project_login.login_button().click()


@when(u'They should then enter a desired amount for reimbursement - {amount} (max 1000) as well as the description, up to 100 characters: {description}')
def step_impl(context,amount,description):
    context.Project_profile.requested_amount().send_keys(amount)
    context.Project_profile.request_description().send_keys(description)


@then(u'They will submit their request and be taken back to their profile page')
def step_impl(context):
    context.Project_profile.submit_request().click()
    context.Project_login.logout_button().click()