from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv

data = ["nameList,titleList,tagList,textList".split(",")]

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

def trade_spiders (max_page):
  page = 1
  while page <= max_page:
    url = 'https://habr.com/ru/search/page{}/?q=react&target_type=posts&order=relevance'.format(page)
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    # pages = int(soup.select("tm-pagination__page"))[-1] сделать вывод с нескольких страниц
    nameList = soup.findAll('a', {'class':'tm-user-info__username'})
    titleList = soup.findAll('h2', {'class':'tm-article-snippet__title'})
    tagList = soup.findAll('div', {'class':'tm-article-snippet__hubs'})
    textList = soup.findAll('div', {'class':'article-formatted-body'})
    for i in range(0, len(nameList)):
      print('\n' + 'Автор: ' + nameList[i].text)
      print('Заголовок: ' + titleList[i].text)
      print('Тег: ' + tagList[i].text)
      print('Текст: ' + textList[i].text)
      print('---------------------------------')
      data.append(
          [str(nameList[i].text.split(",")).strip()] 
                  + [str(titleList[i].text.split(",")).strip()] 
                  + [str(tagList[i].text.split(",")).strip()] 
                  + [str(textList[i].text.split(",")).strip()])
    page+=1
    
trade_spiders(40)
path = "output.csv"
print(data)
csv_writer(data, path)