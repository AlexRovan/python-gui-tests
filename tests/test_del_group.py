from model.group import Group
import random


group1 = Group(name="New group")


def test_del_group(app):
    if(len(app.group.get_group_list())==0):
        app.group.add_new_group(group1)
    old_group = app.group.get_group_list()
    index = random.randrange(len(old_group))
    app.group.delete_group_by_index(index)
    new_list = app.group.get_group_list()
    old_group[index:index+1] = []
    assert sorted(old_group,key=Group.Name) == sorted(new_list,key=Group.Name)