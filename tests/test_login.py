# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.login import LoginPage
from pages.messages import MessagesPage


@pytest.mark.nondestructive
class TestLogin:

    def test_login(self, mozwebqa):
        """Users can log in"""
        login_page = LoginPage(mozwebqa)
        login_page.open()
        messages_page = login_page.login()
        Assert.equal(messages_page.notification, 'You were logged in')

    def test_invalid_username(self, mozwebqa):
        """Attempt to log in with an invalid username"""
        login_page = LoginPage(mozwebqa)
        login_page.open()
        login_page.login(username='invalid')
        Assert.equal(login_page.error, 'Error: Invalid username')

    def test_invalid_password(self, mozwebqa):
        """Attempt to log in with an invalid password"""
        login_page = LoginPage(mozwebqa)
        login_page.open()
        login_page.login(password='invalid')
        Assert.equal(login_page.error, 'Error: Invalid password')

    def test_logout(self, mozwebqa):
        """Make sure logout works"""
        messages_page = MessagesPage(mozwebqa)
        messages_page.open()
        messages_page.login()
        messages_page.logout()
        Assert.equal(messages_page.notification, 'You were logged out')
