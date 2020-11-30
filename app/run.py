#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import json

import os, time, random
from collections import namedtuple

url = "https://www.vocabulary.com"
api = "https://api.vocabulary.com/1.0/lists/?q=GRE&skip=0&limit=20&include=profiles"


def display_to_shell_extension(doc):
    info = '\n'
    info += '\t\t\t<b>'+ doc.word.title() +'</b>\n'
    info += '<b>Meaning:\t</b>' + doc.Meaning.replace('\n',' ').strip().title()+'\n\n'
    info += '<i>'+ doc.Example.replace('\n',' ').strip().title()+'</i>\n'
    
    return info


Vocab = namedtuple('Vocab',['word', 'Meaning','Example'])
words = []

res = requests.get(api)
vlist = json.loads(res.content)
for link in vlist['wordlists']:
    pg = requests.get(url+link['url'])
    soup = BeautifulSoup(pg.content)
    sel = soup.find_all('li',attrs={'class':'entry learnable'})
    for i in sel:
        words.append(
            Vocab(i.a.text,
            i.find('div', attrs={'class':'definition'}).text,
            i.find('div', attrs={'class':'details'}).text
        ))


icons = ['face-angel', 'face-smirk', 'face-laugh', 'face-surprise', 'face-wink']


while True:
    time.sleep(1800 * 2)
    os.system(f'notify-send -u critical -i {random.choice(icons)} "Take A Break" "{display_to_shell_extension(random.choice(words))}"')