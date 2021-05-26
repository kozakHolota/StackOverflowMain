from selenium.webdriver.common.by import By

from locators.abstract_locators import AbstractLocators


class GitHubLoginPageLocators(AbstractLocators):
    USERNAME_FIELD_LOCATOR = (By.ID, "login_field")
    PASSWORD_FIELD_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.NAME, "commit")
    SIGNUP_BUTTON_LOCATOR = (By.ID, 'js-oauth-authorize-btn')

    def __init__(self, by: By, locator: str):
        super().__init__(by, locator)