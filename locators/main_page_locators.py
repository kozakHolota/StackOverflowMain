from selenium.webdriver.common.by import By

from locators.abstract_locators import AbstractLocators


class MainPageLocators(AbstractLocators):
    LOGIN_LINK_LOCATOR = (By.CSS_SELECTOR, ".login-link.s-btn[href*=login]")
    SGNUP_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".login-link.s-btn[href*=signup]")

    def __init__(self, by: By, locator: str):
        super().__init__(by, locator)