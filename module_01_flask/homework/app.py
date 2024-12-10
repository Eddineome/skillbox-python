from flask import Flask
import random
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)

# Глобальные переменные
cars = ["Chevrolet", "Renault", "Ford", "Lada"]
cat_breeds = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
counter = {"visits": 0}

# Путь к файлу с текстом
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

# Список слов из книги
with open(BOOK_FILE, 'r', encoding='utf-8') as book:
    text = book.read()
    words = re.findall(r'\b\w+\b', text)


@app.route('/')
def home():
    return "Добро пожаловать на наш веб-сервер! Вот доступные маршруты:<br>" \
           "/hello_world<br>" \
           "/cars<br>" \
           "/cats<br>" \
           "/get_time/now<br>" \
           "/get_time/future<br>" \
           "/get_random_word<br>" \
           "/counter"


@app.route('/hello_world')
def hello_world():
    return "Привет, мир!"


@app.route('/cars')
def get_cars():
    return ", ".join(cars)


@app.route('/cats')
def get_random_cat():
    return random.choice(cat_breeds)


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Точное время: {current_time}"


@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = (datetime.now() + timedelta(hours=1)).strftime("%H:%M:%S")
    return f"Точное время через час будет {current_time_after_hour}"


@app.route('/get_random_word')
def get_random_word():
    return random.choice(words)


@app.route('/counter')
def visit_counter():
    counter['visits'] += 1
    return f"Эта страница открывалась {counter['visits']} раз(а)"


if __name__ == '__main__':
    app.run(debug=True)
