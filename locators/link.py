from selenium import webdriver

from web_elements.abstract_web_element import AbstractWebElement
from web_elements.web_elements_decorators import click
from selenium.webdriver.support import expected_conditions as EC


@click
class Link(AbstractWebElement):
    def __init__(self, web_driver: webdriver.Remote, locator_args: tuple,
                 expected_condition: EC = EC.element_to_be_clickable):
        super().__init__(web_driver, locator_args, expected_condition)

    @property
    def href(self):
        return self.web_element.get_attribute("href")
