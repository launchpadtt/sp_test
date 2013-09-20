import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re

class RelatedTests(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()

#     def test_verify_see_more_is_in_tags(self):
#         driver = self.driver
#         driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
#         see_more_link_elem = driver.find_element_by_xpath("//div[@class='see-more']//a")
#         see_more_link_text = see_more_link_elem.text
#         result = re.search(r'See\s+More\s+(.*)\s+', see_more_link_text)
#         see_more_tag = result.group(1)
# #         expected_a_tags = [u'Art', u'Accessories', u'Sculptures', u'For Your Home', u'Beer', u'Grumpy', u'Homebrew']
#         expected_a_tags = ['Art', 'Accessories', 'Sculptures', 'For Your Home', 'Beer', 'Grumpy', 'Homebrew']
#         self.assertTrue(see_more_tag in expected_a_tags, "The see more link is referring to a tag that is not one of the products's tags. See More Link Tag: '" + see_more_tag)
#         driver.close()
        
    def test_related_item_shares_a_tag(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # click on the related item
        related_item_div_elem = driver.find_element_by_xpath("//div[@id='favoriters']/following-sibling::div[1]/div[@class='grid-view']/div/div")
        related_item_div_elem.click()
        time.sleep(10)
#         # check its list of tags
#         tags_elems = driver.find_elements_by_xpath("//div[@class='keywords']//a")
#         a_tags = []
#         for a_tag_elem in tags_elems:
#             a_tag_text = a_tag_elem.text
#             a_tag_text = re.sub(',', '', a_tag_text).lower()
#             a_tags.append(a_tag_text)
#         # check whether any of its tags are in the list of tags of the sample item
#         expected_a_tags = [u'art', u'accessories', u'sculptures', u'for your home', u'beer', u'grumpy', u'homebrew']
#         self.assertFalse(set(a_tags).isdisjoint(expected_a_tags), "None of the tags in the related product are in the first sample product")
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
