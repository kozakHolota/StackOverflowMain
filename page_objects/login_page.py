from selenium.webdriver.remote.webdriver import WebDriver
import allure

from locators.common_locators import CommonLocators
from locators.login_page_locators import LoginPageLocators
from page_objects.user_workspace_page import UserWorkSpacePage
from web_elements.button import Button
from web_elements.image import Image
from web_elements.text_field import TextField


class LoginPage(object):
    """
        Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver

        self.stackoverflow_logo = Image(self.web_driver, CommonLocators.STACKOVERFLOW_LOGO_LOCATOR.arguments)
        self.google_login_button = Button(self.web_driver, CommonLocators.GOOGLE_LOGIN_BUTTON_LOCATOR.arguments)
        self.facebook_login_button = Button(self.web_driver, CommonLocators.FACEBOOK_BUTTON_LOCATOR.arguments)
        self.username_field = TextField(self.web_driver, LoginPageLocators.USERNAME_FIELD_LOCATOR.arguments)
        self.password_field = TextField(self.web_driver, LoginPageLocators.PASSWORD_FIELD_LOCATOR.arguments)
        self.login_button = Button(self.web_driver, LoginPageLocators.LOGIN_BUTTON_LOCATOR.arguments)

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
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return UserWorkSpacePage(self.web_driver)
