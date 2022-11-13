from selenium.webdriver.common.by import By


class LoginPageLocators:
    Email_Address = (By.ID, "Email")
    Password = (By.ID, "inputPassword")
    Login_Button = (By.ID, "btnLogin")
    Courses = (By.XPATH, "//a[@id='btnMyCoursesList']")
    Add_Course_Button = (By.ID, "btnListAddCourse")
    Course_Name = (By.ID, "txtCourseName")
    Select_Grade = (By.ID, "courseGrade")
    Higher_edu = (By.XPATH, "//option[normalize-space()='Higher Education']")
    Course_teacher = (By.XPATH, "//span[@aria-label='Course Teacher activate']")
    Teacher = (By.XPATH, "//a[@id='lblCourseOwnerProfilePic']")
    Save_button = (By.ID, "btnSaveAsDraftCourse")
    course_title = (By.XPATH, "body > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(11) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1)")



