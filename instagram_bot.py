from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from configparser import ConfigParser

class InstagramBot:

     def __init__(self, username=None, password =None):

          self.username = username
          self.password = password

          self.options = Options()
          #Selenium fails if your default profile has many bookmarks and extensions
          #Create a new profile and get the paths using chrome://version/
          self.options.add_argument("user-data-dir=/home/soorya/.config/chromium/Profile 1")
          self.driver = webdriver.Chrome(options=self.options,executable_path = "/usr/lib/chromium-browser/chromedriver")
          self.driver.get("https://www.instagram.com/accounts/login/")
          sleep(1)

          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')[0].send_keys(self.username)
          sleep(1)
          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')[0].send_keys(self.password)
          sleep(2)
          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')[0].click()
          sleep(2)
          #self.driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
          self.driver.get("https://www.instagram.com/{}/".format(self.username))
          sleep(2)
          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/button')[0].click()
          sleep(3)
          self.driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div/button[9]')[0].click()
          sleep(5)
          self.driver.quit()
if __name__ == '__main__':

     config = ConfigParser()
     config.read('config.ini')

     username = config.get('AUTH', 'USERNAME')
     password = config.get('AUTH', 'PASSWORD')
     bot = InstagramBot(username,password)