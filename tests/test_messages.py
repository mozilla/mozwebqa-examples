# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.messages import MessagesPage


class TestMessages:

    def test_create_message(self, mozwebqa):
        """Create a message"""
        messages_page = MessagesPage(mozwebqa)
        messages_page.open()
        messages_page.login('admin', 'default')
        messages_page.create_message('<Hello>', '<strong>HTML</strong> allowed here')
        Assert.equal(messages_page.notification, 'New entry was successfully posted')
        Assert.equal(len(messages_page.messages), 1)
        Assert.equal(messages_page.messages[0].title, '<Hello>')
        Assert.equal(messages_page.messages[0].text, 'HTML allowed here')

    @pytest.mark.nondestructive
    def test_empty(self, mozwebqa):
        """Start with an empty list of messages"""
        messages_page = MessagesPage(mozwebqa)
        messages_page.open()
        Assert.equal(messages_page.messages, [])
