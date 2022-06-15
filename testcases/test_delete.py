
import pytest
import allure
from TestCases.test_login import Test_login
from pageobjects.Admin.login_org import Admin2

@pytest.mark.usefixtures("test_logintopage")
class Test_Delete(Test_login):

    def test_delete(self):
        self.ad2 = Admin2(self.driver)
        self.ad2.setadmin2()
        self.logger1.info("--------open adminpage--------")
        location = "navya"
        self.logger1.info("------delete location-----")
        self.ad2.loc_delete(location)

