# Test Strategy

## Scope
The Reimbursement Managment System is a simple reimbursement request tool. Testing will begin at the start of development on 6/6 and we plan to have unit testing finished by 6/10. The rest of testing we plan to finish before the release of the application on 6/17. 


## Test Approach
The testing is divided into 3 main categories, Unit Testing, Automation Testing, and API testing. 

    Unit Testing:
    All methods with user input will be tested with pytest in order to ensure all inputs will be valid. All Login and Request reimbursement methods will be extensively tested for input validation. 

    Automation Testing:
    Services will be tested with full automation with Selenium and Behave. Feature files for each user story and acceptance criteria will be included with full end to end tests. Each scenario will include at least positive test and multiple negative tests. 
   
    API Testing:
    Postman tests will be run on each HTTP request called in app.py. This will include one positive test and multiple failures for each method. Happy path testing with full features for each user story will be conducted as well. 

Task Distribution:
Anthony will be handling the majority of the Unit Testing.
The automation testing will be split between John and Anthony. 
Postman testing...


## Test Environment
All username/password entries were added to the database for testing. 

## Testing Tools
    Unit Testing: Python and Pytest
    Automation Testing: Selenium/Behave
    API Testing: Postman
    
    These test suites can be found in the Test Suites folder

## Release Control
    #TODO
## Risk Analysis
    The method in which Flask-Login handles sessions means that the user must completely close the browser window in order to logout or end their
    session if the user does not explicity log out. If a manager were being neglegent, an unauthorized user could access the manager's account if
    the manager had just closed out a tab without logging out and manipulate reimbursement requests without the manager's knowlege.
## Review and Approvals
    #TODO

