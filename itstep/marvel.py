from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import requests
import csv

driver = webdriver.Firefox()  # You can use other drivers like Firefox, etc.

url = "https://www.marvel.com/characters"
driver.get(url)

sleep(3)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

driver.quit()

soup_cards = soup.find("div", {"class": "content-grid content-grid__6"})

cards = soup_cards.find_all("div", {"class": "mvl-card mvl-card--explore"})

tags_to_extract = ["Universe", "Other Aliases", "Education", "Place of Origin", "Identity", "Known Relatives"]

characters = []

for card in cards:
    character = {}
    link = card.find(class_="explore__link")['href']
    url = "https://www.marvel.com" + link

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    name = soup.find("span", class_="masthead__headline").text
    character["Name"] = name
    character["Link"] = url
    print(character)

    label_tag = soup.find_all(class_="railBioInfo__Item")
    print(len(label_tag))

    for tag in tags_to_extract:
        for item in label_tag:
            if item.find(class_="railBioInfoItem__label").text == tag:
                character[tag] = item.find(class_='railBioLinks').text

    characters.append(character)

print(characters)

with open("marvel_characters_scrap.csv", 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, characters[0])
    dict_writer.writeheader()
    dict_writer.writerows(characters)
