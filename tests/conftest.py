import os
import tempfile

import pytest

from flaskr import flaskr


@pytest.fixture(scope='function')
def app(request):
    db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True
    with flaskr.app.app_context():
        flaskr.init_db()

    def teardown():
        os.close(db_fd)
        os.unlink(flaskr.app.config['DATABASE'])
    request.addfinalizer(teardown)

    return flaskr.app


@pytest.fixture(scope='function')
def base_url(live_server):
    return live_server.url()


@pytest.fixture(scope='function')
def sensitive_url(request):
    return False


@pytest.fixture(scope='function', autouse=True)
def _verify_url(request, base_url):
    from pytest_selenium import pytest_selenium
    pytest_selenium._verify_url(request, base_url)
