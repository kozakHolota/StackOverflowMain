import allure
from elementium.drivers.se import SeElements
from selenium.webdriver.common.keys import Keys

from page_objects.abstract_page import AbstractPage


class UserWorkSpacePage(AbstractPage):
    """
        Test Adaptation Layer
    """
    def __init__(self, se_elements: SeElements):

        super().__init__(se_elements)
        self.profile_button = self.se_elements.find("[name=my-profile]", ttl=25).until(lambda s: s.is_displayed(), ttl=25)
        self.stackoverflow_logo = self.se_elements.find(".-img._glyph", ttl=25).until(lambda s: s.is_displayed(), ttl=25)
        self.inbox_button = self.se_elements.find("[name=js-inbox-button]").until(lambda s: s.is_displayed(), ttl=25)
        self.achivements_button = self.se_elements.find("[name=js-achievements-button]", ttl=25).until(lambda s: s.is_displayed(), ttl=25)
        self.help_button = self.se_elements.find(".js-help-button", ttl=25).until(lambda s: s.is_displayed(), ttl=25)
        self.user_menu = self.se_elements.find("[name=js-site-switcher-button]", ttl=25).until(lambda s: s.is_displayed(), ttl=25)
        self.search_field = self.se_elements.find("[name=q]", ttl=25).until(lambda s: s.is_displayed(), ttl=25)

    @property
    def search_results(self):
        if "deviceName" in self.se_elements.browser.desired_capabilities.keys():
            self.se_elements.find("[aria-controls=search]", ttl=25).click()
        return self.se_elements.find(".search-result", ttl=25)\
            if "deviceName" in self.se_elements.browser.desired_capabilities.keys()\
            else self.se_elements.find('[name=q]', ttl=25)

    @allure.step("Searching for the next pattern: {1}")
    def search(self, request):
        self.search_field.write(request).write(Keys.ENTER)
        return self