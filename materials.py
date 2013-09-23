import taphandle
import unittest

class MaterialsTests(unittest.TestCase):  
    def setUp(self):
        self.taphandle = taphandle.TapHandle("chrisyeem_test", "test_password")

    def test_change_material(self):
        print "\nRunning the testcase 'Change Material'"
        taphandle = self.taphandle
        taphandle.load()
        # get the original material name and price
        print "  Getting the original material name and price"
        original_material = taphandle.get_selected_material_name()
        original_price = taphandle.get_selected_material_price()
        print "  Loading the materials dialog"
        taphandle.load_materials_dialog()
        print "  Getting the name and price of the material whose id is 7"
        new_material_name_in_list = taphandle.get_material_name_in_list("7")
        new_material_price_in_list = taphandle.get_material_price_in_list("7")
        print "  Selecting the material in the list whose id is 7"
        taphandle.select_material_in_list("7")
        print "  Getting the new material name and price"
        new_material_name = taphandle.get_selected_material_name()
        new_material_price = taphandle.get_selected_material_price()
        # the checks that have to be made
        # first check that the original price and the new price are different
        print "  Checking that the new and old price are not the same"
        self.assertNotEqual(original_price, new_material_price, "The new price and the old price are the same. Original Price: '" + original_price + "' New Price: '" + new_material_price + "'")
        # then check that the original name and new name are different
        print "  Checking that the new and old material names are not the same"
        self.assertNotEqual(original_material, new_material_name, "The new price and the old price are the same. Original Name: '" + original_material + "' New Name: '" + new_material_name + "'")
        # then check that the new price in the list and new price are the same
        print "  Checking that the new material price in the list and on the page are the same"
        self.assertEqual(new_material_price_in_list, new_material_price, "The new price on the page is not the same as in the list. New Price in List: '" + new_material_price_in_list + "' New Price in Page: '" + new_material_price + "'")
        # then check that the old price in the list and the old price are the same
        print "  Checking that the new material name in the list and on the page are the same"
        self.assertEqual(new_material_name_in_list, new_material_name, "The new price on the page is not the same as in the list. New Price in List: '" + new_material_name_in_list + "' New Price in Page: '" + new_material_name + "'")
        taphandle.close_session()
        
    def test_revert_change_material(self):
        print "\nRunning the testcase 'Revert a change after loading Materials dialog box'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Getting the original material name and price"
        original_material = taphandle.get_selected_material_name()
        original_price = taphandle.get_selected_material_price()
        print "  Loading the materials dialog"
        taphandle.load_materials_dialog()
        # now to hit the close button
        taphandle.close_materials_dialog()
        print "  Getting the new material name and price"
        new_material_name = taphandle.get_selected_material_name()
        new_material_price = taphandle.get_selected_material_price()
        # the checks that have to be made
        # first check that the original price and the new price are different
        self.assertEqual(original_price, new_material_price, "The new price and the old price are NOT the same. Original Price: '" + original_price + "' New Price: '" + new_material_price + "'")
        # then check that the original name and new name are different
        self.assertEqual(original_material, new_material_name, "The new price and the old price are NOT the same. Original Name: '" + original_material + "' New Name: '" + new_material_name + "'")
        taphandle.close_session()
        
#  
#     def tearDown(self):
#         self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
