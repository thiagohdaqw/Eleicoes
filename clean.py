import re

STOPWORDS_PATH = "dataset/stopwords.txt"
CLEAN_REGEX = r"[.,/\\\[\]\{\}`~^\d&!@#$%*\)\(\'\"<>=+-:;?]"

stopwords = set()

with open(STOPWORDS_PATH, "r") as stop_file:
    for w in stop_file:
        stopwords.add(w.strip().lower())

def cleaner(sentence):
    sentence = " ".join(
        filter(
            lambda x: x not in stopwords,
            re.sub(CLEAN_REGEX, '', sentence).lower().split()
        )
    )
    return sentence