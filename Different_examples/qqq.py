from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://www.labirint.ru/books/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

with open('D://ARZ/Python/parcer/site_books.txt', 'w', encoding='utf-8') as record:
    record.write(soup.prettify())

with open('D://ARZ/Python/parcer/site_books.txt', 'w', encoding='utf-8') as record:
    record.write(soup.prettify())