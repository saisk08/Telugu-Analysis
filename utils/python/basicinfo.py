from scipy.spatial.distance import squareform
from .telugu import chars_pairs


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
    summary.append([1, ones, reaction1 / len(reaction1)])
    summary.append([2, twoes, reaction2 / len(reaction2)])
    summary.append([3, threes, reaction3 / len(reaction3)])
    summary.append([4, fours, reaction4 / len(reaction4)])
    summary.append([5, fives, reaction5 / len(reaction5)])
    data.update({'summary': summary})

    return data
