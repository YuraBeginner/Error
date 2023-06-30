import requests
from bs4 import BeautifulSoup
from config import PARS_URL, HEADERS


def get_html(PARS_URL, HEADERS):
    response = requests.get(PARS_URL,headers=HEADERS)
    if response.status_code == 200:
        return response.text
    raise ValueError("get_html Ошибка код статуса" + str(response.status_code))


def get_source(html):
    soup = BeautifulSoup(html,"lxml").find_all(
        "div", {"class": "sidebar-cat"}
        )

    data = []

    for i in soup:
        if i.find("span", {"class": "text-ru"}) is not None:
            data.append(i.find("span", {"class": "text-ru"}).text)
        continue
    

    return data


def run():
    html = get_html(PARS_URL,HEADERS)
    soup = get_source(html)
    return soup

print(run())