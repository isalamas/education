from selenium import webdriver
import unittest
from Pages.LoginPage import Login
from Utils.CustomLogger import LogGen
from Utils.ReadProperties import ReadConfig
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.headless = True
opt.add_argument('--disable-gpu')
opt.add_argument('--window-size=1280x1696')
driver = webdriver.Chrome(executable_path=r"C:\Users\LA\PycharmProjects\itworx education\Driver\chromedriver.exe", chrome_options=opt)
val = 20
driver.implicitly_wait(val)


class Logins(unittest.TestCase):
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL()

    def test_login(self):
        try:
            self.logger.info("**** start Login test ****")
            login = Login(driver)
            driver.get(self.baseURL)
            login.enter_email("testregister@aaa.com")
            login.enter_Password("Wakram_123")
            login.click_login()
            self.logger.info("**** Login test passed ****")

        except:
            self.logger.info("**** Login test Failed ****")
            driver.save_screenshot(".\\Screenshot\\" + "Login.png")
            raise TypeError("Login test Failed")

    @classmethod
    def tearDownClass(cls):
        driver.close()
        driver.quit()