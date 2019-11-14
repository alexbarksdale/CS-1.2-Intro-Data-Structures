from random import choice
# from dictogram import Dictogram

# TODO: Set up as a class
# class Markov(dict):
#     def __init__(self, world_list):
#         # Checks if there is a word_list
#         if word_list:
#             self.world_list = world_list
#         else:
#             print('Add default text later.')

# text = "the theremin is theirs, ok? yes, it is. this is a a theremin."
source = 'markov_test.txt'
with open(source, 'r') as txt_file:
    text = txt_file.read()

order = 6
ngrams = {}

'''
N-Gram: Contiguous (neighboring) sequqnce of characaters or words.
    » Order: Looks for an (n)gram in a corpus
        ∆ Ex - Bi-gram, n-grams of two or zTri-grams, n-grams of three
        ∆ Tri-gram Example:
            - Corpus: "The dog crossed the street"
            - Tri-gram: The, he_, e_d, dog, og_, g_c, ....
                » Goal: What are the possible characters that follows: The or he_
'''


def ngram():
    for letter in range(len(text) - order):
        # Pulls out the (n)gram, n = order
        gram = text[letter: letter + order]

        if gram not in ngrams:
            # Creates a new list if a new gram is found
            ngrams[gram] = []
        ngrams[gram].append(text[letter + order])

#! Under the hood reference for me
# def ngram():
#     for letter in range(len(text) - order):
#         gram = text[letter: letter + 3]

#         if gram not in ngrams:
#             ngrams[gram] = []
#         ngrams[gram].append(text[letter + 3])
#     print(ngrams)


def markov():
    # Gets the first word
    currentGram = text[0: order]
    result = currentGram

    for i in range(100):
        possibilities = ngrams[currentGram]

        # Ends if there are no possibilities
        if not possibilities:
            print('something went wrong')
            break

        nextChar = choice(possibilities)
        result += nextChar

        txt_len = len(result)
        # Last (order) of characters in the text
        currentGram = result[txt_len - order: txt_len]

    print(result)


ngram()
# print(ngrams)
markov()
