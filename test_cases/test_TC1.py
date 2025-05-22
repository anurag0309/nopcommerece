from Base_Page.login_page import hrm_login_page
from test_cases.conftest import setup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
import time
class Testcase_valid_input:
    login_page_url = Read_Config.get_login_page_url()
    username = Read_Config.get_login_page_hrm_username()
    password = Read_Config.get_login_page_hrm_password()

    def test_check_username(self,setup):
        # try:
        self.driver = setup
        self.driver.get(self.login_page_url)
        self.login_page = hrm_login_page(self.driver)
        self.login_page.hrm_username(self.username)
        self.login_page.hrm_password(self.password)
        self.login_page.hrm_login_btn()
        # print('>>>>>>>>>>>>>>>>>>>>>>')
        # time.sleep(10)
        act_dashboard_text = self.driver.title
        print('act_dashboard_text: ',act_dashboard_text)
        if act_dashboard_text == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\screenshots\\test_valied_cred.png')
            self.driver.close()
            assert False
        # except:
        #     print('Exception')



