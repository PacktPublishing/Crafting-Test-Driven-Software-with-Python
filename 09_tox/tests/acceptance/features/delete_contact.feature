Feature: Deleting Contacts
    Contacts added to our contact book can be removed.

Scenario: Removing a Basic Contact
    Given I have a contact book
    And I have a "John" contact
    When I run the "contacts del John" command
    Then My contacts book is now empty

