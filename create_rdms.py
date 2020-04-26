import json
import numpy as np
import pickle
from scipy.stats import zscore


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
    scores = list()
    reactions = list()
    for user in data:
        temp1 = [toNumber(x['value']) for x in data[user]['data']]
        temp2 = [x['reactionTime'] for x in data[user]['data']]
        scores.append(temp1)
        reactions.append(temp2)
    return np.array(scores), np.array(reactions)


def process_custom(data):
    scores, reactions = preprocess(data)
    rdm = list()
    mul_vec = np.array([-1, -1, 0, 1, 1])
    for i in range(scores.shape[1]):
        median = np.median(scores[:, i])
        count = np.array([np.count_nonzero(scores[:, i] == 1),
                          np.count_nonzero(scores[:, i] == 2),
                          np.count_nonzero(scores[:, i] == 3),
                          np.count_nonzero(scores[:, i] == 4),
                          np.count_nonzero(scores[:, i] == 5)])
        percents = count / count.sum()
        mean = np.array([np.mean(reactions[:, i][scores[:, i] == 1]
                                 if reactions[:, i][scores[:, i] == 1].any() else 0),
                         np.mean(reactions[:, i][scores[:, i] == 2]
                                 if reactions[:, i][scores[:, i] == 2].any() else 0),
                         np.mean(reactions[:, i][scores[:, i] == 3]
                                 if reactions[:, i][scores[:, i] == 3].any() else 0),
                         -np.mean(reactions[:, i][scores[:, i] == 4]
                                  if reactions[:, i][scores[:, i] == 4].any() else 0),
                         -np.mean(reactions[:, i][scores[:, i] == 5]
                                  if reactions[:, i][scores[:, i] == 5].any() else 0)])
        rdm_value = median + ((percents * mul_vec) + (mean * 0.01)).sum()
        if rdm_value < 0:
            rdm_value -= 0.1 * (percents[2] + 0.01 * mean[2])
        else:
            rdm_value += 0.1 * (percents[2] + 0.01 * mean[2])
        rdm.append(rdm_value)
    return zscore(rdm)


def process_minmax(data):
    scores, _ = preprocess(data)
    rdm = list()
    mul_vec = np.array([-1, -0.5, 0, 0.5, 1])
    for i in range(scores.shape[1]):
        median = np.median(scores[:, i])
        count = np.array([np.count_nonzero(scores[:, i] == 1),
                          np.count_nonzero(scores[:, i] == 2),
                          np.count_nonzero(scores[:, i] == 3),
                          np.count_nonzero(scores[:, i] == 4),
                          np.count_nonzero(scores[:, i] == 5)])
        percents = count / count.sum()

        rdm_value = median + (percents * mul_vec).sum()
        rdm.append(rdm_value)
    return zscore(rdm)


def start(ver1, ver2, func):
    return [func(ver1), func(ver2)]


if __name__ == "__main__":
    ver1_file = open('ver1.json')
    ver2_file = open('ver2.json')
    ver1_data = json.load(ver1_file)
    ver2_data = json.load(ver2_file)
    for f, funk in zip(['minmax', 'custom'], [process_minmax, process_custom]):
        f = open('rdms_{}.pkl'.format(f), 'wb')
        pickle.dump(start(ver1_data, ver2_data, funk), f)
        f.close()
