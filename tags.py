import taphandle
import unittest

class TagTests(unittest.TestCase):  
    def setUp(self):
        self.taphandle = taphandle.TapHandle("chrisyeem_test", "test_password")

    def test_verify_tags_list(self):
        print "\nRunning the testcase 'Verify tag list is the expected list'"
        taphandle = self.taphandle
        taphandle.load()
        # get the list of tags
        print "  Getting the items tags"
        a_tags = taphandle.get_tag_list()    
        expected_a_tags = [u'Art', u'Accessories', u'Sculptures', u'For Your Home', u'Beer', u'Grumpy', u'Homebrew']
        print "  Comparing the tags against the expected tags"
        self.assertEqual(sorted(a_tags), sorted(expected_a_tags), "The list of tags are not the expected list")
        taphandle.close_session()

    def test_verify_product_in_tag_list(self):
        print "\nRunning the testcase 'Verify product is in tag list'"
        taphandle = self.taphandle
        taphandle.load()
        # get the list of tags
        print "  Loading the Homebrew tag in the page"
        taphandle.load_tag_list("Homebrew")
        print "  Checking the title to see that it is 'Shapeways | Search Results'"
        self.assertIn("Shapeways | Search Results", taphandle.get_page_title())
        print "  Checking that the page has 'TapHandle' in it"
        self.assertIn("TapHandle", taphandle.get_page_source())
        print "  Checking that the page has '$24.73' in it"
        self.assertIn("$24.73", taphandle.get_page_source())
        print "  Checking that the page has 'by ShapewaysCodeTest' in it"
        self.assertIn("by ShapewaysCodeTest", taphandle.get_page_source())
        print "  Checking that the page has 'This is one grumpy taphandle' in it"
        self.assertIn("This is one grumpy taphandle", taphandle.get_page_source())
        taphandle.close_session()
        
#     def tearDown(self):
#         self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
