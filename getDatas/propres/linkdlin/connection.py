#import webdriver module from  env/lib/selenium
from data import app_data
from time import sleep
from selenium.webdriver.common.keys import Keys

class Connection():
  
    def connectTo(self, driver):
        
        ### go  to login page             __________________________ #
        ### input the email and password  __________________________ #
        ### then click to connect         __________________________ #
        sleep(5)
        input_email      = driver.find_element_by_id("session_key")
        sleep(5)
        input_pass       = driver.find_element_by_id("session_password")
        sleep(5)
        btn_se_connecter = driver.find_element_by_xpath("//button[@type='submit']") 

        # ____________ clear all the inputs ________ #
        input_email.clear()
        input_pass.clear()
        # ___________ send keys and connect   ______ #
        input_email.send_keys(app_data['login']['email'],Keys.ARROW_DOWN)
        input_pass.send_keys(app_data['login']['pass'], Keys.ARROW_DOWN)
        sleep(4)
        btn_se_connecter.click()

    def executeConnection(self,driver):
        #       ______ this function make the website logic _____        #
        # ___ think that is a human that is navigate to the website ____ #
        sleep(8) # wait 28 sec
        self.connectTo(driver)


