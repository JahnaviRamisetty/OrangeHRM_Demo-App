import pytest
import allure
from TestCases.test_login import Test_login
from pageobjects.Admin.login_org import Admin2

@pytest.mark.usefixtures("test_logintopage")
class Test_Link(Test_login):

    def test_link(self):
        self.ad2 = Admin2(self.driver)
        self.ad2.setadmin2()

        self.ad2.clicklink("california")
        #self.ad2.enable()