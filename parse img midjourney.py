from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from PIL import Image
import os

#download dynamic webpage
url='https://www.midjourney.com/showcase/recent/'
browser = webdriver.Chrome()
browser.get(url)
page=browser.page_source

#parsing links
bs_page = BeautifulSoup(page, 'html.parser')
bs_list_of_links=bs_page.find_all(class_='aspect-auto')

#save files
for element in bs_list_of_links:
    link=element.get('src')
    filename = link.split('/')[-2]
    path_name = './images/'+filename

    #download file
    data = requests.get(link)
    open(path_name,'wb').write(data.content)

    #converting file webp to jpg
    im = Image.open(path_name).convert('RGB')
    im.save(path_name+'.jpg','jpeg')

    #delete webp file
    os.remove(path_name)





