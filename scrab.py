from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests 
from bs4 import BeautifulSoup
import csv

def trade_spiders (max_page):
  page = 1
  while page <= 30:
    url = 'https://habr.com/ru/search/?q=react&target_type=posts&order=relevance' + str(page)
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    nameList = bs.findAll('span', {'class':'tm-user-info__user'})
    titleList = bs.findAll('h2', {'class':'tm-article-snippet__title'})
    tagList = bs.findAll('div', {'class':'tm-article-snippet__hubs'})
    textList = bs.findAll('div', {'class':'.article-formatted-body'})
    for i in range(0, len(nameList)):
      print('\n' + 'Автор: ' + nameList[i].text)
      print('Заголовок: ' + titleList[i].text)
      print('Тег: ' + tagList[i].text)
      print('Текст' + textList[i].text)
      print('---------------------------------')
      page+=1

trade_spiders(1)

# with open('test.html', 'w') as output_file:
#   output_file.write(r.text)