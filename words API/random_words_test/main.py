import requests

url = "https://wordsapiv1.p.rapidapi.com/words/"

querystring = {"random":"true"}

headers = {
	"X-RapidAPI-Key": "8edc69c65dmsh9314d6fc748018cp1104aejsn09d9fb0666ae",
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response = response.json()
print(response['word'])
if input("введи склади через пробіл").split(" ") == response['syllables']['list']:
    print("правильні склади")
else:
    print(response['syllables']['list'])

# a = {'word': 'unrhetorical',
#      'results': [{'definition': 'not rhetorical',
#                   'partOfSpeech': 'adjective',
#                   'also': ['informal', 'literal', 'plain'],
#                   'similarTo': ['matter-of-fact', 'plainspoken', 'prosaic'],
#                   'antonyms': ['rhetorical']}],
#      'syllables': {'count': 5, 'list': ['un', 'rhe', 'tor', 'i', 'cal']}}


