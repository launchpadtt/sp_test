import taphandle
import unittest
import time

class CommentsTests(unittest.TestCase):  
    def setUp(self):
        self.taphandle = taphandle.TapHandle("chrisyeem_test", "test_password")

    def test_comment_when_not_logged_in(self):
        print "\nRunning the testcase 'Comment when not logged in'"
        taphandle = self.taphandle
        taphandle.load()
        time.sleep(5)
        taphandle.fill_out_comment("Test Comment")
        print "  Checking that the page has 'Log In' in it"
        self.assertIn("Log In", taphandle.get_page_source())
        taphandle.close_session()
          
    def test_comment(self):
        print "\nRunning the testcase 'Comment when logged in'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Logging in"
        taphandle.login()
        # check the counter for the comments
        print "  Getting current number of comments"
        comments_counter_before = taphandle.get_comments_counter()
        # fill in the comment
        print "  Filling out the comment"
        taphandle.fill_out_comment("Test Comment")
        # check that the comment is good
        comment_text = taphandle.get_comment_text()
        print "  Checking that the comment is the expected comment"
        self.assertEqual(comment_text, "Test Comment", "There's no comment that was made by chrisyeem_test that matches the required text comment details")
        # check the counter for the comments
        taphandle.reload()
        comments_counter_after = taphandle.get_comments_counter()
        # check that the counter on the side has been incremented by one
        print "  Comparing the comments counter so that the comments before is one less than after"
        self.assertEqual(str(int(comments_counter_before) + 1), comments_counter_after, "The number of comments in the counter is not the incremented by one after adding the comment. Before: '" + comments_counter_before + "' After: '" + comments_counter_after + "'")
        # delete the comment for cleanup
        if (comment_text == "Test Comment"):
            taphandle.delete_comment()
        taphandle.close_session()
           
    def test_delete_a_comment(self):
        print "\nRunning the testcase 'Delete a comment'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Logging in"
        taphandle.login()
        # fill in the comment
        print "  Filling out the comment"
        taphandle.fill_out_comment("Test Comment to delete")
        # check that the comment is good
        comment_text = taphandle.get_comment_text()
        self.assertEqual(comment_text, "Test Comment to delete", "There's no comment that was made by chrisyeem_test that matches the required text comment details")
        # check the counter for the comments
        taphandle.reload()
        print "  Getting number of comments before the delete"
        comments_counter_before = taphandle.get_comments_counter()
        # delete the comment for cleanup
        if (comment_text == "Test Comment to delete"):
            taphandle.delete_comment()
#             driver.switch_to_window("TapHandle by ShapewaysCodeTest on Shapeways - Mozilla Firefox")
            try:
                comment_text = taphandle.get_comment_text()
            except:
                self.fail("There's still a comment that was created by chrisyeem_test, after attempting to delete the comment")
        # check the counter for the comments
        taphandle.reload()
        print "  Getting the number of comments after the delete"
        comments_counter_after = taphandle.get_comments_counter()
        # check that the counter on the side has been incremented by one
        print "  Checking that the number of comments after is one less than before"
        self.assertEqual(comments_counter_before, str(int(comments_counter_after) + 1), "The number of comments in the counter is not the incremented by one after adding the comment. Before: '" + comments_counter_before + "' After: '" + comments_counter_after + "'")
        taphandle.close_session()
   
    def test_comment_with_at_reply(self):
        print "\nRunning the testcase 'Comment with an @reply'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Logging in"
        taphandle.login()
        # check the counter for the comments
        print "  Getting current number of comments"
        comments_counter_before = taphandle.get_comments_counter()
        # fill in the comment
        print "  Adding comment with @reply"
        taphandle.fill_out_comment("@chrisyeem_test Test Comment")
        # check that the comment is good
        comment_text = taphandle.get_comment_text()
        print "  Checking that the comment text is right"
        self.assertEqual(comment_text, "@chrisyeem_test Test Comment", "There's no comment that was made by chrisyeem_test that matches the required text comment details Comment Text: '" + comment_text + "'")
        print "  Checking that the comment href is correct"
        comment_at_reply_elem = taphandle.driver.find_element_by_xpath("//strong[text() = 'chrisyeem_test']/../../../../div[@class='comment-body']/div[@class='comment-text']/a")
        comment_at_reply_href = comment_at_reply_elem.get_attribute("href")
        self.assertEqual(comment_at_reply_href, "https://www.shapeways.com/designer/chrisyeem_test", "The @reply does not point to the user's appropriate profile page. href: '" + comment_at_reply_href + "'")
        # check the counter for the comments
        taphandle.reload()
        print "  Getting the number of comments after adding the comment"
        comments_counter_after = taphandle.get_comments_counter()
        # check that the counter on the side has been incremented by one
        print "  Checking that the number of comments before is one less than after"
        self.assertEqual(str(int(comments_counter_before) + 1), comments_counter_after, "The number of comments in the counter is not the incremented by one after adding the comment. Before: '" + comments_counter_before + "' After: '" + comments_counter_after + "'")
        # delete the comment for cleanup
        if (comment_text == "@chrisyeem_test Test Comment"):
            print "  Deleting the comment for cleanup"
            taphandle.delete_comment()
        taphandle.close_session()
          
    def test_reply_button_to_an_existing_comment(self):
        print "\nRunning the testcase 'Reply button to an existing comment'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Logging in"
        taphandle.login()
        # click the reply button on the first reply by user named abbad
        taphandle.reply_comment("abbad")
        # check the text box
        comment_textarea_elem = taphandle.driver.find_element_by_id("commentBox")
        comment_text = comment_textarea_elem.get_attribute("value")
        self.assertEqual(comment_text, "@abbad ", "There's no comment that was made by chrisyeem_test that matches the required text comment details Comment Text: '" + comment_text + "'")
        taphandle.close_session()
      
    def test_flag_a_comment(self):
        print "\nRunning the testcase 'Reply button to an existing comment'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Logging in"
        taphandle.login()
        # click the flag button on the first reply by user named abbad
        taphandle.flag_comment("abbad")
        # check the text box
        self.assertIn("Shapeways", taphandle.get_page_title())
        self.assertIn("Flag this model as inappropriate", taphandle.get_page_source())
        taphandle.close_session()

if __name__ == "__main__":
    unittest.main()
    
