from aiohttp import content_disposition_filename
import requests
from bs4 import BeautifulSoup

def food():
    response = requests.get("https://udn.com/author/articles/2/1911")

    content=""

    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("div", {"class": "story-list__text"})


    for index,d in enumerate(data):
        if index <5:
            title=d.select_one("a").getText()  # 取得標題文字
            href=d.select_one("a").get("href")
            content += "{}\n{}\n".format(title, href)
        else:
            break
    return content

def today():
    response = requests.get("https://udn.com/news/breaknews")
    
    content=""

    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("div", {"class": "story-list__text"})

    base='https://udn.com'
    for index,d in enumerate(data):
        if index <5:
            title=d.select_one("a").getText()  # 取得標題文字
            href= base +d.select_one("a").get("href")
            content += "{}\n{}\n".format(title, href)
        else:
            break
    return content

def entertainment():
    response = requests.get("https://stars.udn.com/star/cate/10087")
    
    content=""

    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("div", {"class": "item-text"})

    base='https://stars.udn.com/'
    for index,d in enumerate(data):
        if index <5:
            title=d.select_one("a").getText()  # 取得標題文字
            href= base +d.select_one("a").get("href")
            content += "{}\n{}\n".format(title, href)
        else:
            break
    return content

def sport():
    response = requests.get("https://tw.news.yahoo.com/sports")
    
    content=""

    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("li", {"class":"Pos(r) Lh(1.5) H(24px) Mb(8px)"})
    for index,d in enumerate(data):
        if index<5:
            title=d.select_one("a").getText()
            href=d.select_one("a").get("href")
            content+="{}\n{}\n".format(title,href)
        else:
            break
    return content

def covid():
    response = requests.get("https://udn.com/news/covid19/COVID19_Taiwan")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find("p").getText()
    content="{}".format(data)
    return content

def life():
    content=""
    response = requests.get("https://www.ettoday.net/news/focus/%E7%94%9F%E6%B4%BB/")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("div",class_="piece clearfix")
    base="https://www.ettoday.net/"
    for index,d in enumerate(data):
        if index <5:
            title=d.select_one("a").get("title")  # 取得標題文字
            href=d.select_one("a").get("href")
            content += "{}\n{}\n".format(title, base+href)
        else:
            break
    return content

def internet():
    content=""
    response = requests.get("https://www.ettoday.net/news/focus/%E5%9C%8B%E9%9A%9B/")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("div",class_="piece clearfix")
    base="https://www.ettoday.net/"
    for index,d in enumerate(data):
        if index <5:
            title=d.select_one("a").get("title")  # 取得標題文字
            href=d.select_one("a").get("href")
            content += "{}\n{}\n".format(title, base+href)
        else:
            break
    return content

def covidnews():
    content=""
    response = requests.get("https://udn.com/search/tagging/2/%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("div",class_="story-list__text")

    for index,d in enumerate(data):
        if index <5:
            title=d.select_one("a").get("title")  # 取得標題文字
            href=d.select_one("a").get("href")
            content += "{}\n{}\n".format(title, href)
        else:
            break
    return content
def movie():

    content=""
    response = requests.get("https://movies.yahoo.com.tw/tagged/movieheadline")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("li",class_="news_content")

    for index,d in enumerate(data):
        if index <5:
            title=d.select_one("h2").getText()  # 取得標題文字
            href=d.select_one("a").get("href")
            content += "{}\n{}\n".format(title, href)
        else:
            break
    return content

def it():

    content=""
    response = requests.get("https://www.ithome.com.tw/")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("p",class_="title")
    base="https://www.ithome.com.tw/"
    for index,d in enumerate(data):
        if index <5:
            title=d.select_one("a").getText()  # 取得標題文字
            href=d.select_one("a").get("href")
            content += "{}\n{}\n".format(title, base+href)
        else:
            break
    return content

def fashion():

    content=""
    response = requests.get("https://www.elle.com/tw/fashion/")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("div",class_="custom-item-content")
    base="https://www.elle.com/"
    for index,d in enumerate(data):
        if index <5:
            title=d.select_one("a").getText()  # 取得標題文字
            href=d.select_one("a").get("href")
            content += "{}\n{}\n".format(title, base+href)
        else:
            break
    return content

def others():
    content="https://news.google.com/search?q="
    return content


