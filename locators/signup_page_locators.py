from selenium.webdriver.common.by import By

from locators.abstract_locators import AbstractLocators


class SignupPageLocators(AbstractLocators):
    GITHUB_SIGNUP_BUTTON = (By.CSS_SELECTOR, '[data-provider=github]')
    DISPLAY_NAME_LOCATOR = (By.ID, "display-name")
    PRODUCT_UPDATES_LOCATOR = (By.ID, "opt-in")
    USERNAME_FIELD_LOCATOR = (By.ID, "email")
    PASSWORD_FIELD_LOCATOR = (By.ID, "password")
    SUBMIT_BUTTON_LOCATOR = (By.ID, "submit-button")

    def __init__(self, by: By, locator: str):
        super().__init__(by, locator)