from selenium import webdriver
import unittest
from Pages.LoginPage import Login
from Utils.CustomLogger import LogGen
from Utils.ReadProperties import ReadConfig
from selenium.webdriver.chrome.options import Options

opt = Options()
# opt.headless = True
opt.add_argument('--disable-gpu')
opt.add_argument('--window-size=1280x1696')
driver = webdriver.Chrome(executable_path=r"D:\Projects\EVO\Drivers\chromedriver.exe", chrome_options=opt)
val = 20
driver.implicitly_wait(val)


class SigningUp(unittest.TestCase):
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL()

    def test_signup(self):
        try:
            self.logger.info("**** start Login test ****")
            login = Login(driver)
            driver.get(self.baseURL)
            login.enter_email("testregister@aaa.com")
            login.enter_Password("Wakram_123")
            login.click_login()
            login.click_courses()
            login.click_add_courses()
            login.course_name("Automation Testing6")
            login.grades()
            login.course_teacher()
            login.click_save_courses()
            login.click_courses()
            self.logger.info("**** Login test passed ****")

        except:
            self.logger.info("**** Login test Failed ****")
            driver.save_screenshot(".\\Screenshot\\" + "Login.png")
            raise TypeError("Login test Failed")
