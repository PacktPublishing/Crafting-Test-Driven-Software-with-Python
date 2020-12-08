===============
Manage Contacts
===============

.. contents::

Contacts can be managed through an instance of 
:class:`contacts.Application`, use :meth:`contacts.Application.run`
to execute any command like you would in the shell.

.. testsetup::

    from contacts import Application

    app = Application()


Adding Contancts
================

.. testcode::

    app.run("contacts add Name 0123456789")

Listing Contacts
================

.. testcode::

    app.run("contacts ls")

.. testoutput::

    Name 0123456789




