import taphandle
import unittest

class FavoritesTests(unittest.TestCase):  
    def setUp(self):
        self.taphandle = taphandle.TapHandle("chrisyeem_test", "test_password")

    def test_favorite_when_not_logged_in(self):
        print "\nRunning the testcase 'Favorite an item when not logged in'"
        taphandle = self.taphandle
        taphandle.load()
        # check the number of favorites before logging in
        no_of_favorites = taphandle.get_number_of_favorites()
        # favorite the item
        print "  Favoriting the item"
        taphandle.favorite_item()
        # check whether you're at the sign up screen or whether you're still at the product page
        print "  Looking for the string 'Log In' in the page source"
        self.assertIn("Log In", taphandle.get_page_source())
        print "  Looking for the string 'Sign Up!' in the page source"
        self.assertIn("Sign Up!", taphandle.get_page_source())
        print "  Looking for the string 'Already a member?' in the page source"
        self.assertIn("Already a member?", taphandle.get_page_source())
        # check the number of favorites after attempting to favorite the item
        taphandle.close_session()

    def test_favorite_when_logged_in(self):
        print "\nRunning the testcase 'Favorite an item when logged in'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Logging in"
        taphandle.login()
        # check whether the item is favorited
#         " Favorite            "
#         " Added to Favorites            "
        print "  Checking that the item is not already favorited"
        favorited = taphandle.get_item_favorited_or_not()
        if (favorited == True):
            print "  The item has already been favorited. Unfavoriting it."
            taphandle.unfavorite_item()
            taphandle.reload()
        # check the number of favorites before favorites before
        print "  Getting the number of favorited items"
        no_of_favorites_before = taphandle.get_number_of_favorites()
        # favorite the item
        print "  Favoriting the item"
        taphandle.favorite_item()
        # go back to the product page
        print "  Forcefully reloading the page"
        taphandle.reload()
        # check whether you're at the sign up screen or whether you're still at the product page
        print "  Looking for the absence of the string 'Log In' in the page source"
        self.assertNotIn("Log In", taphandle.get_page_source())
        print "  Looking for the absence of the string 'Sign Up!' in the page source"
        self.assertNotIn("Sign Up!", taphandle.get_page_source())
        print "  Looking for the absence of the string 'Already a member?' in the page source"
        self.assertNotIn("Already a member?", taphandle.get_page_source())
        print "  Looking for the string 'TapHandle' in the page source"
        self.assertIn("TapHandle", taphandle.get_page_source())
        # check the number of favorites after attempting to favorite the item 
        print "  Getting the number of favorited items again"
        no_of_favorites_after = taphandle.get_number_of_favorites()
        print "  Checking that the number of favorited items after is one more than before"
        self.assertEqual(str(int(no_of_favorites_before) + 1), str(no_of_favorites_after), "The number of favorites before is not one less than the number of favorites after. Before: '" + str(no_of_favorites_before) + "' After: '" + str(no_of_favorites_after) + "'")
        taphandle.close_session()
          
    def test_unfavorite_when_logged_in(self):
        print "\nRunning the testcase 'Favorite an item when logged in'"
        taphandle = self.taphandle
        taphandle.load()
        print "  Logging in"
        taphandle.login()
        # check whether the item is favorited
        print "  Checking that the item is not already favorited"
        favorited = taphandle.get_item_favorited_or_not()
        # if it is not favorited, then favorite it
        if (favorited == False):
            print "  The item is already not favorited. Favoriting it."
            taphandle.favorite_item()
            taphandle.reload()
        # check the number of favorites
        print "  Getting the number of favorited items"
        no_of_favorites_before = taphandle.get_number_of_favorites()
        # then unfavorite it
        taphandle.unfavorite_item()
        taphandle.reload()
        # check the number of favorites
        print "  Getting the number of favorited items again"
        no_of_favorites_after = taphandle.get_number_of_favorites()
        print "  Checking that the number of favorited items after is one less than before"
        self.assertEqual(str(no_of_favorites_before), str(int(no_of_favorites_after) + 1), "The number of favorites after is not one less than the number of favorites before. Before: '" + str(no_of_favorites_before) + "' After: '" + str(no_of_favorites_after) + "'")
        taphandle.close_session()
         
#     def tearDown(self):
#         self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
