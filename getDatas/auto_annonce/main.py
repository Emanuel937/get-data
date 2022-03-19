import logic
import unittest
from selenium import webdriver
from data import app_data

class Main(unittest.TestCase):

    def setUp(self):
        # --------------------------------------- #
        # ---- go to the 'leboncoin'website  ---- #
        # --------------------------------------- #
        self.driver =  webdriver.Firefox(executable_path=r'/Users/emanuelabizimi/Downloads/geckodriver')
        self.driver.get(app_data['links']['leboncoin'])

    def test_runApp(self):
        #  ____  This function execute the logic scrit ____   #
        # ________ it is the brain of the aplication _______  #
        logic.Logic_and_setup(self.driver).run_logic()

if __name__ == "__main__":
    # ____ execute only if run as a script ____ #
    unittest.main()
