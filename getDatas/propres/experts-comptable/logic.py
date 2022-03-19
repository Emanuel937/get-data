from time import sleep
from data import app_data

class Logic:
    def __init__(self, driver):
        self.d = driver
        self.i = 1
        self.p = 1

    def getMorale(self):
        sleep(5)
        # Get THE TOTAL OF MORALE ...
        while(True):

            try:
                morale    =  self.d.find_elements_by_css_selector('.morale')
                conctactBtn = morale[self.i].find_element_by_css_selector('.mailPerso a')
                # THEN CALL THE CLICK ON openForm and set datas
                #CHECK IF THE CONCTACTBTN IS ACTIV AND CLICKBLE
                if conctactBtn.get_attribute('class') != 'no-active':
                    #self.openForm(conctactBtn)
                    print(self.i)
            except:
                # DO NOTHING IF THE ELEMENT IS NOT FOUND ON THE DOM 
                pass
            if self.i == 19:
                sleep(1)
                self.refresh()
                self.i  = 1 #index of the element
                self.p += 1 #page number
            else:
                self.i += 1

    def openForm(self, arg):
        # THIS FUNCTION OPEN THE FORM 
        # AND SET DATA THEN SEND THE MSG
        openForm = arg
        #click
        openForm.click()
        # THEN SET DATA DO EVERY INPUT 
        # AND SEND THE FORM 
        #AFTER SEND THE FORM CLOSE THE FORM
        sleep(4)
        try:
            nameForForm   = arg.find_element_by_css_selector('#contactForm #nom')
            emailFrom     = arg.find_element_by_css_selector('#contactForm #email')
            objectEmail   = arg.find_element_by_css_selector('#contactForm #objet')
            msgBody       = arg.find_element_by_css_selector('#contactForm #message')
            envoiEmailBtn = arg.find_element_by_id("envoiEmailBtn")
            #send the key 'the values' for the inputs 
            nameForForm.send_keys('Agence sitefix')
            emailFrom.send_keys('emanuelabizimi@gmail.com')
            objectEmail.send_keys('SITEFIX ENTREPRISE')
            msgBody.send_keys(app_data['msg'])
            # click on the button for send the form 
            #send the msg 
            envoiEmailBtn.click()
        except:
            print("error")
        
    def refresh(self):
        plusMorale = self.d.find_element_by_id("voirPlus")
        plusMorale.click()

    def runCode(self):
        # THIS IS THE PONTY ENTRY OF THE CODE 
        self.getMorale()
        