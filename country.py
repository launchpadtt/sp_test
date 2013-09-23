import taphandle
import unittest

class CountryTests(unittest.TestCase):  
    def setUp(self):
        self.taphandle = taphandle.TapHandle("chrisyeem_test", "test_password")

    def test_change_country(self):
        print "\nRunning the testcase 'Change Country'"
        taphandle = self.taphandle
        taphandle.load()
        # get the original material name and price
        print "  Getting the country name and country currency"
        country = taphandle.get_country_name()
        currency = taphandle.get_country_currency()
        # change the country to a new valid country
        print "  Changing the country to Trinidad and Tobago"
        taphandle.select_country("Trinidad and Tobago")
        # now check to see if the country matches what is being looked for
        # get the new material name and price
        print "  Getting the new country name and country currency"
        new_country = taphandle.get_country_name()
        new_currency = taphandle.get_country_currency()
        print "  Checking that the new and old country are different"
        self.assertNotEqual(new_country, country, "The new country and old country are still the same. New country: '" + new_country + "' Old country: '" + country + "'")
        print "  Checking that the new country is Trinidad and Tobago"
        self.assertEqual(new_country, "Trinidad and Tobago", "The new country is not the expected value. It should be 'Trinidad and Tobago', it is: '" + new_country + "'")
        print "  Checking that the new currency is $"
        self.assertEqual(new_currency, "$", "The new currency is not the expected value. It should be '$', it is: '" + new_country + "'")
        taphandle.close_session()

    def test_change_country_non_existent(self):
        print "\nRunning the testcase 'Change Country to a non-existent country'"
        taphandle = self.taphandle
        taphandle.load()
        # get the original material name and price
        print "  Getting the country name and country currency"
        country = taphandle.get_country_name()
        currency = taphandle.get_country_currency()
        # change the country to a new invalid country
        print "  Changing the country to Trinbago land of my birth"
        taphandle.select_country("Trinbago land of my birth")
        # now check to see if the country matches what is being looked for
        # get the new material name and price
        print "  Getting the new country name and country currency"
        new_country = taphandle.get_country_name()
        new_currency = taphandle.get_country_currency()
        print " Checking that the new currency and old currency are the same"
        self.assertEqual(new_currency, currency, "The new currency and old currency are NOT still the same. New currency:'" + new_currency + "' Old currency: '" + currency + "'")
        print " Checking that the new country and old country are the same"
        self.assertEqual(new_country, country, "The new country and old country are NOT the same. New country: '" + new_country + "' Old country: '" + country + "'")
        taphandle.close_session()

#     def tearDown(self):
#         self.taphandle.close_session()

if __name__ == "__main__":
    unittest.main()
    
