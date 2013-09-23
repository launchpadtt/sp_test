import taphandle
import unittest

class PermalinkTests(unittest.TestCase):  
    def setUp(self):
        self.taphandle = taphandle.TapHandle("chrisyeem_test", "test_password")

    def test_verify_permalink(self):
        print "\nRunning the testcase 'Verify Permalink'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Get the permalink"
        permalink_url = taphandle.get_permalink()
        taphandle.driver.get(permalink_url)
        print "  Checking the permalink url's title is 'TapHandle by ShapewaysCodeTest on Shapeways'"
        self.assertIn("TapHandle by ShapewaysCodeTest on Shapeways", taphandle.get_page_title())
        print "  Checking the permalink url's page heading is 'TapHandle'"
        self.assertIn("TapHandle", taphandle.get_page_heading())
        taphandle.close_session()

#     def tearDown(self):
#         self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
