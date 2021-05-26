from selenium.webdriver.common.by import By

from locators.abstract_locators import AbstractLocators


class LoginPageLocators(AbstractLocators):
    USERNAME_FIELD_LOCATOR = (By.ID, "email")
    PASSWORD_FIELD_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "submit-button")

    def __init__(self, by: By, locator: str):
        super().__init__(by, locator)
