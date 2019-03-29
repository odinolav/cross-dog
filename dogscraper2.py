import requests
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
import re
import Beeps

# Dog Breed Info: crossbreeds and purebreds
URL = 'https://www.dogbreedinfo.com/a.htm'
URL_BASE = 'https://www.dogbreedinfo.com/'

all_dogs = []
bad_dogs = []

def begin_scrape():
    for link in soup(requests.get(URL).content).find('div', {'class': 'lettersHead'}).find('ul').find_all('a'):
        url = URL_BASE + link['href']
        scrape_page(url)

def scrape_page(url):
    for dog_link in soup(requests.get(url).content).find('div', {'class': 'letter'}).find_all('a'):
        url = URL_BASE + dog_link['href']
        scrape_dog(url)

def scrape_dog(url):
    new_dog = {}
    new_dog['url'] = url
    # test url
    #url = 'https://www.dogbreedinfo.com/alaskankleekai.htm'
    #url = 'https://www.dogbreedinfo.com/a/affenshire.htm'
    try:
        relevant = soup(requests.get(url).content).find('div', {'class': 'mainArea'})
        new_dog['name'] = relevant.find('article').h1.contents[0]
        other_names_box_maybe = relevant.find('article', {'class': 'attribute'})
        new_dog['other_names'] = []
        if other_names_box_maybe.h5.contents[0] == 'Other Names':
            if other_names_box_maybe.p:
                text = other_names_box_maybe.p.text
                new_dog['other_names'] = [text] if (text != '--' and text != '---') else []
            else:
                other_names_li = other_names_box_maybe.find_all('li')
                new_dog['other_names'] = [li.text.strip() for li in other_names_li if (li.text.strip() != '--' and li.text.strip() != '---')]
    except:
        bad_dogs.append(url)
        return

    new_dog['imgs'] = [URL_BASE+i['src'] for i in relevant.find_all('img') if (i['src'].startswith('image') and not i['src'].endswith('gif'))]

    try:
        new_dog['parents'] = [p for p in relevant.find('article').h4.contents[0]\
                .replace(' Mixed Breed Dogs', '').replace('Timber Wolf (Gray Wolf)', 'Gray Wolf')\
                .split(' / ') if len(p) > 1]
        new_dog['parents'] = [p if p != 'American Eskimo' else 'American Eskimo Dog' for p in new_dog['parents']]

        if len(new_dog['parents']) == 1:
            new_dog['parents'] = []
    except:
        new_dog['parents'] = []
    all_dogs.append(new_dog)

begin_scrape()

f = open('dog_list_2.json', 'w')
f.write(json.dumps(all_dogs))
f.close()

Beeps.done()


# Clean Data
f = open('dog_list_2.json', 'r')
data = json.load(f)
f.close()
for d in data:
    d['parents'] = [p.strip().replace('lll', 'll') for p in d['parents'] if p != '']
f = open('dog_list_1.json', 'w')
f.write(json.dumps(data))
