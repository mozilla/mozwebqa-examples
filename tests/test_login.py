# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.login import LoginPage
from pages.messages import MessagesPage

pytestmark = pytest.mark.nondestructive


def test_login(base_url, selenium, variables):
    """Users can log in"""
    login_page = LoginPage(base_url, selenium)
    login_page.open()
    messages_page = login_page.login(variables['username'], variables['password'])
    assert messages_page.notification == 'You were logged in'


def test_invalid_username(base_url, selenium, variables):
    """Attempt to log in with an invalid username"""
    login_page = LoginPage(base_url, selenium)
    login_page.open()
    login_page.login('invalid', variables['password'])
    assert login_page.error == 'Error: Invalid username'


def test_invalid_password(base_url, selenium, variables):
    """Attempt to log in with an invalid password"""
    login_page = LoginPage(base_url, selenium)
    login_page.open()
    login_page.login(variables['username'], 'invalid')
    assert login_page.error == 'Error: Invalid password'


def test_logout(base_url, selenium, variables):
    """Make sure logout works"""
    messages_page = MessagesPage(base_url, selenium)
    messages_page.open()
    messages_page.login(variables['username'], variables['password'])
    messages_page.logout()
    assert messages_page.notification == 'You were logged out'
