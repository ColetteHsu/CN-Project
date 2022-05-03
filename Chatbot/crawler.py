
import requests
from bs4 import BeautifulSoup

def food_crawler():
    response = requests.get(
	"https://udn.com/author/articles/2/1911")


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