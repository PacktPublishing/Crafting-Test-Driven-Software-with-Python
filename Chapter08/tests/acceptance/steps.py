from pytest_bdd import scenario, given, when, then, parsers

import contacts


@given("I have a contact book", target_fixture="contactbook")
def contactbook():
    return contacts.Application()


@given(parsers.parse("I have a \"{contactname}\" contact"))
def have_a_contact(contactbook, contactname):
    contactbook.add(contactname, "000")


@when(parsers.parse("I run the \"{command}\" command"))
def runcommand(contactbook, command):
    contactbook.run(command)
