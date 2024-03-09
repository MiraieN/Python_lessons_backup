import requests
from random_word import RandomWords

url = "https://wordsapiv1.p.rapidapi.com/words/apple/definitions"

headers = {
	"X-RapidAPI-Key": "8edc69c65dmsh9314d6fc748018cp1104aejsn09d9fb0666ae",
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}
#
# r = RandomWords()
# random_words_list = []
# while len(random_words_list) != 15:
#
# print(r.get_random_word())

response = requests.get(url, headers=headers)

for definition in response.json()['definitions']:
	print(definition['definition'])