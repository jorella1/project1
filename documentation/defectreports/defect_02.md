## Defect Report

### ID
    002
### Release
    6/14
### Summary
    Request validation not working
### Description
    Submission of a request with higher than 2 decimal places are being accepted
### Steps to Replicate
    Login as either manager or employee. Submit a request of 100.111 dollars.
### Actual Result
    Account page flash: "reimbursement request successfully submitted."
### Expected Result
    Account page flash: "please enter a correct dollar amount"
### Status
    Fixed
### Notes
    validation service methods were not being called in request service