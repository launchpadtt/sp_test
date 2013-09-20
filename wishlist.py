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
        if (wishlist_text == "Added To Wishlist"):
            # remove it from the wishlist
            wishlist_elem.click()
            # selenium doesn't support compound classes and there's no ids anywhere near the wishlist div
            # hence this hideous xpath
            wishlist_tab_elem = driver.find_element_by_id("//div[@id='wishlist-top']/div/div[1]/div[2]")
            wishlist_tab_elem.click()
            remove_model_link_elem = driver.find_element_by_xpath("//a[@title='Remove Model']")
            remove_model_link_elem.click()
            driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # add it to the wishlist
        wishlist_elem = driver.find_element_by_id("wishlistLink")
        wishlist_elem.click()
        # check the product page to see if its added to wishlist or not
        wishlist_elem = driver.find_element_by_id("wishlistLink")
        wishlist_text = wishlist_elem.text.strip()
        self.assertEqual(wishlist_text, "Added To Wishlist", "The Wishlist section doesn't show that the item was added to the wishlist")
        # check the wishlist to see if its there
        wishlist_elem.click()
        wishlist_tab_elem = driver.find_element_by_id("//div[@id='wishlist-top']/div/div[1]/div[2]")
        wishlist_tab_elem.click()
        self.assertIn("TapHandle", driver.page_source)
        driver.close()

#     def test_favorite_when_not_logged_in(self):
#         driver = self.driver
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         # check the number of favorites before logging in
#         favorites_count_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']//div[@class='counter']")
#         no_of_favorites = favorites_count_elem.text
#         # favorite the item
#         favorites_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']")
#         favorites_elem.click()
#         time.sleep(2)
#         # check whether you're at the sign up screen or whether you're still at the product page
#         self.assertIn("Log In", driver.page_source)
#         self.assertIn("Sign Up!", driver.page_source)
#         self.assertIn("Already a member?", driver.page_source)
#         # check the number of favorites after attempting to favorite the item
#         driver.close()
# Already a member?
#     def test_favorite_when_logged_in(self):
#         driver = self.driver
#         driver.implicitly_wait(10)
#         driver.maximize_window()
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         # login
#         # get the login dialog to display
#         sign_in_elem = driver.find_element_by_link_text("Sign in")
#         hover = ActionChains(driver).move_to_element(sign_in_elem)
#         hover.perform()
#         # fill out the username and password
#         username_elem = driver.find_element_by_id("top_username")
#         username_elem.send_keys("chrisyeem_test")
#         password_elem = driver.find_element_by_id("top_password")
#         password_elem.send_keys("test_password")
#         # login
#         log_in_elem = driver.find_element_by_xpath("//input[@value='Log in']")
#         log_in_elem.click()
#         time.sleep(2)
#         # check whether the item is favorited
# #         " Favorite            "
# #         " Added to Favorites            "
#         favorites_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']")
#         favorites_array = favorites_elem.text.strip().split()[:-1]
#         favorites_text = ' '.join(favorites_array)
#         if (favorites_text == "Added to Favorites"):
#             favorites_elem.click()
#             time.sleep(2)
#             remove_link_elem = driver.find_element_by_xpath("//div[@class='remove-model']//a[text() = 'Remove']")
#             remove_link_elem.click()
#             time.sleep(2)
#             driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         # check the number of favorites before favorites before
#         favorites_count_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']//div[@class='counter']")
#         no_of_favorites_before = favorites_count_elem.text
#         # favorite the item
#         favorites_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']")
#         favorites_elem.click()
#         time.sleep(2)
#         # go back to the product page
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         # check whether you're at the sign up screen or whether you're still at the product page
#         self.assertNotIn("Log In", driver.page_source)
#         self.assertNotIn("Sign Up!", driver.page_source)
#         self.assertNotIn("Already a member?", driver.page_source)
#         self.assertIn("TapHandle", driver.page_source)
#         # check the number of favorites after attempting to favorite the item 
#         favorites_count_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']//div[@class='counter']")
#         no_of_favorites_after = favorites_count_elem.text
#         self.assertEqual(str(int(no_of_favorites_before) + 1), str(no_of_favorites_after), "The number of favorites before is not one less than the number of favorites after. Before: '" + str(no_of_favorites_before) + "' After: '" + str(no_of_favorites_after) + "'")
#         driver.close()
#          
#     def test_unfavorite_when_logged_in(self):
#         driver = self.driver
#         driver.implicitly_wait(10)
#         driver.maximize_window()
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         # login
#         # get the login dialog to display
#         sign_in_elem = driver.find_element_by_link_text("Sign in")
#         hover = ActionChains(driver).move_to_element(sign_in_elem)
#         hover.perform()
#         # fill out the username and password
#         username_elem = driver.find_element_by_id("top_username")
#         username_elem.send_keys("chrisyeem_test")
#         password_elem = driver.find_element_by_id("top_password")
#         password_elem.send_keys("test_password")
#         # click to login
#         log_in_elem = driver.find_element_by_xpath("//input[@value='Log in']")
#         log_in_elem.click()
#         time.sleep(2)
#         # check whether the item is favorited
#         favorites_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']")
#         favorites_array = favorites_elem.text.strip().split()[:-1]
#         favorites_text = ' '.join(favorites_array).strip()
#         # if it is not favorited, then favorite it
#         if (favorites_text == "Favorite"):
#             favorites_elem.click()
#             driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         # check the number of favorites
#         favorites_count_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']//div[@class='counter']")
#         no_of_favorites_before = favorites_count_elem.text
#         # then unfavorite it
#         favorites_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']")
#         favorites_elem.click()
#         remove_link_elem = driver.find_element_by_xpath("//div[@class='remove-model']//a[text() = 'Remove']")
#         remove_link_elem.click()
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         # check the number of favorites
#         favorites_count_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']//div[@class='counter']")
#         no_of_favorites_after = favorites_count_elem.text
#         self.assertEqual(str(no_of_favorites_before), str(int(no_of_favorites_after) + 1), "The number of favorites after is not one less than the number of favorites before. Before: '" + str(no_of_favorites_before) + "' After: '" + str(no_of_favorites_after) + "'")
#         driver.close()
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
