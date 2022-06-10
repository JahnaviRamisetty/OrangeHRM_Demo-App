import time

import pytest
from selenium.webdriver.common.by import By

from testcases.test_login import Test_login

from pageobjects.Admin.Login_timesheet import Time
#@pytest.mark.sanity
@pytest.mark.usefixtures("test_logintopage")
class Test_Time(Test_login):
    def test_time(self):
        self.T =Time(self.driver)
        self.T .time_login()