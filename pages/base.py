# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class Base(Page):

    _login_locator = (By.ID, 'login')
    _logout_locator = (By.ID, 'logout')
    _notification_locator = (By.CLASS_NAME, 'flash')

    def click_login(self):
        self.selenium.find_element(*self._login_locator).click()
        from pages.login import LoginPage
        return LoginPage(self.testsetup)

    def click_logout(self):
        self.selenium.find_element(*self._logout_locator).click()

    def login(self, username=None, password=None):
        login_page = self.click_login()
        return login_page.login(username, password)

    def logout(self):
        self.click_logout()

    @property
    def notification(self):
        return self.selenium.find_element(*self._notification_locator).text
