import time

import pytest
from selenium.webdriver.common.by import By

from testcases.test_login import Test_login

from pageobjects.performance import configure
#@pytest.mark.sanity
@pytest.mark.usefixtures("test_logintopage")

class Test_Tracker(Test_login):
    def test_tracker(self):
        self.perform = configure.Performance(self.driver)
        self.perform.setperformance()

        name = "Jadine Jackie"
        self.perform.settrack("commitments",name)
        self.perform.reuslt_table(name)
