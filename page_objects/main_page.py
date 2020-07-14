import allure
from elementium.drivers.se import SeElements
from selenium.common.exceptions import WebDriverException

from page_objects.abstract_page import AbstractPage
from page_objects.login_page import LoginPage
from page_objects.signup_page import SignUpPage


class MainPage(AbstractPage):
    """
    Test Adaptation Layer
    """
    def __init__(self, se_elements: SeElements):
        super().__init__(se_elements)
        try:
            self.se_elements.browser.maximize_window()
        except WebDriverException:
            pass
        self.se_elements.navigate("https://stackoverflow.com")

        # Instantiating web elements
        self.stackoverflow_logo = self.se_elements.find(".-img._glyph")
        self.login_link = self.se_elements.find(".login-link.s-btn[href*=login]")
        self.sign_up_button = self.se_elements.find(".login-link.s-btn[href*=signup]")


    @allure.step("Click on the Sign Up button")
    def click_on_sign_up_button(self):
        self.sign_up_button.click()
        allure.attach(self.se_elements.browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return SignUpPage(self.se_elements)

    @allure.step("Click on the Sign In button")
    def click_on_login_link(self):
        self.login_link.click()
        allure.attach(self.se_elements.browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return LoginPage(self.se_elements)