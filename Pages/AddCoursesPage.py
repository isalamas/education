from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.Locators import AddCoursesPageLocators


class AddCourse:
    def __init__(self, driver,):
        self.driver = driver
        self.locator = AddCoursesPageLocators
        self.wait = WebDriverWait(driver, 10)

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






