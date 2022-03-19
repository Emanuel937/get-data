#this code just try to extract the data from linkdlin 

import unittest
from selenium import webdriver
from data import app_data
from connection import Connection

class Main():

    def __init__(self):
        # --------------------------------------- #
        # ---- go to the 'leboncoin'website  ---- #
        # --------------------------------------- #
        self.driver =  webdriver.Firefox(executable_path=r'/Users/emanuelabizimi/Downloads/geckodriver')
        self.driver.get(app_data['links']['linkedin'])

    def runApp(self):
        #  ____  This function execute the logic scrit ____   #
        # ________ it is the brain of the aplication _______  #
        connectionTo = Connection()
        #execute the code for connection 
        connectionTo.executeConnection(self.driver)

if __name__ == "__main__":
    # ____ execute only if run as a script ____ #
    main = Main()
    #execute the code 
    #runApp method from main function 
    #that execute the logic function
    main.runApp()
    

