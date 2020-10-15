from pytest_bdd import scenario, given, when, then, parsers

import contacts

from .steps import *

@scenario("features/list_contacts.feature", 
            "Listing Added Contacts")
def test_listing_added_contacts(capsys):
    pass


@given("I have a first <first> contact")
def have_a_first_contact(contactbook, first):
    contactbook.add(first, "000")
    return first


@given("I have a second <second> contact")
def have_a_second_contact(contactbook, second):
    contactbook.add(second, "000")
    return second


@then("the output contains <listed_contacts> contacts")
def outputcontains(listed_contacts, capsys):
    expected_list = "".join([f"{c} 000\n" for c in listed_contacts.split(",")])
    out, _ = capsys.readouterr()
    assert out == expected_list
