# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_valid_group(app):
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name="11111", header="1111111", footer="1111111"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

