import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
class Admin2(BaseDriver):
    admin_btn_id = "menu_admin_viewAdminModule"
    org_btn_id = "menu_admin_Organization"
    loc_btn_id = "menu_admin_viewLocations"
    country_id = "searchLocation_country"
    search_btn_id = "btnSearch"
    add_loc_id = "btnAdd"
    name_id = "location_name"
    cntry_id = "location_country"
    state_id = "location_province"
    city_id = "location_city"
    add_id = "location_address"
    zip_id = "location_zipCode"
    phone_id = "location_phone"
    fax_id = "location_fax"
    notes_id = "location_notes"
    save_id = "btnSave"
    rows_in_table = "//*[@id='resultTable']/tbody/tr"
    cols_in_table = "//*[@id='resultTable']/tbody/tr/td"
    loc_name = "//*[@id='searchLocation_city']"
    search_btn = "//*[@id='btnSearch']"
    # Table data search results locators
    empinfo_table = "//table[@id='resultTable']"
    empinfo_tbcols = "//table[@id='resultTable']//tbody/tr/td"
    empinfo_tbrows = "//table[@id='resultTable']//tbody/tr"
    empinfo_tb_br1 = "["
    empinfo_tb_br2 = "]"
    empinfo_tb_cols = "/td"
    tb_col_tag = "td"
    tb_row_tag = "tr"
    popUpLocationsPageDeleteOkBtn = "//*[@id='dialogDeleteBtn']"
    success_notification_msg="//*[@id='content']"
    # tb_xp = "//table[@id='customers']//tbody/tr[" + str(r) + "]/td[1]"
    # Delete Employee locators
    elist_delete = "//input[@id='btnDelete']"
    loc_chkbox_xp ="//preceding-sibling::td//input"
    elist_chckbx = "//input[@value='']"
    loc_linktext_click="/a"
    edit_name="btnSave"
    editlocation_name="location[name]"
    country_name="location[country]"
    save_name="btnSave"
    form_xp = "//form[@id='frmLocation']"
    tag_input_xp = "input"
    tag_select_xp="select"


    def __init__(self, driver):
      self.driver = driver

    def setadmin2(self):
       admin= self.driver.find_element(By.ID,self.admin_btn_id)
       #time.sleep(2)
       org=self.driver.find_element(By.ID,self.org_btn_id)
       time.sleep(1)
       loc=self.driver.find_element(By.ID,self.loc_btn_id)
       time.sleep(1)
       actions = ActionChains(self.driver)
       actions.move_to_element(admin).move_to_element(org).move_to_element(loc).click().perform()
       # self.driver.close()

    def add_loc(self,name, state, city, address, zip, phone, fax, notes):
        self.driver.find_element(By.ID, self.add_loc_id).click()
        self.driver.find_element(By.ID, self.name_id).send_keys(name)
        self.driver.find_element(By.ID, self.cntry_id).click()
        time.sleep(1)
        drp_down = Select(self.driver.find_element(By.ID, "location_country"))
        time.sleep(1)
        drp_down.select_by_value('IN')
        self.driver.find_element(By.ID, self.state_id).send_keys(state)
        time.sleep(2)
        self.driver.find_element(By.ID, self.city_id).send_keys(city)
       #time.sleep(1)
        self.driver.find_element(By.ID, self.add_id).send_keys(address)
       #time.sleep(2)
        self.driver.find_element(By.ID, self.zip_id).send_keys(zip)
        time.sleep(1)
        self.driver.find_element(By.ID, self.phone_id).send_keys(phone)
        time.sleep(1)
        self.driver.find_element(By.ID, self.fax_id).send_keys(fax)
        time.sleep(1)
        self.driver.find_element(By.ID, self.notes_id).send_keys(notes)
        time.sleep(1)
        self.driver.find_element(By.ID, self.save_id).click()
        time.sleep(1)

    def verify_addlocation(self):
        self.data = self.driver.find_element(By.XPATH, self.success_notification_msg).text
        # print(self.data, end=' ')
        print(self.data)

        if 'Successfully Saved' in self.data:
            assert True
            print("success")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "locationadding in ORANGEhrm.png")  # Screenshot
            assert False

        self.driver.close()


    def search_data(self, name):
        self.driver.find_element(By.XPATH, self.loc_name).send_keys(name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.search_btn).click()
        time.sleep(1)

    def user_data(self,name):
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.empinfo_table)
        rows = result_table.find_elements(By.TAG_NAME, self.tb_row_tag)
        rows_count = len(rows)
        # print(rows_count)
        print("Name" + "      " + "city" + "       " + "Country" + "       " + "Phone number" + "       " + "Number of emploees")
        for r in range(1, rows_count):
            cols = rows[r].find_elements(By.TAG_NAME, self.tb_col_tag)
            cols_count = len(cols)
            # print(cols_count)
            for c in range(1, cols_count):
                col_value = self.driver.find_element(By.XPATH, self.empinfo_tbrows + self.empinfo_tb_br1 + str(r)
                                                     + self.empinfo_tb_br2 +self.empinfo_tb_cols + self.empinfo_tb_br1
                                                     + str(3) + self.empinfo_tb_br2)
                value = col_value.text
                if value == name:
                    print(cols[c].text,  end="         ")

            print()

    def loc_delete(self, loc_name):
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.empinfo_table)
        rows = result_table.find_elements(By.TAG_NAME, self.tb_row_tag)
        rows_count = len(rows)
        for r in range(1, rows_count):
            # cols = rows[r].find_elements(By.TAG_NAME, self.tb_col_tag)
            # cols_count = len(cols)
            # print(cols_count)

            chkvalue_xpath = self.empinfo_tbrows + self.empinfo_tb_br1 + str(r)+ self.empinfo_tb_br2 + self.empinfo_tb_cols + self.empinfo_tb_br1\
                                 + str(2) + self.empinfo_tb_br2
            chkvalue_xpath2 = self.empinfo_tbrows + self.empinfo_tb_br1 + str(r)+ self.empinfo_tb_br2 + self.empinfo_tb_cols+ self.loc_chkbox_xp
                #"//table[@id='resultTable']//tbody/tr["+str(r)+"]/td//preceding-sibling::td//input"
            col_chkvalue = self.driver.find_element(By.XPATH,chkvalue_xpath)
            checkbox_value = col_chkvalue.text
            # print(checkbox_value)
            if checkbox_value == loc_name:
                    self.driver.find_element(By.XPATH, chkvalue_xpath2).click()
                    time.sleep(3)
                    self.driver.find_element(By.XPATH,self.elist_delete).click()
                    time.sleep(2)
                    self.driver.find_element(By.XPATH,self.popUpLocationsPageDeleteOkBtn).click()
                    time.sleep(5)

                    print("deleted one thing")
                    # self.driver.close()

    def clicklink(self,loc_name):
        result_table = self.wait_until_element_is_clickable(By.XPATH, self.empinfo_table)
        rows = result_table.find_elements(By.TAG_NAME, self.tb_row_tag)
        rows_count = len(rows)
        for r in range(1, rows_count):
            chkvalue_xpath = self.empinfo_tbrows + self.empinfo_tb_br1 + str(r) + self.empinfo_tb_br2 + self.empinfo_tb_cols + self.empinfo_tb_br1 \
                                  + str(2) + self.empinfo_tb_br2
            #chkvalue_xpath2 = self.empinfo_tbrows + self.empinfo_tb_br1 + str(r) + self.empinfo_tb_br2 +self.empinfo_tb_cols+ self.loc_chkbox_xp
            col_chkvalue = self.driver.find_element(By.XPATH, chkvalue_xpath)
            checkbox_value = col_chkvalue.text
            if checkbox_value == loc_name:
                # print(checkbox_value)
                    #self.driver.find_element(By.XPATH, chkvalue_xpath2).click()
                    # time.sleep(3)
                    # self.driver.find_element(By.LINK_TEXT,self.loc_linktext_click).click()
                self.driver.find_element(By.XPATH, self.empinfo_tbrows +self.empinfo_tb_br1 + str(r) + self.empinfo_tb_br2 + self.empinfo_tb_cols+ self.loc_linktext_click).click()
                break
            self.driver.find_element(By.NAME,self.edit_name).click()
        # self.driver.find_element(By.NAME,self.editlocation_name).clear()
        # self.driver.find_element(By.NAME,self.editlocation_name).send_keys(name)
        # self.driver.find_element(By.NAME, self.country_name).click()
        # drp_down = Select(self.driver.find_element(By.NAME, "location[country]"))
        # time.sleep(1)
        # drp_down.select_by_value("IN")
        # self.driver.find_element(By.NAME,self.save_name).click()

    def enable(self):
        pd_form = self.driver.find_element(By.XPATH, self.form_xp)
        all_text = pd_form.find_elements(By.TAG_NAME, self.tag_input_xp)
        fsize = len(all_text)
        print(fsize)
        for i in all_text:
            verify = i.is_enabled()
            text = i.get_attribute("id")
            if verify == False:
                print(text, verify, "Element is Disabled")
            else:
                print(text, verify, "Element is enabled")




