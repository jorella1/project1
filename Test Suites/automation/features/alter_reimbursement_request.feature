Feature: A manger is able to alter an employee's reimbursement request

    Scenario Outline: From the menu a manager is able to select a request ID an accept or deny it
    Given A manager is on the profile page
    Then They enter a valid pending request ID - <requestid> and choose to accept or deny it - <choice> and will be returned to their profile page with an updated list of reimbursement requests

    Examples:
    |requestid  |   choice  |
    |58         |   decline |
    |58         |   accept  |
