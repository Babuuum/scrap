import requests
from bs4 import BeautifulSoup

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

response = requests.get("https://habr.com/ru/all/")
response.raise_for_status()

text = response.text

soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    titles = article.find_all("span", class_="tm-article-snippet__title tm-article-snippet__title_h2")
    hubs = article.find_all('span', class_='tm-article-snippet__hubs-item')
    bodies = article.find_all('p', class_='article-formatted-body')
    hubs_text = {hub.text for hub in hubs}
    titles_text = {title.text for title in titles}
    bodies_text = {body.text for body in bodies}
    if KEYWORDS & (hubs_text or titles_text or bodies_text):
            title_show = article.find("h2")
            link = title_show.find("a").attrs.get("href")
            url = "https://habr.com" + link
            time = article.find("time")
            print(f"<{time}>-<{title_show}>-<{url}>")
print("хотел бы попросить прочитать закомментированую часть под кодом")
#долго пытался установить библиотеку(SOUP), нашел только эту(дефолтная выдовала ошибку при установке)
#код запускается раз в 30+ попыток, возможно это защита сайта так себя ведет
#если есть способ обойти ограничение хотел бы вас попросить, рассказать о нем
#если из за моей ошибки, хотел бы попросить указать на нее
#к слову закономерность я так и не выяснил
#тестить что то ОЧЕНЬ проблематично
#так как не знаю, есть ли смысл писать в слак(в меру прошедшего времени), пишу это тут
#по поводу задачи, так и не понял в чем ошибка в 14 строке, но заголовки так и не нашлись(((

