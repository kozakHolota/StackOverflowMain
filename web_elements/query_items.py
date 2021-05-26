from selenium import webdriver

from web_elements.abstract_web_element import AbstractWebElement
from selenium.webdriver.support import expected_conditions as EC


class QueryItems(AbstractWebElement):
    def __init__(self, web_driver: webdriver.Remote, locator_args: tuple, expected_condition: EC = EC.visibility_of_all_elements_located):
        super().__init__(web_driver, locator_args, expected_condition)

    def __len__(self):
        return len(self.web_element)