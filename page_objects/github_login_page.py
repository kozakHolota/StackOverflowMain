import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.github_login_page_locators import GitHubLoginPageLocators
from page_objects.user_workspace_page import UserWorkSpacePage
from selenium.webdriver.remote.webdriver import WebDriver

from web_elements.button import Button
from web_elements.text_field import TextField


class GitHubLoginPage(object):
    """
        Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.username_field = TextField(self.web_driver, GitHubLoginPageLocators.USERNAME_FIELD_LOCATOR.arguments)
        self.password_field = TextField(self.web_driver, GitHubLoginPageLocators.PASSWORD_FIELD_LOCATOR.arguments)
        self.login_button = Button(self.web_driver, GitHubLoginPageLocators.PASSWORD_FIELD_LOCATOR.arguments)
        self.signup_button = Button(self.web_driver, GitHubLoginPageLocators.PASSWORD_FIELD_LOCATOR.arguments)

    @allure.step("Enter username {1}")
    def enter_login(self, username):
        self.username_field.send_keys(username)
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self

    @allure.step("Filling in the password")
    def enter_password(self, password):
        self.password_field.send_keys(password)
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self

    @allure.step("Clicking on the Login Button")
    def click_on_login_button(self):
        self.login_button.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), name="Login result screenshot", attachment_type=allure.attachment_type.PNG)
        return self

    @allure.step("Accepting signup")
    def accept_signup(self):
        try:
            click_button = self.signup_button\
                if "deviceName" in self.web_driver.desired_capabilities.keys()\
            else self.login_button
            click_button.click()
        finally:
            return UserWorkSpacePage(self.web_driver)