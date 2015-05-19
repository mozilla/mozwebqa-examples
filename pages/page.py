# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


class Page(object):

    def __init__(self, base_url, selenium):
        self.base_url = base_url
        self.selenium = selenium
