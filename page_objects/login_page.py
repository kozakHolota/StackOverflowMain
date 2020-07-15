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
        self.stackoverflow_logo = self.se_elements.find(".-img._glyph").until(lambda s: s.is_displayed(), ttl=25)
        self.google_login_button = self.se_elements.find('[data-provider=google]').until(lambda s: s.is_displayed(), ttl=25)
        self.facebook_login_button = self.se_elements.find('[data-provider=facebook]').until(lambda s: s.is_displayed(), ttl=25)
        self.username_field = self.se_elements.find("#email").until(lambda s: s.is_displayed(), ttl=25)
        self.password_field = self.se_elements.find("#password").until(lambda s: s.is_displayed(), ttl=25)
        self.login_button = self.se_elements.find("#submit-button").until(lambda s: s.is_displayed(), ttl=25)

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
        self.login_button.click()
        allure.attach(self.se_elements.browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return UserWorkSpacePage(self.se_elements)
