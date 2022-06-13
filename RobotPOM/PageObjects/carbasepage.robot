*** Settings ***
Library     SeleniumLibrary
Variables       ../Resources/locators.py



*** Keywords ***
Verify car heading
    [Arguments]     ${carheading}
    Element Text Should Be    ${carheading_xpath}    ${carheading}

get car name
    @{carnames}=    Get WebElements    ${carnames_xpath}
    
    FOR    ${carname}    IN    @{carnames}
        ${text}=    Get Text    ${carname}
        Log To Console    ${text}
    END