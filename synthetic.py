import re
import argparse
from collections import defaultdict
import random


class Dictionaries:
    dictionary = defaultdict(lambda: defaultdict(int))
    first_letters = defaultdict(int)


def words(filename, num, seed=None):
    if seed is not None:
        random.seed(seed)

    training_words = read_file(filename)
    dictionaries = create_dictionary(training_words)
    word_list = generate_words(dictionaries.first_letters, dictionaries.dictionary, num)
    return word_list


def read_file(filename):
    training_words = []
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            for word in re.split('\W+', line):
                word = word.lower()
                training_words.append(word)

    training_words.pop(-1)
    return training_words


def create_dictionary(training_words):
    dictionaries = Dictionaries()

    for word in training_words:
        dictionaries.first_letters[word[0]] += 1
        for i in range(len(word) - 1):
            dictionaries.dictionary[word[i]][word[i + 1]] += 1

        dictionaries.dictionary[word[-1]][""] += 1

    return dictionaries


def generate_words(first_letters, dictionary, num):
    word_list = []
    letters = list(first_letters.keys())
    probability = list(first_letters.values())

    for i in range(num):
        word = list_to_string(random.choices(letters, weights=probability, k=1))

        while True:
            next_letters = list(dictionary[word[-1]].keys())
            next_probability = list(dictionary[word[-1]].values())
            next_letter = list_to_string(random.choices(next_letters, weights=next_probability, k=1))
            if next_letter == '':
                break
            word += next_letter

        word_list.append(word)

    return word_list


def list_to_string(s):
    new = ""
    for x in s:
        new += x

    return new

def setup_parser():
    hash_parser = argparse.ArgumentParser(description="Program which calculates time of adding, "
                                                      "enumerating and deleting elements from hashmap "
                                                      "consisting of singly linked lists")

    group_req = hash_parser.add_argument_group("arguments")
    group_req.add_argument("-i", "--input", required=True,
                           help="input file with words")
    group_req.add_argument("-n", "--number", type=int, required=True,
                           help="number of words generated")
    group_req.add_argument("-o", "--output", required=True,
                           help="output file")
    group_req.add_argument("-s", "--seed", required=False, default=None,
                           help="optional seed for generation")

    return hash_parser


if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()
    words_list = words(args.input, args.number, args.seed)
    with open(args.output, 'w') as file:
        for word in words_list:
            file.write(str(word + " "))

    print("Generated successfully to", args.output)
