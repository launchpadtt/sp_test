import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class ContactTests(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_contact_designer_when_not_logged_in(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        elem = driver.find_element_by_xpath("//div[@class='send-message']/a")
        elem.click()
        time.sleep(2)
        self.assertIn("Log In", driver.page_source)
        self.driver.close()
        

    def test_contact_designer_when_logged_in(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # get the login dialog to display
        sign_in_elem = driver.find_element_by_link_text("Sign in")
        hover = ActionChains(driver).move_to_element(sign_in_elem)
        hover.perform()
        # fill out the username and password
        username_elem = driver.find_element_by_id("top_username")
        username_elem.send_keys("chrisyeem_test")
        password_elem = driver.find_element_by_id("top_password")
        password_elem.send_keys("test_password")
        # login
        log_in_elem = driver.find_element_by_xpath("//input[@value='Log in']")
        log_in_elem.click()
        time.sleep(2)
        # hit contact designer
        elem = driver.find_element_by_xpath("//div[@class='send-message']/a")
        elem.click()
        time.sleep(2)
        # fill in the information
        subject_elem = driver.find_element_by_xpath("//input[@name='msg_subject']")
        subject_elem.send_keys("Test Subject")
        body_elem = driver.find_element_by_id("txtb")
        body_elem.send_keys("Test Body")
        send_message_elem = driver.find_element_by_link_text("Send Message")
        send_message_elem.click()
        # check that it took you to the Inbox page
        self.assertIn("Inbox", driver.page_source)
        # check that sent folder to see if you actually sent that message 
        driver.find_element_by_xpath("//select[@name='folder_id']/option[text()='Sent']").click()
        go_link_elem = driver.find_element_by_xpath("//form//a[text()='Go']")
        go_link_elem.click()
        self.assertIn("Test Subject", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
