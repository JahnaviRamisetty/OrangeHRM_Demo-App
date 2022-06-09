import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
class Time(BaseDriver):
    admin_btn_id = "menu_admin_viewAdminModule"
    time_id="menu_time_viewTimeModule"
    timesheets_id="menu_time_Timesheets"
    mytimesheet_id="menu_time_viewMyTimesheet"
    edit_id="btnEdit"
    empinfo_table = "//table[@class='table']"

    empinfo_tbcols = "//table[@class='table']//tbody/tr/td"
    empinfo_tbrows = "//table[@class='table']//tbody/tr"
    empinfo_tb_br1 = "["
    empinfo_tb_br2 = "]"
    empinfo_tb_cols = "/td"
    tb_col_tag = "td"
    tb_row_tag = "tr"
    project_id="initialRows_0_projectName"
    activity_id="initialRows_0_projectActivityName"
    mon6_xp = "//input[@id='initialRows_0_0']"
    tues_id="initialRows_0_1"
    employeetimesheet_id="menu_time_viewEmployeeTimesheet"
    employeename_id="employee"
    viewbtn_id="btnView"
    addtimesheet_id="btnAddTimesheet"
    calender_id="time_date"
    title_xp="//*[@id='ui-datepicker-div']/div/div"
    calenbox_xp="//*[@id='ui-datepicker-div']/table"
    ok_id="addTimesheetBtn"

    def __init__(self, driver):
        self.driver = driver

    def time_login(self):
        admin= self.driver.find_element(By.ID,self.admin_btn_id)
        time=self.driver.find_element(By.ID,self.time_id)
        time_sheet=self.driver.find_element(By.ID,self.timesheets_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(admin).move_to_element(time).move_to_element(time_sheet).click().perform()
    def timesheet(self):
        time = self.driver.find_element(By.ID, self.time_id)
        time_sheet = self.driver.find_element(By.ID, self.timesheets_id)
        mytime_sheet=self.driver.find_element(By.ID,self.mytimesheet_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(time).move_to_element(time_sheet).move_to_element(mytime_sheet).click().perform()
        self.driver.find_element(By.ID,self.edit_id).click()

    def table_data(self,value,mon,tues):

                drp_down1 = self.driver.find_element(By.ID, self.project_id)
                drp_down1.clear()
                drp_down1.send_keys("Apache")
                drp_down1.send_keys(Keys.ARROW_DOWN)
                drp_down1.send_keys(Keys.ENTER)
                drp_down = self.driver.find_element(By.ID, self.activity_id)
                drp_down.click()
                time.sleep(3)
                drp_down.send_keys(value)
                drp_down.send_keys(Keys.ENTER)

                self.driver.find_element(By.XPATH,self.mon6_xp).send_keys(mon)
                self.driver.find_element(By.ID,self.tues_id).send_keys(tues)
                # break

    def employeetimesheet(self,name):
        time= self.driver.find_element(By.ID, self.time_id)
        time_sheet = self.driver.find_element(By.ID, self.timesheets_id)
        employeetime_sheet = self.driver.find_element(By.ID, self.employeetimesheet_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(time).move_to_element(time_sheet).move_to_element(employeetime_sheet).click().perform()
        self.driver.find_element(By.ID,self.employeename_id).clear()
        self.driver.find_element(By.ID,self.employeename_id).send_keys(name)
        self.driver.find_element(By.ID,self.employeename_id).send_keys(Keys.ENTER)
       #time.sleep(3)
        self.driver.find_element(By.ID, self.viewbtn_id).click()
        self.driver.find_element(By.ID,self.addtimesheet_id).click()
        self.driver.find_element(By.ID,self.calender_id).click()
        self.driver.find_element(By.XPATH,self.title_xp).click()
        self.driver.find_element(By.XPATH,self.calenbox_xp).click()
        self.driver.find_element(By.ID,self.ok_id).click()









