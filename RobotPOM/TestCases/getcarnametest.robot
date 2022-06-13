*** Settings ***
Library     SeleniumLibrary
Resource    ../PageObjects/HomePage.robot
Resource    ../Resources/Commons.robot
Resource    ../PageObjects/Newcarpage.robot
Resource    ../PageObjects/toyotacarPage.robot
Resource    ../PageObjects/carbasepage.robot
Library     DataDriver      ../Resources/testdata.xlsx      sheet_name=Sheet1

Test Template       find new cars
Test Teardown       Finish test case


*** Variables ***
${testsiteurl}=     https://www.carwale.com/

*** Test Cases ***
find new cars ${Brandname}      ${Browser}         ${Brandname}        ${carheading}

*** Keywords ***
find new cars
    [Arguments]     ${Browser}      ${Brandname}    ${carheading}
    launching browser    ${testsiteurl}     ${Browser}
    Go to new car page
    IF    "${Brandname}" == "toyota"
        Go to toyota
    ELSE IF    "${Brandname}" == "kia"
        Go to Kia
    END
    Verify car heading    ${carheading}
    get car name
    Sleep    2



##    Go to toyota
##    Verify car heading    Toyota Cars
#    Go to Kia
#    Verify car heading    Kia Cars
#    Sleep    3





