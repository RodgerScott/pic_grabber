import requests
from bs4 import BeautifulSoup


def get_images(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')

    for link in soup.find_all('img'):
        image = link.get('src')
        image = 'http:' + image
        print(image)
