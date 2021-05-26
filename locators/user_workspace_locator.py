from selenium.webdriver.common.by import By

from locators.abstract_locators import AbstractLocators


class UserWorkspaceLocators(AbstractLocators):
    PROFILE_BUTTON_LOCATOR = (By.CLASS_NAME, "my-profile")
    INBOX_BUTTON_LOCATOR = (By.CLASS_NAME, "js-inbox-button")
    ACHIVEMENTS_BUTTON_LOCATOR = (By.CLASS_NAME, "js-achievements-button")
    HELP_BUTTON_LOCATOR = (By.CLASS_NAME, "js-help-button")
    USER_MENU_BUTTON_LOCATOR = (By.CLASS_NAME, "js-site-switcher-button")
    SEARCH_FIELD_LOCATOR = (By.NAME, "q")
    SEARCH_BUTTON_MOBILE_LOCATOR = (By.CSS_SELECTOR, "[aria-controls=search]")
    FOUND_ITEMS_MOBILE_LOCATOR = (By.CSS_SELECTOR, ".search-result")
    FOUND_ITEMS_LOCATOR = (By.NAME, "q")

    def __init__(self, by: By, locator: str):
        super().__init__(by, locator)