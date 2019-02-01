from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="New contact"))
    app.contact.modify_first_contact(Contact(firstname="host_pidaras"))


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="New contact"))
    app.contact.modify_first_contact(Contact( lastname="host"))
