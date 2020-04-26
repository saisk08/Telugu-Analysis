import json
import numpy as np
import pickle
from scipy.stats import zscore


def get_mul_vec(index):
    if index == 0:
        return np.array([1, 1, 1, 1, 1])
    if index == 1:
        return np.array([-1, 1, 1, 1, 1])
    if index == 2:
        return np.array([-1, -1, 1, 1, 1])
    if index == 3:
        return np.array([-1, -1, -1, 1, 1])
    if index == 4:
        return np.array([-1, -1, -1, -1, 1])


def get_score(counts):
    vals = counts / counts.sum()
    mul_vec = get_mul_vec(np.argmax(vals))
    return vals.max() + vals * mul_vec


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


def process(data):
    scores = list()
    reactions = list()
    for user in data:
        temp1 = [toNumber(x['value']) for x in data[user]['data']]
        temp2 = [x['reactionTime'] for x in data[user]['data']]
        scores.append(temp1)
        reactions.append(temp2)
    scores, reactions = np.array(scores), np.array(reactions)
    rdm = list()

    for i in range(scores.shape[1]):
        median = np.median(scores[:, i])
        count = np.array([np.count_nonzero(scores[:, i] == 1),
                          np.count_nonzero(scores[:, i] == 2),
                          np.count_nonzero(scores[:, i] == 3),
                          np.count_nonzero(scores[:, i] == 4),
                          np.count_nonzero(scores[:, i] == 5)])
        mu, sigma = reactions[:, i].mean(), reactions[:, i].std()
        rdm.append((neg_sigmoid(count) * values).sum() + mu + sigma)
    print(max(rdm), min(rdm))
    z = zscore(rdm)
    print(z.min(), z.max(), z.shape)
    return zscore(rdm)


ver1_file = open('ver1.json')
ver2_file = open('ver2.json')
ver1_data = json.load(ver1_file)
ver2_data = json.load(ver2_file)

dump1 = process(ver1_data)
dump2 = process(ver2_data)
f = open('rdms_minmax.pkl', 'wb')
pickle.dump((dump1, dump2), f)
f.close()
