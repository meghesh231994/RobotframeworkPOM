*** Settings ***
Library     SeleniumLibrary
Variables       ../Resources/locators.py

*** Keywords ***
Go to new car page
    Maximize Browser Window
    Wait Until Element Is Visible    ${newcar_xpath}
    Sleep    2
    Mouse Over          ${newcar_xpath}
    Sleep    2
    Click Element       ${findnewcarxpath}
    Element Text Should Be    ${newcar_header_xpath}        New Cars