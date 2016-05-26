# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from messages import MessagesPage
from base import Base


class LoginPage(Base):

    URL_TEMPLATE = '/login'

    _error_locator = (By.CLASS_NAME, 'error')
    _password_locator = (By.ID, 'password')
    _submit_locator = (By.ID, 'submit')
    _username_locator = (By.ID, 'username')

    def click_login(self):
        self.find_element(*self._submit_locator).click()

    @property
    def error(self):
        return self.find_element(*self._error_locator).text

    def login(self, username, password):
        self.type_username(username)
        self.type_password(password)
        self.click_login()
        return MessagesPage(self.selenium, self.base_url)

    def type_password(self, value):
        self.find_element(*self._password_locator).send_keys(value)

    def type_username(self, value):
        self.find_element(*self._username_locator).send_keys(value)
