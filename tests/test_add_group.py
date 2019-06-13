from model.group import Group

group = Group(name="New group")


def test_add_group(app):
    old_group = app.group.get_group_list()
    app.group.add_new_group(group)
    new_list = app.group.get_group_list()
    old_group.append(group)
    assert sorted(old_group,key=Group.Name) == sorted(new_list,key=Group.Name)



