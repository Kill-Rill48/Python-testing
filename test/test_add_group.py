# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="asdsdfsdf", header="fasdfasdf", footer="asdasd"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="alex", middlename="andreev", lastname="igorevich", nickname="w3qxst1ck", home="Izhevsk", email="w3qxst1ck@mail.ru"))


