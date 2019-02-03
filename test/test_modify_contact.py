from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="New contact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="host_pidaras")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)


# def test_modify_contact_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create_contact(Contact(lastname="New contact"))
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(lastname="host")
#     contact.id = old_contacts[0].id
#     app.contact.modify_first_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[0] = contact
#     assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
