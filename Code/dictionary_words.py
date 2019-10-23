from random import choice
from sys import argv


def load_words(amount):
    # ? ------- [VESRION 1 (FASTER)] -------
    # with open('/usr/share/dict/words', 'r') as file:

    #     word = file.read().split()
    #     random_word = []

    #     for x in range(int(amount)):
    #         random_word.append(choice(word))

    #     print(' '.join(random_word) + '.')

    # ? ------- [VESRION 2 (SLOWER)] -------
    # random_word = []
    # for x in range(int(amount)):
    #     random_word.append(
    #         choice(open('/usr/share/dict/words', 'r').read().split()))

    # print(' '.join(random_word) + '.')

    # ? ------- [VESRION 3 (CLOSE TO V1)] -------

    with open('/usr/share/dict/words', 'r') as file:
        words = [word for word in file.read().split()]
        random_word = ' '.join(choice(words) for i in range(int(amount))) + '.'

        print(random_word)


    # Slices from the first(int) argument until the end(':')
args = argv[1:]
load_words(args[0])
