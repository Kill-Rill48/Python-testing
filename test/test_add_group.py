# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="asdsdfsdf", header="fasdfasdf", footer="asdasd")
    app.group.create_group(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="alex", middlename="andreev", lastname="igorevich", nickname="w3qxst1ck", home="Izhevsk", email="w3qxst1ck@mail.ru")
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
