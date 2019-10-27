from sys import argv

source = '/Users/alexbarksdale/Dropbox/[DEV]Development/Make School/CS-1.2-Intro-Data-Structures/tweetgen.txt'


def histogram(source_text):
    with open(source_text, 'r') as source:

        word = source.read().split()

        # word_freq = []
        # for x in word:
        #     word_freq.append(word.count(x))

        word_freq = [word.count(x) for x in word]

        # zip returns a zip object which is an iterator of tuples which pairs the words together
        return print(dict(list(zip(word, word_freq))))


dictionary = histogram(source)
print(dictionary)
