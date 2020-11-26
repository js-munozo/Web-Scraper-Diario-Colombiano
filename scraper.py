# Web scraper para obtener noticias del diario "El Colombiano"

import requests
from bs4 import BeautifulSoup

url = 'https://www.elcolombiano.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encuentra la ubicacion de las noticias en la clase right e ingresa a h3
news_colombiano = soup.select('.right h3')

news = []
for new in news_colombiano:

    # ubica la <a> del comienzo con su atributo href. Se agregan los titulos de las noticias a la lista
    news.append(new.find('a').attrs['href'])

count = 0
for title in news:
    print('{})\t'.format(count) ,title)
    count += 1

user_selection = int(input('\nIngrese el número de la noticia que desea leer: \t'))
new_selected = 'https://www.elcolombiano.com{}'.format(news[user_selection])
print('Ingresando a la noticia: \t', new_selected + '\n')

# Ingresar a la noticia seleccionada por el ususario
response_new_selected = requests.get(new_selected)
soup_new_selected = BeautifulSoup(response_new_selected.text , 'html.parser')

# Ingresar al texto de la noticia a través de los selectores css
text_new_selected = soup_new_selected.select('div.iter-page-frame div.iter-content-wrapper section.seccion-internas-articulo div.content div.portlet-layout div.col-left-general div.text p')
for parrafo in text_new_selected:
    # El .text indica que se va a imprimir texto , entonces omite los <p>, </p> , <b> ....
    print(parrafo.text)
