from __future__ import division, print_function  # Python 2 and 3 compatibility
import re
from random import choice

'''
===================================
! Please grade markov_ngram.py !
===================================
'''


class Markov(dict):
    def __init__(self, source_file=None):

        if source_file:
            self.word_list = source_file
            self.markov = self.gen_markov()
        else:
            raise ValueError('No source file found')

    def gen_markov(self):
        '''
        Generates a markov chain
        @param: word_list - A source for a body of text
        '''
        markov_dict = {}

        # Last character not included
        for i, curr_word in enumerate(self.word_list[:-1]):
            next_word = self.word_list[i + 1]

            if curr_word in markov_dict:
                markov_dict[curr_word].append(next_word)
            else:
                markov_dict[curr_word] = [next_word]

        return markov_dict

    def gen_sentence(self, amt=15):
        '''
        Generate a setence based off a markov chain
        @param: amt - Amount of words in the sentence
        '''
        # Picks a random first word to start the sentence
        start = choice(self.word_list)

        sentence = [start]

        for i in range(amt):
            sentence.append(choice(self.markov[sentence[- 1]]))

        # View sentence
        print(' '.join(sentence) + '.')

        return ' '.join(sentence) + '.'


if __name__ == "__main__":
    source = 'medium_sample.txt'
    with open(source, 'r') as file:
        source_file = file.read().lower()
        filtered_file = re.sub(r'[^a-zA-Z\s]', '', source_file)
        filtered_file = filtered_file.replace('\n', ' ').split()

    markov = Markov(filtered_file)
    markov.gen_sentence()
