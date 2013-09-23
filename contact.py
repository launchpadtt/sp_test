import taphandle
import unittest

class ContactTests(unittest.TestCase):  
    def setUp(self):
        self.taphandle = taphandle.TapHandle("chrisyeem_test", "test_password")
    
    def test_contact_designer_when_not_logged_in(self):
        print "\nRunning the testcase 'Contact the Designer when not logged in'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Clicking contact designer"
        taphandle.click_contact_designer()
        print "  Looking for the string 'Log In' in the page source"
        self.assertIn("Log In", taphandle.get_page_source())
        taphandle.close_session()
        

    def test_contact_designer_when_logged_in(self):
        print "\nRunning the testcase 'Contact the Designer when logged in'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Logging in"
        taphandle.login()
        # hit contact designer
        print "  Clicking contact designer"
        taphandle.click_contact_designer()
        
        # fill in the information
        print "  Filling in basic information for a message"
        taphandle.fill_in_contact_designer_message("Test Subject", "Test Message")
        # check that it took you to the Inbox page
        print "  Looking for the string 'Inbox' in the page source"
        self.assertIn("Inbox", taphandle.get_page_source())
        # check that sent folder to see if you actually sent that message 
        print "  Accessing sent messages"
        taphandle.access_sent_messages()
        print "  Looking for the string 'Test Subject' in the page source"
        self.assertIn("Test Subject", taphandle.get_page_source())
        taphandle.close_session()

#     def tearDown(self):
#         self.taphandle.close_session()

if __name__ == "__main__":
    unittest.main()
    
