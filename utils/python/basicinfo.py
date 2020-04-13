from scipy.spatial.distance import squareform
from .telugu import chars_pairs
import numpy as np


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


def basics(user, user_data):
    data = dict()
    data.update({'user': user})

    basic_info = list()
    basic_info.append(['Unique ID', user])
    telugu_attr = ''
    if user_data['userInfo']['content']['read'] == 'Yes':
        telugu_attr += 'Read '

    if user_data['userInfo']['content']['speak'] == 'Yes':
        telugu_attr += 'Speak '

    if user_data['userInfo']['content']['write'] == 'Yes':
        telugu_attr += 'Write '

    basic_info.append(['Telugu', telugu_attr])

    for language in user_data['userInfo']['content']['languages']:
        basic_info.append([language['name'], language['attr']])

    # Get reaction and scores
    ones, twoes, threes, fours, fives = 0, 0, 0, 0, 0
    reaction1, reaction2, reaction3, reaction4, reaction5 = [], [], [], [], []
    score_table = list()
    val = 0
    for value, pair in zip(user_data['data'], chars_pairs):
        if value['value'] is '1' or value['value'] == 'Very dissimilar':
            ones += 1
            val = 1
            reaction1.append(value['reactionTime'])

        elif value['value'] is '2' or value['value'] == 'Dissimilar':
            twoes += 1
            val = 2
            reaction2.append(value['reactionTime'])

        elif value['value'] is '3' or value['value'] == 'Neutral':
            threes += 1
            val = 3
            reaction3.append(value['reactionTime'])

        elif value['value'] is '4' or value['value'] == 'Similar':
            fours += 1
            val = 4
            reaction4.append(value['reactionTime'])

        elif value['value'] is '5' or value['value'] == 'Very Similar':
            fives += 1
            val = 5
            reaction5.append(value['reactionTime'])

        score_table.append([pair, val, value['reactionTime']])
    reactions = sum(reaction1) + sum(reaction2) + \
        sum(reaction3) + sum(reaction4) + sum(reaction5)
    reactions /= len(user_data['data'])
    basic_info.append(['Avg. reaction time(seconds)', reactions])
    data.update({'info': basic_info})
    data.update({'scores': score_table})
    summary = list()
    summary.append([1, ones, np.mean(reaction1 or 0), np.std(reaction1 or 0)])
    summary.append([2, twoes, np.mean(reaction2 or 0), np.std(reaction2 or 0)])
    summary.append(
        [3, threes, np.mean(reaction3 or 0), np.std(reaction3 or 0)])
    summary.append([4, fours, np.mean(reaction4 or 0), np.std(reaction4 or 0)])
    summary.append([5, fives, np.mean(reaction5 or 0), np.std(reaction5 or 0)])
    data.update({'summary': summary})

    return data


def overall_data(data):
    processed_data = dict()
    scores = list()
    reactions = list()
    for user in data:
        temp1 = [toNumber(x['value']) for x in data[user]['data']]
        temp2 = [x['reactionTime'] for x in data[user]['data']]
        scores.append(temp1)
        reactions.append(temp2)
    scores, reactions = np.array(scores), np.array(reactions)

    consolidated = list()
    for i in range(scores.shape[1]):
        median = np.median(scores[:, i])
        count = np.array([np.count_nonzero(scores[:, i] == 1),
                          np.count_nonzero(scores[:, i] == 2),
                          np.count_nonzero(scores[:, i] == 3),
                          np.count_nonzero(scores[:, i] == 4),
                          np.count_nonzero(scores[:, i] == 5)])
        percentages = (count / count.sum()) * 100
        midx = np.argmax(percentages)
        agreement = np.array([percentages[midx], ])
        mean = [np.mean(reactions[:, i][scores[:, i] == 1]
                        if reactions[:, i][scores[:, i] == 1].any() else 0),
                np.mean(reactions[:, i][scores[:, i] == 2]
                        if reactions[:, i][scores[:, i] == 2].any() else 0),
                np.mean(reactions[:, i][scores[:, i] == 3]
                        if reactions[:, i][scores[:, i] == 3].any() else 0),
                np.mean(reactions[:, i][scores[:, i] == 4]
                        if reactions[:, i][scores[:, i] == 4].any() else 0),
                np.mean(reactions[:, i][scores[:, i] == 5]
                        if reactions[:, i][scores[:, i] == 5].any() else 0)]
        std = [np.std(reactions[:, i][scores[:, i] == 1]
                      if reactions[:, i][scores[:, i] == 1].any() else 0),
               np.std(reactions[:, i][scores[:, i] == 2]
                      if reactions[:, i][scores[:, i] == 2].any() else 0),
               np.std(reactions[:, i][scores[:, i] == 3]
                      if reactions[:, i][scores[:, i] == 3].any() else 0),
               np.std(reactions[:, i][scores[:, i] == 4]
                      if reactions[:, i][scores[:, i] == 4].any() else 0),
               np.std(reactions[:, i][scores[:, i] == 5]
                      if reactions[:, i][scores[:, i] == 5].any() else 0)]
        consolidated.append([count, percentages, mean, std, median])
    processed_data.update({'overall': consolidated})
    scores = {'Score': [1, 2, 3, 4, 5],
              'Means': [
        reactions[scores == 1].mean(),
        reactions[scores == 2].mean(),
        reactions[scores == 3].mean(),
        reactions[scores == 4].mean(),
        reactions[scores == 5].mean()
    ],
        'Std': [
        reactions[scores == 1].std(),
        reactions[scores == 2].std(),
        reactions[scores == 3].std(),
        reactions[scores == 4].std(),
        reactions[scores == 5].std()
    ]}
    processed_data.update({'scores': scores})
    return processed_data
