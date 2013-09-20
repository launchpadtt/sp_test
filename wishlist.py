import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class WishlistTests(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_add_to_wishlist_when_not_logged_in(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        wishlist_elem = driver.find_element_by_id("wishlistLink")
        wishlist_elem.click()
        time.sleep(2)
        # check whether you're at the sign up screen or whether you're still at the product page
        self.assertIn("Log In", driver.page_source)
        self.assertIn("Sign Up!", driver.page_source)
        self.assertIn("Already a member?", driver.page_source)
        driver.close()

    def test_add_to_wishlist_when_logged_in(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # log in
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
        # check if the item is already in the wishlist
        wishlist_elem = driver.find_element_by_id("wishlistLink")
        wishlist_text = wishlist_elem.text.strip()
        # if it is then remove it from the wishlist
        if (wishlist_text == "Added to Wishlist"):
            # remove it from the wishlist
            wishlist_elem.click()
            time.sleep(2)
            wishlist_tab_elem = driver.find_element_by_xpath("//div[@id='wishlist-top']/div/div[1]/div[2]/div")
#             wishlist_tab_elem = driver.find_element_by_id("//div[@class='wishlist-summary-border list-wishlist']/div")
            wishlist_tab_elem.click()
            time.sleep(5)
            remove_model_link_elem = driver.find_element_by_xpath("//a[@title='Remove Model']")
            remove_model_link_elem.click()
            driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # add it to the wishlist
        wishlist_elem = driver.find_element_by_id("wishlistLink")
        wishlist_elem.click()
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # check the product page to see if its added to wishlist or not
        wishlist_elem = driver.find_element_by_id("wishlistLink")
        wishlist_text = wishlist_elem.text.strip()
        self.assertEqual(wishlist_text, "Added to Wishlist", "The Wishlist section doesn't show that the item was added to the wishlist")
        # check the wishlist to see if its there
        wishlist_elem.click()
        wishlist_tab_elem = driver.find_element_by_xpath("//div[@id='wishlist-top']/div/div[1]/div[2]/div")
        wishlist_tab_elem.click()
        self.assertIn("TapHandle", driver.page_source)
        driver.close()

    def test_remove_from_wishlist_when_logged_in(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # log in
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
        # check if the item is not already in the wishlist
        wishlist_elem = driver.find_element_by_id("wishlistLink")
        wishlist_text = wishlist_elem.text.strip()
        # if it is then add it from the wishlist
        if (wishlist_text == "Wishlist"):
            wishlist_elem.click()
            time.sleep(2)
            driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # remove it from the wishlist
        wishlist_elem = driver.find_element_by_id("wishlistLink")
        wishlist_elem.click()
        time.sleep(2)
        wishlist_tab_elem = driver.find_element_by_xpath("//div[@id='wishlist-top']/div/div[1]/div[2]/div")
#             wishlist_tab_elem = driver.find_element_by_id("//div[@class='wishlist-summary-border list-wishlist']/div")
        wishlist_tab_elem.click()
        time.sleep(5)
        remove_model_link_elem = driver.find_element_by_xpath("//a[@title='Remove Model']")
        remove_model_link_elem.click()
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        wishlist_elem = driver.find_element_by_id("wishlistLink")
        wishlist_text = wishlist_elem.text.strip()
        self.assertEqual(wishlist_text, "Wishlist", "The Wishlist section doesn't show that the item was removed from the wishlist")
            
            
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
