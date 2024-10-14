from bs4 import BeautifulSoup
import requests
from googletrans import Translator

translator = Translator()

def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        text = response.text

        soup = BeautifulSoup(text, 'html.parser')
        english_words = soup.find("div", id='random_word').text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        rus_words = translator.translate(english_words, dest='ru').text.strip()
        rus_definition = translator.translate(word_definition, dest='ru').text.strip()

        return {
            "rus_words": rus_words,
            "rus_definition": rus_definition
        }
    except:
        print("произошла ошибка")

def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("rus_words")
        rus_definition = word_dict.get("rus_definition")

        print(f'значение слова: "{rus_definition}"')
        user = input("что это за слово? ")
        if user == word:
            print("верно!")
        else:
            print(f'ты ошибся! Верное слово "{word}"')

        play_again = input("Хотите сыграть еще раз? да/нет ")
        if play_again != 'да':
            print('Спасибо за игру!')
            break
word_game()