from selenium.webdriver.common.by import By
import yaml

# Load the config
with open("G:/Selenimun Projects/OrangeHRM/configurations/locators_config.yml", "r") as locators_config_file:
    loc_config = yaml.safe_load(locators_config_file)


class hrm_login_page:
    def __init__(self,driver):
        self.driver = driver
    def hrm_username(self,username):
        self.driver.find_element(By.XPATH,loc_config["locators"]["loc_username"]).clear()
        self.driver.find_element(By.XPATH,loc_config["locators"]["loc_username"]).send_keys(username)
    def hrm_password(self,password):
        self.driver.find_element(By.XPATH,loc_config["locators"]["loc_password"]).clear()
        self.driver.find_element(By.XPATH,loc_config["locators"]["loc_password"]).send_keys(password)
    def hrm_login_btn(self):
        self.driver.find_element(By.XPATH,loc_config["locators"]["loc_login_btn"]).click()
