''' Returns: a histogram of unique words with the number of times the word appears '''


def histogram(source_text):
    with open(source_text, 'r') as source:

        source_file = source.read().split()

        # Dictionary of key-value pairs
        word_freq = {}
        for word in source_file:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        return word_freq

        # ? ------- [Easy way (SLOW)] -------
        # word_freq = [source_file.count(word) for word in source_file]
        # # print(len(word_freq), len(source_file))

        # # zip returns a zip object which is an iterator of tuples which pairs the words together
        # return dict(zip(source_file, word_freq))


'''
Sorts the word frequency.
'Lambda' is used to define anonymous functions which are functions with no name.
Acknowledgement: https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
'''


def sort_histo(histo):
    for key, value in sorted(histo.items(), reverse=False, key=lambda item: item[1]):
        print(f'{key} - {value}')

# def sort_histo(histo):
#     sort_freq = [(histo[key], key) for key in histo]
#     sort_freq.sort()
#     sort_freq.reverse()
#     return sort_freq


''' Returns: the total count of words in histogram() '''


def unique_words(histogram):
    return len(histogram)


''' Returns: the number of times "word" appears in the histogram '''


def frequency(word, histogram):
    return histogram[word]


if __name__ == '__main__':
    source = '/Users/alexbarksdale/Dropbox/[DEV]Development/Make School/CS-1.2-Intro-Data-Structures/Code/tweetgen.txt'

    histo = histogram(source)
    # print(histo)
    sort_histo(histo)
