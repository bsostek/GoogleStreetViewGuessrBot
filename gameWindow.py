import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import CHROMEDRIVER_PATH
from PIL import Image

#Change chrome driver path accordingly
driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# URL of website
url = "https://openguessr.com"

def startGame():
    # Opening the website
    driver.get(url)

def getScreenshot():
    time.sleep(5)
    driver.save_screenshot("image.png")
    return Image.open('image.png') 

def closeGame():
    driver.close()
    
