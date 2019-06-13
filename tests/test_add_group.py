from model.group import Group

group1 = Group(name="New group")


def test_add_group(app,excel_groups):
    group=excel_groups
    old_group = app.group.get_group_list()
    app.group.add_new_group(group)
    new_list = app.group.get_group_list()
    old_group.append(group)
    assert sorted(old_group,key=Group.Name) == sorted(new_list,key=Group.Name)

