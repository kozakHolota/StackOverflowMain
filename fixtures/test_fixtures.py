import pytest
import yaml

from config.test_conf import Config
from helpers.getters import get_browser, get_main_page

from browsers.browsers import Browsers


@pytest.fixture(scope='session', autouse=True)
def init_drivers(request):
    config = None
    with open(request.config.getoption("--conf")) as yaml_file:
        config = yaml.load(yaml_file)

    Config.browsers = config["browsers"]
    Config.grid_address = config["grid_url"]

    def _get_browser(browser_name):
        Config.webdrivers[browser_name] = Browsers[browser_name]

    for br in Config.browsers:
        _get_browser(br)

@pytest.fixture
def main_page(request):
    next_brw = None
    if not Config.brw:
        Config.brw = get_browser()

    try:
        next_brw = Config.brw.__next__()
    except StopIteration:
        Config.brw = get_browser()
        next_brw = Config.brw.__next__()

    res = get_main_page(next_brw)

    def fin():
        res.web_driver.quit()

    request.addfinalizer(fin)

    return res


def pytest_generate_tests(metafunc):
    config = None
    with open(metafunc.config.getoption("--conf")) as yaml_file:
        config = yaml.load(yaml_file)
    params = tuple(map(lambda browser: (config["login"],
                                        config["password"],
                                        config["github_login"],
                                        config["github_password"]),
                       config["browsers"]
                       )
                   )

    metafunc.parametrize("username, password, github_username, github_password", params)