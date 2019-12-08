from random import randint
from sys import argv

'''
Utilizes the Fisher-Yates shuffle Alogirthm
Desc: This alogrithm takes the index value and swaps it with the current value until the end of the list
https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/
'''


def rearrange_word(input):
    # Initializes a list
    un_arranged = list(input)

    for word in range(len(un_arranged)):

        # Picks a random index from 0 to word
        arranged = randint(0, word)

        # Swaps un_arranged[word] with the element at a random index
        un_arranged[word], un_arranged[arranged] = un_arranged[arranged], un_arranged[word]

        # ---- Uncomment to see what's happening easier ----
        # print(un_arranged[word], un_arranged[arranged])
        # print(' '.join(un_arranged) + '.')

    # ? Is this supposed to return in setence form or list?
    return ' '.join(un_arranged) + '.'
    # return un_arranged


if __name__ == '__main__':
    # Slices from the first(int) argument until the end(':')
    args = argv[1:]
    arranged_words = rearrange_word(args)
    print(arranged_words)
