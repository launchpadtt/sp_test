import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class CommentsTests(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()

#     def test_comment_when_not_logged_in(self):
#         driver = self.driver
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         comment_textarea_elem = driver.find_element_by_id("commentBox")
#         comment_textarea_elem.click()
#         comment_textarea_elem.send_keys("Test Comment")
#         comment_textarea_elem = driver.find_element_by_id("submitComment")
#         comment_textarea_elem.click()
#         self.assertIn("Log In", driver.page_source)
#         driver.close()
#          
#     def test_comment(self):
#         driver = self.driver
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
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
#         # check the counter for the comments
#         counter_elem = driver.find_element_by_xpath("//a[@class='add-to-comments']/div")
#         comments_counter_before = counter_elem.text
#         # fill in the comment
#         comment_textarea_elem = driver.find_element_by_id("commentBox")
#         comment_textarea_elem.click()
#         comment_textarea_elem.send_keys("Test Comment")
#         comment_textarea_elem = driver.find_element_by_id("submitComment")
#         comment_textarea_elem.click()
#         time.sleep(2)
#         # check that the comment is good
#         comment_text_elem = driver.find_element_by_xpath("//strong[text() = 'chrisyeem_test']/../../../../div[@class='comment-body']/div[@class='comment-text']")
#         comment_text = comment_text_elem.text
#         self.assertEqual(comment_text, "Test Comment", "There's no comment that was made by chrisyeem_test that matches the required text comment details")
#         # check the counter for the comments
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         counter_elem = driver.find_element_by_xpath("//a[@class='add-to-comments']/div")
#         comments_counter_after = counter_elem.text
#         # check that the counter on the side has been incremented by one
#         self.assertEqual(str(int(comments_counter_before) + 1), comments_counter_after, "The number of comments in the counter is not the incremented by one after adding the comment. Before: '" + comments_counter_before + "' After: '" + comments_counter_after + "'")
#         # delete the comment for cleanup
#         if (comment_text == "Test Comment"):
#             delete_comment_button_elem = driver.find_element_by_xpath("//strong[text() = 'chrisyeem_test']/../../../../../div[@class='comment-wrap']/div[@class='clearfix']/div[@class='comment-tools']/div/a")
#             hover = ActionChains(driver).move_to_element(delete_comment_button_elem)
#             hover.perform()
#             delete_comment_button_elem.click()
#             alert_dialog = driver.switch_to_alert()
#             alert_dialog.accept()
#         driver.close()
#           
#     def test_delete_a_comment(self):
#         driver = self.driver
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
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
#         # fill in the comment
#         comment_textarea_elem = driver.find_element_by_id("commentBox")
#         comment_textarea_elem.click()
#         comment_textarea_elem.send_keys("Test Comment to delete")
#         comment_textarea_elem = driver.find_element_by_id("submitComment")
#         comment_textarea_elem.click()
#         time.sleep(2)
#         # check that the comment is good
#         comment_text_elem = driver.find_element_by_xpath("//strong[text() = 'chrisyeem_test']/../../../../div[@class='comment-body']/div[@class='comment-text']")
#         comment_text = comment_text_elem.text
#         self.assertEqual(comment_text, "Test Comment to delete", "There's no comment that was made by chrisyeem_test that matches the required text comment details")
#         # check the counter for the comments
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         counter_elem = driver.find_element_by_xpath("//a[@class='add-to-comments']/div")
#         comments_counter_before = counter_elem.text
#         # delete the comment for cleanup
#         if (comment_text == "Test Comment to delete"):
#             delete_comment_button_elem = driver.find_element_by_xpath("//strong[text() = 'chrisyeem_test']/../../../../../div[@class='comment-wrap']/div[@class='clearfix']/div[@class='comment-tools']/div/a")
#             hover = ActionChains(driver).move_to_element(delete_comment_button_elem)
#             hover.perform()
#             delete_comment_button_elem.click()
#             alert_dialog = driver.switch_to_alert()
#             alert_dialog.accept()
# #             driver.switch_to_window("TapHandle by ShapewaysCodeTest on Shapeways - Mozilla Firefox")
#             try:
#                 comment_text_elem = driver.find_element_by_xpath("//strong[text() = 'chrisyeem_test']/../../../../div[@class='comment-body']/div[@class='comment-text']")
#             except:
#                 self.fail("There's still a comment that was created by chrisyeem_test, after attempting to delete the comment")
#         # check the counter for the comments
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         counter_elem = driver.find_element_by_xpath("//a[@class='add-to-comments']/div")
#         comments_counter_after = counter_elem.text
#         # check that the counter on the side has been incremented by one
#         self.assertEqual(comments_counter_before, str(int(comments_counter_after) + 1), "The number of comments in the counter is not the incremented by one after adding the comment. Before: '" + comments_counter_before + "' After: '" + comments_counter_after + "'")
#         driver.close()
#   
    def test_comment_with_at_reply(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
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
        # check the counter for the comments
        counter_elem = driver.find_element_by_xpath("//a[@class='add-to-comments']/div")
        comments_counter_before = counter_elem.text
        # fill in the comment
        comment_textarea_elem = driver.find_element_by_id("commentBox")
        comment_textarea_elem.click()
        comment_textarea_elem.send_keys("@chrisyeem_test Test Comment")
        comment_textarea_elem = driver.find_element_by_id("submitComment")
        comment_textarea_elem.click()
        time.sleep(2)
        # check that the comment is good
        comment_text_elem = driver.find_element_by_xpath("//strong[text() = 'chrisyeem_test']/../../../../div[@class='comment-body']/div[@class='comment-text']")
        comment_text = comment_text_elem.text
        self.assertEqual(comment_text, "@chrisyeem_test Test Comment", "There's no comment that was made by chrisyeem_test that matches the required text comment details Comment Text: '" + comment_text + "'")
        comment_at_reply_elem = driver.find_element_by_xpath("//strong[text() = 'chrisyeem_test']/../../../../div[@class='comment-body']/div[@class='comment-text']/a")
        comment_at_reply_href = comment_at_reply_elem.get_attribute("href")
        self.assertEqual(comment_at_reply_href, "https://www.shapeways.com/designer/chrisyeem_test", "The @reply does not point to the user's appropriate profile page. href: '" + comment_at_reply_href + "'")
        # check the counter for the comments
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        counter_elem = driver.find_element_by_xpath("//a[@class='add-to-comments']/div")
        comments_counter_after = counter_elem.text
        # check that the counter on the side has been incremented by one
        self.assertEqual(str(int(comments_counter_before) + 1), comments_counter_after, "The number of comments in the counter is not the incremented by one after adding the comment. Before: '" + comments_counter_before + "' After: '" + comments_counter_after + "'")
        # delete the comment for cleanup
        if (comment_text == "Test Comment"):
            delete_comment_button_elem = driver.find_element_by_xpath("//strong[text() = 'chrisyeem_test']/../../../../../div[@class='comment-wrap']/div[@class='clearfix']/div[@class='comment-tools']/div/a")
            hover = ActionChains(driver).move_to_element(delete_comment_button_elem)
            hover.perform()
            delete_comment_button_elem.click()
            alert_dialog = driver.switch_to_alert()
            alert_dialog.accept()
        driver.close()
         
#     def test_reply_to_an_existing_comment(self):
#         driver = self.driver
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         driver.close()
#     
#     def test_flag_a_comment(self):
#         driver = self.driver
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         driver.close()
 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
