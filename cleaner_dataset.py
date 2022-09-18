from clean import cleaner

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
            words.add(cleaner(word))

def write_dataset(file, words, number):
    words.remove("")
    for word in words:
        file.write(f"{number}{DELIMITER}{word}\n")


read_file(POSITIVE_PATH, positives)
read_file(NEGATIVE_PATH, negatives)

with open(DATASET_PATH, "w") as dataset_file:
    write_dataset(dataset_file, positives, POSITIVE_NUMBER)
    write_dataset(dataset_file, negatives, NEGATIVE_NUMBER)