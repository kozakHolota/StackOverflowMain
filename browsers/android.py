from browsers.abstract_browser import AbstractBrowser


class Chrome(AbstractBrowser):
    def __init__(self, command_executor):
        chrome_cpabilities = {
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "automationName": "UIAutomator2",
  "browserName": "Chrome"
}
        super().__init__(name="Android Chrome",
                         command_executor=command_executor,
                         desired_capabilities=chrome_cpabilities
                         )