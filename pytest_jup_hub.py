# -*- coding: utf-8 -*-

import pytest
from firstuseauthenticator import FirstUseAuthenticator

def pytest_addoption(parser):
    group = parser.getgroup('jup_hub')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default='2022',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo


@pytest.fixture
def firstuseauthenticator_configured():
    """firstuseauthenticator object with min_password_length set to 10"""
    auth = FirstUseAuthenticator()
    auth.min_password_length = 10
    return auth