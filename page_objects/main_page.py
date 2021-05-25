from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver
import allure

from locators.common_locators import CommonLocators
from locators.link import Link
from locators.main_page_locators import MainPageLocators
from page_objects.login_page import LoginPage
from page_objects.signup_page import SignUpPage
from web_elements.button import Button
from web_elements.image import Image


class MainPage(object):
    """
    Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        try:
            self.web_driver.maximize_window()
        except WebDriverException:
            pass
        self.web_driver.get("https://stackoverflow.com")

        # Instantiating web elements
        self.stackoverflow_logo = Image(self.web_driver, CommonLocators.STACKOVERFLOW_LOGO_LOCATOR.arguments)
        self.login_link = Link(self.web_driver, MainPageLocators.LOGIN_LINK_LOCATOR.arguments)
        self.sign_up_button = Button(self.web_driver, MainPageLocators.SGNUP_BUTTON_LOCATOR.arguments)


    @allure.step("Click on the Sign Up button")
    def click_on_sign_up_button(self):
        self.sign_up_button.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return SignUpPage(self.web_driver)

    @allure.step("Click on the Sign In button")
    def click_on_login_link(self):
        self.login_link.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return LoginPage(self.web_driver)