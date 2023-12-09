import requests
from bs4 import BeautifulSoup as bs
from time import sleep

# передаем данные при осуществелнии запроса, чтобы сайт не распознавал как бота и не блокировал
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

# собираем ссылки на страинцы товаров и возвращаем их по одной
def get_link():
    for page in range(1, 7):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={page}"
        response = requests.get(url, headers=headers).text
        soup = bs(response, 'lxml')
        data = soup.findAll("div", class_="w-full rounded border")

        for i in data:
            card_url = 'https://scrapingclub.com' + i.find('a').get('href')
            yield card_url

# собираем данные из каждой карточки товара и возвращаем их по очереди, страница за страницей
def get_info_for_recording():
    for card in get_link():
        response = requests.get(card, headers=headers).text
        sleep(3)
        soup = bs(response, 'lxml')
        data = soup.find('div', class_='my-8 w-full rounded border')

        name = data.find('h3', class_='card-title').text
        price = data.find('h4', class_='my-4 card-price').text
        description = data.find('p', class_='card-description').text
        img_link = 'https://scrapingclub.com' + data.find('img', class_='card-img-top').get('src')
        yield name, price, description, img_link

