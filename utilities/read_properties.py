import yaml

# Load the config
with open("G:/Selenimun Projects/OrangeHRM/configurations/config.yml", "r") as file:
    config = yaml.safe_load(file)

class Read_Config:
    @staticmethod
    def get_login_page_url():
        # provide group name and varible name from config.ini file
        url = config['login']['hrm_url']
        # url = config.get(config['login']['hrm_url'])
        return url

    @staticmethod
    def get_login_page_hrm_username():
        # provide group name and varible name from config.ini file
        # hrm_username = config.get(config['login']['hrm_username'])
        hrm_username = config['login']['hrm_username']
        return hrm_username

    @staticmethod
    def get_login_page_hrm_password():
        # provide group name and varible name from config.ini file
        # hrm_password = config.get(config['login']['hrm_password'])
        hrm_password = config['login']['hrm_password']
        return hrm_password