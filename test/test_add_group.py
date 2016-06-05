# -*- coding: utf-8 -*-
from model.group import Group





def test_add_valid_group(app):
    old_group = app.group.get_group_list()
    group = Group(name="11111", header="1111111", footer="1111111")
    app.group.create(group)
    assert len(old_group) + 1 == app.group.count() # Heshing
    new_group = app.group.get_group_list()

    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)



def test_add_empty_group(app):
    old_group = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)



