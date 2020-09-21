from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstaBot:
    def __init__(self, username, pw):
        """
        Initializes an instace of the Instagrambot class
        Call the login method to auntheticate a user with IG

        Args:
            username:str: The Instagram username for login
            passwordR: str: The Instagram password for a user

        Attributes:
            driver: Selenium.webdriver.Chrome: The ChromeDriver that is used to automate browser actions.
            """

        self.driver = webdriver.Chrome("C:/Users/chong/AppData/Local/Programs/Python/Python38-32/Scripts/chromedriver.exe")
        self.driver.get("https://instagram.com")
        self.base_url = 'https://www.instagram.com'


   
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        element.send_keys("*****")

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys("*****")
        self.driver.find_element_by_id("loginForm").click()
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "react-root"))).click()
        time.sleep(2)
        self.driver.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")[0].click()
        time.sleep(2)
        self.driver.get('{}/{}'.format(self.base_url, 'fatcatharvey'))
        time.sleep(6)
        self.driver.find_element_by_css_selector('[alt= "Harvey ll\'s profile picture"]').click()
        time.sleep(10)
