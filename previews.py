import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class PreviewsTests(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_change_preview_by_selecting_picture_in_list(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")

    def test_change_preview_by_selecting_back(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")

    def test_change_preview_by_selecting_next(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")

    def test_change_preview_to_gif(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")

    def test_change_preview_to_video(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")

    def test_play_video_in_preview(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
