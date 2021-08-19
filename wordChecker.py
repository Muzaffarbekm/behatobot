from uzwords import words
from difflib import get_close_matches


def checker(word, words = words):
    word = word.lower
    match = set(get_close_matches(word, words))
    available = False
    
    if word in match:
        available = True
        match = word
    
    return { "available": available ,"match": match }

