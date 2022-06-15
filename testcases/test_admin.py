
import pytest
import allure
from pageobjects.Admin import admin_org_geninfo
from pageobjects.Admin.login_org import Admin2
from TestCases.test_login import Test_login
#from pageobjects.Admin import addloc


@pytest.mark.usefixtures("test_logintopage")
@allure.severity(allure.severity_level.NORMAL)
class Test_admin(Test_login):

    # def test_admin_org(self):
    #     self.logger1.info("********* Open adminpage  *********")
    #     self.ad = admin_org.Admin_Org(self.driver)
    #     self.logger1.info("********* Open locationpage  *********")
    #     self.ad.setadmin("orange HRM","0000","9988776654","chinna@gmail.com","2345","vijayawada","vijayawada")

    def test_admin2(self):
        self.ad2 = Admin2(self.driver)
        self.logger1.error("********* Open adminpage  *********")
        self.logger1.info("********* close adminpage  *********")
        self.ad2.setadmin2()
        self.driver.close()



        # self.driver.close()
        #self.ad.search_loc("abcd","tenali")

        #self.driver.execute_script("arguments[0].scrollIntoView();",cntry)

    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_addloc(self):
    #     self.logger1.info("********* Open adminpage  *********")
    #     self.ad = admin_org.Admin_Org(self.driver)
    #     self.ad.setadmin()
    #     self.logger1.info("********* Open addlocation page  *********")
    #     #self.adloc=addloc.Add_Loc(self.driver)
    #     self.adloc.setloc("abcd","Andhra pradesh","tenali","Tenali","522201","123456789","999999","Not Applicable")


