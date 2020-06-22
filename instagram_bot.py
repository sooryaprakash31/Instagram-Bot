from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from configparser import ConfigParser
from utils.utils import *
username=""
password=""
class InstagramBot:
     def __init__(self):
          #open Browser - instagram.com
          self.options = Options()
          '''
          Selenium fails if your default profile has many bookmarks and extensions
          Create a new profile and get the paths using chrome://version/
          '''
          self.options.add_argument("user-data-dir=/home/soorya/.config/chromium/Profile 1")
          self.driver = webdriver.Chrome(options=self.options,executable_path = "/usr/lib/chromium-browser/chromedriver")
          self.driver.get("https://www.instagram.com/accounts/login/")        
          
     @operation
     def autoPilot(self):
          #login
          self.login()
          #following the suggested accounts in main page
          self.follow_suggested(2)
          #To log out
          self.logout()

     @operation
     def login(self):
          global username,password
          #input username and password
          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')[0].send_keys(username)
          sleep(1)
          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')[0].send_keys(password)
          sleep(2)
          #log in button
          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')[0].click()
          
     @operation
     def follow_suggested(self,count=None):
          self.driver.get("https://www.instagram.com/")
          #see all button in suggested for you
          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a')[0].click()
          sleep(2)
          #getting the suggesstions list
          suggested_accounts_list = self.driver.find_elements_by_xpath("//*[text()='{}']".format("Follow"))
          if count is None:
               for i in range(5):
                    suggested_accounts_list[i].click()
                    sleep(1)
          else:
               for i in range(count):
                    suggested_accounts_list[i].click()
                    sleep(1)
     @operation
     def logout(self):
          self.driver.get("https://www.instagram.com/{}/".format(username))
          sleep(3)
          #settings in profile
          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/button')[0].click()
          sleep(3)
          #Log out
          self.driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div/button[9]')[0].click()
          sleep(5)
          self.driver.quit()
def get_credentials():
     global username,password
     config = ConfigParser()
     config.read('config.ini')
     username = config.get('AUTH', 'USERNAME')
     password = config.get('AUTH', 'PASSWORD')

def auto_pilot():
     bot=InstagramBot()
     bot.autoPilot()
     
if __name__ == '__main__':

     choice = int(input("Select Mode \n 1 - Auto Pilot\n 2 - Follow\n 3 - Like\n 4 - Comment\n 5 - Download Media\n"))
     mode={
          1:auto_pilot,
     }  
     #mode[choice]()
     get_credentials()
     auto_pilot()