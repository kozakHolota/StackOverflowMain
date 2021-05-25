from selenium.webdriver.common.by import By

from locators.abstract_locators import AbstractLocators


class CommonLocators(AbstractLocators):
    STACKOVERFLOW_LOGO_LOCATOR = (By.CSS_SELECTOR, ".-img._glyph")
    GOOGLE_LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[data-provider=google]')
    FACEBOOK_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[data-provider=facebook]')

    def __init__(self, by: By, locator: str):
        super().__init__(by, locator)