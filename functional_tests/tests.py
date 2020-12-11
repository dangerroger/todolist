from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

#from webdriver_manager.firefox import GeckoDriverManager
#browser = webdriver.Firefox()
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#broweser = webdriver.Firefox()
class NewVisitorTest(LiveServerTestCase):
# class changed to LiveServerTestCase
#class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
# helper function to prevent duplication of code
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
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
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers' )

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

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


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

        self.fail('Finish the test!')

# She visits the URl abd her To-do list is still there

# Satisfied m she goes to sleep

if __name__ == '__main__':
    unittest.main()

#browser.quit()
