from .telugu import chars_pairs
import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange


def toNumber(x):
    if x is '1' or x == 'Very dissimilar':
        return 1
    if x is '2' or x == 'Dissimilar':
        return 2
    if x is '3' or x == 'Neutral':
        return 3
    if x is '4' or x == 'Similar':
        return 4
    if x is '5' or x == 'Very Similar':
        return 5


def preprocess(data):
    values = list()
    for user in data:
        temp = [toNumber(x['value']) for x in data[user]['data']]
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
        plt.savefig('Plots/bar-{}.png'.format(chars_pairs[i]))
        plt.clf()
    return
