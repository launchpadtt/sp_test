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
        # get the image that is in the slideshow bug section
        big_image_elem = driver.find_element_by_xpath("//div[@id='slideshow-big']//img[@class='film-strip-img']")
        orig_big_image_url = big_image_elem.get_attribute("src")
        # click on the first image in the list
        first_image_elem = driver.find_element_by_id("picThumb0")
        first_image_elem.click()
        # get the image that should now be in the slideshow bug section
        big_image_elem = driver.find_element_by_xpath("//div[@id='slideshow-big']//img[@class='film-strip-img']")
        new_big_image_url = big_image_elem.get_attribute("src")
        self.assertNotEqual(orig_big_image_url, new_big_image_url, "The big image preview did not change even though the option was selected")
        self.driver.close()

    def test_change_preview_by_selecting_next(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # make sure that the first picture is selected
        first_image_elem = driver.find_element_by_id("picThumb0")
        first_image_elem.click()
        # get the image that is in the slideshow bug section
        big_image_elem = driver.find_element_by_xpath("//div[@id='slideshow-big']//img[@class='film-strip-img']")
        orig_big_image_url = big_image_elem.get_attribute("src")
        # click on the back button
        first_image_elem = driver.find_element_by_id("slideShowRight")
        first_image_elem.click()
        # get the image that should now be in the slideshow bug section
        big_image_elem = driver.find_element_by_xpath("//div[@id='slideshow-big']//img[@class='film-strip-img']")
        new_big_image_url = big_image_elem.get_attribute("src")
        self.assertNotEqual(orig_big_image_url, new_big_image_url, "The big image preview did not change even though the option was selected")
        self.driver.close()
 
    def test_change_preview_by_selecting_back(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # make sure that the second picture is selected
        first_image_elem = driver.find_element_by_id("picThumb1")
        first_image_elem.click()
        # get the image that is in the slideshow bug section
        big_image_elem = driver.find_element_by_xpath("//div[@id='slideshow-big']//img[@class='film-strip-img']")
        orig_big_image_url = big_image_elem.get_attribute("src")
        # click on the back button
        first_image_elem = driver.find_element_by_id("slideShowLeft")
        first_image_elem.click()
        # get the image that should now be in the slideshow bug section
        big_image_elem = driver.find_element_by_xpath("//div[@id='slideshow-big']//img[@class='film-strip-img']")
        new_big_image_url = big_image_elem.get_attribute("src")
        self.assertNotEqual(orig_big_image_url, new_big_image_url, "The big image preview did not change even though the option was selected")
        self.driver.close()
 
    def test_change_preview_to_interactable_iframe(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # make sure that the second picture is selected
        first_image_elem = driver.find_element_by_id("picThumb3")
        first_image_elem.click()
        # get the iframe that is in the slideshow big section with the interactable html5 thing in it
        try:
            iframe_elem = driver.find_element_by_xpath("//div[@id='slideshow-big']//iframe[@id='HTMLViewer']")
        except:
            self.fail("The iframe with the interactable element is not present")
        self.driver.close()
             
    def test_change_preview_to_video(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # make sure that the second picture is selected
        first_image_elem = driver.find_element_by_id("picThumb2")
        first_image_elem.click()
        # get the div that is in the slideshow big section with the video in it
        try:
            video_elem = driver.find_element_by_xpath("//div[@id='slideshow-big']//div[@class='video-iframe-container']")
        except:
            self.fail("The iframe with the video is not present")
 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
