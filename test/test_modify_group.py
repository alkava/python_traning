
from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_group = app.group.get_group_list()
    index = randrange(len(old_group))
    group = Group(name="New group")
    group.id = old_group[index].id
    app.group.modify_group_by_index(index, group)
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)
    old_group[index] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_group = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_group = app.group.get_group_list()
#    assert len(old_group) + 1 == len(new_group)
