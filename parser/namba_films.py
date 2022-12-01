import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint
URL = 'https://sumki-dina.com.ua/catalog/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.findAll('figure', class_="r_corners photoframe type_2 t_align_c tr_all_hover shadow relative")
    list_bags = []
    for item in items:
        bag = {
            "title": item.find('h5', class_="m_bottom_10").text,
            "price": item.find('p', class_="scheme_color f_size_large m_bottom_15").text[5:],
            "link": f"{URL[0:-9]}{item.find('a', class_='d_block relative wrapper pp_wrap m_bottom_15').get('href')}"
        }
        list_bags.append(bag)
    return list_bags



def parser():
    html = get_html(URL)
    data = get_data(html.text)
    return data