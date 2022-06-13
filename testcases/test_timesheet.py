import time

import pytest
from selenium.webdriver.common.by import By

from testcases.test_login import Test_login

from pageobjects.Admin.Login_timesheet import  Time
#@pytest.mark.sanity
@pytest.mark.usefixtures("test_logintopage")
class Test_Time(Test_login):

    def test_time(self):
        self.T =Time(self.driver)
        self.T . timesheet()
        # drp_value = "Bug Fixes"
        # mon6_value = "2"
        #
        # self.T.table_data("Fresh",drp_value,mon6_value,"7","8","9","10","11","10")
        self.T.employeetimesheet("Russel Hamilton	")
        #self.driver.close()
