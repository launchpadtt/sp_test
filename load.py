import unittest
from selenium import webdriver

class LoadTests(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_verify_page_loads(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        self.assertIn("TapHandle by ShapewaysCodeTest on Shapeways", driver.title)
        elem = driver.find_element_by_class_name("shop-info-text")
        self.assertIn("TapHandle", elem.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
