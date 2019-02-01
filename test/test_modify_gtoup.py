from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="Host_pidor"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="Host_pidor"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

