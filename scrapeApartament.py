#https://www.youtube.com/watch?v=RvCBzhhydNk
from bs4 import BeautifulSoup
import requests 


url = 'https://www.pararius.com/pisos/den-haag/apartamento-piso'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_='listing-search-item listing-search-item--list listing-search-item--for-rent')


for list in lists:

    title = list.find('a', class_='listing-search-item__link listing-search-item__link--title').get_text(strip=True, separator=' ')
    location = list.find('div',class_='listing-search-item__sub-title').get_text(strip=True, separator=' ')
    price = list.find('div',class_='listing-search-item__price').get_text(strip=True, separator=' ')
    area = list.find('ul',class_='illustrated-features illustrated-features--compact').get_text(strip=True, separator=' ')


