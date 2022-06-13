*** Settings ***
Library     SeleniumLibrary
Variables       ../Resources/locators.py

*** Keywords ***
Go to toyota
    Click Element    ${toyota_xpath}

Go to Kia
    Click Element    ${kia_xpath}