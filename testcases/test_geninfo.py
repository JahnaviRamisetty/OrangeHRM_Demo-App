import allure
import pytest
from pageobjects.Admin.admin_org_geninfo import Admin_Org
#from pageobjects.Admin.login_org import Admin2
from TestCases.test_login import Test_login
#from pageobjects.Admin import addloc


@pytest.mark.usefixtures("test_logintopage")
@allure.severity(allure.severity_level.NORMAL)
class Test_admin(Test_login):

    def test_admin2(self):
        self.ad2 = Admin_Org(self.driver)
        self.logger1.info("********* Open adminpage  *********")
        self.logger1.info("********* close adminpage  *********")
        self.ad2.setadmin("aaa","000","999","china@mail.com","999","sss","qq")
        self.ad2.enable()
        self.driver.close()

