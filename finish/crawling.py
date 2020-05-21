from bs4 import BeautifulSoup
from selenium import webdriver
import time
from urllib.request import urlopen

def danggn(search):
    query_txt = search

    path = 'C:\\bootstrap\\sample_template\\ogani\\py\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get("https://www.daangn.com/search/" + query_txt)

    i = 0
    while i < 1:
        driver.find_element_by_class_name("more-btn").click()
        i = i + 1

    time.sleep(1)

    full_html = driver.page_source

    soup = BeautifulSoup(full_html, "html.parser")

    data = []
    n = 1
    for item in soup.select("a[href*=articles]"):
        data.append("https://www.daangn.com" + item.get("href", "/"))
        n +=1
        if n >7:
            break

    return data



def imageurl(search):
    query_txt = search

    path = 'C:\\bootstrap\\sample_template\\ogani\\py\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get("https://www.daangn.com/search/" + query_txt)

    i = 0
    while i < 1:
        driver.find_element_by_class_name("more-btn").click()
        i = i + 1

    time.sleep(1)

    full_html = driver.page_source

    soup = BeautifulSoup(full_html, "html.parser")

    imgurl = []
    n = 1
    for i in soup.find_all(class_="card-photo"):
        # img = soup.find_all(class_="card-photo")
        imgurl.append(i.find("img")["src"])
        n +=1
        if n >7:
            break
    return imgurl