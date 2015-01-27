# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from flask import url_for
from selenium.webdriver.common.by import By

from messages import MessagesPage
from base import Base


class LoginPage(Base):

    _error_locator = (By.CLASS_NAME, 'error')
    _password_locator = (By.ID, 'password')
    _submit_locator = (By.ID, 'submit')
    _username_locator = (By.ID, 'username')

    def click_login(self):
        self.selenium.find_element(*self._submit_locator).click()

    @property
    def error(self):
        return self.selenium.find_element(*self._error_locator).text

    def login(self, username=None, password=None):
        credentials = self.testsetup.credentials
        username = credentials.get('username') if username is None else username
        password = credentials.get('password') if password is None else password
        self.type_username(username)
        self.type_password(password)
        self.click_login()
        return MessagesPage(self.testsetup)

    def open(self):
        self.selenium.get(url_for('login', _external=True))

    def type_password(self, value):
        self.selenium.find_element(*self._password_locator).send_keys(value)

    def type_username(self, value):
        self.selenium.find_element(*self._username_locator).send_keys(value)
