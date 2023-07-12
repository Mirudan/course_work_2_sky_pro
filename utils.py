import json
import requests
import random
import basicword_class


def load_random_word(JSON_DATA_URL, DATA_PATH):
    """
    Получаем список слов с внешнего ресурса,
    выбираем случайное слово из списка,
    создаем экземпляр класса `BasicWord`
    :return: экземпляр класса `BasicWord`
    """
    # запрос на получение данных по url для дальнейшей работы
    response = requests.get(JSON_DATA_URL)

    # если сайт с json файлом недоступен, то загружается локальный файл
    if response.status_code != 200:
        with open(DATA_PATH, encoding='utf-8') as file:
            words_json = json.load(file)
    else:
        words_json = response.json()

    # получаем случайный словарь из списка
    random_dict = random.choice(words_json)

    # объявляем экземпляр класса 'BasicWord'
    random_basic_word = basicword_class.BasicWord(random_dict["word"], random_dict["subwords"])

    return random_basic_word
