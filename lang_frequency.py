import codecs
from collections import Counter
import argparse
import re


def load_data(file_path):
    with codecs.open(file_path, 'r', 'cp1251') as opened_file:
        text = opened_file.read()
    return text


def get_most_frequent_words(text):
    text = re.findall(r'\w+', text.lower())
    most_frequent_words = Counter(text)
    return most_frequent_words


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path')
    parser.add_argument('most_frequent_words_amount')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    text = load_data(args.file_path)
    most_frequent_words_amount = int(args.most_frequent_words_amount)
    most_frequent_words = get_most_frequent_words(text)
    for word, count in most_frequent_words.most_common(most_frequent_words_amount):
        print('{0:3} - {1:0d}'.format(word, count))
