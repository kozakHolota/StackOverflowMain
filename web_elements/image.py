from selenium import webdriver

from web_elements.abstract_web_element import AbstractWebElement


class Image(AbstractWebElement):
    def __init__(self, web_driver: webdriver.Remote, locator_args: tuple,):
        super().__init__(web_driver, locator_args)