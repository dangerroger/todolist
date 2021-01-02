#from django.test import LiveServerTestCase - changed to StaticLiverServerTestCase after importing Bootstrap page 150
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.common.exceptions import WebDriverException
import os

MAX_WAIT = 10


#from webdriver_manager.firefox import GeckoDriverManager
#browser = webdriver.Firefox()
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#broweser = webdriver.Firefox()
#class NewVisitorTest(LiveServerTestCase): changed to StaticLiveServerTestCase
class NewVisitorTest(StaticLiveServerTestCase):

# class changed to LiveServerTestCase
#class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()
# helper function to prevent duplication of code
    #def check_for_row_in_list_table(self, row_text): changed to
    def wait_for_row_in_list_table (self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return

            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)





    # test for every list ti have a unique URl

    def test_can_start_a_list_for_one_user(self):


    #def test_can_start_a_list_and_retrieve_it_later(self): - changed to the above test
        #Edith has heard about a cool new online to-do app. She goes to checkout its homepage
        # changed after importing LiveServerTestcase
        #self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)

        #She notices the page headher and title mntions a to-do list

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        #self.fail('Finish the test!')

        #She is invited to enter a To Do item straighaway
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

            # She enters "Buy Peackock feathers" into a text box (Edith's hobby is
            #trying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter. the page updates and now the page lists
        #"1: Buy Packock feathers" as a to do item in a to do item lists

        inputbox.send_keys(Keys.ENTER)
        #time.sleep(1) - removed after creating wait function in line 27
        #self.check_for_row_in_list_table('1: Buy peacock feathers' )
        self.wait_for_row_in_list_table('1: Buy peacock feathers' )

        # disabled after writing helper function in line 21
        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertTrue(
            #any(row.text == '1: Buy peacock feathers' for row in rows),
            #this is a custom error message
            #

        # New method:

        #self.assertIn('1: Buy peacock feathers' ,[row.text for row in rows])
        #f"New to-do item did not appear in table. Contents were: \n{table.text}"
    #)

# There is still a text box to add anothet item. She enters
# Use peacock feathers to make a fly".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)



#The page updates and now shows both items on her lists
        # Both function below changed to wait function created in row 27
        #self.check_for_row_in_list_table('1: Buy peacock feathers')
        #self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')


        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertIn('1: buy peacok feathers', [row.text for row in rows])
        #self.assertIn(
        #    '2: use peacock feathers to make a fly',
            #[row.text for row in rows]
        #)

# Edith wonders if the site will remeber her list. Then She
# sees that the site has generated a unique URL for her --
# there is some explanatory text to that effect.

        #self.fail('Finish the test!')

# She visits the URl abd her To-do list is still there

# Satisfied m she goes to sleep

    def test_multiple_user_can_start_lists_at_different_urls(self):
        #Edith starts a new to-do list

        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

    # She notices that her list has a unique URl

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

    # A new user Francis comes to the site.

    ## We use a new browser session to make sure that no information of Edith
    ## is coming through from cookies etc.

        self.browser.quit()
        self.browser = webdriver.Firefox()

    # Francis visits the HomePage . There is no sign of Edith''s list

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

    #Francis starts a new list by entering a new ItemModelTest
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

    #Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

    #Again there is no trace of Edith's lists

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

    # satisfied, they both go back to sleep
    def test_layout_and_styling(self):
        #Edith goes to home page

        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)

        #She notices inputbox is nicely centred

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
        inputbox.location['x'] + inputbox.size['width']/2,
        512,
        delta=50
                )
        # She starts a new list and sees that the inputbox is nicely centred to


        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
        inputbox.location['x'] + inputbox.size['width'] /2,

        512,
        delta=50
        )

#if __name__ == '__main__':
   #unittest.main()

#browser.quit()
