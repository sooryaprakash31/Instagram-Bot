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
          self.driver.get("https://www.instagram.com/accounts/login/")
          sleep(1)

          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')[0].send_keys("hello")
          sleep(1)
          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')[0].send_keys("hello")
          sleep(2)
          self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')[0].click()


if __name__ == '__main__':

     bot = InstagramBot()