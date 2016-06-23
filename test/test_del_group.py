from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = list(map(app.group.clean, db.get_group_list()))
    chosen_group = random.choice(old_groups)
    app.group.delete_group_by_id(chosen_group.id)

    new_groups = list(map(app.group.clean, db.get_group_list()))
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(chosen_group)
    assert old_groups == new_groups
    if check_ui:
        ui_groups = sorted(app.group.get_group_list(), key=Group.id_or_max)
        groups_from_db = sorted(new_groups, key=Group.id_or_max)
        assert groups_from_db == ui_groups


'''
from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_group = app.group.get_group_list()
    index = randrange(len(old_group))
    app.group.delete_group_by_index(index)
    new_group = app.group.get_group_list()
    assert len(old_group) - 1 == len(new_group)

    old_group[index:index+1] = []
    assert old_group == new_group
'''