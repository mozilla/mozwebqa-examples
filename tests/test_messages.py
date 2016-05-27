# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.messages import MessagesPage


def test_create_message(base_url, selenium, variables):
    """Create a message"""
    messages_page = MessagesPage(selenium, base_url).open()
    messages_page.login(variables['username'], variables['password'])
    messages_page.create_message('<Hello>', '<strong>HTML</strong> allowed here')
    assert messages_page.notification == 'New entry was successfully posted'
    assert len(messages_page.messages) == 1
    assert messages_page.messages[0].title == '<Hello>'
    assert messages_page.messages[0].text == 'HTML allowed here'


@pytest.mark.nondestructive
def test_empty(base_url, selenium):
    """Start with an empty list of messages"""
    messages_page = MessagesPage(selenium, base_url).open()
    assert messages_page.messages == []
