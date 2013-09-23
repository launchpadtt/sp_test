import taphandle
import unittest
import re

class RelatedTests(unittest.TestCase):  
    def setUp(self):
        self.taphandle = taphandle.TapHandle("chrisyeem_test", "test_password")

    def test_verify_see_more_is_in_tags(self):
        print "\nRunning the testcase 'Verify See More ... Link is choosing among existing tags'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Pulling out the tag from the See More Link"
        see_more_link_text = taphandle.get_see_more_link()
        result = re.search(r'See\s+More\s+(.*)\s+', see_more_link_text)
        see_more_tag = result.group(1)
#         expected_a_tags = [u'Art', u'Accessories', u'Sculptures', u'For Your Home', u'Beer', u'Grumpy', u'Homebrew']
        expected_a_tags = ['Art', 'Accessories', 'Sculptures', 'For Your Home', 'Beer', 'Grumpy', 'Homebrew']
        print "  Comparing the See More link to the expected tags"
        self.assertTrue(see_more_tag in expected_a_tags, "The see more link is referring to a tag that is not one of the products's tags. See More Link Tag: '" + see_more_tag)
        taphandle.close_session()
        
    def test_related_item_shares_a_tag(self):
        print "\nRunning the testcase 'Verify related item shares a tag with existing item'"
        taphandle = self.taphandle
        taphandle.load()
        # click on the related item
        print "  Loading the related item"
        taphandle.load_related_item()
        # check its list of tags
        print "  Getting the related items tags"
        a_tags_normal = taphandle.get_tag_list()    
        a_tags = [x.lower() for x in a_tags_normal]
        # check whether any of its tags are in the list of tags of the sample item
        expected_a_tags = [u'art', u'accessories', u'sculptures', u'for your home', u'beer', u'grumpy', u'homebrew']
        print "  Comparing the tags against the expected list of tags to see if there's an intersection"
        self.assertFalse(set(a_tags).isdisjoint(expected_a_tags), "None of the tags in the related product are in the first sample product")
        taphandle.close_session()
        
#     def tearDown(self):
#         self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
