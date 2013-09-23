import taphandle
import unittest

class LoadTests(unittest.TestCase):  
    def setUp(self):
        self.taphandle = taphandle.TapHandle("chrisyeem_test", "test_password", "Firefox")
    
    def test_verify_page_loads(self):
        print "\nRunning the testcase 'Verify that the page loads'"
        taphandle = self.taphandle
        taphandle.load()
        page_title = taphandle.get_page_title()
        print "  Looking for the title 'TapHandle by ShapewaysCodeTest on Shapeways' in the page title"
        self.assertIn("TapHandle by ShapewaysCodeTest on Shapeways", page_title)
        page_heading = taphandle.get_page_heading()
        print "  Looking for the page heading 'TapHandle' in the page header"
        self.assertIn("TapHandle", page_heading)

    def tearDown(self):
        self.taphandle.close_session()
        
if __name__ == "__main__":
    unittest.main()
    
