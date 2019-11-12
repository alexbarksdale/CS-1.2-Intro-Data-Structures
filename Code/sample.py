# from Code.histogram import histogram_dict
from histogram import histogram_dict
from random import randint


def sample_freq(histogram):
    # Length of the histogram based off values
    hist_length = sum(histogram.values())
    word_predict = randint(1, hist_length)
    counter = 0

    print('Histogram: ' + str(histogram) + '\n')
    print('Word predict: ' + str(word_predict) + '\n' + '_' * 20)

    for word in histogram.keys():
        print('Histo Word: ' + str(histogram[word]) + '\n')

        # Adds the histogram value to the counter
        counter += histogram[word]

        print('Counter: ' + str(counter) + '\n')

        if word_predict <= counter:
            return word


def test_sample_freq(histogram):
    word_freq = []
    for i in range(2000):
        sample = sample_freq(histogram)
        word_freq.append(sample)

    return histogram_dict(word_freq)


# TODO: Remove after application is done
if __name__ == "__main__":
    source = 'sampletest.txt'
    with open(source, 'r') as source:
        source_file = source.read().split()

    sample = sample_freq(histogram_dict(source_file))
    print(sample)

    # test = test_sample_freq(histogram_dict(source_file))
    # print(test)
