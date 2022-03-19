from selenium import webdriver
from time import sleep

class Goto():
    def __init__(self):
      self.driver = webdriver.Firefox(executable_path=r'/Users/emanuelabizimi/Downloads/geckodriver')
      self.driver.get("https://www.google.com/search?q=agence+web+paris&source=hp&ei=xBHvYfKgKpKPlwSknJ2gCg&iflsig=ALs-wAMAAAAAYe8f1A_7YBhp8TbJlzAmMP6FPGnCysNY&ved=0ahUKEwjykv7Gosv1AhWSx4UKHSROB6QQ4dUDCAY&uact=5&oq=agence+web+paris&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDILCC4QgAQQxwEQrwEyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoRCC4QgAQQsQMQgwEQxwEQ0QM6CwgAEIAEELEDEIMBOggIABCABBCxAzoOCC4QgAQQsQMQxwEQ0QM6CwguEIAEEMcBENEDOg4ILhCABBCxAxDHARCjAjoOCC4QgAQQsQMQxwEQrwE6CAgAELEDEIMBOgUILhCABDoICC4QgAQQsQM6CwgAEIAEELEDEMkDOgUIABCSAzoICAAQgAQQyQNQigVYoENgkkloAHAAeAOAAfYEiAGkO5IBBzMtMi44LjaYAQCgAQGwAQA&sclient=gws-wiz")

Goto()