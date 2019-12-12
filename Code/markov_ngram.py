from __future__ import division, print_function  # Python 2 and 3 compatibility
from random import choice

# ---------- App.py Connection ----------
# --- Comment out if not in use ---
# from Code.utils import read_file
# ---------- Command Line Connection ----------
# --- Comment out if not in use ---
from utils import read_file


class Markov(dict):
    '''Acknowledgement: Received help from github@noahkrause to improve the ngram functionality'''

    def __init__(self, source_file=None, order=5):
        self.order = order  # The order of the (n)gram
        self.ngrams_dict = {}  # Contains a dict. of (n)grams

        if source_file:
            self.word_list = read_file(source_file)
            self.ngram = self.gen_ngram()
            self.n_markov = self.gen_ngram_markov()
        else:
            raise ValueError('No source file found')
    '''
    N-Gram: Contiguous (neighboring) sequence of characaters or words.
        - Order: Looks for an (n)gram in a corpus
            Ex - Bi-gram, n-grams of two or Tri-grams, n-grams of three
            - Tri-gram Example:
                - Corpus: "The dog crossed the street"
                - Tri-gram: The, he_, e_d, dog, og_, g_c, ....
                    - Goal: What are the possible characters that follows: The or he_
                    and pick randomly from the possibilities
    '''

    def gen_ngram(self):
        '''Generates a dict. of ngrams from a given corpus (word_list)'''
        for char in range(len(self.word_list) - self.order + 1):
            # Pulls out the (n)gram, n = order
            gram = self.word_list[char: char + self.order]

            if gram not in self.ngrams_dict:
                # Creates a new list if a new gram is found
                self.ngrams_dict[gram] = []

            # Works by getting the letter/char after the ngram
            # If its the end of the text, there is no letter, so just append a space.
            if char + self.order < len(self.word_list):
                letter = self.word_list[char + self.order]
            else:
                letter = ' '

            self.ngrams_dict[gram].append(letter)
        # View the dict.
        # print(self.ngrams_dict)

    def gen_ngram_markov(self):
        '''Generates a sentence based off the markov-chain using ngrams'''

        # Gets one FULL word rather than a random word cut off from the ngram
        availableWords = [word for word in self.word_list.split()
                          if len(word) == self.order]

        # Checks if there aren't any word's length == to the order
        if len(availableWords) == 0:
            availableWords.append(self.word_list[:self.order])

        currentGram = choice(availableWords)

        # Stores the sentence
        result = currentGram.capitalize()

        i = 0
        while True:
            # Ends if there are no possibilities
            if currentGram not in self.ngrams_dict:
                return result[:len(result)-1] + '.'

            # Possible next characters based off the current gram
            possibilities = self.ngrams_dict[currentGram]
            nextChar = choice(possibilities)
            result += nextChar

            txt_len = len(result)

            # Get's the last (order) chracters of the text
            currentGram = result[txt_len - self.order: txt_len]

            # Runs until (i) amount and the next char is a space
            if (i > 150 and nextChar is ' '):
                break
            i += 1

        # # View the random sentence
        print(result[:len(result)-1] + '.')

        return result[:len(result)-1] + '.'


if __name__ == "__main__":
    Markov('medium_sample.txt')
