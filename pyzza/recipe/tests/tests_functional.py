from django.test import TestCase
from selenium import webdriver
import time
# Create your tests here.

class FunctionalTestCase(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Pyzza', self.browser.page_source)

    def test_vote_action(self):
        self.browser.get('http://localhost:8000/recipe/3')
        votes = self.browser.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div[2]/span[2]').text
        submit = self.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/form/input[2]')
        submit.click()
        time.sleep(1)
        votes_1 = self.browser.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div[2]/span[2]').text
        self.assertEqual(int(votes_1), int(votes)+1)
        
    def tearDown(self):
        self.browser.quit()