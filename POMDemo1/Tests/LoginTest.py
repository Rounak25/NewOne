from selenium import webdriver
import unittest
import time

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        cls.driver = webdriver.Chrome(executable_path="C:/Users/cp/PycharmProjects/SeleniumPOM/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_Login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(3)
        driver.find_element_by_id("txtUsername").clear()
        time.sleep(3)
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").clear()
        time.sleep(3)
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()
        x = driver.title
        assert x == 'OrangeHRM'
        print(x)

#def test_tearDown():
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Accomplished")


#if "__name__" == "__main__":
    if __name__ == '__main__':
        unittest.main()
