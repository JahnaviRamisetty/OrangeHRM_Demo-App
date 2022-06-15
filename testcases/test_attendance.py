import pytest
from selenium.webdriver.common.by import By

from TestCases.test_login import Test_login

from pageobjects.Admin.Login_timesheet import  Time
@pytest.mark.usefixtures("test_logintopage")
class Test_Time(Test_login):

    def test_time(self):
        self.T =Time(self.driver)
        #self.T.attendance("Not applicable","Not applicable")
        self.T. employee_records("John smith")