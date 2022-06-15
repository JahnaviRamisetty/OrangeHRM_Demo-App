import pytest
import allure
from TestCases.test_login import Test_login
from pageobjects.Admin.login_org import Admin2
from TestCases.test_addloc import Test_Addloc
@pytest.mark.usefixtures("test_logintopage")
class Test_verify(Test_login):
    ad3 = Test_Addloc
    def test_verify(self):
        # self.ad2 = Admin2(self.driver)
        # self.ad2.setadmin2()
        #self.ad2.test_AddLoc()
        self.ad2.verify_addlocation()