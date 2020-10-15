Feature: Listing Contacts
    Contacts added to our contact book can be listed back.

Scenario: Listing Added Contacts
    Given I have a contact book
    And I have a first <first> contact
    And I have a second <second> contact
    When I run the "contacts ls" command
    Then the output contains <listed_contacts> contacts

    Examples:
    | first    | second  | listed_contacts  |
    |  Mario   |  Luigi  |  Mario,Luigi     |
    |  John    |  Jane   |  John,Jane       |
