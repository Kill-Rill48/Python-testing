from model.group import Group
from random import randrange


def test_del_some_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="Host_Pidor"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.del_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups) + 1
    old_groups[index:index+1] = []
    assert old_groups == new_groups


# def test_del_first_contact(app):
#     app.contact.del_first_contact()
