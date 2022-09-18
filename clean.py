import re
from unidecode import unidecode

STOPWORDS_PATH = "dataset/stopwords.txt"
CLEAN_REGEX = r"[.,/\\\[\]\{\}`~^\d&!@#$%*\)\(\'\"<>=+-:;?“]"

stopwords = set()

with open(STOPWORDS_PATH, "r") as stop_file:
    for w in stop_file:
        stopwords.add(w.strip().lower())

def remove_genre(word):
    return " ".join(re.sub(r"[oa]s?$", "", w) for w in word.split())

def remove_accent(word):
    return unidecode(word)

def cleaner(sentence):
    sentence = " ".join(
        filter(
            lambda x: x not in stopwords,
            re.sub(CLEAN_REGEX, '', sentence).lower().split()
        )
    )
    return sentence