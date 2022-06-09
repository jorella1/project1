from behave import when, then, given
from selenium.webdriver.support.select import Select

@given(u'I am on the project homepage')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5000/login")

@when(u'I enter {username} and {password}')
def step_impl(context, username, password):
    context.Project_login.username_bar().send_keys(username)
    context.Project_login.password_bar().send_keys(password)

""" @when(u'I enter ')
def step_impl(context, password):
    context.project_login.password_bar().send_keys(password) """

@when(u'I click the submit button')
def step_impl(context):
    context.Project_login.submit_button().click()

@then(u'I should be directed to the employee profile page with {title}')
def step_impl(context, title):
    assert context.driver.title == title

@then(u'I should be able to logout')
def step_impl(context):
    context.Project_login.logout_button().click()