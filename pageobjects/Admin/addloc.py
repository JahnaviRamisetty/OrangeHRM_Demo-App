from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

class Add_Loc():
    add_loc_id = "btnAdd"
    name_id="location_name"
    cntry_id="location_country"
    state_id="location_province"
    city_id="location_city"
    add_id="location_address"
    zip_id="location_zipCode"
    phone_id="location_phone"
    fax_id="location_fax"
    notes_id="location_notes"
    save_id="btnSave"

    def __init__(self, driver):
        self.driver = driver
    def setloc(self,name,state,city,address,zip,phone,fax,notes):
        self.driver.find_element(By.ID, self.add_loc_id).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.name_id).send_keys(name)
        time.sleep(2)
        self.driver.find_element(By.ID, self.cntry_id).click()
        time.sleep(2)
        drp_down = Select(self.driver.find_element(By.ID, "location_country"))
        time.sleep(2)
        drp_down.select_by_value('IN')
        self.driver.find_element(By.ID, self.state_id).send_keys(state)
        time.sleep(2)
        self.driver.find_element(By.ID, self.city_id).send_keys(city)
        time.sleep(2)
        self.driver.find_element(By.ID, self.add_id).send_keys(address)
        time.sleep(2)
        self.driver.find_element(By.ID, self.zip_id).send_keys(zip)
        time.sleep(2)
        self.driver.find_element(By.ID, self.phone_id).send_keys(phone)
        time.sleep(2)
        self.driver.find_element(By.ID, self.fax_id).send_keys(fax)
        time.sleep(2)
        self.driver.find_element(By.ID,self.notes_id).send_keys(notes)
        time.sleep(2)
        self.driver.find_element(By.ID,self.save_id).click()
        time.sleep(2)
        self.driver.close()



