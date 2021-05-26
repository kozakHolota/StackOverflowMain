from abc import ABC

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AbstractWebElement(ABC):
    def __init__(self, web_driver: webdriver.Remote, locator_args: tuple, expected_condition: EC = EC.visibility_of_element_located):
        self.__webdriver = web_driver
        self.__locator_args = locator_args
        self.__expected_condition = expected_condition
        self.__wait = WebDriverWait(web_driver, 15)

    @property
    def web_element(self):
        return self.__wait.until(self.__expected_condition(self.__locator_args))

    @property
    def text(self):
        return self.web_element.text

    def execute_script(self, script: str):
        self.__webdriver.execute_script(script, self.web_element)

    def is_displayed(self):
        return self.web_element.is_displayed()