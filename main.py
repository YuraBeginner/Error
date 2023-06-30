import requests
from bs4 import BeautifulSoup
from config import PARS_URL, HEADERS


def get_html(PARS_URL, HEADERS):
    response = requests.get(PARS_URL,headers=HEADERS)
    if response.status_code == 200:
        return response.text
    raise ValueError("get_html Ошибка код статуса" + str(response.status_code))


def get_source(html):
    soup = BeautifulSoup(html,"lxml").find("ul", {"class": "products columns-4"}).find_all("li")
    
    data = dict()

    for item in soup:
        title = item.find("h2", {"class": "woocommerce-loop-product__title"})
        if title is not None:
            data.update({"title": title.text})
        continue

    return data


def run():
    html = get_html(PARS_URL,HEADERS)
    soup = get_source(html)
    return soup

print(run())