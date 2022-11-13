from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.Locators import LoginPageLocators


class Login:
    def __init__(self, driver,):
        self.driver = driver
        self.locator = LoginPageLocators
        self.wait = WebDriverWait(driver, 10)

    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.locator.Email_Address)).send_keys(email)

    def enter_Password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.locator.Password)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.locator.Login_Button)).click()






