from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

def urls():
    driver.get("http://www.youtube.com")
    time.sleep(2)
    driver.get("http://www.twitter.com")
    time.sleep(2)
    driver.get("https://docs.google.com/spreadsheets/u/1/d/1_NS8RzEDIdly5pCphfcCKxDIMb1kBGufPsbOCNihido/edit#gid=194510782")
    time.sleep(2)
    driver.get("https://www.simscale.com/users/dgomez_arboled/#viewMode=thumbView&sortBy=project_popular")
    time.sleep(2)
    driver.get("http://www.google.com")
    time.sleep(2)
    urls()
try:
    urls()
except:
    print("Browser window closed by user")