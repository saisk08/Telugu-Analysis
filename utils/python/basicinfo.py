from scipy.spatial.distance import squareform


def basics(user_data):
    info = list()
    info.append(['Reg. no', user_data['userInfo']['content']['user']])
    telugu_attr = ''
    if user_data['userInfo']['content']['read'] == 'Yes':
        telugu_attr += 'Read '

    if user_data['userInfo']['content']['speak'] == 'Yes':
        telugu_attr += 'Speak '

    if user_data['userInfo']['content']['write'] == 'Yes':
        telugu_attr += 'Write '

    info.append(['Telugu', telugu_attr])

    for language in user_data['userInfo']['content']['languages']:
        info.append([language['name'], language['attr']])

    ones, twoes, threes, fours, fives = 0, 0, 0, 0, 0
    reactions = 0
    values = list()

    for value in user_data['data']:
        if value['value'] is '1' or value['value'] == 'Very dissimilar':
            ones += 1
            values.append(1)
        if value['value'] is '2' or value['value'] == 'Dissimilar':
            twoes += 1
            values.append(2)
        if value['value'] is '3' or value['value'] == 'Neutral':
            threes += 1
            values.append(3)
        if value['value'] is '4' or value['value'] == 'Similar':
            fours += 1
            values.append(4)
        if value['value'] is '5' or value['value'] == 'Very Similar':
            fives += 1
            values.append(5)
        reactions += value['reactionTime']

    reactions /= len(user_data['data'])

    info.append(['Reaction time(avg)', reactions])
    info.append(['Ones', ones])
    info.append(['Twos', twoes])
    info.append(['Threes', threes])
    info.append(['Fours', fours])
    info.append(['Fives', fives])
    info.append(squareform(values))

    return info
