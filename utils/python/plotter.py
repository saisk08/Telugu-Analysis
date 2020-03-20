from .telugu import chars
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
from tqdm import trange


def preprocess(data):
    values = list()
    for user in data:
        temp = [int(x['value']) for x in data[user]['data']]
        values.append(temp)
    values = np.array(values)
    counts = []
    for i in range(values.shape[1]):
        count = [np.count_nonzero(values[:, i] == 1),
                 np.count_nonzero(values[:, i] == 2),
                 np.count_nonzero(values[:, i] == 3),
                 np.count_nonzero(values[:, i] == 4),
                 np.count_nonzero(values[:, i] == 5)]
        counts.append(count)
    return np.array(counts)


def make_bar_plot(data):
    processed_data = preprocess(data)
    # Get pairs
    chars_pairs = list(combinations(chars, 2))
    chars_pairs = [x + '-' + y for x, y in chars_pairs]

    # Do plots
    N = processed_data.shape[0]
    x = ['Very Similar', 'Similar', 'Neutral', 'Dissimilar', 'Very Dissimilar']
    x_pos = np.arange(len(x))
    for i in trange(N):
        # print(processed_data[i].shape, processed_data[i])
        plt.bar(x_pos, processed_data[i], color='b')
        plt.ylabel('Number of occurences')
        plt.xlabel('Scores')
        plt.xticks(x_pos, x)
        plt.savefig('Images/bar-{}.png'.format(chars_pairs[i]))
        plt.clf()
    return
