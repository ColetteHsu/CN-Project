from bs4 import BeautifulSoup
import requests
 
 
# 連結網站
response = requests.get(
	"https://udn.com/author/articles/2/1911")

# HTML原始碼解析
soup = BeautifulSoup(response.text, "html.parser")
 
content=""
# 取得所有class為post_title的<h3>
data = soup.find_all("div", {"class": "story-list__text"})
 
for index,d in enumerate(data):
    if index <8:
        title=d.select_one("a").getText()  # 取得標題文字
        href=d.select_one("a").get("href")
        content += "{}\n{}\n".format(title, href)
    else:
        break

print(content)