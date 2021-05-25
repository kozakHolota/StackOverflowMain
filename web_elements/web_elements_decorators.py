from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, \
    WebDriverException


def click(cls):
    def click(self):
        try:
            self.web_element.click()
        except (ElementClickInterceptedException, ElementNotInteractableException, WebDriverException):
            self.driver.execute_script("arguments[0].click()", self.web_element)

    def wrapper():
        cls.click = click
        return cls

    return wrapper()


def send_keys(cls):
    def send_keys(self, text: str):
        try:
            self.web_element.send_keys(text)
        except WebDriverException:
            self.driver.execute_script(f"arguments[0].value='{text}';", self.web_element)

    def wrapper():
        cls.send_keys = send_keys
        return cls

    return wrapper()
