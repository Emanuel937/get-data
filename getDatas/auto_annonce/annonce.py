""" 
    This file is imported on logic py file 
    the script over here, is used to make 
    annonce on website name 'leboncoin'

"""

from time import sleep

class Annonce:

    def __init__(self, driver):
        self.driver = driver
    # _____________ Find element function ______________ #
    def elem(self,selector):
        return  self.driver.find_element_by_xpath(selector)

    def el_id(self, selector):
        return  self.driver.find_element_by_id(selector)

    # ___________ The end of find element function ______ #
    # ___________ The steps for make an announce   ______ #
    
    def annonce_button(self):
        deposer_annonce = self.elem("//a[@data-qa-id='header_newad_link']")
        deposer_annonce.click()
    
    def annonce_title_and_content(self):
        sleep(4)
        ####   _____________  Select some inputs _________________ #######################
        annonce_title   = self.el_id("//input[@id='subject']")                           #
        annonce_content = self.el_id("//textarea[@data-qa-id='depositad-text_body']")    #                  
        annonce_ref     = self.el_id("//input[@id='custom_ref']")                        #    
        #### ____________________ send_keys ______________________  ######################   
        annonce_title.send_keys("titre")   
        annonce_content.send_keys("context")
        annonce_ref.send_keys("rabi mendes")


    def categories(self): 
        sleep(5)
        #   ____________ click on categories ____________    #
        btn_category = self.elem("//span[@data-qa-id='cta-categories_category_services-desktop']")
        btn_category.click()
       
        #   ____________ click on subcategories ___________  #
        btn_sub_catg = self.elem("//span[@data-qa-id='cta-categories_category_prestations_de_services-desktop-child']")
        btn_sub_catg.click()

        # _____________      continuer     ________________  #
        btn_continue = self.elem("//button[@data-qa-id='depositad-button-next-categories']")
        btn_continue.click()
        sleep(5) ######  wait for 5 sec  #########

    def annonce_steps(self):
        # 1) - click on the button to start the annonce         +
        self.annonce_button()
        # 2) - select the annonce category'services-prestation' +
        self.categories()
        # 3) - set the annonce title and the annonce content    +
        self.annonce_title_and_content()
        