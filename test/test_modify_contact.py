from model.contact import Contact
import random


def test_modify_contact_firstname(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="New contact"))
    old_contacts = db.get_contact_list()
    modiffying_contact = random.choice(old_contacts)
    contact = Contact(firstname="host_pidaras")
    index = old_contacts.index(modiffying_contact)
    contact.id = modiffying_contact.id
    app.contact.modify_contact_by_id(id, contact)
    new_contacts = db.get_contact_list()
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
