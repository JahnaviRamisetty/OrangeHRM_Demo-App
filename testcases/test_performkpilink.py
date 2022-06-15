import pytest
from selenium.webdriver.common.by import By

from TestCases.test_login import Test_login

from pageobjects.performance import configure
#@pytest.mark.sanity
@pytest.mark.usefixtures("test_logintopage")
class Test_Performance(Test_login):
    def test_perform(self):
        self.perform =configure.Performance(self.driver)
        self.perform.setperformance()
        self.perform.clicklink("Authored Tests","Testing")
