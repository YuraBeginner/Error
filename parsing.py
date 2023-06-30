# import requests
from bs4 import BeautifulSoup

# url = "https://www.websklad.biz.ua"

# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0"
#     "accept:" "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
# }

# req = requests.get(url,headers=headers)
# src = req.text

# # print(src)
# with open("index.html","w",encoding="utf-8") as file:
#     file.write(src)

with open("index.html",encoding="utf-8") as file:
    src = file.read()
    
soup = BeautifulSoup(src,"lxml")

all_products_href = soup.find_all(class_="sidebar-cat")
for item in all_products_href:
    print(item)
    
