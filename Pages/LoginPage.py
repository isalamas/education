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

    def click_courses(self):
        self.wait.until(EC.element_to_be_clickable(self.locator.Courses)).click()

    def click_add_courses(self):
        self.wait.until(EC.element_to_be_clickable(self.locator.Add_Course_Button)).click()

    def course_name(self, coursename):
        self.wait.until(EC.element_to_be_clickable(self.locator.Course_Name)).send_keys(coursename)

    def grades(self):
        self.wait.until(EC.element_to_be_clickable(self.locator.Select_Grade)).click()
        self.wait.until(EC.element_to_be_clickable(self.locator.Higher_edu)).click()

    def course_teacher(self):
        self.wait.until(EC.element_to_be_clickable(self.locator.Course_teacher)).click()
        self.wait.until(EC.element_to_be_clickable(self.locator.Teacher)).click()

    def click_save_courses(self):
        self.wait.until(EC.element_to_be_clickable(self.locator.Save_button)).click()

    def course_name_exists(self):
        if self.wait.until(EC.visibility_of_element_located(self.locator.course_title)):
            return ModuleNotFoundError
        return False






