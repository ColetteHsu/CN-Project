from aiohttp import content_disposition_filename
import requests
import datetime
from bs4 import BeautifulSoup
from crawler import today



def star(msg):
    sname=msg[7:]
    response = requests.get("https://www.daily-zodiac.com/mobile/zodiac/"+sname)

    content=""

    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("section")
    today=str(datetime.date.today())
    
    for title in data:
        content=today+" 今日運勢"+title.select_one("article").getText()
    return content
