import allure
from selenium.webdriver.remote.webdriver import WebDriver

from locators.common_locators import CommonLocators
from locators.signup_page_locators import SignupPageLocators
from page_objects.github_login_page import GitHubLoginPage
from web_elements.button import Button
from web_elements.header import Header
from web_elements.image import Image
from web_elements.text_field import TextField


class SignUpPage(object):
    """
        Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.stackoverflow_logo = Image(self.web_driver, CommonLocators.STACKOVERFLOW_LOGO_LOCATOR.arguments)
        self.google_login_button = Button(self.web_driver, CommonLocators.GOOGLE_LOGIN_BUTTON_LOCATOR.arguments)
        self.facebook_login_button = Button(self.web_driver, CommonLocators.FACEBOOK_BUTTON_LOCATOR.arguments)
        self.github_login_button = Button(self.web_driver, SignupPageLocators.GITHUB_SIGNUP_BUTTON.arguments)
        self.display_name = Header(self.web_driver, SignupPageLocators.DISPLAY_NAME_LOCATOR.arguments)
        self.product_updates = Header(self.web_driver, SignupPageLocators.PRODUCT_UPDATES_LOCATOR.arguments)
        self.username_field = TextField(self.web_driver, SignupPageLocators.USERNAME_FIELD_LOCATOR.arguments)
        self.password_field = TextField(self.web_driver, SignupPageLocators.PASSWORD_FIELD_LOCATOR.arguments)
        self.signup_button = Button(self.web_driver, SignupPageLocators.GITHUB_SIGNUP_BUTTON.arguments)

    @allure.step("Signing up from GitHub")
    def click_github_signup(self):
        self.github_login_button.click()
        return GitHubLoginPage(self.web_driver)