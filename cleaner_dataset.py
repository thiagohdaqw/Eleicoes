from clean import cleaner, remove_accent, remove_genre
from unidecode import unidecode

POSITIVE_PATH = "dataset/positivas.txt"
NEGATIVE_PATH = "dataset/negativas.txt"
DATASET_PATH = "dataset/dataset.csv"

DELIMITER = ","

POSITIVE_NUMBER = 1
NEGATIVE_NUMBER = 0

positives = set()
negatives = set()

def read_file(path, words):
    with open(path, "r") as file:
        for word in file:
            word = cleaner(word)
            accentless_word = unidecode(word)
            words.add(word)
            words.add(accentless_word)
            words.add(remove_genre(word))
            words.add(remove_genre(accentless_word))

def write_dataset(file, words, number):
    words.remove("")
    for word in words:
        file.write(f"{number}{DELIMITER}{word}\n")


read_file(POSITIVE_PATH, positives)
read_file(NEGATIVE_PATH, negatives)

with open(DATASET_PATH, "w") as dataset_file:
    dataset_file.write(f"sentiment{DELIMITER}sentence\n")
    write_dataset(dataset_file, positives, POSITIVE_NUMBER)
    write_dataset(dataset_file, negatives, NEGATIVE_NUMBER)