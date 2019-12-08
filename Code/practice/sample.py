# from Code.histogram import histogram_dict
from histogram import histogram_dict
from read_file import read_file
from random import randint


def sample_freq(histogram):
    # Length of the histogram based off values
    hist_length = sum(histogram.values())
    word_predict = randint(1, hist_length)
    counter = 0
    for word in histogram.keys():

        # Adds the histogram value to the counter
        counter += histogram[word]

        if word_predict <= counter:
            return word


def test_sample_freq(histogram):
    word_freq = []
    for _ in range(2000):
        sample = sample_freq(histogram)
        word_freq.append(sample)

    return histogram_dict(word_freq)


if __name__ == "__main__":
    source = 'tweetgen.txt'
    sample = sample_freq(histogram_dict(read_file(source)))
    print(sample)

    # test = test_sample_freq(histogram_dict(read_file(source)))
    # print(test)
