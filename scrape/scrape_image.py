import os
from bs4 import BeautifulSoup
import time
import requests
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(executable_path='/Users/antonskovpen/Downloads/geckodriver')
driver.get("http://www.chrisburkard.com/Stills")

iterations = 0
while iterations < 10:
    html = driver.execute_script("return document.documentElement.outerHTML")
    sel_soup = BeautifulSoup(html,'html.parser')
    print(len(sel_soup.findAll("img")))
    images = []
    for i in sel_soup.findAll("img"):
        src = i["src"]
        images.append(src)
    print(images)
    current_path = os.getcwd()
    for img in images:
        try:
            file_name = os.path.basename(img)
            img_r = requests.get(img, stream=True)
            new_path = os.path.join(current_path, "images", file_name)
            with open(new_path, "wb") as output_file:
                shutil.copyfileobj(img_r.raw, output_file)
            del img_r
        except:
            pass
    iterations += 1
    time.sleep(5)

'''   
driver = webdriver.Firefox(executable_path=r'/Users/antonskovpen/Downloads/geckodriver') 
driver.get("https://rozetka.com.ua/")

iterations = 0
while iterations < 10:
    html = driver.execute_script("return document.documentElement.outerHTML")
    sel_soup = BeautifulSoup(html, 'html.parser')
    print(len(sel_soup.findAll("img")))
    images = []
    for i in sel_soup.findAll("img"):
        scr = i["src"]
        images.append(scr)
    print(images)
    current_path = os.getcwd()
    for img in images:
        try:
            file_name = os.path.basename(img)
            img_r = requests.get(img, stream=True)
            new_path = os.path.join(current_path, "images", file_name)
            with open(new_path, "wb") as output_file:
                shutil.copyfileobj(img_r.raw, output_file)
            del img_r
        except:
            pass
    iterations += 1
    time.sleep(5)
'''