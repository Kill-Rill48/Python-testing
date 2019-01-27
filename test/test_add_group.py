# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="asdsdfsdf", header="fasdfasdf", footer="asdasd"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="", header="", footer=""))
    app.session.logout()

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="alex", middlename="andreev", lastname="igorevich", nickname="w3qxst1ck", home="Izhevsk", email="w3qxst1ck@mail.ru", bday="25", bmonth="July", byear="1996"))
    app.session.logout()


