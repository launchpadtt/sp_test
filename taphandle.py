from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# class definition

#constructor
# instantiate a new driver

class TapHandle:
    taphandle_url = "http://www.shapeways.com/model/835204/taphandle.html?key=9ec3dcf7d26711bb0ca53db314ebb550"
    
    def __init__(self, username = "chrisyeem_test", password = "test_password", browser = "Firefox"):
        self.username = username
        self.password = password
        
        if (browser == "Chrome"):
            self.driver = webdriver.Chrome()
        elif (browser == "IE"):
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Firefox()
                  
#     def __del__(self):
#         self.close_session()
                  
    def close_session(self):
        self.driver.close()
                  
    def load(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        print "    Accessing the TapHandle page at " + self.taphandle_url
        driver.get(self.taphandle_url)

    def reload(self):
        driver = self.driver
        print "    Accessing the TapHandle page at " + self.taphandle_url
        driver.get(self.taphandle_url)

    def get_page_source(self):
        print "    Accessing the web page source"
        return self.driver.page_source

    def get_page_title(self):
        driver = self.driver
        print "    Accessing the web page title"
        return driver.title
        
    def get_page_heading(self):
        driver = self.driver
        title_xpath = "//div[@class='shop-info-title']//h2"
        print "    Getting the Page title from " + title_xpath
        elem = driver.find_element_by_xpath(title_xpath)
        return elem.text

    def click_contact_designer(self):
        driver = self.driver
        contact_designer_link_xpath = "//div[@class='send-message']/a"
        print "    Getting the Contact Designer Link from " + contact_designer_link_xpath
        elem = driver.find_element_by_xpath(contact_designer_link_xpath)
        elem.click()
        time.sleep(2)

    def login(self, username = "", password = ""):
        driver = self.driver
        print "    Moving the mouse over the Sign in link"
        # get the login dialog to display
        sign_in_elem = driver.find_element_by_link_text("Sign in")
        hover = ActionChains(driver).move_to_element(sign_in_elem)
        hover.perform()

        if (username == ""):
            username = self.username
        elif (self.username == ""):
            username = "chrisyeem_test"
            
        if (password == ""):
            password = self.password
        elif (self.password == ""):
            password = "test_password"
        print "    Entering " + username + " for the username and " + password + " for the password"
        # fill out the username and password
        username_id = "top_username"
        print "    Entering in " + username + " in the username text box whose id is " + username_id 
        username_elem = driver.find_element_by_id(username_id)
        username_elem.send_keys(username)
        password_id = "top_password"
        print "    Entering in " + password + " in the username text box whose id is " + password_id 
        password_elem = driver.find_element_by_id(password_id)
        password_elem.send_keys(password)
        
        # login
        login_xpath = "//input[@value='Log in']"
        print "    Clicking the login link located at " + login_xpath
        log_in_elem = driver.find_element_by_xpath(login_xpath)
        log_in_elem.click()
        time.sleep(2)

    def fill_in_contact_designer_message(self, subject, message):
        driver = self.driver
        subject_textbox_xpath = "//input[@name='msg_subject']"
        print "    Filling in the subject textbox located at " + subject_textbox_xpath
        subject_elem = driver.find_element_by_xpath(subject_textbox_xpath)
        subject_elem.send_keys(subject)
        
        body_id = "txtb"
        print "    Filling in the message body textbox whose id is " + body_id
        body_elem = driver.find_element_by_id(body_id)
        body_elem.send_keys(message)
        
        print "    Clicking the Send Message link"
        send_message_elem = driver.find_element_by_link_text("Send Message")
        send_message_elem.click()
        
    def access_sent_messages(self):
        driver = self.driver
        sent_drop_down_xpath = "//select[@name='folder_id']/option[text()='Sent']"
        print "    Selecting the Sent messages from the drop down located at " + sent_drop_down_xpath 
        driver.find_element_by_xpath(sent_drop_down_xpath).click()
        
        go_link_xpath = "//form//a[text()='Go']"
        print "    Clicking the Go button link located at " + go_link_xpath
        go_link_elem = driver.find_element_by_xpath(go_link_xpath)
        go_link_elem.click()

    def get_country_name_and_currency(self):
        driver = self.driver
        country_xpath = "//div[@id='countryCurrencySelectControl']//span[@class='currency']"
        print "    Getting the country name and currency from the drop down located at " + country_xpath
        country_name_elem = driver.find_element_by_xpath(country_xpath)
        currency_and_country_name = country_name_elem.text
        currency_and_country = currency_and_country_name.split(None, 1)
        currency = currency_and_country[0]
        country = currency_and_country[1]
        return dict([("country", country), ("currency", currency)])
        
    def get_country_name(self):
        country_and_currency = self.get_country_name_and_currency()
        return country_and_currency['country'] 
        
    def get_country_currency(self):
        country_and_currency = self.get_country_name_and_currency()
        return country_and_currency['currency'] 
        
    def select_country(self, country):
        driver = self.driver
        country_id = "countryCurrencySelectControl"
        print "    Clicking the country selection link whose id is at " + country_id
        country_elem = driver.find_element_by_id(country_id)
        country_elem.click()
        time.sleep(5)
        
        country_text_box_id = "autocompleteCountry"
        print "    Filling out the country selection textbox whose id is at " + country_text_box_id + " with the value: " + country
        country_textbox_elem = driver.find_element_by_id(country_text_box_id)
        country_textbox_elem.clear()
        country_textbox_elem.send_keys(Keys.CONTROL + "a");
        country_textbox_elem.send_keys(Keys.DELETE);
        country_textbox_elem.send_keys(country)
        time.sleep(5)
        
        change_country_id = "submitChangeCountryCurrency"
        print "    Clicking the link to change the country " + change_country_id
        country_submit_elem = driver.find_element_by_id(change_country_id)
        country_submit_elem.click()
        time.sleep(5)

    def get_number_of_favorites(self):
        driver = self.driver
        favorites_elem_xpath = "//a[@id='favoritesLink']//div[@class='counter']"
        print "    Getting the number of favorites from the favorites counter located at " + favorites_elem_xpath 
        favorites_count_elem = driver.find_element_by_xpath(favorites_elem_xpath)
        no_of_favorites = favorites_count_elem.text
        return no_of_favorites
    
    def favorite_item(self):
        driver = self.driver
        favorites_xpath = "//a[@id='favoritesLink']"
        print "    Clicking the favorite link located at " + favorites_xpath 
        favorites_elem = driver.find_element_by_xpath(favorites_xpath)
        favorites_elem.click()
        time.sleep(5)
        
    def get_item_favorited_or_not(self): 
        driver = self.driver
        favorites_xpath = "//a[@id='favoritesLink']"
        favorites_elem = driver.find_element_by_xpath("//a[@id='favoritesLink']")
        print "    Getting the favorite link located at " + favorites_xpath 
        favorites_array = favorites_elem.text.strip().split()[:-1]
        favorites_text = ' '.join(favorites_array)
        if (favorites_text == "Added to Favorites"):
            favorited = True
        else:
            favorited = False
        return favorited
            
    def unfavorite_item(self):
        driver = self.driver
        favorites_xpath = "//a[@id='favoritesLink']"
        print "    Clicking the unfavorite link located at " + favorites_xpath 
        favorites_elem = driver.find_element_by_xpath(favorites_xpath)
        favorites_elem.click()
        time.sleep(5)
        confirm_remove_xpath = "//div[@class='remove-model']//a[text() = 'Remove']"
        print "    Clicking the confirm removal link located at " + confirm_remove_xpath 
        remove_link_elem = driver.find_element_by_xpath(confirm_remove_xpath)
        remove_link_elem.click()
        time.sleep(2)
        driver.get(self.taphandle_url)
        