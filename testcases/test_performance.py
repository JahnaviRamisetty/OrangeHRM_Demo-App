import time

import pytest
from selenium.webdriver.common.by import By

from TestCases.test_login import Test_login

from pageobjects.performance import configure
#@pytest.mark.sanity
@pytest.mark.usefixtures("test_logintopage")
class Test_Performance(Test_login):
    def test_perform(self):
        self.perform =configure.Performance(self.driver)
        self.perform.setperformance()
        #self.per = configure.Perfor(self.driver)
        # name="Jadine Jackie"
        # self.per.settrack("commitments",name)
        # time.sleep(10)
        # self.per.reuslt_table(name)
        #assert  True == status
        #print(status)
