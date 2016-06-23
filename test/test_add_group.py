# -*- coding: utf-8 -*-
from model.group import Group
import pytest
# from data.groups import testdata # from data.add_group import constant as testdata


# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])

def test_add_valid_group(app, db, json_groups):  # data_groups заменили на json_groups в лекции 6.6.
    #  В лекции 7.4. добавили вызов фикстуры db
    group = json_groups
    old_group = db.get_group_list()
    # group = Group(name="11111", header="1111111", footer="1111111")
    app.group.create(group)
    # assert len(old_group) + 1 == app.group.count()  # Heshing
    new_group = db.get_group_list()
    old_group.append(group)

    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)



# def test_add_empty_group(app):
#    old_group = app.group.get_group_list()
#    group = Group(name="", header="", footer="")
#    app.group.create(group)
#    new_group = app.group.get_group_list()
#    assert len(old_group) + 1 == len(new_group)
#    old_group.append(group)
#    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)



