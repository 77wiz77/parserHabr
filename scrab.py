from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv

data = ["name,title,tags,text".split(",")]

def trade_spiders (max_page):
  page = 1
  while page <= max_page:
    url = 'https://habr.com/ru/search/page{}/?q=%D0%B1%D0%BB%D0%BE%D0%BA%D1%87%D0%B5%D0%B9%D0%BD&target_type=posts&order=relevance'.format(page)
    source_code = requests.get(url).content.decode("utf-8")
    soup = BeautifulSoup(source_code, 'lxml')
    linkList = soup.findAll('a', {'class':'tm-article-snippet__title-link'})
    for i in range(0, len(linkList)-1):
      link = linkList[i].get('href') #ссылка текущей страницы
      link_url = 'http://habr.com'+link
      link_source_code = requests.get(link_url)
      link_soup = BeautifulSoup(link_source_code.text, 'lxml')

      name = link_soup.find('span', {'class':'tm-user-info__user'})
      title = link_soup.find('h1', {'class':'tm-article-snippet__title'})
      tagsList = link_soup.find('div', {'class':'tm-article-snippet__hubs'})
      text = link_soup.find('div', {'class':'tm-article-body'})

      print('\n' + 'Автор: ' + name.text)
      print('\n' + 'Заголовок: ' + title.text)
      print('Теги: ' + tagsList.text)
      print('\n' + 'Текст: ' + text.text)
      data.append(
          [str(name.text.split(",")).strip()] 
                  + [str(title.text.split(",")).strip()]
                  + [str(tagsList.text.split(",")).strip()]
                  + [str(text.text.split(",")).strip()])
    page+=1
    
trade_spiders(3) #количество страниц / можно и больше, но долго обрабатывает

def csv_writer(data, path): #сохранение результатов в CSV
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

path = "output.csv"
print(data)
csv_writer(data, path)