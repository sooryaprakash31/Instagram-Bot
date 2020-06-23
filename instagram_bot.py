from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import random
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
          self.follow_suggested()
          #To log out
          self.logout()
     
     @operation
     def unfollowAll(self):
          #login
          self.login()
          self.driver.get("https://www.instagram.com/{}/".format(username))
          sleep(3)
          unfollowing = True
          while unfollowing:    
               following_count=int(self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')[0].text)
               print("count",following_count)
               #following count button
               self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')[0].click()
               sleep(2)
               following_list=self.driver.find_elements_by_xpath("//button[text()='{}']".format("Following"))
               print(len(following_list))
               if following_count<5:            
                    for i in range(following_count):
                         self.unfollow(following_list[i])
                         unfollowing = False     
               else:
                    for i in range(5):
                         self.unfollow(following_list[i])
                    sleep(random.randint(2,6))
                    self.driver.refresh()
          sleep(2)
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
     def follow_suggested(self):
          self.driver.get("https://www.instagram.com/")
          count=25
          while count>0:
               #see all button in suggested for you
               self.driver.find_elements_by_xpath("//div[text()='{}']".format("See All"))[0].click()
               #self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a')[0].click()
               sleep(2)
               for i in range(5):
                    self.follow(i)
                    count = count-1
               sleep(random.randint(2,6))
               self.driver.refresh()
               
     @operation
     def follow(self,position):
          #Follow button
          self.driver.find_elements_by_xpath("//*[text()='{}']".format("Follow"))[int(position)].click()
          
     @operation
     def unfollow(self,account):
          account.click()
          sleep(1)
          self.driver.find_elements_by_xpath("//button[text()='{}']".format("Unfollow"))[0].click()

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
     get_credentials()
     bot=InstagramBot()
     bot.autoPilot()

def unfollow_all():
     get_credentials()
     bot=InstagramBot()
     bot.unfollowAll()     
if __name__ == '__main__':

     choice = int(input("Select Mode \n 1 - Auto Pilot\n 2 - Follow\n 3 - Unfollow\n 4 - Comment\n 5 - Download Media\n"))
     mode={
          1:auto_pilot,
          3:unfollow_all,
     }  
     mode[choice]()
     #get_credentials()
     #auto_pilot()