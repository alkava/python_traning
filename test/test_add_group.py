# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = \
    [
        Group(name="11111", header="1111111", footer="1111111"),
        Group(name="", header="", footer="")
    ]+[
        Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
        for i in range(5)
    ]
#+[Group(name=name, header=header, footer=footer)
#  for name in ["", random_string("name", 10)]
#for header in ["", random_string("header", 20)]
#for footer in ["", random_string("footer", 20)]
#  ]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_valid_group(app, group):
    old_group = app.group.get_group_list()
    group = Group(name="11111", header="1111111", footer="1111111")
    app.group.create(group)
    assert len(old_group) + 1 == app.group.count() # Heshing
    new_group = app.group.get_group_list()

    old_group.append(group)

    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)



#def test_add_empty_group(app):
#    old_group = app.group.get_group_list()
#    group = Group(name="", header="", footer="")
#    app.group.create(group)
#    new_group = app.group.get_group_list()
#    assert len(old_group) + 1 == len(new_group)
#    old_group.append(group)
#    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)



