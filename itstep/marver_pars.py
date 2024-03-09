import requests
from bs4 import BeautifulSoup
import csv

# Функція для отримання даних зі сторінки Marvel про героїв
def get_marvel_characters():
    url = "https://www.marvel.com/characters"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    characters = []

    # Знаходимо всіх героїв у списку
    character_cards = soup.find_all("div", class_="card_wrapper")
    for card in character_cards:
        character = {}

        # Отримуємо ім'я героя
        name = card.find("h4", class_="card__headline").text.strip()
        character["name"] = name

        # Отримуємо посилання на сторінку героя
        link = card.find("a", class_="card__anchor")["href"]
        character["link"] = link

        # Отримуємо всю інформацію про героя (якщо доступно)
        character_info = card.find("div", class_="card__content")
        if character_info:
            character_info = character_info.find_all("div", class_="copy")
            for info in character_info:
                label = info.find("p", class_="copy__label").text.strip()
                value = info.find("p", class_="copy__text").text.strip()
                character[label] = value

        characters.append(character)

    return characters

# Функція для збереження даних у файл CSV
def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Отримуємо дані про героїв Marvel
characters = get_marvel_characters()

# Зберігаємо дані у файл CSV
save_to_csv(characters, "marvel_characters.csv")

print("Дані збережено у файлі marvel_characters.csv")
