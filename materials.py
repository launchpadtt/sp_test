import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class MaterialsTests(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_change_material(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # get the original material name and price
        material_drop_down_elem = driver.find_element_by_id("selectedMaterialContent")
        # get the price first
        original_price_elem = material_drop_down_elem.find_element_by_class_name("price")
        original_price = original_price_elem.text
        # get the name of the material next
        original_material_elem = material_drop_down_elem.find_element_by_xpath("//li[@id='selectedMaterialContent']//p")
        original_material = original_material_elem.text
        # now click on the material drop down to bring up the list
        material_drop_down_elem.click()
        
        # get the information for the new material that is gonna be selected
        new_material_in_list_elem = driver.find_element_by_id("materialContent7")
        # get the new materials name first
        new_material_name_elem = new_material_in_list_elem.find_element_by_xpath("//li[@id='materialContent7']//p")
        new_material_name_in_list = new_material_name_elem.text
        # then get the materials price next
        new_material_price_elem = new_material_in_list_elem.find_element_by_class_name("price")
        new_material_price_in_list = new_material_price_elem.text
        # now to click the new material element
        new_material_in_list_elem.click()
        
        # now to collect the name and price of the new element
        material_drop_down_elem = driver.find_element_by_id("selectedMaterialContent")
        # get the price first
        new_material_price_elem = material_drop_down_elem.find_element_by_class_name("price")
        new_material_price = new_material_price_elem.text
        # get the name of the material next
        new_material_elem = material_drop_down_elem.find_element_by_xpath("//li[@id='selectedMaterialContent']//p")
        new_material_name = new_material_elem.text
        # the checks that have to be made
        # first check that the original price and the new price are different
        self.assertNotEqual(original_price, new_material_price, "The new price and the old price are the same. Original Price: '" + original_price + "' New Price: '" + new_material_price + "'")
        # then check that the original name and new name are different
        self.assertNotEqual(original_material, new_material_name, "The new price and the old price are the same. Original Name: '" + original_material + "' New Name: '" + new_material_name + "'")
        # then check that the new price in the list and new price are the same
        self.assertEqual(new_material_price_in_list, new_material_price, "The new price on the page is not the same as in the list. New Price in List: '" + new_material_price_in_list + "' New Price in Page: '" + new_material_price + "'")
        # then check that the old price in the list and the old price are the same
        self.assertEqual(new_material_name_in_list, new_material_name, "The new price on the page is not the same as in the list. New Price in List: '" + new_material_name_in_list + "' New Price in Page: '" + new_material_name + "'")
        self.driver.close()
        
    def test_revert_change_material(self):
        driver = self.driver
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # get the original material name and price
        material_drop_down_elem = driver.find_element_by_id("selectedMaterialContent")
        # get the price first
        original_price_elem = material_drop_down_elem.find_element_by_class_name("price")
        original_price = original_price_elem.text
        # get the name of the material next
        original_material_elem = material_drop_down_elem.find_element_by_xpath("//li[@id='selectedMaterialContent']//p")
        original_material = original_material_elem.text
        # now click on the material drop down to bring up the list
        material_drop_down_elem.click()
        # now to hit the close button
        close_button = driver.find_element_by_xpath("//span[@id='ui-dialog-title-materialSelect']/following-sibling::a[1]")
        close_button.click()
        # now to collect the name and price of the new element
        material_drop_down_elem = driver.find_element_by_id("selectedMaterialContent")
        # get the price first
        new_material_price_elem = material_drop_down_elem.find_element_by_class_name("price")
        new_material_price = new_material_price_elem.text
        # get the name of the material next
        new_material_elem = material_drop_down_elem.find_element_by_xpath("//li[@id='selectedMaterialContent']//p")
        new_material_name = new_material_elem.text
        # the checks that have to be made
        # first check that the original price and the new price are different
        self.assertEqual(original_price, new_material_price, "The new price and the old price are NOT the same. Original Price: '" + original_price + "' New Price: '" + new_material_price + "'")
        # then check that the original name and new name are different
        self.assertEqual(original_material, new_material_name, "The new price and the old price are NOT the same. Original Name: '" + original_material + "' New Name: '" + new_material_name + "'")
        self.driver.close()
        
 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
