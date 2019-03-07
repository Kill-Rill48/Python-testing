from model.group import Group
import random


def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="Host_pidor"))
    old_groups = db.get_group_list()
    modify_group = random.choice(old_groups)
    index = old_groups.index(modify_group)
    group = Group(name="RAggelyadayn")
    group.id = modify_group.id
    app.group.modify_group_by_id(modify_group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create_group(Group(name="Host_pidor"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

