*** Settings ***
Library    HelloLibrary

*** Keywords ***
Echo Hello
    Log    Hello!

*** Test Cases ***
Use Custom Keywords
    Echo Hello
    Say Hello