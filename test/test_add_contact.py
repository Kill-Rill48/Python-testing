from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    symbols2 = string.ascii_letters + string.digits
    if prefix == "email" or prefix == "email2" or prefix == "email3":
        return prefix + "".join([random.choice(symbols2) for i in range(random.randrange(maxlen))]) + "@mail.ru"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", email="", email2="", email3="", homephone="", workphone="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 15), lastname=random_string("lastname", 12),
            nickname=random_string("nickname", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), homephone=random_string("homephone", 10), workphone=random_string("workphone", 10))
    for i in range(2)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)



