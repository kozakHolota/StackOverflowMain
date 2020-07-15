import allure
from elementium.drivers.se import SeElements

from page_objects.abstract_page import AbstractPage
from page_objects.github_login_page import GitHubLoginPage


class SignUpPage(AbstractPage):
    """
        Test Adaptation Layer
    """
    def __init__(self, se_elements: SeElements):
        # Initialize web driver
        super().__init__(se_elements)
        self.stackoverflow_logo = self.se_elements.find(".-img._glyph").until(lambda s: s.is_displayed(), ttl=25)
        self.google_login_button = self.se_elements.find('[data-provider=google]').until(lambda s: s.is_displayed(), ttl=25)
        self.facebook_login_button = self.se_elements.find('[data-provider=facebook]').until(lambda s: s.is_displayed(), ttl=25)
        self.github_login_button = self.se_elements.find('[data-provider=github]').until(lambda s: s.is_displayed(), ttl=25)
        self.display_name = self.se_elements.find("#display-name").until(lambda s: s.is_displayed(), ttl=25)
        self.product_updates = self.se_elements.find("#opt-in").until(lambda s: s.is_displayed(), ttl=25)
        self.username_field = self.se_elements.find("#email").until(lambda s: s.is_displayed(), ttl=25)
        self.password_field = self.se_elements.find("#password").until(lambda s: s.is_displayed(), ttl=25)
        self.signup_button = self.se_elements.find("#submit-button").until(lambda s: s.is_displayed(), ttl=25)

    @allure.step("Signing up from GitHub")
    def click_github_signup(self):
        self.github_login_button.click()
        return GitHubLoginPage(self.se_elements)