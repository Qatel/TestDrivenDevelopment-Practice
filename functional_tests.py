from selenium import  webdriver
import unittest
# commenting out functional test to use unittest module
# browser = webdriver.Firefox()
class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        
        self.assertIn('To-Do', self.browser.title)
        
        self.fail('Finished testing')
    
# edith has heard about a cool online to-do-lists
# she goes out to check its homepage

# she notices the page title and header mention to-do-list

# assert 'To-Do' in browser.title, "browser title was "+ browser.title
# she is invited to enter a to-do item straight away
# she types "Buy peacock feathers" into a text box
# browser.quit()
if __name__ == '__main__':  
    unittest.main(warnings='ignore')