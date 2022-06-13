*** Settings ***
Resource    ../PageObjects/HomePage.robot
Resource    ../Resources/Commons.robot
Resource    ../PageObjects/Newcarpage.robot
Resource    ../PageObjects/toyotacarPage.robot
Resource    ../PageObjects/carbasepage.robot
Test Teardown       Finish test case


*** Variables ***
${testsiteurl}=     https://www.carwale.com/


*** Test Cases ***
find new car test
    launching browser    ${testsiteurl}        Chrome
    Go to new car page
#    Go to toyota
#    Verify car heading    Toyota Cars
    Go to Kia
    Verify car heading    Kia Cars
    Sleep    3





