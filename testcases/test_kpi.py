import time

import pytest
from selenium.webdriver.common.by import By

from testcases.test_login import Test_login

from pageobjects.performance import configure
#@pytest.mark.sanity
@pytest.mark.usefixtures("test_logintopage")

class Test_KPI(Test_login):
    def test_kpi(self):
        self.perform = configure.Performance(self.driver)
        self.perform.setperformance()
        self.logger1.info("------open adminpage------")
        self.perform.kpi()
        name="Personally credible"
        self.logger1.info("-----delete the given name-----")
        self.perform. kpi_delete(name)
        self.driver.close()
