from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from browsers.abstract_browser import AbstractBrowser


class Safari(AbstractBrowser):
    def __init__(self):
        safari_cpabilities = DesiredCapabilities.SAFARI.copy()
        super().__init__(name="MacOS X Safari",
                         webdriver_class=webdriver.Safari,
                         desired_capabilities=safari_cpabilities
                         )


class SafriRemote(AbstractBrowser):
    def __init__(self, command_executor):
        safari_cpabilities = DesiredCapabilities.SAFARI.copy()
        safari_cpabilities["acceptSslCerts"] = True
        super().__init__(name="MacOS X Safari",
                         command_executor=command_executor,
                         desired_capabilities=safari_cpabilities
                         )
