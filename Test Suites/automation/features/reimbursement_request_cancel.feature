Feature:cancel reimbursement requests
    Scenario Outline: On their profile page an employee can cancel any of their posted reimbursement requests.
        Given An employee is on the profile page with a request pending <amount> <description>
        Then They are able to cancel their request and not see <amount> and <description>
        Then They will then log out
        
        
        Examples:
        |amount     |   description          |
        |50         |I dont feel like working|
        |100        |8 hours overtime        |
