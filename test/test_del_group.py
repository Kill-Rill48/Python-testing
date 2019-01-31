from model.group import Group

def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="Host_Pidor"))
    app.group.del_first_group()


# def test_del_first_contact(app):
#     app.contact.del_first_contact()
