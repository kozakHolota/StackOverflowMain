from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from browsers.abstract_browser import AbstractBrowser


class Edge(AbstractBrowser):
    def __init__(self):
        edge_capabilities = DesiredCapabilities.EDGE.copy()
        edge_capabilities["acceptSslCerts"] = True
        edge_capabilities["requireWindowFocus"] = True
        super().__init__(name="Microsoft Edge",
                         webdriver_class=webdriver.Edge,
                         webdriver_manager=EdgeChromiumDriverManager(),
                         desired_capabilities=edge_capabilities
                         )


class EdgeRemote(AbstractBrowser):
    def __init__(self, command_executor):
        edge_capabilities = DesiredCapabilities.EDGE.copy()
        edge_capabilities["acceptSslCerts"] = True
        edge_capabilities["requireWindowFocus"] = True
        super().__init__(name="Microsoft Edge",
                         command_executor=command_executor,
                         desired_capabilities=edge_capabilities
                         )
