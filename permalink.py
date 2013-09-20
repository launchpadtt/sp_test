import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class PermalinkTests(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_verify_permalink(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        permalink_text_box_elem = driver.find_element_by_id("permalinkTextBox")
        permalink_url = permalink_text_box_elem.get_attribute("value")
        driver.get(permalink_url)
        self.assertIn("TapHandle by ShapewaysCodeTest on Shapeways", driver.title)
        elem = driver.find_element_by_xpath("//div[@class='shop-info-title']//h2")
        self.assertIn("TapHandle", elem.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
