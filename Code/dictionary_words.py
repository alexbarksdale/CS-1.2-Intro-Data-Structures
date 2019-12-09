from random import choice, randrange
from utils import time_it, read_file
from sys import argv


@time_it  # From ben's utils
def load_words(amount, source_file):

    # ? ------- [VESRION 1] -------
    #! Benchmark with 5 words: roughly 170 ms

    # random_word = []
    # for _ in range(int(amount)):
    #     random_word.append(
    #         choice(open('/usr/share/dict/words', 'r').read().split()))

    # return ' '.join(random_word) + '.'

    # ? ------- [VESRION 2 (FASTEST)] -------
    #! Benchmark with 5 words: roughly 35 ms

    # with open(word_file, 'r') as file:

    # word = file.read().split()
    # 'for x...' runs first. It loops through and runs 'choice(word)' then assigns the value to 'random_word'.
    random_word = [choice(source_file) for x in range(int(amount))]

    return ' '.join(random_word) + '.'

    # ? ------- [VESRION 3] -------
    #! Benchmark with 5 words: roughly 44 ms

    # with open('/usr/share/dict/words', 'r') as file:
    #     words = [word for word in file.read().split()]
    #     random_word = ' '.join(choice(words) for i in range(int(amount))) + '.'

    #     return ''.join(random_word) + '.'


if __name__ == '__main__':
    source = '/usr/share/dict/words'
    args = argv[1:]
    test = load_words(args[0], read_file(source))
    print(test)
