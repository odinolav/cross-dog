import requests
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
import re
import Beeps

# Dog Breed +: crossbred dogs with detailed stats
URLS_1 = ['https://www.dogbreedplus.com/dog_categories/hybrid_dogs.htm',
          'https://www.dogbreedplus.com/dog_categories/hybrid_dogs_def.htm',
          'https://www.dogbreedplus.com/dog_categories/hybrid_dogs_ghi.htm',
          'https://www.dogbreedplus.com/dog_categories/hybrid_dogs_jkl.htm',
          'https://www.dogbreedplus.com/dog_categories/hybrid_dogs_mno.htm',
          'https://www.dogbreedplus.com/dog_categories/hybrid_dogs_pqr.htm',
          'https://www.dogbreedplus.com/dog_categories/hybrid_dogs_stu.htm',
          'https://www.dogbreedplus.com/dog_categories/hybrid_dogs_vwx.htm',
          'https://www.dogbreedplus.com/dog_categories/hybrid_dogs_yz.htm']

all_dogs = []

def scrape_url_1(url) -> list:
    # test url
    #url = 'https://www.dogbreedplus.com/dog_categories/hybrid_dogs.htm'
    page_soup = soup(requests.get(url).content)
    dog_blocks = page_soup.find_all('div', {'class': 'single-breed-overview'})
    new_dogs = []
    for dog in dog_blocks:
        dog_info = {}
        dog_info['imgs'] = [dog.find('div', {'class': 'breed-image'}).a.img['src']]
        dog_info['name'] = dog.find('div', {'class': 'image-next-part'}).a.contents[0].strip()
        dog_info['url'] = dog.find('div', {'class': 'image-next-part'}).a['href'].strip()
        dog_info['parents'] = dog.find('div', {'class': 'image-next-part'}).span.contents[0]\
            .replace(' and ', ', ').replace(' Mix', '').replace('/', ', ')\
            .replace('Dachshund ', 'Dachshund, ').replace('German Shepherd ', 'German Shepherd, ')\
            .replace('Golden Retriever ', 'Golden Retriever, ').replace('Husky ', 'Husky, ')\
            .replace('Pitbull ', 'Pitbull, ').replace('Rottweiler ', 'Rottweiler, ')\
            .replace('Poodle ', 'Poodle, ').replace('Lab', 'Labrador Retriever')\
            .replace('Labrador Retriever ', 'Labrador Retriever, ')\
            .replace('Husky', 'Siberian Husky')\
            .strip().split(', ')
        if len(dog_info['parents']) == 1:
            dog_info['parents'] = input(dog_info['name']+ ': Retype "' + dog_info['parents'][0] + '" with commas.').split(', ')
        # Unneeded edge cases where no parents were found
        #elif len(parents) == 0:
        #    parents = input('Type the parents of "' + name + '" separated by commas.').split(', ')
        for r in dog.find('table', {'class': 'breed-overview-table'}).find_all('tr'):
            tds = r.find_all('td')
            dog_info[tds[0].contents[0].strip()] = tds[1].contents[0].strip()
        dog_info['hypoallergenic'] = dog.find('div', {'class': 'breed-info-circle'}).p.contents[0]
        dog_info['traits'] = [item.strip() for item in list(filter(lambda v: isinstance(v, str) , dog.find('div', {'class': 'single-breed-colum-03'}).contents[2:]))]

        new_dogs.append(dog_info)
    return new_dogs

for u in URLS_1:
    all_dogs += scrape_url_1(u)


f = open('dog_list_1.json', 'w')
f.write(json.dumps(all_dogs))
f.close()

Beeps.done()
