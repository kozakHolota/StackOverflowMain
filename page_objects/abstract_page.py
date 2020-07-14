from abc import ABC

from elementium.drivers.se import SeElements


class AbstractPage(ABC):
    def __init__(self, se_elements: SeElements):
        self.se_elements = se_elements
