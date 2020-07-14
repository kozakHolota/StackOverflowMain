from browsers.abstract_browser import AbstractBrowser


class Safari(AbstractBrowser):
    def __init__(self, command_executor):
        safari_cpabilities = {
            "appium-version": "1.17.1-1",
            "platformName": "iOS",
            "platformVersion": "13.5",
            "deviceName": "iPhone 11 Pro Max",
            "newCommandTimeout": 600,
            "bundleId": "com.apple.mobilesafari",
             "useLocationServices": False
        }

        super().__init__(name="IOS Safari",
                         command_executor=command_executor,
                         desired_capabilities=safari_cpabilities
                         )