import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver

class Admin_Org(BaseDriver):
    admin_btn_id="menu_admin_viewAdminModule"
    org_btn_id="menu_admin_Organization"
    gen_info="menu_admin_viewOrganizationGeneralInformation"
    loc_btn_id="menu_admin_viewLocations"
    save_id_="btnSaveGenInfo"
    org_name="organization_name"
    org_tax="organization_taxId"
    org_phone="organization_phone"
    org_mail="organization_email"
    org_fax="organization_fax"
    org_stree="organization_street2"
    org_city="organization_city"
    org_save="btnSaveGenInfo"
    form_xp = "//*[@id='content']"
    tag_input_xp = "input"


    #ind_value="value"


    def __init__(self, driver):
        self.driver = driver

    def setadmin(self,name,tax,phone,mail,fax,street,city):
       admin= self.driver.find_element(By.ID,self.admin_btn_id)
       time.sleep(2)
       org=self.driver.find_element(By.ID,self.org_btn_id)
       time.sleep(2)
       geninfo=self.driver.find_element(By.ID,self.gen_info)
       # loc=self.driver.find_element(By.ID,self.loc_btn_id)
       # time.sleep(2)
       actions=ActionChains(self.driver)
       actions.move_to_element(admin).move_to_element(org).move_to_element(geninfo).click().perform()
       self.driver.find_element(By.ID,self.save_id_).click()
       self.driver.find_element(By.ID,self.org_name).clear()
       self.driver.find_element(By.ID,self.org_name).send_keys(name)
       self.driver.find_element(By.ID,self.org_tax).clear()
       self.driver.find_element(By.ID,self.org_tax).send_keys(tax)
       self.driver.find_element(By.ID,self.org_phone).clear()
       self.driver.find_element(By.ID,self.org_phone).send_keys(phone)
       self.driver.find_element(By.ID,self.org_mail).clear()
       self.driver.find_element(By.ID,self.org_mail).send_keys(mail)
       self.driver.find_element(By.ID,self.org_fax).clear()
       self.driver.find_element(By.ID,self.org_fax).send_keys(fax)
       self.driver.find_element(By.ID,self.org_stree).clear()
       self.driver.find_element(By.ID,self.org_stree).send_keys(street)
       self.driver.find_element(By.ID,self.org_city).clear()
       self.driver.find_element(By.ID,self.org_city).send_keys(city)
       self.driver.find_element(By.ID,self.org_save).click()

    def search(self, param):
        pass

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







