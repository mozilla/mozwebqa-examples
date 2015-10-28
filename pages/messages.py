# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import Base
from page import PageRegion


class MessagesPage(Base):

    _messages_locator = (By.CLASS_NAME, 'entry')
    _share_locator = (By.ID, 'share')
    _text_locator = (By.ID, 'text')
    _title_locator = (By.ID, 'title')

    def create_message(self, title, text):
        self.type_title(title)
        self.type_text(text)
        self.click_share()

    def click_share(self):
        self.selenium.find_element(*self._share_locator).click()

    @property
    def messages(self):
        return [self.Message(self.selenium, el) for el in
                self.selenium.find_elements(*self._messages_locator)]

    def type_text(self, value):
        self.selenium.find_element(*self._text_locator).send_keys(value)

    def type_title(self, value):
        self.selenium.find_element(*self._title_locator).send_keys(value)

    class Message(PageRegion):

        _title_locator = (By.TAG_NAME, 'h2')
        _text_locator = (By.CLASS_NAME, 'text')

        @property
        def text(self):
            return self.root.find_element(*self._text_locator).text

        @property
        def title(self):
            return self.root.find_element(*self._title_locator).text
