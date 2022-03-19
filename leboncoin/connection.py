from selenium import webdriver
from time import sleep

class Goto():
    def __init__(self):
      self.driver = webdriver.Firefox(executable_path=r'/Users/emanuelabizimi/Downloads/geckodriver')
      self.driver.get("https://leboncoin.fr/")

Goto()