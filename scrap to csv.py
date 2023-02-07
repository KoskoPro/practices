# Parse webpage and save to csv file

import requests
from bs4 import BeautifulSoup
import csv

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
data = BeautifulSoup(response.content, 'html.parser')


quotes = data.find_all(class_='quote')
with open('test.csv', 'w') as file:
    headers = ['quote', 'author', 'keywords']
    file_writer = csv.DictWriter(file, fieldnames=headers)
    file_writer.writeheader()

    for quote in quotes:
        text = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        keywords = quote.find(class_='keywords')['content']
        file_writer.writerow({
            'quote': text,
            'author': author,
            'keywords': keywords
        })
