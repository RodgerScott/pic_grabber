import requests
from bs4 import BeautifulSoup
import os


r = requests.get('https://en.wikipedia.org/wiki/Hippopotamus')
data = r.text
soup = BeautifulSoup(data, 'lxml')

for link in soup.find_all('img'):
    image = link.get('src')
    image = 'http:' + image
    print(image)
