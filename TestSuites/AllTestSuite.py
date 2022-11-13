import unittest
from Tests.TestLoginPage import Logins
from Tests.TestAddCoursesPage import AddCourses

tc1 = unittest.TestLoader().loadTestsFromTestCase(Logins)
tc2 = unittest.TestLoader().loadTestsFromTestCase(AddCourses)


smoketest = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner().run(smoketest)
