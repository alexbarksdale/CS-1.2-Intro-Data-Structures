from random import choice
# from dictogram import Dictogram


# class Markov(dict):
#     def __init__(self, world_list):
#         # Checks if there is a word_list
#         if word_list:
#             self.world_list = world_list
#         else:
#             print('Add default text later.')

source = 'markov_test.txt'
with open(source, 'r') as txt_file:
    text = txt_file.read()

# change variable name to ngram_len
# text = "The donkey ran over the kid and the donkey was full of sadness."
order = 6
ngrams = {}


def setup():
    for i in range(len(text) - order):
        gram = text[i: i + order]

        if gram not in ngrams:
            ngrams[gram] = []
        ngrams[gram].append(text[i + order])


def markov():
    currentGram = text[0: order]
    result = currentGram

    for i in range(100):
        possibilities = ngrams[currentGram]

        # Not sure if this is needed
        if not possibilities:
            print('something went wrong')
            break

        nextChar = choice(possibilities)
        result += nextChar

        txt_len = len(result)
        currentGram = result[txt_len - order: txt_len]

    print(result)


setup()
markov()
