import pytest
import allure
from testcases.test_login import Test_login
from pageobjects.Admin.login_org import Admin2

@pytest.mark.usefixtures("test_logintopage")
class Test_Search(Test_login):

    def test_search(self):
        self.ad2 = Admin2(self.driver)
        self.ad2.setadmin2()
        self.ad2.user_data("goa")
        self.ad2.search_data("goa")
        name="pavan"
        self.ad2.loc_delete(name)