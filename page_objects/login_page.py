import allure
from elementium.drivers.se import SeElements

from page_objects.abstract_page import AbstractPage
from page_objects.user_workspace_page import UserWorkSpacePage


class LoginPage(AbstractPage):
    """
        Test Adaptation Layer
    """
    def __init__(self, se_elements: SeElements):

        super().__init__(se_elements)
        self.stackoverflow_logo = self.se_elements.find(".-img._glyph")
        self.google_login_button = self.se_elements.find('[data-provider=google]')
        self.facebook_login_button = self.se_elements.find('[data-provider=facebook]')
        self.username_field = self.se_elements.find("#email")
        self.password_field = self.se_elements.find("#password")
        self.login_button = self.se_elements.find("#submit-button")

    @allure.step("Enter username {1}")
    def enter_login(self, username):
        self.username_field.write(username)
        allure.attach(self.se_elements.browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self

    @allure.step("Filling in the password")
    def enter_password(self, password):
        self.password_field.write(password)
        allure.attach(self.se_elements.browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self

    @allure.step("Clicking on the Login Button")
    def click_on_login_button(self):
        self.se_elements.browser.execute_script("arguments[0].click()", self.login_button)
        allure.attach(self.se_elements.browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return UserWorkSpacePage(self.se_elements)
