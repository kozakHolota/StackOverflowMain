from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.microsoft import IEDriverManager

from browsers.abstract_browser import AbstractBrowser


class Ie(AbstractBrowser):
    def __init__(self):
        ie_capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
        ie_capabilities["acceptSslCerts"] = True
        ie_capabilities["requireWindowFocus"] = True
        super().__init__(name="Internet Explorer",
                         webdriver_class=webdriver.Ie,
                         webdriver_manager=IEDriverManager(),
                         desired_capabilities=ie_capabilities
                         )


class IeRemote(AbstractBrowser):
    def __init__(self, command_executor):
        ie_capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
        ie_capabilities["acceptSslCerts"] = True
        ie_capabilities["requireWindowFocus"] = True
        super().__init__(name="Internet Explorer",
                         command_executor=command_executor,
                         desired_capabilities=ie_capabilities
                         )
