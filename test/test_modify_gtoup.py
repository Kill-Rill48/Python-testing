from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="Host_pidor"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="Host_pidor"))
    app.group.modify_first_group(Group(header="New header"))


