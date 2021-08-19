from uzwords import words
from difflib import get_close_matches


def checker(word, words = words):
    word = word.lower
    match = set(get_close_matches(word, words))
    available = False
    
    if word in match:
        available = True # mavjud
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        match.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        match.update(get_close_matches(word, words))
    
    return { "available": available ,"match": match }

if __name__ == '__main__':
    print("hello world")
    print(checker("тариҳ"))