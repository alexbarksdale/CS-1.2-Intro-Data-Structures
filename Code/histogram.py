from sys import argv

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

        # ? ------- [Easy way] -------
        # word_freq = [word.count(x) for x in word]

        # # zip returns a zip object which is an iterator of tuples which pairs the words together
        # return dict(list(zip(word, word_freq)))


''' Returns: the total count of words in histogram() '''


def unique_words(histogram):
    return len(histogram)


''' Returns: the number of times "word" appears in the histogram '''


def frequency(word, histogram):
    return histogram[word]


if __name__ == '__main__':
    source = '/Users/alexbarksdale/Dropbox/[DEV]Development/Make School/CS-1.2-Intro-Data-Structures/Code/tweetgen.txt'

    histo = histogram(source)
    print(histo)

    print(unique_words(histo))
