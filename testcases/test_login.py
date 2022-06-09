import time
import pytest

from pageobjects.loginpage import login
from utilites.readproperties import ReadConfig
from utilites.customlogger import LogGen
@pytest.mark.login
#@pytest.fixture(scope="function")
class Test_login():
    URL = ReadConfig.getApplicationURL()
    user = ReadConfig.getusername()
    pwd = ReadConfig.getpassword()
    logger1 = LogGen.loggen()

    @pytest.mark.login
    @pytest.fixture(scope="function")
    def test_logintopage(self,setup):
        self.logger1.info("********* Test_001_login *********")
        self.driver = setup
        self.driver.get(self.URL)
        self.logger1.info("********* Open Loginpage  *********")
        self.lp = login(self.driver)
        self.lp.setusername(self.user,self.pwd)
        self.logger1.info("********* Loginpage close *********")
        #self.driver.close()
        # self.lp.setpassword(self.pwd)
        # self.lp.clicklogin()
        # self.logger1.info("********* Successfully login  into the page *********")
        # time.sleep(3)
        # self.lp.click_logout_btn()
        # self.driver.close()


