from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import shutil

def cimg():

    ## 所以要取得每日人數的圖片，只需要爬此網頁
    infogram_url = 'https://infogram.com/21e6afd5-1359-4206-87ca-00a58b08950d'
    session = HTMLSession()
    r = session.get(url=infogram_url)
    ## 等待網頁炫染完成（最多等待6秒）
    r.html.render(timeout=10)
    img = r.html.find('img')
    img_url_list = []
    content=""
    for i in img:
        soup = BeautifulSoup(i.html, 'html.parser')
        ## 選找 img class_="ItemContent-image YCcPGnS5dPOBZH7uB0ZNs"
        img_class = soup.find_all('img', class_='ItemContent-image YCcPGnS5dPOBZH7uB0ZNs')
        if len(img_class) < 1:
            pass
        else:
            for src in img_class:
                ## 取回當天的 圖片 url ，（每天應該會換）。
                img_url_list.append(src.get('src'))
    content=img_url_list[0]
    return content            

#print(cimg())
    # for i in range(0, len(img_url_list)):
    #     response = requests.get(img_url_list[i], stream=True)
    #     content=str(img_url_list[0])
    #         # with open(f'img{i}.png', 'wb') as out_file:
    #         #     shutil.copyfileobj(response.raw, out_file)
    #         # del response

    # #r.close()
    # return content
