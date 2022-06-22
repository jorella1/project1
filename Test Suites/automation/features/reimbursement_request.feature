Feature: Employees can make requests for reimbursement by logging in. They should provide a description/reason of justification and their dollar amount of compensation up to $1000

Scenario Outline: An employeee can submit a request after logging in
    Given An employee is on the login page
    When They log in with <username> and <password> and are taken to the profile page
    When They should then enter a desired amount for reimbursement - <amount> (max 1000) as well as the description, up to 100 characters: <description>
    Then They will submit their request and be taken back to their profile page to see <amount> and <description>
    Then They will log out
    Examples:
    | username     | password   |amount     |   description          |
    |  tylerb1     |pass2       |50         |I dont feel like working|
    |  joeor1      |password1   |111        |overtime        |

