from selenium.webdriver.common.by import By

from Base.base_driver import BaseDriver


class login(BaseDriver):
    username_id = "txtUsername"
    password_id = "txtPassword"
    login_id = "btnLogin"
    logout_id="//*[@id='welcome']"
    logout = "//*[@id='welcome-menu']/ul/li[3]/a"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username,password):
         self.driver.find_element(By.ID, self.username_id).send_keys(username)
         self.driver.find_element(By.ID, self.password_id).send_keys(password)

         self.driver.find_element(By.ID, self.login_id).click()


def click_logout_btn(self):
        self.wait_until_element_is_clickable(By.XPATH,self.logout_id).click()
        self.wait_until_element_is_clickable(By.XPATH,self.logout).click()






