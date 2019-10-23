from random import choice
from sys import argv


def load_words(amount):
    with open('/usr/share/dict/words', 'r') as file:

        word = file.read().split()
        random_word = []

        for i in range(int(amount)):
            random_word.append(choice(word))

        print(' '.join(random_word))


if __name__ == '__main__':
    # Slices from the first(int) argument until the end(':')
    args = argv[1:]
    load_words(args[0])
