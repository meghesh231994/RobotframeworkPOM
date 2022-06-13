*** Settings ***
Library     SeleniumLibrary



*** Keywords ***
launching browser
    [Arguments]    ${url}    ${browserName}
    open browser    ${url}    ${browserName}
    set selenium implicit wait    10 seconds
    log title

Finish test case
    Log    Ending the test cases
    Close Browser


