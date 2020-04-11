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
    data.update({'user', user})

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
    reaction1, reaction2, reaction3, reaction4, reaction5 = 0, 0, 0, 0, 0
    score_table = list()
    for value, pair in zip(user_data['data'], chars_pairs):
        if value['value'] is '1' or value['value'] == 'Very dissimilar':
            ones += 1
            reaction1 += value['reactionTime']

        elif value['value'] is '2' or value['value'] == 'Dissimilar':
            twoes += 1
            reaction2 += value['reactionTime']

        elif value['value'] is '3' or value['value'] == 'Neutral':
            threes += 1
            reaction3 += value['reactionTime']

        elif value['value'] is '4' or value['value'] == 'Similar':
            fours += 1
            reaction4 += value['reactionTime']

        elif value['value'] is '5' or value['value'] == 'Very Similar':
            fives += 1
            reaction5 += value['reactionTime']

        score_table.append([pair, value['value'], value['reactionTime']])

    reactions = reaction1 + reaction2 + reaction3 + reaction4 + reaction5
    reactions /= len(user_data['data'])
    basic_info.append(['Avg. reaction time(seconds)', reactions])
    data.update({'info': basic_info})
    data.update({'scores': score_table})
    summary = list()
    summary.append([1, ones, np.mean(reaction1), np.std(reaction1)])
    summary.append([2, twoes, np.mean(reaction2), np.std(reaction2)])
    summary.append([3, threes, np.mean(reaction3), np.std(reaction3)])
    summary.append([4, fours, np.mean(reaction4), np.std(reaction4)])
    summary.append([5, fives, np.mean(reaction5), np.std(reaction5)])
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
        count = [np.count_nonzero(scores[:, i] == 1),
                 np.count_nonzero(scores[:, i] == 2),
                 np.count_nonzero(scores[:, i] == 3),
                 np.count_nonzero(scores[:, i] == 4),
                 np.count_nonzero(scores[:, i] == 5)]
        mean = [np.mean(reactions[:, i][scores[:, i] == 1]),
                np.mean(reactions[:, i][scores[:, i] == 2]),
                np.mean(reactions[:, i][scores[:, i] == 3]),
                np.mean(reactions[:, i][scores[:, i] == 4]),
                np.mean(reactions[:, i][scores[:, i] == 5])]
        std = [np.std(reactions[:, i][scores[:, i] == 1]),
               np.std(reactions[:, i][scores[:, i] == 2]),
               np.std(reactions[:, i][scores[:, i] == 3]),
               np.std(reactions[:, i][scores[:, i] == 4]),
               np.std(reactions[:, i][scores[:, i] == 5])]
        consolidated.append((count, mean, std))
    processed_data.update({'overall': consolidated})

    processed_data.update(
        {'score1': (reactions[reactions == 1].mean(), reactions[reactions == 1].std())})
    processed_data.update(
        {'score2': (reactions[reactions == 2].mean(), reactions[reactions == 1].std())})
    processed_data.update(
        {'score3': (reactions[reactions == 3].mean(), reactions[reactions == 1].std())})
    processed_data.update(
        {'score4': (reactions[reactions == 4].mean(), reactions[reactions == 1].std())})
    processed_data.update(
        {'score5': (reactions[reactions == 5].mean(), reactions[reactions == 1].std())})
