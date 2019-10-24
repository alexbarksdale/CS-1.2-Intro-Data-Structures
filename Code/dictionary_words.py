from random import choice, randrange
from sys import argv
from utils import time_it

# Todo: Check for repeats


@time_it
def load_words(word_file, amount):

    # ? ------- [VESRION 1] -------
    # random_word = []
    # for x in range(int(amount)):
    #     random_word.append(
    #         choice(open('/usr/share/dict/words', 'r').read().split()))

    # print(' '.join(random_word) + '.')

    # ? ------- [VESRION 2] -------
    with open(word_file, 'r') as file:

        word = file.read().split()
        # random_word = []

        # for x in range(int(amount)):
        #     random_word.append(choice(word))

        random_word = [choice(word) for x in range(int(amount))]

        return ' '.join(random_word) + '.'

    # ? ------- [VESRION 3] -------

    # with open('/usr/share/dict/words', 'r') as file:
    #     words = [word for word in file.read().split()]
    #     random_word = ' '.join(choice(words) for i in range(int(amount))) + '.'

    #     return random_word


if __name__ == '__main__':
    dict_words = '/usr/share/dict/words'
    # Slices from the first(int) argument until the end(':')
    args = argv[1:]
    test = load_words(dict_words, args[0])
    print(test)
