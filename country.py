import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class CountryTests(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_change_country(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # get the original material name and price
        country_elem = driver.find_element_by_id("countryCurrencySelectControl")
        country_name_elem = country_elem.find_element_by_xpath("//div[@id='countryCurrencySelectControl']//span[@class='currency']")
        # actually pull out the currency and country
        currency_and_country_name = country_name_elem.text
        currency_and_country = currency_and_country_name.split(None, 1)
        currency = currency_and_country[0]
        country = currency_and_country[1]
        # now to click on the country element
        country_elem.click()
        # change the country to a new valid country
        country_textbox_elem = driver.find_element_by_id("autocompleteCountry")
        time.sleep(5)
        country_textbox_elem.clear()
        country_textbox_elem.send_keys(Keys.CONTROL + "a");
        country_textbox_elem.send_keys(Keys.DELETE);
        country_textbox_elem.send_keys("Trinidad and Tobago")
        time.sleep(5)
        country_submit_elem = driver.find_element_by_id("submitChangeCountryCurrency")
        country_submit_elem.click()
        time.sleep(5)
        # now check to see if the country matches what is being looked for
        # get the new material name and price
        country_elem = driver.find_element_by_id("countryCurrencySelectControl")
        country_name_elem = country_elem.find_element_by_xpath("//div[@id='countryCurrencySelectControl']//span[@class='currency']")
        # actually pull out the currency and country
        new_currency_and_country_name = country_name_elem.text
        new_currency_and_country = new_currency_and_country_name.split(None, 1)
        new_currency = new_currency_and_country[0]
        new_country = new_currency_and_country[1]
        #self.assertNotEqual(new_currency, currency, "The new currency and old currency are still the same. New currency:'" + new_currency + "' Old currency: '" + currency + "'")
        self.assertNotEqual(new_country, country, "The new country and old country are still the same. New country: '" + new_country + "' Old country: '" + country + "'")
        self.assertEqual(new_country, "Trinidad and Tobago", "The new country is not the expected value. It should be 'Trinidad and Tobago', it is: '" + new_country + "'")
        self.assertEqual(new_currency, "$", "The new currency is not the expected value. It should be '$', it is: '" + new_country + "'")

    def test_change_country_non_existent(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550")
        # get the original material name and price
        country_elem = driver.find_element_by_id("countryCurrencySelectControl")
        country_name_elem = country_elem.find_element_by_xpath("//div[@id='countryCurrencySelectControl']//span[@class='currency']")
        # actually pull out the currency and country
        currency_and_country_name = country_name_elem.text
        currency_and_country = currency_and_country_name.split(None, 1)
        currency = currency_and_country[0]
        country = currency_and_country[1]
        # now to click on the country element
        country_elem.click()
        # change the country to a new valid country
        country_textbox_elem = driver.find_element_by_id("autocompleteCountry")
        time.sleep(5)
        country_textbox_elem.clear()
        country_textbox_elem.send_keys(Keys.CONTROL + "a");
        country_textbox_elem.send_keys(Keys.DELETE);
        country_textbox_elem.send_keys("Trinbago land of my birth")
        time.sleep(5)
        country_submit_elem = driver.find_element_by_id("submitChangeCountryCurrency")
        country_submit_elem.click()
        time.sleep(5)
        # now check to see if the country matches what is being looked for
        # get the new material name and price
        country_elem = driver.find_element_by_id("countryCurrencySelectControl")
        country_name_elem = country_elem.find_element_by_xpath("//div[@id='countryCurrencySelectControl']//span[@class='currency']")
        # actually pull out the currency and country
        new_currency_and_country_name = country_name_elem.text
        new_currency_and_country = new_currency_and_country_name.split(None, 1)
        new_currency = new_currency_and_country[0]
        new_country = new_currency_and_country[1]
        self.assertEqual(new_currency, currency, "The new currency and old currency are NOT still the same. New currency:'" + new_currency + "' Old currency: '" + currency + "'")
        self.assertEqual(new_country, country, "The new country and old country are NOT the same. New country: '" + new_country + "' Old country: '" + country + "'")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
