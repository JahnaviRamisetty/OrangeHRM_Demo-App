from selenium.webdriver import ActionChains, Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Base.base_driver import BaseDriver
class Performance(BaseDriver):
    per_bt_id="menu__Performance"
    config_bt_id="menu_performance_Configure"
    Kpi_bt_id="menu_performance_searchKpi"
    jobtitle_bt_xpath="//select[@id='kpi360SearchForm_jobTitleCode']"
    search_id="searchBtn"
    tracker_id="menu_performance_addPerformanceTracker"
    add_id="btnAdd"
    trackername_name="addPerformanceTracker[tracker_name]"
    employee_name="addPerformanceTracker[employeeName][empName]"
    box_id="addPerformanceTracker_availableEmp"
    box_name="John Smith"
    add__id="btnAssignEmployee"
    save_btn="btnSave"
    result_table = "//table[@id='resultTable']"
    result_table_rows= "//table[@id='resultTable']//tbody/tr"
    result_table_cols = "//table[@id='resultTable']//tbody/tr/td"
    total_table="//table[@id='resultTable']"
    empinfo_tb_br1 = "["
    empinfo_tb_br2 = "]"
    empinfo_tb_cols = "/td"
    tb_col_tag = "td"
    tb_row_tag = "tr"
    delete_id="//input[@id='btnDelete']"
    loc_linktext_click = "/a"
    popUpLocationsPageDeleteOkBtn = "//input[@id='dialogDeleteBtn']"
    loc_chkbox_xp = "//preceding-sibling::td//input"
    elist_chckbx = "//input[@value='']"
    linktext_jobtitle_id="defineKpi360_jobTitleCode"
    linktext_keyperformance_name="defineKpi360[keyPerformanceIndicators]"
    save_id="saveBtn"
    searchdropdown_id="kpi360SearchForm_jobTitleCode"
    searchbtn_id="searchBtn"
    hide="//a[@ class ='toggle tiptip activated']"
    edit_btn = "//input[@id='btnSave']"
    form_xp = "//form[@id='frmEmpPersonalDetails']"
    tag_input_xp = "input"

    def __init__(self, driver):
        self.driver = driver

    def __init__(self, driver):
        self.driver = driver

    def setperformance(self):
        perf = self.driver.find_element(By.ID, self. per_bt_id)
        self.driver.maximize_window()
        config= self.driver.find_element(By.ID, self.config_bt_id)
        time.sleep(2)
        kpi = self.driver.find_element(By.ID, self.Kpi_bt_id)
        #kpi= self.driver.find_element(By.ID, self.Kpi_bt_id)
        #time.sleep(2)
        actions = ActionChains(self.driver)
        actions.move_to_element(perf).move_to_element(config).move_to_element(kpi).click().perform()

    def kpi(self):
        config = self.driver.find_element(By.ID, self.config_bt_id)
        kpi=self.driver.find_element(By.ID,self.Kpi_bt_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(config).move_to_element(kpi).click().perform()
        drp_down = Select(self.wait_until_element_is_clickable(By.XPATH, self.jobtitle_bt_xpath))
        drp_down.select_by_visible_text("HR Associate")
        #drp_down.select_by_value(8)
        self.driver.find_element(By.ID,self.search_id).click()


    def settrack(self,name,empname):
       # perf = self.driver.find_element(By.ID, self.per_bt_id)
        config = self.driver.find_element(By.ID, self.config_bt_id)
        track = self.driver.find_element(By.ID, self.tracker_id)
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.move_to_element(config).move_to_element(track).click().perform()
        time.sleep(2)
        #config = self.driver.find_element(By.ID, self.config_bt_id)
        #tracker=self.driver.find_element(By.ID, self.tracker_id)
        self.driver.find_element(By.ID,self.add_id).click()
        self.driver.find_element(By.NAME,self.trackername_name).send_keys(name)
        #employeename = "Ananya Dash"
        employeename=self.driver.find_element(By.NAME,self.employee_name)
        employeename.send_keys(empname)
        employeename.send_keys(Keys.ARROW_DOWN)
        employeename.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.ID,self.box_id).send_keys(self.box_name)
        time.sleep(2)

        self.driver.find_element(By.ID,self.add__id).click()
        time.sleep(1)
        self.driver.find_element(By.ID,self.save_btn).click()
        time.sleep(1)



    def reuslt_table(self, name):
        print("employee"+"        "+"tracker"+"       "+"added date"+"          "+"          "+"Modified date")
        #for r in range(1, self.getrow_count() + 1):
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.result_table)
        rows = result_table.find_elements(By.TAG_NAME, "tr")
        rows_count = len(rows)
        for r in range(1, rows_count, 1):
            cols = rows[r].find_elements(By.TAG_NAME, "td")
            cols_count = len(cols)
            for c in range(1, cols_count, 1):
                value = cols[c].text
                print(value, end="      ")
            print('\n')

    def kpi_delete(self,indicator):

        result_table=self.driver.find_element(By.XPATH,self.total_table)
        rows = result_table.find_elements(By.TAG_NAME, self.tb_row_tag)
        rows_count = len(rows)

        for r in range(1, rows_count):
            chkvalue_xpath = self.result_table_rows + self.empinfo_tb_br1 + str(r) + self.empinfo_tb_br2 + self.empinfo_tb_cols + self.empinfo_tb_br1 \
                                + str(2) + self.empinfo_tb_br2
            chkvalue_xpath2 = self.result_table_rows + self.empinfo_tb_br1 + str(r) + self.empinfo_tb_br2 + self.empinfo_tb_cols + self.loc_chkbox_xp

            col_chkvalue = self.driver.find_element(By.XPATH, chkvalue_xpath)
            checkbox_value = col_chkvalue.text
            if checkbox_value == indicator:
              self.driver.find_element(By.XPATH, chkvalue_xpath2).click()
              time.sleep(3)
              self.driver.find_element(By.XPATH, self.delete_id).click()
              time.sleep(2)
              self.driver.find_element(By.XPATH, self.popUpLocationsPageDeleteOkBtn).click()

              print("deleted one thing")
    def clicklink(self,loc_name,keyperformance):
        #self.driver.find_element(By.CLASS_NAME,self.hide).click()
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.result_table)
        rows = result_table.find_elements(By.TAG_NAME, self.tb_row_tag)
        rows_count = len(rows)
        for r in range(1, rows_count):
            chkvalue_xpath = self. result_table_rows + self.empinfo_tb_br1 + str(r) + self.empinfo_tb_br2 + self.empinfo_tb_cols + self.empinfo_tb_br1 \
                                  + str(2) + self.empinfo_tb_br2
            #chkvalue_xpath2 = self.empinfo_tbrows + self.empinfo_tb_br1 + str(r) + self.empinfo_tb_br2 +self.empinfo_tb_cols+ self.loc_chkbox_xp
            col_chkvalue = self.driver.find_element(By.XPATH, chkvalue_xpath)
            checkbox_value = col_chkvalue.text
            if checkbox_value == loc_name:
                # print(checkbox_value)
                    #self.driver.find_element(By.XPATH, chkvalue_xpath2).click()
                    # time.sleep(3)
                    # self.driver.find_element(By.LINK_TEXT,self.loc_linktext_click).click()
                self.driver.find_element(By.XPATH, self. result_table_rows +self.empinfo_tb_br1 + str(r) + self.empinfo_tb_br2 + self.empinfo_tb_cols+ self.loc_linktext_click).click()
                break
        drp_down = Select(self.wait_until_element_is_clickable(By.ID, self.linktext_jobtitle_id))
        drp_down.select_by_visible_text("Chief Financial Officer")
        time.sleep(2)
        self.driver.find_element(By.NAME,self.linktext_keyperformance_name).clear()
        self.driver.find_element(By.NAME, self.linktext_keyperformance_name).send_keys(keyperformance)
        time.sleep(2)
        self.driver.find_element(By.ID,self.save_id).click()
        drp_down = Select(self.wait_until_element_is_clickable(By.ID, self.searchdropdown_id))
        time.sleep(2)
        drp_down.select_by_visible_text("QA Engineer")
        self.driver.find_element(By.ID,self. searchbtn_id).click()

        # def all_fields_verify(self):
        #     pd_form = self.driver.find_element(By.XPATH, self.form_xp)
        #     all_text = pd_form.find_elements(By.TAG_NAME, self.tag_input_xp)
        #     fsize = len(all_text)
        #     print(fsize)
        #     for i in all_text:
        #         verify = i.is_enabled()
        #         text = i.get_attribute("name")
        #         if verify == False:
        #             print(text, verify, "Element is Disabled")
        #         else:
        #             print(text, verify, "Element is enabled")
        #

