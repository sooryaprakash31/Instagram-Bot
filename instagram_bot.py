from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

class InstagramBot:

     def __init__(self, username=None, password =None):

          self.username = username
          self.password = password

          self.options = Options()
          #Selenium fails if your default profile has many bookmarks and extensions
          #Create a new profile and get the paths using chrome://version/
          self.options.add_argument("user-data-dir=/home/soorya/.config/chromium/Profile 1")
          self.driver = webdriver.Chrome(options=self.options,executable_path = "/usr/lib/chromium-browser/chromedriver")
          self.driver.get("https://instagram.com/")
          sleep(1)


if __name__ == '__main__':

     bot = InstagramBot()