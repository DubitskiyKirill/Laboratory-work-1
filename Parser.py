from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    url = 'https://auto.drom.ru' # передаем необходимый URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    f = open('file.txt', 'w', encoding='utf-8')
    allCars = soup.findAll('div', class_='css-17lk78h e3f4v4l2')#марка и модель автомобиля, год выпуска
    #allCars = soup.findAll('div', class_='css-13ocj84 e1icyw250')  # всё вышеперечисленное, плюс краткое описание
    description = ' '
    for data in allCars: # проходим циклом по содержимому контейнера
        if data.find('span'): # находим тег <span>
            f.write(f"{data.text}\n")
            description = data.text # записываем в переменную содержание тега
        print(description)