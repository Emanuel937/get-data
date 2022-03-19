#this code just try to extract the data from linkdlin 

from selenium import webdriver
from data import app_data
from time import sleep
from logic import Logic


class Main():

    def __init__(self):
        # --------------------------------------- #
        # ---- go to the 'leboncoin'website  ---- #
        # --------------------------------------- #
        self.driver =  webdriver.Firefox(executable_path=r'/Users/emanuelabizimi/Downloads/geckodriver')
        self.driver.get(app_data['links']['experts'])

    def search(self):
        selectBtn = self.driver.find_element_by_id("departement")
        #click on it 
        selectBtn.click()
        #wait for 5 sg then click on li 
        sleep(5)
        #find the option that has 75 as value 
        setOption = self.driver.find_element_by_xpath("//option[@value='75']")
        #click on the button finaly
        setOption.click()
        #rechercheBtn
        rechercheBtn = self.driver.find_element_by_id("rechercheBtn")
        rechercheBtn.click()
        
    def runApp(self):
        #  ____  This function execute the logic scrit ____   #
        # ________ it is the brain of the aplication _______  #
       self.search()
       #run the logic code to send the msg
       classLogic =  Logic(self.driver)
       classLogic.runCode()

if __name__ == "__main__":
    # ____ execute only if run as a script ____ #
    main = Main()
    #execute the code 
    #runApp method from main function 
    #that execute the logic function
    main.runApp()
    

