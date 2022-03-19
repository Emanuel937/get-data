#import webdriver module from  env/lib/selenium
from data import app_data
from time import sleep
from selenium.webdriver.common.keys import Keys
import annonce 

class Logic_and_setup():

    def __init__(self,driver):
        # --------------------------------------- #
        # ---- pass the webdriver parametor  ---- #
        # --------------------------------------- #
        self.webdriver = driver

    def connect_to(self):
        
        ### go  to login page             __________________________ #
        ### input the email and password  __________________________ #
        ### then click to connect         __________________________ #
        self.webdriver.get(app_data['links']["leboncoin_login"])
        sleep(5)
        input_email      = self.webdriver.find_element_by_id("email")
        sleep(5)
        input_pass       = self.webdriver.find_element_by_id("password")
        sleep(5)
        btn_se_connecter = self.webdriver.find_element_by_xpath("//button[@data-testid='submitButton']") 

        # ____________ clear all the inputs ________ #
        input_email.clear()
        input_pass.clear()
        # ___________ send keys and connect   ______ #
        input_email.send_keys(app_data['login']['email'],Keys.ARROW_DOWN)
        input_pass.send_keys(app_data['login']['pass'], Keys.ARROW_DOWN)
        sleep(4)
        btn_se_connecter.click()

    def execute_code(self):
        #       ______ this function make the website logic _____        #
        # ___ think that is a human that is navigate to the website ____ #
        sleep(28) # wait 28 sec
        self.webdriver.get(app_data['links']['leboncoin']) # rearch the browser 
        sleep(3)
        self.connect_to()  # connect to an account, leboncoin
        sleep(1)  # whait 3 sec
        an_post = annonce.Annonce(self.webdriver) # finaly start make annonce then 
        an_post.annonce_steps()

    def run_logic(self):
        self.execute_code()

