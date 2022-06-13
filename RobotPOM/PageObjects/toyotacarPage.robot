*** Settings ***
Library     SeleniumLibrary
Variables       ../Resources/locators.py


*** Keywords ***
Verify toyota car heading
    [Arguments]     ${carheading}
    Element Text Should Be    ${toyota_text}    ${carheading}