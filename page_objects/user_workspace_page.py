import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.common_locators import CommonLocators
from locators.user_workspace_locator import UserWorkspaceLocators
from web_elements.button import Button
from web_elements.image import Image
from web_elements.query_items import QueryItems
from web_elements.text_field import TextField


class UserWorkSpacePage(object):
    """
        Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver

        self.profile_button = Button(self.web_driver, UserWorkspaceLocators.PROFILE_BUTTON_LOCATOR.arguments, expected_condition=expected_conditions.visibility_of_element_located)
        self.stackoverflow_logo = Image(self.web_driver, CommonLocators.STACKOVERFLOW_LOGO_LOCATOR.arguments)
        self.inbox_button = Button(self.web_driver, UserWorkspaceLocators.INBOX_BUTTON_LOCATOR.arguments)
        self.achivements_button = Button(self.web_driver, UserWorkspaceLocators.ACHIVEMENTS_BUTTON_LOCATOR.arguments)
        self.help_button = Button(self.web_driver, UserWorkspaceLocators.HELP_BUTTON_LOCATOR.arguments)
        self.user_menu = Button(self.web_driver, UserWorkspaceLocators.USER_MENU_BUTTON_LOCATOR.arguments)
        self.search_field = TextField(self.web_driver, UserWorkspaceLocators.SEARCH_FIELD_LOCATOR.arguments)
        self.search_button_mobile = Button(self.web_driver, UserWorkspaceLocators.SEARCH_BUTTON_MOBILE_LOCATOR.arguments)
        self.found_items_mobile = QueryItems(self.web_driver, UserWorkspaceLocators.FOUND_ITEMS_MOBILE_LOCATOR.arguments)
        self.found_items = QueryItems(self.web_driver, UserWorkspaceLocators.FOUND_ITEMS_LOCATOR.arguments)

    @property
    def search_results(self):
        if "deviceName" in self.web_driver.desired_capabilities.keys():
            self.search_button_mobile.click()
        return self.found_items_mobile\
            if "deviceName" in self.web_driver.desired_capabilities.keys()\
            else self.found_items

    @allure.step("Searching for the next pattern: {1}")
    def search(self, request):
        self.search_field.send_keys(request)
        ActionChains(self.web_driver).send_keys(Keys.ENTER).perform()
        return self