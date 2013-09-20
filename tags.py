import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re

class TagTests(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_verify_tags_list(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # get the list of tags
        tags_elems = driver.find_elements_by_xpath("//div[@class='keywords']//a")
        a_tags = []
        for a_tag_elem in tags_elems:
            a_tag_text = a_tag_elem.text
            a_tag_text = re.sub(',', '', a_tag_text)
            a_tags.append(a_tag_text)
        expected_a_tags = [u'Art', u'Accessories', u'Sculptures', u'For Your Home', u'Beer', u'Grumpy', u'Homebrew']
        self.assertEqual(sorted(a_tags), sorted(expected_a_tags), "The list of tags are not the expected list")
        driver.close()

    def test_verify_product_in_tag_list(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # get the list of tags
        homebrew_a_tag_elem = driver.find_element_by_xpath("//div[@class='keywords']//a[text() = 'Homebrew']")
        homebrew_a_tag_elem.click()
        self.assertIn("Shapeways | Search Results", driver.title)
        self.assertIn("TapHandle", driver.page_source)
        self.assertIn("$24.73", driver.page_source)
        self.assertIn("by ShapewaysCodeTest", driver.page_source)
        self.assertIn("This is one grumpy taphandle", driver.page_source)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
