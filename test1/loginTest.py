from selenium import webdriver
from time import sleep
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome('C:\chrome\chromedriver.exe')

    def test_find_login_page(self):
        driver = self.driver
        driver.get("https://w3schools.com/")
        driver.find_element_by_id('w3loginbtn').click()
        sleep(5)
        cur_url = driver.current_url
        expected_url = 'https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com'
        self.assertEqual(cur_url, expected_url )

    def test_login(self):
        driver = self.driver
        driver.get("https://profile.w3schools.com/log-in")
        driver.find_element_by_id('modalusername').send_keys("mohtasham_mohamad@yahoo.com")
        driver.find_element_by_id('current-password').send_keys("Mm_199069")
        driver.find_element_by_class_name('_1VfsI').click()
        sleep(5)
        cur_url = driver.current_url
        excepted_url = 'https://my-learning.w3schools.com/'
            
        self.assertEqual(cur_url, excepted_url)

    def test_catch_user_name(self):
        driver = self.driver
        driver.get("https://profile.w3schools.com/log-in")
        driver.find_element_by_id('modalusername').send_keys("mohtasham_mohamad@yahoo.com")
        driver.find_element_by_id('current-password').send_keys("Mm_199069")
        driver.find_element_by_class_name('_1VfsI').click()
        sleep(5)
        name = driver.find_element_by_id('profile-name').text
        correct_name = 'mohamad mohtasham'
        self.assertEqual(name, correct_name)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
        

