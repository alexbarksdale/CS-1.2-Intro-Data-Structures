from random import randint, random
from sys import argv


'''
Returns: a histogram of unique words with the number of times the word appears

Dictionary: INEFFICIENT for space | FAST read speed
Tuple: EFFICIENT for space | SLOW read speed
List: EFFICIENT for space | SLOW read speed

'''


def histogram_dict(source_text):
    word_freq = {}
    for word in source_text:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq


def histogram_tuple(source_text):
    word_freq = []
    for word in source_text:
        word_count = 0
        for same_word in source_text:
            if word == same_word:
                word_count += 1
        if word and word_count not in word_freq:
            # append() takes 1 parameters so put it in () to append/push the word & count together
            word_freq.append((word, word_count))
    return word_freq

    # ? ------- [Non-algorithmic way] -------
    # word_freq = [source_file.count(word) for word in source_file]

    # # zip returns a zip object which is an iterator of tuples which pairs the words together
    # return list(zip(source_file, word_freq))


def histogram_list(source_text):
    word_freq = []
    for word in source_text:
        word_count = 0
        for same_word in source_text:
            if word == same_word:
                word_count += 1
        if word and word_count not in word_freq:
            # append() takes 1 parameters so put it in () to append/push the word & count together
            word_freq.append([word, word_count])
    return word_freq


'''
Sorts the word frequency.
#! Bug: Doesn't sort tuple and list

- sorted() returns a sorted list of specified iterable objects
    - sorted(iterable, key=key, reverse=reverse)
        - iterable : Required. The sequence to sort, list, dictionary, tuple
        - key : Optional. A function to execute to decide the order
        - reverse : Optional. A boolean. False will sort ascending, vice-versa
- .items() is used to return the list with all dictionary keys with values
- 'Lambda' is used to define anonymous functions which are functions with no name.
Acknowledgement: https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
'''


def sort_histo(histo):
    for key, value in sorted(histo.items(), key=lambda word: word[1], reverse=False):
        print(f'{key} - {value}')


''' Returns: the total count of words in histogram() '''


def unique_words(histogram):
    return len(histogram)


''' Returns: the number of times "word" appears in the histogram '''


def frequency(word, histogram):
    return histogram[word]


if __name__ == '__main__':

    source = 'sampletest.txt'
    with open(source, 'r') as source:
        source_file = source.read().split()

    # ? ------- [Dictionary] -------
    histo_dict = histogram_dict(source_file)
    args = argv[1:]

    print(histo_dict)

    # sort_histo(histo_dict)
    # print(sample(histo_dict, 1))

    # ? ------- [Tuple] -------
    # histo_tuple = histogram_tuple(source_file)
    # print(histo_tuple)

    # sort_histo(histo_tuple)

    # ? ------- [List] -------

    # histo_list = histogram_list(source_file)
    # print(histo_list)
    # sort_histo(histo_list)
