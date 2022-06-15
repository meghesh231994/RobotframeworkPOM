*** Settings ***

Library    Collections
Library    RequestsLibrary
Library    String
Library    ../custom/Ra.py
Library     SeleniumLibrary


*** Variables ***
${base_url}     https://rahulshettyacademy.com/
${id}
${book_name}     Robotframe
${rand_XYZ}



*** Test Cases ***
dictionary
    [Tags]      API
    &{dict}=        Create Dictionary       name=meghesh    value=1     sex=male
    Log    ${dict}
    Dictionary Should Contain Key    ${dict}    name
    ${url}=        Get From Dictionary    ${dict}    sex
    Log To Console    ${url}


Generate random no

    ${rand_XYZ}=     Generate Random String      4       [NUMBERS]
    Set Global Variable    ${rand_XYZ}
    Log     ${rand_XYZ}



Add book into lib databse
    [Tags]      API
    &{req_body}=        Create Dictionary       name=${book_name}      isbn=122393     aisle=212     author=supapor4dstTrainer

    ${response}=       POST        ${base_url}/Library/Addbook.php     json=${req_body}        expected_status=200
    log     ${response.json()}
    Dictionary Should Contain Key    ${response.json()}    ID

    ${id}=      Get From Dictionary     ${response.json()}     ID
    Set Global Variable    ${id}
    Log     ${id}
    Should Be Equal As Strings     successfully added         ${response.json()}[Msg]
    Status Should Be    200     ${response}


Get book details from post
    [Tags]      API
    ${getresponse}=      GET     ${base_url}/Library/GetBook.php     params=ID=${id}     expected_status=200
    log     ${getresponse.json()}
    Should Be Equal As Strings    ${book_name}    ${getresponse.json()}[0][book_name]





Delete the book
    [Tags]      API
    ${delete}=      Create Dictionary       ID=${id}
    ${deleetresp}=      POST        ${base_url}/Library/DeleteBook.php      json=${delete}      expected_status=200
    log      ${deleetresp.json()}
    Should Be Equal As Strings     book is successfully deleted      ${deleetresp.json()}[msg]



