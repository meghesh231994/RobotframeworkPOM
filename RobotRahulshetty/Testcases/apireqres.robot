*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***

${base_url}     https://reqres.in
${get_id}


*** Test Cases ***

Get the list of users
    ${listofuser}       GET     ${base_url}/api/users?page     params=2     expected_status=200
    Log    ${listofuser}


Create new user
    ${req_body}=        Create Dictionary     name=megheshBhusari     job=leader

    ${user}=        POST       ${base_url}/api/users    json=${req_body}        expected_status=201
    Log     ${user.json()}
    Dictionary Should Contain Key       ${user.json()}        id

    ${get_id}=      Get From Dictionary      ${user.json()}        id
    Set Global Variable    ${get_id}
    Log To Console    ${get_id}


Get id
    ${getid_post}=      GET     ${base_url}/api/users       params=id=12     expected_status=200
    Log To Console    ${getid_post}

    Delete id


*** Keywords ***
Delete id
    ${delete_id}=       Delete      ${base_url}/api/users/2     expected_status=204
    Log To Console    ${delete_id}