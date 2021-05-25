from enum import Enum

from selenium.webdriver.common.by import By


class AbstractLocators(Enum):
    def __init__(self, by: By, locator: str):
        self.locator = locator
        self.by = by

    @property
    def arguments(self) -> tuple:
        return self.by, self.locator