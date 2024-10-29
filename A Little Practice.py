
import requests

response = requests.get('https://www.gutenberg.org/files/3201/files/COMMON.TXT')

words = response.text.split('\r\n')

def get_long_words(text):
    long_words = []
    for word in text:
        letter_count = 0
        for char in word:
            if char.isalnum():
                letter_count += 1
        if letter_count > 20:
            long_words.append(word)
    return long_words

def no_e(word):
    for char in word:
        if char == 'e':
            return False
    else: return True

print(no_e('word'))

def e_elim(text):
    e_free = []
    e_count = 0
    for word in text:
        if no_e(word):
            e_free.append(word)
            e_count += 1
    print(e_free)
    print(e_count / len(text))

def avoids(word: str, forbidden: str):
    for char in word:
        for letter in forbidden:
            if letter == char:
                return False
    else: return True

print(avoids('delicious', 'yzm'))

def avoid_largescale(text, forbidden):
    num_avoid = 0
    for word in text:
        if avoids(word, forbidden):
            num_avoid += 1
    print(num_avoid)
    print(num_avoid / len(text))

def useseonly(word: str, letters: str):
    for char in word:
        for letter in letters:
            if letter != char:
                return False
    else: return True

avoid_largescale(words, 'zqvjx')

def usesall(word, required):
    pass