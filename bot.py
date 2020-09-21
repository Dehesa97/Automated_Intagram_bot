from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
print(driver.title)

search = driver.find_element_by_class_name("_2hvTZ pexuQ zyHYP")
search.send_keys("test")
search.send_keys(Keys.RETURN)

link = driver.find_element_by_link_text


