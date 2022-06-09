import pytest
import allure
from testcases.test_login import Test_login
from pageobjects.Admin.login_org import Admin2
@pytest.mark.usefixtures("test_logintopage")
class Test_Addloc(Test_login):

    def test_AddLoc(self):
        self.ad2 = Admin2(self.driver)
        self.ad2.setadmin2()
        self.ad2.add_loc("n01", "Andhra pradesh", "vizag", "vizag", "522201", "123456789", "999999", "Not Applicable")
        self.ad2.verify_addlocation()